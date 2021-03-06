# Generated by Django 2.1.2 on 2018-10-25 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=50)),
                ('status', models.CharField(blank=True, default=None, max_length=50)),
                ('distype', models.CharField(blank=True, default=None, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cityname',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.City'),
            preserve_default=False,
        ),
    ]
