# Generated by Django 3.2.6 on 2023-09-15 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_customer_avatar_remove_customer_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]