# Generated by Django 2.1.7 on 2019-04-04 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='upload',
            new_name='FileUpload',
        ),
    ]