# Generated by Django 4.0.7 on 2022-10-31 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0060_refauthors_id_alter_refauthors_rid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reffieldname',
            name='field_id',
            field=models.IntegerField(db_column='field_ID'),
        ),
        migrations.AddField(
            model_name='reffieldname',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]