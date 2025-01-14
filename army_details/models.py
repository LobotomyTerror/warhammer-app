from django.db import models


class Factions(models.Model):
    id = models.CharField(primary_key=True, max_length=5, blank=True)
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=1000)

    def __str__(self):
        return self.name


# id|name|type|edition|version|errata_date|errata_link|
class Source(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    edition = models.IntegerField()
    version = models.FloatField(max_length=100)
    errata_date = models.DateField(max_length=50)
    errata_link = models.URLField(max_length=5000)

    def __str__(self):
        return self.name


# faction_id|id|name|type|cp_cost|legend|turn|phase|detachment|description|
class Stratagems(models.Model):
    main = models.ForeignKey(Factions, on_delete=models.SET_NULL, related_name="stratagems", blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=100)
    type_char = models.CharField(max_length=1000)
    cp_cost = models.IntegerField()
    legend = models.CharField()
    turn = models.CharField()
    phase = models.CharField()
    detachment = models.CharField()
    description = models.CharField()

    def __str__(self):
        return self.name


# id|name|legend|faction_id|description|
class Abilities(models.Model):
    abilities_id = models.CharField(max_length=15)
    name = models.CharField()
    legend = models.CharField()
    main = models.ForeignKey(Factions, on_delete=models.SET_NULL, related_name="abilities", blank=True, null=True)
    description = models.CharField()

    def __str__(self):
        return self.name


# faction_id|id|name|legend|description|cost|detachment|
class Enhancements(models.Model):
    main = models.ForeignKey(Factions, on_delete=models.SET_NULL, related_name='enhancements', blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField()
    legend = models.CharField()
    description = models.CharField()
    cost = models.IntegerField()
    detachment = models.CharField()

    def __str__(self):
        return self.name


# id|faction_id|name|legend|description|detachment|
class DetachmentAbilities(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    main = models.ForeignKey(Factions, on_delete=models.SET_NULL, related_name='detachment_abilities', blank=True, null=True)
    name = models.CharField()
    legend = models.CharField()
    description = models.CharField()
    detachment = models.CharField()

    def __str__(self):
        return self.name
    

# id|name|faction_id|source_id|legend|role|loadout|transport|virtual|leader_head|leader_footer|damaged_w|damaged_description|link|
class Datasheets(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=100)
    faction = models.ForeignKey(Factions, on_delete=models.SET_NULL, related_name="datasheet_factions", blank=True, null=True)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, related_name="source_datasheets", blank=True, null=True)
    legend = models.CharField(blank=True, null=True)
    role = models.CharField(blank=True, null=True)
    loadout = models.CharField(blank=True, null=True)
    transport = models.CharField(blank=True, null=True)
    virtual = models.BooleanField(blank=True, null=True)
    leader_head = models.CharField(blank=True, null=True)
    leader_footer = models.CharField(blank=True, null=True)
    damaged_w = models.CharField(blank=True, null=True)
    damaged_descp = models.CharField(blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.name


# datasheet_id|line|ability_id|model|name|description|type|parameter|
class DatasheetsAbilities(models.Model):
    datasheets = models.ForeignKey(Datasheets, on_delete=models.SET_NULL, related_name="abilities_set", blank=True, null=True)
    line = models.IntegerField(blank=True, null=True)
    abilities_id = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    type_char = models.CharField(blank=True, null=True)
    parameter = models.CharField(blank=True, null=True)

    # @property
    # def abilities_id(self):
    #     return Abilities.objects.filter(abilities_id=self.abilities)

    def __str__(self):
        return self.name


# datasheet_id|keyword|model|is_faction_keyword|
class DatasheetsKeyword(models.Model):
    main = models.ForeignKey(Datasheets, on_delete=models.SET_NULL, related_name="faction_keywords", blank=True, null=True)
    keyword = models.CharField()
    model = models.CharField()
    is_faction_keyword = models.BooleanField()

    def __str__(self):
        return self.name


# datasheet_id|line|name|M|T|Sv|inv_sv|inv_sv_descr|W|Ld|OC|base_size|base_size_descr|
class DatasheetsModels(models.Model):
    main = models.ForeignKey(Datasheets, on_delete=models.SET_NULL, related_name="models_details", blank=True, null=True)
    line = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    move = models.CharField(blank=True, null=True)
    toughness = models.CharField(blank=True, null=True)
    save_char = models.CharField(blank=True, null=True)
    invul_save = models.CharField(blank=True, null=True)
    invul_save_descr = models.CharField(blank=True, null=True)
    wounds = models.CharField(blank=True, null=True)
    leadership = models.CharField(blank=True, null=True)
    obj_control = models.CharField(blank=True, null=True)
    base_size = models.CharField(blank=True, null=True)
    base_size_desc = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.name


# datasheet_id|line|button|description|
class DatasheetsOptions(models.Model):
    main = models.ForeignKey(Datasheets, on_delete=models.SET_NULL, related_name="model_options", blank=True, null=True)
    line = models.IntegerField()
    button = models.CharField()
    description = models.CharField()

    def __str__(self):
        return self.name


# datasheet_id|line|line_in_wargear|dice|name|description|range|type|A|BS_WS|S|AP|D|
class DatasheetsWargear(models.Model):
    main = models.ForeignKey(Datasheets, on_delete=models.SET_NULL, related_name="wargear", blank=True, null=True)
    line = models.IntegerField()
    line_in_wargear = models.IntegerField()
    dice = models.CharField()
    name = models.CharField(max_length=100)
    description = models.CharField()
    range_char = models.CharField()
    type_char = models.CharField()
    attacks = models.CharField()
    bs_ws = models.CharField()
    strength = models.CharField()
    armour_pen = models.CharField()
    damage = models.CharField()

    def __str__(self):
        return self.name


# datasheet_id|line|description|
class DatasheetsUnitComp(models.Model):
    main = models.ForeignKey(Datasheets, on_delete=models.SET_NULL, related_name="unit_compisitions", blank=True, null=True)
    line = models.CharField()
    description = models.CharField()


# datasheet_id|line|description|cost|
class DatasheetsModelsCost(models.Model):
    main = models.ForeignKey(Datasheets, on_delete=models.SET_NULL, related_name="models_cost", blank=True, null=True)
    line = models.CharField()
    description = models.CharField()
    cost = models.CharField()

    def __str__(self):
        return self.name


# datasheet_id|stratagem_id|
class DatasheetsStratagems(models.Model):
    datasheet = models.ForeignKey(Datasheets, on_delete=models.CASCADE, related_name="stratagems")
    stratagem = models.ForeignKey(Stratagems, on_delete=models.CASCADE, related_name='datasheets')

    def __str__(self):
        return self.name


# datasheet_id|enhancement_id|
class DatasheetsEnhancements(models.Model):
    datasheet = models.ForeignKey(Datasheets, on_delete=models.CASCADE, related_name="enhancements")
    enhancements = models.ForeignKey(Enhancements, on_delete=models.CASCADE, related_name="datasheets")

    def __str__(self):
        return self.name


# datasheet_id|detachment_ability_id|
class DatasheetsDetachmentAbilities(models.Model):
    datasheet = models.ForeignKey(Datasheets, on_delete=models.CASCADE, related_name="detachment_abilities")
    detachment_abilities = models.ForeignKey(DetachmentAbilities, on_delete=models.CASCADE, related_name="datasheets")

    def __str__(self):
        return self.name


# leader_id|attached_id|
class DatasheetsLeader(models.Model):
    leader = models.ForeignKey(Datasheets, on_delete=models.SET_NULL, related_name="leader_ids", blank=True, null=True)
    attached = models.ForeignKey(Datasheets, on_delete=models.SET_NULL, related_name="attached_ids", blank=True, null=True)

    def __str__(self):
        return self.name


# last_update|
class LastUpdated(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.name
