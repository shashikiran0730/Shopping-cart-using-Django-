# Generated by Django 3.1.7 on 2021-12-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Itemid', models.CharField(max_length=200)),
                ('Itemname', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('imageurl', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
