# Generated by Django 4.1.3 on 2022-11-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0066_alter_jamsabad_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'managed': True, 'verbose_name': 'تخفیف ها '},
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='اسم محصول'),
        ),
    ]