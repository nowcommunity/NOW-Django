# Generated by Django 4.0.7 on 2022-10-27 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0024_rename_nowtau_nowtimeunitupdate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NowTr',
            new_name='NowTimeUnitUpdateReference',
        ),
    ]