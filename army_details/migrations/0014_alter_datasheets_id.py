# Generated by Django 4.2.17 on 2025-01-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('army_details', '0013_remove_datasheetsabilities_ability_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasheets',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
