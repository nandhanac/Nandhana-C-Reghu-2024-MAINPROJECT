# Generated by Django 4.2.6 on 2023-10-10 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0028_alter_booking_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='selected_service_price',
        ),
    ]
