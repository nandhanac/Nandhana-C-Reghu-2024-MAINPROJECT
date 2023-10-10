# Generated by Django 4.2.5 on 2023-10-09 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0023_rename_phone_number_booking_alternative_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='selected_service_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings_price', to='vehicle.subsubcategory'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='selected_subsubcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings_subsubcategory', to='vehicle.subsubcategory'),
        ),
    ]
