# Generated by Django 4.1 on 2022-08-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_image_u_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='end_price',
            field=models.IntegerField(default=0, verbose_name='end price'),
            preserve_default=False,
        ),
    ]
