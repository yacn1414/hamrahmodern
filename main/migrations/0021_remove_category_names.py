# Generated by Django 4.1 on 2022-08-10 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_category_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='names',
        ),
    ]