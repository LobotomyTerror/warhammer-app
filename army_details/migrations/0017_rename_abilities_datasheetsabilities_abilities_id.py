# Generated by Django 4.2.17 on 2025-01-13 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('army_details', '0016_alter_abilities_abilities_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasheetsabilities',
            old_name='abilities',
            new_name='abilities_id',
        ),
    ]
