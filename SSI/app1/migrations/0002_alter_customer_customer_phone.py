# Generated by Django 4.1 on 2022-09-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_phone',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, unique=True),
        ),
    ]
