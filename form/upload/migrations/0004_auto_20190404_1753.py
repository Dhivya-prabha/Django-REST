# Generated by Django 2.1.7 on 2019-04-04 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20190404_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='positions',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='ships',
            name='mode',
        ),
    ]