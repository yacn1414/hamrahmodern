# Generated by Django 4.1.3 on 2022-11-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0068_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colors',
            name='color',
            field=models.CharField(choices=[('white', 'white'), ('black', 'black'), ('gray', 'gray'), ('yellow', 'yellow'), ('blue', 'blue'), ('red', 'red'), ('gold', 'gold'), ('silwer', 'silwer')], max_length=255),
        ),
    ]