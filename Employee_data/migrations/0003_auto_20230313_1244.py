# Generated by Django 3.2.17 on 2023-03-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_data', '0002_auto_20230313_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='salarypdffiles',
            name='Employee_Firstname',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='salarypdffiles',
            name='Employee_Lastname',
            field=models.CharField(default='', max_length=64),
        ),
    ]
