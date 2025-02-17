# Generated by Django 4.2.17 on 2025-01-11 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('army_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abilities_id', models.CharField(max_length=15)),
                ('name', models.CharField()),
                ('legend', models.CharField()),
                ('description', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Datasheets',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('faction_id', models.CharField(verbose_name=5)),
                ('source_id', models.IntegerField()),
                ('legend', models.CharField()),
                ('role', models.CharField()),
                ('loadout', models.CharField()),
                ('transport', models.CharField()),
                ('virtual', models.BooleanField()),
                ('leader_head', models.CharField()),
                ('leader_footer', models.CharField()),
                ('damaged_w', models.CharField()),
                ('damaged_descp', models.CharField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='DatasheetsLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader_id', models.CharField(max_length=20)),
                ('attached_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LastUpdated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('edition', models.IntegerField()),
                ('version', models.FloatField(max_length=100)),
                ('errata_date', models.DateField(max_length=50)),
                ('errata_link', models.URLField(max_length=5000)),
            ],
        ),
        migrations.RemoveField(
            model_name='factions',
            name='abbrev_id',
        ),
        migrations.AlterField(
            model_name='factions',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Strategems',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type_char', models.CharField(max_length=1000)),
                ('cp_cost', models.IntegerField()),
                ('legend', models.CharField()),
                ('turn', models.CharField()),
                ('phase', models.CharField()),
                ('detachment', models.CharField()),
                ('description', models.CharField()),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategems', to='army_details.factions')),
            ],
        ),
        migrations.CreateModel(
            name='Enhancements',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('legend', models.CharField()),
                ('description', models.CharField()),
                ('cost', models.IntegerField()),
                ('detachment', models.CharField()),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enhancements', to='army_details.factions')),
            ],
        ),
        migrations.CreateModel(
            name='DetachmentAbilities',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('legend', models.CharField()),
                ('description', models.CharField()),
                ('detachment', models.CharField()),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detachment_abilities', to='army_details.factions')),
            ],
        ),
        migrations.CreateModel(
            name='DatashetsModelsCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField()),
                ('description', models.CharField()),
                ('cost', models.IntegerField()),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models_cost', to='army_details.datasheets')),
            ],
        ),
        migrations.CreateModel(
            name='DatasheetsWargear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.IntegerField()),
                ('line_in_wargear', models.IntegerField()),
                ('dice', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField()),
                ('range_char', models.IntegerField()),
                ('type_char', models.CharField()),
                ('attacks', models.IntegerField()),
                ('bs_ws', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('armour_pen', models.IntegerField()),
                ('damage', models.IntegerField()),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wargear', to='army_details.datasheets')),
            ],
        ),
        migrations.CreateModel(
            name='DatasheetsUnitComp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField()),
                ('description', models.CharField()),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_compisitions', to='army_details.datasheets')),
            ],
        ),
        migrations.CreateModel(
            name='DatasheetsStratagems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasheet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategems', to='army_details.datasheets')),
                ('strategem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasheets', to='army_details.strategems')),
            ],
        ),
        migrations.CreateModel(
            name='DatasheetsOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.IntegerField()),
                ('button', models.CharField()),
                ('description', models.CharField()),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_options', to='army_details.datasheets')),
            ],
        ),
        migrations.CreateModel(
            name='DatasheetsModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.IntegerField()),
                ('name', models.CharField()),
                ('move', models.CharField()),
                ('toughness', models.CharField()),
                ('invul_save', models.CharField()),
                ('invul_save_descr', models.CharField()),
                ('wounds', models.CharField()),
                ('leadership', models.CharField()),
                ('obj_control', models.CharField()),
                ('base_size', models.CharField()),
                ('base_size_desc', models.CharField()),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models_details', to='army_details.datasheets')),
            ],
        ),
        migrations.CreateModel(
            name='DatasheetsKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField()),
                ('model', models.CharField()),
                ('is_faction_keyword', models.BooleanField()),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faction_keywords', to='army_details.datasheets')),
            ],
        ),
        migrations.CreateModel(
            name='DatasheetsEnhancements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasheet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enhancements', to='army_details.datasheets')),
                ('enhancements_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasheets', to='army_details.enhancements')),
            ],
        ),
        migrations.CreateModel(
            name='DatasheetsDetachmentAbilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasheet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detachment_abilities', to='army_details.datasheets')),
                ('detachment_abilities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasheets', to='army_details.abilities')),
            ],
        ),
        migrations.CreateModel(
            name='DatasheetsAbilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.IntegerField()),
                ('model', models.CharField()),
                ('name', models.CharField()),
                ('description', models.CharField()),
                ('type_char', models.CharField()),
                ('parameter', models.CharField()),
                ('ability_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ability_id', to='army_details.abilities')),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abilities_set', to='army_details.datasheets')),
            ],
        ),
        migrations.AddField(
            model_name='abilities',
            name='main',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abilities', to='army_details.factions'),
        ),
    ]
