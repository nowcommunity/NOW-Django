# Generated by Django 4.0.7 on 2022-10-27 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0023_rename_nowsynloc_nowlocalitysynonym'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NowTau',
            new_name='NowTimeUnitUpdate',
        ),
    ]
