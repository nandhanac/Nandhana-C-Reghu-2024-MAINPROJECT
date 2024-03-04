# Generated by Django 4.2.6 on 2024-02-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0054_alter_mechanic_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='pickup_service',
            field=models.CharField(choices=[('Yes', 'Yes, I need pickup service'), ('No', 'No, I will manage myself')], default='No', max_length=5, null=True),
        ),
    ]