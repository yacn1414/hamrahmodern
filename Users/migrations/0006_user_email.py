# Generated by Django 4.1 on 2022-09-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_alter_user_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
