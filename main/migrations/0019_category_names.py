# Generated by Django 4.1 on 2022-08-10 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_category_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='names',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='main.product'),
            preserve_default=False,
        ),
    ]