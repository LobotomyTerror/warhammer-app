# Generated by Django 4.2.17 on 2025-01-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('army_details', '0034_alter_lastupdated_last_updated_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastupdated',
            name='last_updated_date',
        ),
        migrations.AlterField(
            model_name='lastupdated',
            name='id',
            field=models.DateField(primary_key=True, serialize=False),
        ),
    ]
