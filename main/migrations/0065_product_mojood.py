# Generated by Django 4.1.3 on 2022-11-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0064_alter_brandmobile_name_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mojood',
            field=models.CharField(choices=[('موجود', 'ناموجود')], default='موجود', max_length=20),
        ),
    ]
