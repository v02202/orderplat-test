from django import forms
from .models import Customer, product_choice, Contact



class CustomerModelForm(forms.ModelForm):
    product_id = forms.ChoiceField(choices=product_choice)
    vip_check = forms.BooleanField(required=False)
    class Meta:
        
        model = Customer
        fields = ('product_id', 'qty', 'customer_id','vip_check')


class ContactModelForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email')
