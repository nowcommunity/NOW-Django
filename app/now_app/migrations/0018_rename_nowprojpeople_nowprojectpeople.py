# Generated by Django 4.0.7 on 2022-10-27 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0017_rename_nowplr_nowprojectlocality'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NowProjPeople',
            new_name='NowProjectPeople',
        ),
    ]