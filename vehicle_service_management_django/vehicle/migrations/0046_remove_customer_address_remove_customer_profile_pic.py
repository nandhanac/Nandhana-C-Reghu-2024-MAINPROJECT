# Generated by Django 4.2.6 on 2023-10-24 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0045_remove_booking_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]
