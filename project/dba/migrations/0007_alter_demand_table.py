# Generated by Django 4.1.5 on 2023-01-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dba', '0006_demand_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='table',
            field=models.FileField(upload_to='media/'),
        ),
    ]
