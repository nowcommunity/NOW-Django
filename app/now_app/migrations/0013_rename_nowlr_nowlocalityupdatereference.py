# Generated by Django 4.0.7 on 2022-10-27 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0012_rename_nowlau_nowlocalityupdate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NowLr',
            new_name='NowLocalityUpdateReference',
        ),
    ]
