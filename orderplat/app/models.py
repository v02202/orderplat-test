from django.db import models
from django_q.models import Schedule

# Create your models here.
product_choice = (
    ('Select product','Select product'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7')
)


class Product(models.Model):
    product_id = models.CharField(max_length=255, primary_key=True)
    stock_pcs = models.PositiveIntegerField(default=0,blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    shop_id = models.CharField(max_length=255, blank=True, null=True)
    vip = models.BooleanField(null=False)

    class Meta:
        db_table = 'Product'

class Customer(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=255, blank=False, null=False, choices=product_choice)
    qty = models.PositiveIntegerField(default =0, blank=True, null=False)
    customer_id = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        db_table = 'Customer'

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    schedule_id = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Create the schedule
        schedule = Schedule.objects.create(
            name=self.__str__(),
            func="app.views.send_email",
            args=f"'{self.email}'",
            schedule_type=Schedule.DAILY,

        )
        # Save the model with the schedule id
        self.schedule_id = schedule.pk
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the schedule
        Schedule.objects.get(pk=self.schedule_id).delete()
        # Delete the person
        super().delete(*args, **kwargs)

    class Meta:
        db_table = 'Contact'
