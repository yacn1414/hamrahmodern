# Generated by Django 4.1 on 2022-08-15 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_alter_product_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='sabad',
            name='T',
            field=models.IntegerField(default=None, verbose_name='تعداد'),
            preserve_default=False,
        ),
    ]
