# Generated by Django 4.0.7 on 2022-10-27 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0003_rename_nowtubound_nowtimeunitboundary'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NowTuSequence',
            new_name='NowTimeUnitSequence',
        ),
    ]
