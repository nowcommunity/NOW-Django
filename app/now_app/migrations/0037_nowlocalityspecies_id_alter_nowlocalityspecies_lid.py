# Generated by Django 4.0.7 on 2022-10-31 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0036_alter_nowlocalityupdatereference_luid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nowlocalityspecies',
            name='lid',
            field=models.OneToOneField(db_column='lid', on_delete=django.db.models.deletion.DO_NOTHING, to='now_app.nowlocality'),
        ),
        migrations.AddField(
            model_name='nowlocalityspecies',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
