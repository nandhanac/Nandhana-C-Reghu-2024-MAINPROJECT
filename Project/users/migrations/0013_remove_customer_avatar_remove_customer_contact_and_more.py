# Generated by Django 4.1.2 on 2023-09-13 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_customer_avatar_customer_contact_customer_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
    ]