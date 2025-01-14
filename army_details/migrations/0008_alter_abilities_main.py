# Generated by Django 4.2.17 on 2025-01-12 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('army_details', '0007_alter_stratagems_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abilities',
            name='main',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='abilities', to='army_details.factions'),
        ),
    ]
