# Generated by Django 4.2.6 on 2023-10-24 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0050_deletedcustomer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DeletedCustomer',
        ),
    ]