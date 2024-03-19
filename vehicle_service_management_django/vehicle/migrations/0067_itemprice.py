# Generated by Django 4.2.6 on 2024-03-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0066_delete_progressphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
