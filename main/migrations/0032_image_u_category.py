# Generated by Django 4.1 on 2022-08-13 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_alter_image_u_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_u',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
            preserve_default=False,
        ),
    ]
