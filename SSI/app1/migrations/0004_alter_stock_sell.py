# Generated by Django 4.1 on 2022-09-11 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_stock_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='sell',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
