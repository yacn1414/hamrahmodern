# Generated by Django 4.1 on 2022-08-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_category_tpost_alter_product_star_userphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pro', models.IntegerField()),
                ('id_user', models.IntegerField()),
            ],
            options={
                'verbose_name': 'علاقه مندی ها',
                'verbose_name_plural': 'علاقه مندی ها',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=None, upload_to='category'),
            preserve_default=False,
        ),
    ]
