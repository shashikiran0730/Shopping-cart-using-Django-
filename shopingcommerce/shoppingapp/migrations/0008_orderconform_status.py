# Generated by Django 3.1.7 on 2022-03-18 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0007_adminlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderconform',
            name='status',
            field=models.CharField(default='orderplaced', max_length=100),
        ),
    ]
