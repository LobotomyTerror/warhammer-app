# Generated by Django 4.2.17 on 2025-01-13 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('army_details', '0030_rename_datasheet_id_datasheetsstratagems_datasheet_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasheetsenhancements',
            old_name='datasheet_id',
            new_name='datasheet',
        ),
        migrations.RenameField(
            model_name='datasheetsenhancements',
            old_name='enhancements_id',
            new_name='enhancements',
        ),
    ]
