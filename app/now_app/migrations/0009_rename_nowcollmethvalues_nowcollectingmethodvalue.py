# Generated by Django 4.0.7 on 2022-10-27 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0008_rename_nowbr_nowtimeunitboundaryupdatereference'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NowCollMethValues',
            new_name='NowCollectingMethodValue',
        ),
    ]