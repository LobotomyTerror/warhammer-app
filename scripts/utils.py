import csv
# import os
from datetime import datetime
from army_details.models import (
    Factions,
    Stratagems,
    Source,
    Abilities,
    Enhancements,
    Datasheets,
    DetachmentAbilities,
    DatasheetsDetachmentAbilities,
    DatasheetsAbilities,
    DatasheetsEnhancements,
    DatasheetsKeyword,
    DatasheetsLeader,
    DatasheetsModels,
    DatasheetsModelsCost,
    DatasheetsOptions,
    DatasheetsStratagems,
    DatasheetsUnitComp,
    DatasheetsWargear,
    LastUpdated
)

def run():
    with open("/Users/danielfishbein/Documents/warhammer-app/csv_files/Datasheets_models_cost.csv", newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter="|")
        DatasheetsModelsCost.objects.all().delete()

        count: int = 1
        for row in csvreader:
            if count == 1:
                pass
            else:
                print(row)
                # date_parsed = row[0].split()
                
                # LastUpdated.objects.create(
                #     date=date_parsed[0]
                # )
                
                # DatasheetsLeader.objects.create(
                #     attached_id=row[1],
                #     leader_id=row[0]
                # )
                
                # datasheet_id|detachment_ability_id|
                # DatasheetsDetachmentAbilities.objects.create(
                #     datasheet_id=row[0],
                #     detachment_abilities_id=row[1]
                # )
                
                # datasheet_id|enhancement_id|
                # DatasheetsEnhancements.objects.create(
                #     datasheet_id=row[0],
                #     enhancements_id=row[1]
                # )
                
                # datasheet_id|stratagem_id|
                # DatasheetsStratagems.objects.create(
                #     datasheet_id=row[0],
                #     stratagem_id=row[1]
                # )
                
                
                # datasheet_id|line|description|cost|
                DatasheetsModelsCost.objects.create(
                    line=row[1],
                    description=row[2],
                    cost=row[3],
                    main_id=row[0]
                )
                
                
                # datasheet_id|line|description|
                # DatasheetsUnitComp.objects.create(
                #     line=row[1],
                #     description=row[2],
                #     main_id=row[0]
                # )
                
                # datasheet_id|line|line_in_wargear|dice|name|description|range|type|A|BS_WS|S|AP|D|
                # DatasheetsWargear.objects.create(
                #     line=int(row[1]),
                #     line_in_wargear=int(row[2]),
                #     dice=row[3],
                #     name=row[4],
                #     description=row[5],
                #     range_char=row[6],
                #     type_char=row[7],
                #     attacks=row[8],
                #     bs_ws=row[9],
                #     strength=row[10],
                #     armour_pen=row[11],
                #     damage=row[12],
                #     main_id=row[0]
                # )

                # datasheet_id|line|button|description|
                # DatasheetsOptions.objects.create(
                #     line=row[1],
                #     button=row[2],
                #     description=row[3],
                #     main_id=row[0]
                # )
                
                # if count == 2:
                #     break
                # if row[6]:
                #     description = row[6]
                # else:
                #     description = None
                # datasheet_id|line|name|M|T|Sv|inv_sv|inv_sv_descr|W|Ld|OC|base_size|base_size_descr|
                # DatasheetsModels.objects.create(
                #     line=row[1],
                #     name=row[2],
                #     move=row[3],
                #     toughness=row[4],
                #     save_char=row[5],
                #     invul_save=row[6],
                #     invul_save_descr=row[7],
                #     wounds=row[8],
                #     leadership=row[9],
                #     obj_control=row[10],
                #     base_size=row[11],
                #     base_size_desc=row[12],
                #     main_id=row[0]
                # )
                
                
                # if row[3] == "false":
                #     faction_keyword = False
                # else:
                #     faction_keyword = True
                
                # DatasheetsKeyword.objects.create(
                #     keyword=row[1],
                #     model=row[2],
                #     is_faction_keyword=faction_keyword,
                #     main_id=row[0]
                # )
                
                
                # Factions.objects.create(
                #     id=row[0],
                #     name=row[1],
                #     link=row[2]
                # )
                # # id|name|type|edition|version|errata_date|errata_link|
                # if row[4]:
                #     version = float(row[4])
                # else:
                #     version = 0.0
                # parsed_date = datetime.strptime(row[5], "%d.%m.%Y %H:%M:%S")
                # Source.objects.create(
                #     id=row[0],
                #     name=row[1],
                #     type=row[2],
                #     edition=int(row[3]),
                #     version=version,
                #     errata_date=parsed_date,
                #     errata_link=row[6]
                # )
                # if row[0]:
                #     datasheet_id = row[0]
                # else:
                #     datasheet_id = None

                # if row[2]:
                #     abilities_id = row[2]
                # else:
                #     abilities_id = None

                # datasheet_id|line|ability_id|model|name|description|type|parameter|
                
                # DatasheetsAbilities.objects.create(
                #     line=int(row[1]),
                #     model=row[3],
                #     name=row[4],
                #     description=row[5],
                #     type_char=row[6],
                #     parameter=row[7],
                #     abilities_id=row[2],
                #     datasheets_id=datasheet_id
                # )
                
                # if row[2]:
                #     faction_id = row[2]
                # else:
                #     faction_id = None
                # if row[3]:
                #     source_id = row[3]
                # else:
                #     source_id = None
                # if row[8] == "false":
                #     virtual = False
                # else:
                #     virtual = True

                # id|name|faction_id|source_id|legend|role|loadout|transport|virtual|leader_head|leader_footer|damaged_w|damaged_description|link|
                # Datasheets.objects.create(
                #     id=row[0],
                #     name=row[1],
                #     faction_id=faction_id,
                #     source_id=source_id,
                #     legend=row[4],
                #     role=row[5],
                #     loadout=row[6],
                #     transport=row[7],
                #     virtual=virtual,
                #     leader_head=row[9],
                #     leader_footer=row[10],
                #     damaged_w=row[11],
                #     damaged_descp=row[12],
                #     link=row[13]
                # )
                
                # if row[1]:
                #     main_id = row[1]
                # else:
                #     main_id = None

                # # id|faction_id|name|legend|description|detachment|
                # DetachmentAbilities.objects.create(
                #     id=row[0],
                #     name=row[2],
                #     legend=row[3],
                #     description=row[4],
                #     detachment=row[5],
                #     main_id=main_id
                # )
                
                # if row[0]:
                #     main_id = row[0]
                # else:
                #     main_id = None

                # # faction_id|id|name|legend|description|cost|detachment|
                # Enhancements.objects.create(
                #     id=row[1],
                #     name=row[2],
                #     legend=row[3],
                #     description=row[4],
                #     cost=int(row[5]),
                #     detachment=row[6],
                #     main_id=main_id
                # )

                # id|name|legend|faction_id|description|
                # if count == 5:
                #     break
                # Factions.objects.create(
                #     id=row[0],
                #     name=row[1],
                #     link=row[2]
                # )
                
                # if row[3]:
                #     main_id = row[3]
                # else:
                #     main_id = None

                # Abilities.objects.create(
                #     abilities_id=row[0],
                #     name=row[1],
                #     legend=row[2],
                #     description=row[4],
                #     main_id=main_id
                # )
                
                # if row[0]:
                #     main_id = row[0]
                # else:
                #     main_id = None

                # Stratagems.objects.create(
                #     id=row[1],
                #     name=row[2],
                #     type_char=row[3],
                #     cp_cost=int(row[4]),
                #     legend=row[5],
                #     turn=row[6],
                #     phase=row[7],
                #     detachment=row[8],
                #     description=row[9],
                #     main_id=main_id
                # )
            count += 1
