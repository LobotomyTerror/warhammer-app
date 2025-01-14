# Generated by Django 4.2.17 on 2025-01-12 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('army_details', '0014_alter_datasheets_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abilities',
            name='abilities_id',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='datasheetsabilities',
            name='abilities',
            field=models.ForeignKey(blank=True, db_column='abilities_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ability_id', to='army_details.abilities', to_field='abilities_id'),
        ),
    ]
