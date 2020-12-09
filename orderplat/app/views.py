from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Count, Sum
from app.models import Product, Customer
from .forms import CustomerModelForm, ContactModelForm
import itertools
import json


# Create your views here.
def index(request):
    form = CustomerModelForm()
    product_info = Product.objects.all()
    if request.method == "POST" and 'action_one' in request.POST:
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data.get('product_id')
            qty = form.cleaned_data.get('qty')
            customer_id = form.cleaned_data.get('customer_id')
            vip_check = form.cleaned_data.get('vip_check')

            product_stock = Product.objects.filter(product_id=product_id).values_list('stock_pcs', flat=True)[0]
            if qty > product_stock:
                messages.error(request, 'Sorry, the order quantity is out of stock.')
            else:
                if vip_check == False:
                    if product_id in Product.objects.filter(vip=False).values_list('product_id', flat=True):
                        form.save()
                        Product.objects.filter(product_id=product_id).update(stock_pcs=product_stock - qty)
                    else:
                        messages.error(request, 'Sorry, this product is only for vip.')
                else:
                    form.save()
                    Product.objects.filter(product_id=product_id).update(stock_pcs=product_stock - qty)

        return redirect('index')

    order_info = Customer.objects.all()

    if request.method == "POST" and 'delete_items' in request.POST:  # If method is POST,
        items_to_delete = request.POST['delete_items']
        items = items_to_delete.split(',')
        del_order_id = items[0]
        del_product_id = items[1]
        del_qty = int(items[2])
        product_stock = Product.objects.filter(product_id=del_product_id).values_list('stock_pcs', flat=True)[0]
        Product.objects.filter(product_id=del_product_id).update(stock_pcs=product_stock + del_qty)
        ii = Customer.objects.filter(order_id=del_order_id).delete()
        
        

        return redirect('index')  # Finally, redirect to the homepage.

    product_calculate = Customer.objects.values('product_id').annotate(sum=Sum('qty'), count=Count('product_id'))
    cal = []
    for i in product_calculate:
        cal.append({
            'product_id': i['product_id'],
            'product_sum': i['sum'],
        })
    max_order = sorted(cal, key=lambda i: i['product_sum'], reverse=True)[:3]

    context = {
        'form':form,
        'product_info':product_info,
        'order_info': order_info,
        'max_order': max_order
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request,'index.html', context = context)


def count_order(request):
    form = ContactModelForm()

    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            form.save()
        


    context = {
        'form':form,

    }

    return render(request, 'order.html', context=context)

def send_email(to):
    product_calculate = Customer.objects.values('product_id').annotate(sum=Sum('qty'), count=Count('product_id'))
    # print(product_calculate)
    cal_product_id = [product['product_id'] for product in product_calculate]
    cal_product_price = Product.objects.filter(product_id__in=cal_product_id).values('price', 'shop_id', 'product_id')
    cal = []
    for i, j in zip(product_calculate, cal_product_price):
        cal.append({
            'product_id': j['product_id'],
            'order_count': i['count'],
            'product_sum': i['sum'] * j['price'],
            'shop_id': j['shop_id']
        })
    # print(cal)
    cal_shop = []
    for key, group in itertools.groupby(cal, lambda item: item["shop_id"]):
        groups = list(group)
        cal_shop.append({
            'Popular shop': key,
            'Total ordering': sum(item01['order_count'] for item01 in groups),
            'Total selling': sum(item02['product_sum'] for item02 in groups)
        })
    content = json.dumps(cal_shop)

    send_mail(
        subject="Here are popular products!",
        message=content,
        from_email = "r06b44005@g.ntu.edu.tw",
        recipient_list=[to],
    )

    

