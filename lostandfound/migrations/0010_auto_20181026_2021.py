# Generated by Django 2.1.2 on 2018-10-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostandfound', '0009_auto_20181026_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='found',
            name='pic',
            field=models.ImageField(default='def.jpg', upload_to='profile_pics'),
        ),
    ]
