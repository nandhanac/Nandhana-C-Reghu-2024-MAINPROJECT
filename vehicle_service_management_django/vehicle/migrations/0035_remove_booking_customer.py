# Generated by Django 4.2.6 on 2023-10-11 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0034_alter_booking_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='customer',
        ),
    ]