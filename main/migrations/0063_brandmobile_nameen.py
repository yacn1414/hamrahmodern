# Generated by Django 4.1.3 on 2022-11-13 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_remove_category_tpost_remove_category_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandmobile',
            name='nameEn',
            field=models.CharField(default=None, max_length=255, verbose_name='اسم انگلیسی'),
            preserve_default=False,
        ),
    ]