# Generated by Django 4.0.7 on 2022-10-27 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0026_rename_nowtur_nowtimeunitboundaryreference'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RefKeywordsRef',
            new_name='RefKeywordsReference',
        ),
    ]
