# Generated by Django 3.0.5 on 2023-09-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20230918_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='category',
            field=models.CharField(choices=[('Diagnostic services', 'Diagnostic services'), ('Denting  & painting', 'Denting  & painting')], max_length=50),
        ),
    ]