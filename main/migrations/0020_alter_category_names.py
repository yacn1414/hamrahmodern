# Generated by Django 4.1 on 2022-08-10 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_category_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='names',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='main.product'),
        ),
    ]