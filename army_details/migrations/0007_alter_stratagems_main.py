# Generated by Django 4.2.17 on 2025-01-12 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('army_details', '0006_alter_abilities_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stratagems',
            name='main',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stratagems', to='army_details.factions'),
        ),
    ]
