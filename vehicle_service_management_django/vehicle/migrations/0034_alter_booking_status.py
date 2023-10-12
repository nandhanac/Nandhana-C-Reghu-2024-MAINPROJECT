# Generated by Django 4.2.6 on 2023-10-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0033_booking_customer_booking_mechanic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Repairing', 'Repairing'), ('Repairing Done', 'Repairing Done'), ('Released', 'Released')], default='Pending', max_length=50, null=True),
        ),
    ]