# Generated by Django 3.1.4 on 2020-12-05 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201205_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
