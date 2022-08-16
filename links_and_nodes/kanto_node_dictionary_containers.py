from class_definitions import Node


from links_and_nodes import kanto_all_warp_points_dict, johto_all_warp_points_dict

kmd = kanto_all_warp_points_dict.buildKantoWarpLinks()
johto = johto_all_warp_points_dict.buildJohtoWarpLinks()

print(kmd)

def buildKantoMajorNodes():
    MajorNodes_Kanto = dict()

#Pallet + Viridian + Pewter + Victoryroad Gate Entrance + Mount Moon Entrance(note: maybe split later?) 
    MajorNodes_Kanto['Pallet, Viridian, and Pewter Node'] = Node(
            [kmd["Pallet_Town_Links"].get(key) for key in kmd["Pallet_Town_Links"]]
        +   [kmd["Viridian_City_Links"].get(key) for key in kmd["Viridian_City_Links"]]
        +   [kmd["Route_22_Links"].get("ROUTE_22_TO_VICTORY_ROAD_GATE_1_LINK")]
        +   [kmd["Pewter_City_Links"].get(key) for key in kmd["Pewter_City_Links"]]
        +   [kmd["Route_3_Links"].get("ROUTE_3_TO_MOUNT_MOON_1_LINK")])

    #Cerulean (note: block on underground) (bikeshop closed) + route 5
    MajorNodes_Kanto['Cerulean City Node'] = Node(
            [kmd["Cerulean_City_Links"].get(key) for key in kmd["Cerulean_City_Links"]]
        +   [kmd["Route_25_Links"].get("ROUTE_25_TO_BILLS_HOUSE_1_LINK")]
        +   [kmd["Route_5_Links"].get("ROUTE_5_TO_ROUTE_5_CLEANSE_TAG_HOUSE_1_LINK")]
        +   [kmd["Route_5_Links"].get("ROUTE_5_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_1_LINK")]
        +   [kmd["Route_5_Links"].get("ROUTE_5_TO_ROUTE_5_SAFFRON_GATE_1_LINK")])

    #Vermillion (note: snorlax key) excluded gym + route 6
    MajorNodes_Kanto['Vermilion City Node'] = Node(
            [kmd["Vermilion_City_Links"].get(key) for key in kmd["Vermilion_City_Links"] if key not in
            [kmd["Vermilion_City_Links"].get("VERMILION_CITY_TO_VERMILION_GYM_1_LINK")] +
             [kmd["Vermilion_City_Links"].get("VERMILION_CITY_TO_VERMILION_PORT_PASSAGE_1_LINK")]]
        +   [kmd["Route_6_Links"].get("ROUTE_6_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_1_LINK")]
        +   [kmd["Route_6_Links"].get("ROUTE_6_TO_ROUTE_6_SAFFRON_GATE_3_LINK")])


    #Celadon + route 8 and 16 gates
    MajorNodes_Kanto['Celadon City Node'] = Node(
            [kmd["Celadon_City_Links"].get(key) for key in kmd["Celadon_City_Links"] if key not in
            [kmd["Celadon_City_Links"].get("CELADON_CITY_TO_CELADON_GYM_1_LINK")]]
        +   [kmd["Route_7_Links"].get("ROUTE_7_TO_ROUTE_7_SAFFRON_GATE_1_LINK")]
        +   [kmd["Route_16_Links"].get("ROUTE_16_TO_ROUTE_16_GATE_3_LINK")])

    #Lavender + rocktunnel entrance + route 7 gate + superrodhouse + route 15 gate
    MajorNodes_Kanto['Lavender Town Node'] = Node(
            [kmd["Lavender_Town_Links"].get(key) for key in kmd["Lavender_Town_Links"]]
        +   [kmd["Route_10_South_Links"].get("ROUTE_10_SOUTH_TO_ROCK_TUNNEL_1F_2_LINK")]
        +   [kmd["Route_8_Links"].get("ROUTE_8_TO_ROUTE_8_SAFFRON_GATE_3_LINK")]
        +   [kmd["Route_12_Links"].get("ROUTE_12_TO_ROUTE_12_SUPER_ROD_HOUSE_1_LINK")]
        +   [kmd["Route_15_Links"].get("ROUTE_15_TO_ROUTE_15_FUCHSIA_GATE_3_LINK")]) #(#todo make this gate a dead end for less pain ?)

    #Saffron
    MajorNodes_Kanto['Saffron City Node'] = Node(
            [kmd["Saffron_City_Links"].get(key) for key in kmd["Saffron_City_Links"]])

    #Fuchsia + gates
    MajorNodes_Kanto['Fuchsia City Node'] = Node(
            [kmd["Fuchsia_City_Links"].get(key) for key in kmd["Fuchsia_City_Links"] if key not in
            [kmd["Fuchsia_City_Links"].get("FUCHSIA_CITY_TO_FUCHSIA_MART_2_LINK")]]
        +   [kmd["Route_18_Links"].get("ROUTE_18_TO_ROUTE_17_ROUTE_18_GATE_3_LINK")])

    return MajorNodes_Kanto

def buildKantoImportantDeadEnds():
    ImportantDeadEndNodes_Kanto = dict()

# Route 2 Gates Entrances bottom
    ImportantDeadEndNodes_Kanto['Route 02 Gate Exterior (Bottom Side) Node'] = Node(
        [kmd["Route_2_Links"].get("ROUTE_2_TO_ROUTE_2_GATE_3_LINK")]
    )
# Route 2 Gates Entrances top
    ImportantDeadEndNodes_Kanto['Route 02 Gate Exterior (Top Side) Node'] = Node(
        [kmd["Route_2_Links"].get("ROUTE_2_TO_ROUTE_2_GATE_1_LINK")]
    )
# Mount Moon Ledge (unimportant?)
    ImportantDeadEndNodes_Kanto['Mount Moon (Above Ledge) Node'] = Node(
        [kmd["Mount_Moon_Links"].get("MOUNT_MOON_TO_MOUNT_MOON_8_LINK")]
    )
# Route 4 Cerulean Ledge (unimportant?)
    ImportantDeadEndNodes_Kanto['Route 04 (Above Ledge) Node'] = Node(
        [kmd["Route_4_Links"].get("ROUTE_4_TO_MOUNT_MOON_2_LINK")]
    )
# Powerplant Exterior
    ImportantDeadEndNodes_Kanto['Power Plant Exterior Node'] = Node(
        [kmd["Route_10_North_Links"].get("ROUTE_10_NORTH_TO_POWER_PLANT_1_LINK")]
    )
# Surge Exterior
    ImportantDeadEndNodes_Kanto['Vermillion Gym Exterior Node'] = Node(
        [kmd["Vermilion_City_Links"].get("VERMILION_CITY_TO_VERMILION_GYM_1_LINK")]
    )

# Erika Exterior
    ImportantDeadEndNodes_Kanto['Celadon Gym Exterior Node'] = Node(
        [kmd["Celadon_City_Links"].get("CELADON_CITY_TO_CELADON_GYM_1_LINK")]
    )
# Route 16 Cycling Road House
    ImportantDeadEndNodes_Kanto['Route 16 Fuchsia Speech House Exterior Node'] = Node(
        [kmd["Route_16_Links"].get("ROUTE_16_TO_ROUTE_16_FUCHSIA_SPEECH_HOUSE_1_LINK")]
    )
# Fuchsia Market
    ImportantDeadEndNodes_Kanto['Fuchsia Mart Exterior Node'] = Node(
        [kmd["Fuchsia_City_Links"].get("FUCHSIA_CITY_TO_FUCHSIA_MART_2_LINK")]
    )
# Route 19 Fuchsia Gate
    ImportantDeadEndNodes_Kanto['Route 19 Gate Exterior Node'] = Node(
        [kmd["Route_19_Links"].get("ROUTE_19_TO_ROUTE_19_FUCHSIA_GATE_3_LINK")]
    )
# Cinnabar PokeCenter Exterior
    ImportantDeadEndNodes_Kanto['Cinnabar Pokecenter Exterior Node'] = Node(
        [kmd["Cinnabar_Island_Links"].get("CINNABAR_ISLAND_TO_CINNABAR_POKECENTER_1F_1_LINK")]
    )
# Cinnabar Blain Exterior
    ImportantDeadEndNodes_Kanto['Seafoam_Gym_Exterior_Node'] = Node(
        [kmd["Route_20_Links"].get("ROUTE_20_TO_SEAFOAM_GYM_1_LINK")]
    )
# # Vermillion Port Ship Entrance
#     Vermilion_Port_Node = Node(
#         [kmd["Vermilion_Port_Links"]VERMILION_PORT_TO_VERMILION_PORT_PASSAGE_5_LINK]
#     )

#Interior Nodes
# Powerplant
    ImportantDeadEndNodes_Kanto['Power Plant Node'] = Node(
        [kmd["Power_Plant_Links"].get("POWER_PLANT_TO_ROUTE_10_NORTH_2_LINK")]
    )
# Route 12 Superrod House
    ImportantDeadEndNodes_Kanto['Route 12 Super Rod House Node'] = Node(
        [kmd["Route_12_Super_Rod_House_Links"].get("ROUTE_12_SUPER_ROD_HOUSE_TO_ROUTE_12_1_LINK")]
    )
# Pallet Oaks Lab
    ImportantDeadEndNodes_Kanto['Oaks Lab Node'] = Node(
        [kmd["Oaks_Lab_Links"].get("OAKS_LAB_TO_PALLET_TOWN_3_LINK")]
    )
# Mount Moon Mart
    ImportantDeadEndNodes_Kanto['Mount Moon Gift Shop Node'] = Node(
        [kmd["Mount_Moon_Gift_Shop_Links"].get("MOUNT_MOON_TO_ROUTE_3_1_LINK")]
    )
# Route 2 Nugget House
    ImportantDeadEndNodes_Kanto['Route 02 Nugget House Node'] = Node(
        [kmd["Route_2_Nugget_House_Links"].get("ROUTE_2_NUGGET_HOUSE_TO_ROUTE_2_1_LINK")]
    )
# Viridian TrainerHouse B1F
    ImportantDeadEndNodes_Kanto['Trainer House B1F Node'] = Node(
        [kmd["Trainer_House_B1F_Links"].get("TRAINER_HOUSE_B1F_TO_TRAINER_HOUSE_1F_3_LINK")]
    )
# Viridian Gym
    ImportantDeadEndNodes_Kanto['Viridian Gym Node'] = Node(
        [kmd["Viridian_Gym_Links"].get("VIRIDIAN_GYM_TO_VIRIDIAN_CITY_1_LINK")]
    )
# Viridian Mart
    ImportantDeadEndNodes_Kanto['Viridian Mart Node'] = Node(
        [kmd["Viridian_Mart_Links"].get("VIRIDIAN_MART_TO_VIRIDIAN_CITY_4_LINK")]
    )
# Pewter Gym
    ImportantDeadEndNodes_Kanto['Pewter Gym Node'] = Node(
        [kmd["Pewter_Gym_Links"].get("PEWTER_GYM_TO_PEWTER_CITY_2_LINK")]
    )
# Pewter Mart
    ImportantDeadEndNodes_Kanto['Pewter Mart Node'] = Node(
        [kmd["Pewter_Mart_Links"].get("PEWTER_MART_TO_PEWTER_CITY_3_LINK")]
    )
# Cerulean BillHouse
    ImportantDeadEndNodes_Kanto['Route 25 Bills House Node'] = Node(
        [kmd["Bills_House_Links"].get("BILLS_HOUSE_TO_ROUTE_25_1_LINK")]
    )
# Cerulean Gym
    ImportantDeadEndNodes_Kanto['Cerulean Gym Node'] = Node(
        [kmd["Cerulean_Gym_Links"].get("CERULEAN_GYM_TO_CERULEAN_CITY_5_LINK")]
    )
# Cerulean Mart
    ImportantDeadEndNodes_Kanto['Cerulean Mart Node'] = Node(
        [kmd["Cerulean_Mart_Links"].get("CERULEAN_MART_TO_CERULEAN_CITY_6_LINK")]
    )
# Route Route5CleanseTagHouse
    ImportantDeadEndNodes_Kanto['Route 05 Cleanse Tag House Node'] = Node(
        [kmd["Route_5_Cleanse_Tag_House_Links"].get("ROUTE_5_CLEANSE_TAG_HOUSE_TO_ROUTE_5_4_LINK")]
    )
# Vermillion Gym
    ImportantDeadEndNodes_Kanto['Vermilion Gym Node'] = Node(
        [kmd["Vermilion_Gym_Links"].get("VERMILION_GYM_TO_VERMILION_CITY_7_LINK")]
    )
# Vermillion Mart
    ImportantDeadEndNodes_Kanto['Vermilion Mart Node'] = Node(
        [kmd["Vermilion_Mart_Links"].get("VERMILION_MART_TO_VERMILION_CITY_5_LINK")]
    )
# Vermillion PokemonFanClub
    ImportantDeadEndNodes_Kanto['Vermilion Pokemon Fan Club Node'] = Node(
        [kmd["Pokemon_Fan_Club_Links"].get("POKEMON_FAN_CLUB_TO_VERMILION_CITY_3_LINK")]
    )
# Lavender Mart
    ImportantDeadEndNodes_Kanto['Lavender Mart Node'] = Node(
        [kmd["Lavender_Mart_Links"].get("LAVENDER_MART_TO_LAVENDER_TOWN_5_LINK")]
    )
# Lavender NameRater
    ImportantDeadEndNodes_Kanto['Lavender Name Rater Node'] = Node(
        [kmd["Lavender_Name_Rater_Links"].get("LAVENDER_NAME_RATER_TO_LAVENDER_TOWN_4_LINK")]
    )
# Lavender RadioTower
    ImportantDeadEndNodes_Kanto['Lavender Radio Tower 1F Node'] = Node(
        [kmd["Lav_Radio_Tower_1F_Links"].get("LAV_RADIO_TOWER_1F_TO_LAVENDER_TOWN_7_LINK")]
    )
# Celadon Cafe
    ImportantDeadEndNodes_Kanto['Celadon Cafe Node'] = Node(
        [kmd["Celadon_Cafe_Links"].get("CELADON_CAFE_TO_CELADON_CITY_9_LINK")]
    )
# Celadon Game Corner
    ImportantDeadEndNodes_Kanto['Celadon Game Corner Node'] = Node(
        [kmd["Celadon_Game_Corner_Links"].get("CELADON_GAME_CORNER_TO_CELADON_CITY_6_LINK")]
    )
# Celadon Game Corner Prize
    ImportantDeadEndNodes_Kanto['Celadon Game Corner Prize Room Node'] = Node(
        [kmd["Celadon_Game_Corner_Prize_Room_Links"].get("CELADON_GAME_CORNER_PRIZE_ROOM_TO_CELADON_CITY_7_LINK")]
    )
# Celadon Gym
    ImportantDeadEndNodes_Kanto['Celadon Gym Node'] = Node(
        [kmd["Celadon_Gym_Links"].get("CELADON_GYM_TO_CELADON_CITY_8_LINK")]
    )
# Celadon Roof House Back
    ImportantDeadEndNodes_Kanto['Celadon Mansion Roof House Node'] = Node(
        [kmd["Celadon_Mansion_Roof_House_Links"].get("CELADON_MANSION_ROOF_HOUSE_TO_CELADON_MANSION_ROOF_3_LINK")]
    )
# Saffron Copycat House 2F
    ImportantDeadEndNodes_Kanto['Saffron Copycats House 2F Node'] = Node(
        [kmd["Copycats_House_2F_Links"].get("COPYCATS_HOUSE_2F_TO_COPYCATS_HOUSE_1F_3_LINK")]
    )
# Saffron Fighting Dojo
    ImportantDeadEndNodes_Kanto['Saffron Fighting Dojo Node'] = Node(
        [kmd["Fighting_Dojo_Links"].get("FIGHTING_DOJO_TO_SAFFRON_CITY_1_LINK")]
    )
# Saffron Mr Psychic House
    ImportantDeadEndNodes_Kanto['Saffron Mr Psychics House Node'] = Node(
        [kmd["Mr_Psychics_House_Links"].get("MR_PSYCHICS_HOUSE_TO_SAFFRON_CITY_5_LINK")]
    )
# Saffron Gym
    ImportantDeadEndNodes_Kanto['Saffron Gym Node'] = Node(
        [kmd["Saffron_Gym_Links"].get("SAFFRON_GYM_TO_SAFFRON_CITY_2_LINK")]
    )
# Saffron MagnetTrain
    ImportantDeadEndNodes_Kanto['Saffron Magnet Train Station Node'] = Node(
        [kmd["Saffron_Magnet_Train_Station_Links"].get("SAFFRON_MAGNET_TRAIN_STATION_TO_SAFFRON_CITY_6_LINK")]
    )
# Saffron Mart
    ImportantDeadEndNodes_Kanto['Saffron Mart Node'] = Node(
        [kmd["Saffron_Mart_Links"].get("SAFFRON_MART_TO_SAFFRON_CITY_3_LINK")]
    )
# Saffron SilphCo
    ImportantDeadEndNodes_Kanto['Saffron Silph Co 1F Node'] = Node(
        [kmd["Silph_Co_1F_Links"].get("SILPH_CO_1F_TO_SAFFRON_CITY_7_LINK")]
    )
# Fuchsia Gym
    ImportantDeadEndNodes_Kanto['Fuchsia Gym Node'] = Node(
        [kmd["Fuchsia_Gym_Links"].get("FUCHSIA_GYM_TO_FUCHSIA_CITY_3_LINK")]
    )
# Fuchsia Mart
    ImportantDeadEndNodes_Kanto['Fuchsia Mart Node'] = Node(
        [kmd["Fuchsia_Mart_Links"].get("FUCHSIA_MART_TO_FUCHSIA_CITY_1_LINK")]
    )
# Cinnabar Gym
    ImportantDeadEndNodes_Kanto['Seafoam Gym Node'] = Node(
        [kmd["Seafoam_Gym_Links"].get("SEAFOAM_GYM_TO_ROUTE_20_1_LINK")]
    )
#Gate Route16
    ImportantDeadEndNodes_Kanto['Route 16 Gate Right Node'] = Node(
        [kmd["Route_16_Gate_Links"].get("ROUTE_16_GATE_TO_ROUTE_16_2_LINK")]
    )

    ImportantDeadEndNodes_Kanto['Route 16 Gate Left Node'] = Node(
        [kmd["Route_16_Gate_Links"].get("ROUTE_16_GATE_TO_ROUTE_16_4_LINK")]
    )

#Gate Route17 - 18
    ImportantDeadEndNodes_Kanto['Route 17 Route 18 Gate Left Node'] = Node(
        [kmd["Route_17_Route_18_Gate_Links"].get("ROUTE_17_ROUTE_18_GATE_TO_ROUTE_17_1_LINK")]
    )

    ImportantDeadEndNodes_Kanto['Route 17 Route 18 Gate Right Node'] = Node(
        [kmd["Route_17_Route_18_Gate_Links"].get("ROUTE_17_ROUTE_18_GATE_TO_ROUTE_18_1_LINK")]
    )
# #Fast Ship Cabin Warp 4 lazy sailor
#     Fast_Ship_Cabins_NNW_NNE_NE_Cabin_4_Node = Node(
#         [kmd["Fast_Ship_Cabins_NNW_NNE_NE_Links"]FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_4_LINK]
#     )
# #Fast Ship Cabin Warp 5 player cabin
#     Fast_Ship_Cabins_SW_SSW_NW_Cabin_5_Node = Node(
#         [kmd["Fast_Ship_Cabins_SW_SSW_NW_Links"]FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_5_LINK]
#     )
# #Fast Ship Cabin Warp 10 captain
#     Fast_Ship_Cabins_SE_SSE_Captains_Cabin_10_Node = Node(
#         [kmd["Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links"]FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_10_LINK]
#     )
    ImportantDeadEndNodes_Kanto['Route 28 Steel Wing House Node'] = Node(
        [kmd["Route_28_Steel_Wing_House_Links"].get("ROUTE_28_STEEL_WING_HOUSE_TO_ROUTE_28_1_LINK")]
    )

    ImportantDeadEndNodes_Kanto['Useless Route 28 Steel Wing House Exterior Node'] = Node(
        [kmd["Route_28_Links"].get("ROUTE_28_TO_ROUTE_28_STEEL_WING_HOUSE_1_LINK")]
    )

    ImportantDeadEndNodes_Kanto['Silver Cave Room 2 Item Node 1'] = Node(
        [kmd["Silver_Cave_Room_2_Links"].get("SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_1_LINK")]
    )

    ImportantDeadEndNodes_Kanto['Silver Cave Room 2 Item Node 2'] = Node(
        [kmd["Silver_Cave_Room_2_Links"].get("SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_2_LINK")]
    )

    ImportantDeadEndNodes_Kanto['Silver_Cave_Item_Room_1_Node'] = Node(
        [kmd["Silver_Cave_Item_Rooms_Links"].get("SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_3_LINK")]
    )

    ImportantDeadEndNodes_Kanto['Silver Cave Item Room 2 Node'] = Node(
        [kmd["Silver_Cave_Item_Rooms_Links"].get("SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_4_LINK")]
    )

    return ImportantDeadEndNodes_Kanto

# class ReachableUselessDeadEndNodes_Kanto(Enum):
#     pass

def buildKantoUselessDeadEnds():
    UnreachableUselessDeadEndNodes_Kanto = dict()

#All Interiors
# Route 16 Cycling Road House
    UnreachableUselessDeadEndNodes_Kanto['Route 16 Fuchsia Speech House Node'] = Node(
        [kmd["Route_16_Fuchsia_Speech_House_Links"].get("ROUTE_16_FUCHSIA_SPEECH_HOUSE_TO_ROUTE_16_1_LINK")]
    )
# Pallet Blues House
    UnreachableUselessDeadEndNodes_Kanto['Blues House Node'] = Node(
        [kmd["Blues_House_Links"].get("BLUES_HOUSE_TO_PALLET_TOWN_2_LINK")]
    )
# Pallet Reds House 2F
    UnreachableUselessDeadEndNodes_Kanto['Reds House 2F Node'] = Node(
        [kmd["Reds_House_2F_Links"].get("REDS_HOUSE_2F_TO_REDS_HOUSE_1F_3_LINK")]
    )
# Viridian NicknameSpeechHouse
    UnreachableUselessDeadEndNodes_Kanto['Viridian Nickname Speech House Node'] = Node(
        [kmd["Viridian_Nickname_Speech_House_Links"].get("VIRIDIAN_NICKNAME_SPEECH_HOUSE_TO_VIRIDIAN_CITY_2_LINK")]
    )
# Pewter NidoranSpeechHouse
    UnreachableUselessDeadEndNodes_Kanto['Pewter Nidoran Speech House Node'] = Node(
        [kmd["Pewter_Nidoran_Speech_House_Links"].get("PEWTER_NIDORAN_SPEECH_HOUSE_TO_PEWTER_CITY_1_LINK")]
    )
# Pewter SnoozeSpeechHouse
    UnreachableUselessDeadEndNodes_Kanto['Pewter Snooze Speech House Node'] = Node(
        [kmd["Pewter_Snooze_Speech_House_Links"].get("PEWTER_SNOOZE_SPEECH_HOUSE_TO_PEWTER_CITY_5_LINK")]
    )
# Cerulean GymBadgeSpeechHouse
    UnreachableUselessDeadEndNodes_Kanto['Cerulean Gym Badge Speech House Node'] = Node(
        [kmd["Cerulean_Gym_Badge_Speech_House_Links"].get("CERULEAN_GYM_BADGE_SPEECH_HOUSE_TO_CERULEAN_CITY_1_LINK")]
    )
# Cerulean PoliceStation
    UnreachableUselessDeadEndNodes_Kanto['Cerulean Police Station Node'] = Node(
        [kmd["Cerulean_Police_Station_Links"].get("CERULEAN_POLICE_STATION_TO_CERULEAN_CITY_2_LINK")]
    )
# Cerulean TradespeechHouse
    UnreachableUselessDeadEndNodes_Kanto['Cerulean Trade Speech House Node'] = Node(
        [kmd["Cerulean_Trade_Speech_House_Links"].get("CERULEAN_TRADE_SPEECH_HOUSE_TO_CERULEAN_CITY_3_LINK")]
    )
# Vermillion DiglettCaveSpeechHouse
    UnreachableUselessDeadEndNodes_Kanto['Vermilion Digletts Cave Speech House Node'] = Node(
        [kmd["Vermilion_Digletts_Cave_Speech_House_Links"].get("VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_TO_VERMILION_CITY_6_LINK")]
    )
# Vermillion FishingSpeechHouse
    UnreachableUselessDeadEndNodes_Kanto['Vermilion Fishing Speech House Node'] = Node(
        [kmd["Vermilion_Fishing_Speech_House_Links"].get("VERMILION_FISHING_SPEECH_HOUSE_TO_VERMILION_CITY_1_LINK")]
    )
# Vermillion MagnetTrainSpeechHouse
    UnreachableUselessDeadEndNodes_Kanto['Vermilion Magnet Train Speech House Node'] = Node(
        [kmd["Vermilion_Magnet_Train_Speech_House_Links"].get("VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_TO_VERMILION_CITY_4_LINK")]
    )
# Lavender SpeechHouse
    UnreachableUselessDeadEndNodes_Kanto['Lavender Speech House Node'] = Node(
        [kmd["Lavender_Speech_House_Links"].get("LAVENDER_SPEECH_HOUSE_TO_LAVENDER_TOWN_3_LINK")]
    )
# Lavender MrFujiHouse
    UnreachableUselessDeadEndNodes_Kanto['Mr Fujis House Node'] = Node(
        [kmd["Mr_Fujis_House_Links"].get("MR_FUJIS_HOUSE_TO_LAVENDER_TOWN_2_LINK")]
    )
# Lavender SoulHouse
    UnreachableUselessDeadEndNodes_Kanto['Soul House Node'] = Node(
        [kmd["Soul_House_Links"].get("SOUL_HOUSE_TO_LAVENDER_TOWN_6_LINK")]
    )
# Celadon Roof Front
    UnreachableUselessDeadEndNodes_Kanto['Celadon Mansion Roof Node'] = Node(
        [kmd["Celadon_Mansion_Roof_Links"].get("CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_4_LINK")]
    )
# Fuchsia BillsBrother House
    UnreachableUselessDeadEndNodes_Kanto['Bills Brothers House Node'] = Node(
        [kmd["Bills_Brothers_House_Links"].get("BILLS_BROTHERS_HOUSE_TO_FUCHSIA_CITY_4_LINK")]
    )
# Fuchsia SafariZone Main Office
    UnreachableUselessDeadEndNodes_Kanto['Safari Zone Main Office Node'] = Node(
        [kmd["Safari_Zone_Main_Office_Links"].get("SAFARI_ZONE_MAIN_OFFICE_TO_FUCHSIA_CITY_2_LINK")]
    )
# Fuchsia SafariZone Wardens Home
    UnreachableUselessDeadEndNodes_Kanto['Safari Zone Wardens Home Node'] = Node(
        [kmd["Safari_Zone_Wardens_Home_Links"].get("SAFARI_ZONE_WARDENS_HOME_TO_FUCHSIA_CITY_6_LINK")]
    )

#Fast Ship Cabin Warp 2
    UnreachableUselessDeadEndNodes_Kanto['Fast Ship Cabins NNW NNE NE Cabin 2 Node'] = Node(
        [kmd["Fast_Ship_Cabins_NNW_NNE_NE_Links"].get("FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_2_LINK")]
    )
#Fast Ship Cabin Warp 3
    UnreachableUselessDeadEndNodes_Kanto['Fast Ship Cabins NNW NNE NE Cabin 3 Node'] = Node(
        [kmd["Fast_Ship_Cabins_NNW_NNE_NE_Links"].get("FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_3_LINK")]
    )
#Fast Ship Cabin Warp 5
    # Fast_Ship_Cabins_SW_SSW_NW_Cabin_5_Node = Node(
    #     [kmd["Fast_Ship_Cabins_SW_SSW_NW_Links"]FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_5_LINK]
    # )
#Fast Ship Cabin Warp 6
    UnreachableUselessDeadEndNodes_Kanto['Fast Ship Cabins SW SSW NW Cabin 6 Node'] = Node(
        [kmd["Fast_Ship_Cabins_SW_SSW_NW_Links"].get("FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_6_LINK")]
    )
#Fast Ship Cabin Warp 7
    UnreachableUselessDeadEndNodes_Kanto['Fast Ship Cabins SW SSW NW Cabin 7 Node'] = Node(
        [kmd["Fast_Ship_Cabins_SW_SSW_NW_Links"].get("FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_7_LINK")]
    )
#Fast Ship Cabin Warp 8
    UnreachableUselessDeadEndNodes_Kanto['Fast Ship Cabins SE SSE Captains Cabin 8 Node'] = Node(
        [kmd["Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links"].get("FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_8_LINK")]
    )
#Fast Ship Cabin Warp 9
    # Fast_Ship_Cabins_SE_SSE_Captains_Cabin_9_Node = Node(
    #     [kmd["Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links"]FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_9_LINK]
    # )
    return UnreachableUselessDeadEndNodes_Kanto

def buildKantoCorridors():
    TwoWayCorridorNodes_Kanto = dict()

    TwoWayCorridorNodes_Kanto['Silver Cave Room 1 Corridor Node'] = Node(
        [kmd["Silver_Cave_Room_1_Links"].get(key) for key in kmd["Silver_Cave_Room_1_Links"]]
    )

    TwoWayCorridorNodes_Kanto['Silver Cave Room 2 Corridor Node'] = Node(
        [kmd["Silver_Cave_Room_2_Links"].get("SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_1_2_LINK"),
         kmd["Silver_Cave_Room_2_Links"].get("SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_3_1_LINK")]
    )

    TwoWayCorridorNodes_Kanto['Silver Cave Pokecenter 1F_Node'] = Node(
        [kmd["Silver_Cave_Pokecenter_1F_Links"].get(key) for key in kmd["Silver_Cave_Pokecenter_1F_Links"]]
    )

#Outside Diglett - Pewter
    TwoWayCorridorNodes_Kanto['Route 02 Diglett Cave To Nugget House_Node'] = Node(
        [kmd["Route_2_Links"].get("ROUTE_2_TO_ROUTE_2_NUGGET_HOUSE_1_LINK"),
         kmd["Route_2_Links"].get("ROUTE_2_TO_DIGLETTS_CAVE_3_LINK")]
    )
#Diglett Cave
    TwoWayCorridorNodes_Kanto['Digletts Cave Vermillion Side Node'] = Node(
        [kmd["Digletts_Cave_Links"].get("DIGLETTS_CAVE_TO_VERMILION_CITY_10_LINK"),
         kmd["Digletts_Cave_Links"].get("DIGLETTS_CAVE_TO_DIGLETTS_CAVE_5_LINK")]
    )
#Diglett Cave
    TwoWayCorridorNodes_Kanto['Digletts Cave Route 2 Side Node'] = Node(
        [kmd["Digletts_Cave_Links"].get("DIGLETTS_CAVE_TO_ROUTE_2_5_LINK"),
         kmd["Digletts_Cave_Links"].get("DIGLETTS_CAVE_TO_DIGLETTS_CAVE_6_LINK")]
    )
#Diglett Cave
    TwoWayCorridorNodes_Kanto['Digletts Cave Main Tunnel Node'] = Node(
        [kmd["Digletts_Cave_Links"].get("DIGLETTS_CAVE_TO_DIGLETTS_CAVE_2_LINK"),
         kmd["Digletts_Cave_Links"].get("DIGLETTS_CAVE_TO_DIGLETTS_CAVE_4_LINK")]
    )
#Pkmcenter - Rocktunnel Route 9,10
    TwoWayCorridorNodes_Kanto['Route 10 Pokecenter To Rock Tunnel Node'] = Node(
        [kmd["Route_10_North_Links"].get("ROUTE_10_NORTH_TO_ROUTE_10_POKECENTER_1F_1_LINK"),
         kmd["Route_9_Links"].get("ROUTE_9_TO_ROCK_TUNNEL_1F_1_LINK")]
    )
#Cycling Road Route 17
    TwoWayCorridorNodes_Kanto['Route 16 Route 17 Node'] = Node(
        [kmd["Route_17_Links"].get("ROUTE_17_TO_ROUTE_17_ROUTE_18_GATE_1_LINK"),
         kmd["Route_16_Links"].get("ROUTE_16_TO_ROUTE_16_GATE_1_LINK")]
    )
#Kanto Underground
    TwoWayCorridorNodes_Kanto['Underground Path Node'] = Node(
        [kmd["Underground_Path_Links"].get("UNDERGROUND_PATH_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_3_LINK"),
         kmd["Underground_Path_Links"].get("UNDERGROUND_PATH_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_3_LINK")]
    )
#Vermillion Port Passage
#     Vermilion_Port_Passage_Entrance_Node = Node(
#         [kmd["Vermilion_Port_Passage_Links"]VERMILION_PORT_PASSAGE_TO_VERMILION_CITY_8_LINK,
#          kmd["Vermilion_Port_Passage_Links"]VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_PASSAGE_4_LINK]
#     )
# #Vermillion Port Passage
#     Vermilion_Port_Passage_Tunnel_Node = Node(
#         [kmd["Vermilion_Port_Passage_Links"]VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_PASSAGE_3_LINK,
#          kmd["Vermilion_Port_Passage_Links"]VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_1_LINK]
#     )
#Rocktunnel 1F
    TwoWayCorridorNodes_Kanto['Rock Tunnel 1F Route 9 Side Node'] = Node(
        [kmd["Rock_Tunnel_1F_Links"].get("ROCK_TUNNEL_1F_TO_ROUTE_9_1_LINK"),
         kmd["Rock_Tunnel_1F_Links"].get("ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_4_LINK")]
    )
#Rocktunnel 1F
    TwoWayCorridorNodes_Kanto['Rock Tunnel 1F Lavender Side Node'] = Node(
        [kmd["Rock_Tunnel_1F_Links"].get("ROCK_TUNNEL_1F_TO_ROUTE_10_SOUTH_1_LINK"),
         kmd["Rock_Tunnel_1F_Links"].get("ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_1_LINK")]
    )
#Rocktunnel 1F
    TwoWayCorridorNodes_Kanto['Rock Tunnel 1F Middle Part Node'] = Node(
        [kmd["Rock_Tunnel_1F_Links"].get("ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_3_LINK"),
         kmd["Rock_Tunnel_1F_Links"].get("ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_2_LINK")]
    )
#Rocktunnel B1F
    TwoWayCorridorNodes_Kanto['Rock Tunnel B1F NW Node'] = Node(
        [kmd["Rock_Tunnel_B1F_Links"].get("ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_6_LINK"),
         kmd["Rock_Tunnel_B1F_Links"].get("ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_4_LINK")]
    )
#Rocktunnel B1F
    TwoWayCorridorNodes_Kanto['Rock Tunnel B1F SE Node'] = Node(
        [kmd["Rock_Tunnel_B1F_Links"].get("ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_3_LINK"),
         kmd["Rock_Tunnel_B1F_Links"].get("ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_5_LINK")]
    )
#Mount Moon inbetween
    TwoWayCorridorNodes_Kanto['Mount Moon Entrance NE Node'] = Node(
        [kmd["Mount_Moon_Links"].get("MOUNT_MOON_TO_MOUNT_MOON_SQUARE_1_LINK"),
         kmd["Mount_Moon_Links"].get("MOUNT_MOON_TO_MOUNT_MOON_3_LINK")]
    )
#Mount Moon inbetween
    TwoWayCorridorNodes_Kanto['Mount Moon Entrance SE Node'] = Node(
        [kmd["Mount_Moon_Links"].get("MOUNT_MOON_TO_MOUNT_MOON_SQUARE_2_LINK"),
         kmd["Mount_Moon_Links"].get("MOUNT_MOON_TO_MOUNT_MOON_4_LINK")]
    )
#PokemonCenter Route 10 Inside
    TwoWayCorridorNodes_Kanto['Route 10 Pokecenter 1F Node'] = Node(
        [kmd["Route_10_Pokecenter_1F_Links"].get("ROUTE_10_POKECENTER_1F_TO_ROUTE_10_NORTH_1_LINK"),
         kmd["Route_10_Pokecenter_1F_Links"].get("ROUTE_10_POKECENTER_1F_TO_POKECENTER_2F_1_LINK")]
    )
#PokemonCenter Viridian
    TwoWayCorridorNodes_Kanto['Viridian Pokecenter 1F Node'] = Node(
        [kmd["Viridian_Pokecenter_1F_Links"].get("VIRIDIAN_POKECENTER_1F_TO_VIRIDIAN_CITY_5_LINK"),
         kmd["Viridian_Pokecenter_1F_Links"].get("VIRIDIAN_POKECENTER_1F_TO_POKECENTER_2F_1_LINK")]
    )
#PokemonCenter Pewter
    TwoWayCorridorNodes_Kanto['Pewter Pokecenter 1F Node'] = Node(
        [kmd["Pewter_Pokecenter_1F_Links"].get("PEWTER_POKECENTER_1F_TO_PEWTER_CITY_4_LINK"),
         kmd["Pewter_Pokecenter_1F_Links"].get("PEWTER_POKECENTER_1F_TO_POKECENTER_2F_1_LINK")]
    )
#PokemonCenter Cerulean
    TwoWayCorridorNodes_Kanto['Cerulean Pokecenter 1F Node'] = Node(
        [kmd["Cerulean_Pokecenter_1F_Links"].get("CERULEAN_POKECENTER_1F_TO_CERULEAN_CITY_4_LINK"),
         kmd["Cerulean_Pokecenter_1F_Links"].get("CERULEAN_POKECENTER_1F_TO_POKECENTER_2F_1_LINK")]
    )
#PokemonCenter Vermilion
    TwoWayCorridorNodes_Kanto['Vermilion Pokecenter 1F Node'] = Node(
        [kmd["Vermilion_Pokecenter_1F_Links"].get("VERMILION_POKECENTER_1F_TO_VERMILION_CITY_2_LINK"),
         kmd["Vermilion_Pokecenter_1F_Links"].get("VERMILION_POKECENTER_1F_TO_POKECENTER_2F_1_LINK")]
    )
#PokemonCenter Lavender
    TwoWayCorridorNodes_Kanto['Lavender Pokecenter 1F Node'] = Node(
        [kmd["Lavender_Pokecenter_1F_Links"].get("LAVENDER_POKECENTER_1F_TO_LAVENDER_TOWN_1_LINK"),
         kmd["Lavender_Pokecenter_1F_Links"].get("LAVENDER_POKECENTER_1F_TO_POKECENTER_2F_1_LINK")]
    )
#PokemonCenter Celadon
    TwoWayCorridorNodes_Kanto['Celadon Pokecenter 1F Node'] = Node(
        [kmd["Celadon_Pokecenter_1F_Links"].get("CELADON_POKECENTER_1F_TO_CELADON_CITY_5_LINK"),
         kmd["Celadon_Pokecenter_1F_Links"].get("CELADON_POKECENTER_1F_TO_POKECENTER_2F_1_LINK")]
    )
#PokemonCenter Saffron
    TwoWayCorridorNodes_Kanto['Saffron Pokecenter 1F Node'] = Node(
        [kmd["Saffron_Pokecenter_1F_Links"].get("SAFFRON_POKECENTER_1F_TO_SAFFRON_CITY_4_LINK"),
         kmd["Saffron_Pokecenter_1F_Links"].get("SAFFRON_POKECENTER_1F_TO_POKECENTER_2F_1_LINK")]
    )
#PokemonCenter Fuchsia
    TwoWayCorridorNodes_Kanto['Fuchsia Pokecenter 1F Node'] = Node(
        [kmd["Fuchsia_Pokecenter_1F_Links"].get("FUCHSIA_POKECENTER_1F_TO_FUCHSIA_CITY_5_LINK"),
         kmd["Fuchsia_Pokecenter_1F_Links"].get("FUCHSIA_POKECENTER_1F_TO_POKECENTER_2F_1_LINK")]
    )
#PokemonCenter Cinnabar
    TwoWayCorridorNodes_Kanto['Cinnabar Pokecenter 1F Node'] = Node(
        [kmd["Cinnabar_Pokecenter_1F_Links"].get("CINNABAR_POKECENTER_1F_TO_CINNABAR_ISLAND_1_LINK"),
         kmd["Cinnabar_Pokecenter_1F_Links"].get("CINNABAR_POKECENTER_1F_TO_POKECENTER_2F_1_LINK")]
    )
#Gate Route2
    TwoWayCorridorNodes_Kanto['Route 02 Gate Node'] = Node(
        [kmd["Route_2_Gate_Links"].get("ROUTE_2_GATE_TO_ROUTE_2_3_LINK"),
         kmd["Route_2_Gate_Links"].get("ROUTE_2_GATE_TO_ROUTE_2_2_LINK")]
    )
#Gate Route5 - Saffron
    TwoWayCorridorNodes_Kanto['Route 05 Saffron Gate Node'] = Node(
        [kmd["Route_5_Saffron_Gate_Links"].get("ROUTE_5_SAFFRON_GATE_TO_ROUTE_5_2_LINK"),
         kmd["Route_5_Saffron_Gate_Links"].get("ROUTE_5_SAFFRON_GATE_TO_SAFFRON_CITY_9_LINK")]
    )
#Gate Route6 - Saffron
    TwoWayCorridorNodes_Kanto['Route 06 Saffron Gate Node'] = Node(
        [kmd["Route_6_Saffron_Gate_Links"].get("ROUTE_6_SAFFRON_GATE_TO_SAFFRON_CITY_12_LINK"),
         kmd["Route_6_Saffron_Gate_Links"].get("ROUTE_6_SAFFRON_GATE_TO_ROUTE_6_2_LINK")]
    )
#Gate Route7 - Saffron
    TwoWayCorridorNodes_Kanto['Route 07 Saffron Gate Node'] = Node(
        [kmd["Route_7_Saffron_Gate_Links"].get("ROUTE_7_SAFFRON_GATE_TO_ROUTE_7_1_LINK"),
         kmd["Route_7_Saffron_Gate_Links"].get("ROUTE_7_SAFFRON_GATE_TO_SAFFRON_CITY_10_LINK")]
    )
#Gate Route8 - Saffron
    TwoWayCorridorNodes_Kanto['Route 08 Saffron Gate Node'] = Node(
        [kmd["Route_8_Saffron_Gate_Links"].get("ROUTE_8_SAFFRON_GATE_TO_SAFFRON_CITY_14_LINK"),
         kmd["Route_8_Saffron_Gate_Links"].get("ROUTE_8_SAFFRON_GATE_TO_ROUTE_8_1_LINK")]
    )
#Gate Route15 - Fuchsia
    TwoWayCorridorNodes_Kanto['Route 15 Fuchsia Gate Node'] = Node(
        [kmd["Route_15_Fuchsia_Gate_Links"].get("ROUTE_15_FUCHSIA_GATE_TO_FUCHSIA_CITY_8_LINK"),
         kmd["Route_15_Fuchsia_Gate_Links"].get("ROUTE_15_FUCHSIA_GATE_TO_ROUTE_15_1_LINK")]
    )
#Gate Route19 - Fuchsia
    TwoWayCorridorNodes_Kanto['Route 19 Fuchsia Gate Node'] = Node(
        [kmd["Route_19_Fuchsia_Gate_Links"].get("ROUTE_19_FUCHSIA_GATE_TO_FUCHSIA_CITY_10_LINK"),
         kmd["Route_19_Fuchsia_Gate_Links"].get("ROUTE_19_FUCHSIA_GATE_TO_ROUTE_19_1_LINK")]
    )
#Reds House 1F
    TwoWayCorridorNodes_Kanto['Reds House 1F_Node'] = Node(
        [kmd["Reds_House_1F_Links"].get("REDS_HOUSE_1F_TO_PALLET_TOWN_1_LINK"),
         kmd["Reds_House_1F_Links"].get("REDS_HOUSE_1F_TO_REDS_HOUSE_2F_1_LINK")]
    )
#Viridian Trainer School
    TwoWayCorridorNodes_Kanto['Trainer House 1F Node'] = Node(
        [kmd["Trainer_House_1F_Links"].get("TRAINER_HOUSE_1F_TO_VIRIDIAN_CITY_3_LINK"),
         kmd["Trainer_House_1F_Links"].get("TRAINER_HOUSE_1F_TO_TRAINER_HOUSE_B1F_1_LINK")]
    )
#Celadon Mansion Front 1F
    TwoWayCorridorNodes_Kanto['Celadon Mansion 1F Front_Node'] = Node(
        [kmd["Celadon_Mansion_1F_Links"].get("CELADON_MANSION_1F_TO_CELADON_CITY_2_LINK"),
         kmd["Celadon_Mansion_1F_Links"].get("CELADON_MANSION_1F_TO_CELADON_MANSION_2F_4_LINK")]
    )
#Celadon Mansion Back 1F
    TwoWayCorridorNodes_Kanto['Celadon Mansion 1F Back_Node'] = Node(
        [kmd["Celadon_Mansion_1F_Links"].get("CELADON_MANSION_1F_TO_CELADON_CITY_3_LINK"),
         kmd["Celadon_Mansion_1F_Links"].get("CELADON_MANSION_1F_TO_CELADON_MANSION_2F_1_LINK")]
    )
#Celadon Mansion Front 2F
    TwoWayCorridorNodes_Kanto['Celadon Mansion 2F Front Node'] = Node(
        [kmd["Celadon_Mansion_2F_Links"].get("CELADON_MANSION_2F_TO_CELADON_MANSION_3F_3_LINK"),
         kmd["Celadon_Mansion_2F_Links"].get("CELADON_MANSION_2F_TO_CELADON_MANSION_1F_5_LINK")]
    )
#Celadon Mansion Back 2F
    TwoWayCorridorNodes_Kanto['Celadon Mansion 2F Back Node'] = Node(
        [kmd["Celadon_Mansion_2F_Links"].get("CELADON_MANSION_2F_TO_CELADON_MANSION_1F_4_LINK"),
         kmd["Celadon_Mansion_2F_Links"].get("CELADON_MANSION_2F_TO_CELADON_MANSION_3F_2_LINK")]
    )
#Celadon Mansion Front 3F
    TwoWayCorridorNodes_Kanto['Celadon Mansion 3F Front Node'] = Node(
        [kmd["Celadon_Mansion_3F_Links"].get("CELADON_MANSION_3F_TO_CELADON_MANSION_2F_3_LINK"),
         kmd["Celadon_Mansion_3F_Links"].get("CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_2_LINK")]
    )
#Celadon Mansion Back 3F
    TwoWayCorridorNodes_Kanto['Celadon Mansion 3F Back Node'] = Node(
        [kmd["Celadon_Mansion_3F_Links"].get("CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_1_LINK"),
         kmd["Celadon_Mansion_3F_Links"].get("CELADON_MANSION_3F_TO_CELADON_MANSION_2F_2_LINK")]
    )
#Celadon Mansion Roof Back
    TwoWayCorridorNodes_Kanto['Celadon Mansion Roof Node'] = Node(
        [kmd["Celadon_Mansion_Roof_Links"].get("CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_1_LINK"),
         kmd["Celadon_Mansion_Roof_Links"].get("CELADON_MANSION_ROOF_TO_CELADON_MANSION_ROOF_HOUSE_1_LINK")]
    )
#Saffron CopyCat 1F
    TwoWayCorridorNodes_Kanto['Copycats House 1F Node'] = Node(
        [kmd["Copycats_House_1F_Links"].get("COPYCATS_HOUSE_1F_TO_SAFFRON_CITY_8_LINK"),
         kmd["Copycats_House_1F_Links"].get("COPYCATS_HOUSE_1F_TO_COPYCATS_HOUSE_2F_1_LINK")]
    )
    TwoWayCorridorNodes_Kanto['Victory Road Gate Kanto Node'] = Node(
        [johto["Victory_Road_Gate_Links"].get("VICTORY_ROAD_GATE_TO_VICTORY_ROAD_1_LINK"),
         johto["Victory_Road_Gate_Links"].get("VICTORY_ROAD_GATE_TO_ROUTE_22_1_LINK")]
    )
#Fast Ship F1 Corridor Outside Captains Room
    # Fast_Ship_1F_Corridor_Node = Node(
    #     [kmd["Fast_Ship_1F_Links"]FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5_LINK,
    #      kmd["Fast_Ship_1F_Links"]FAST_SHIP_1F_TO_FAST_SHIP_B1F_1_LINK]
    # )
#Fast Ship B1F Corridor
    # Fast_Ship_B1F_Node = Node(
    #     [kmd["Fast_Ship_B1F_Links"]FAST_SHIP_B1F_TO_FAST_SHIP_1F_11_LINK,
    #      kmd["Fast_Ship_B1F_Links"]FAST_SHIP_B1F_TO_FAST_SHIP_1F_12_LINK]
    # )

    return TwoWayCorridorNodes_Kanto

def buildKantoHubNodes():
    HubNodes_Kanto = dict()

    HubNodes_Kanto['Route 28 Silver Cave Outside Node'] = Node(
        [kmd["Route_28_Links"].get("ROUTE_28_TO_VICTORY_ROAD_GATE_7_LINK"),
         kmd["Silver_Cave_Outside_Links"].get("SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_ROOM_1_1_LINK"),
         kmd["Silver_Cave_Outside_Links"].get("SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_POKECENTER_1F_1_LINK")]
    )

#Mount Moon 
    HubNodes_Kanto['Mount Moon Node'] = Node(
        [kmd["Mount_Moon_Links"].get("MOUNT_MOON_TO_ROUTE_3_1_LINK"),
         kmd["Mount_Moon_Links"].get("MOUNT_MOON_TO_ROUTE_4_1_LINK"),
         kmd["Mount_Moon_Links"].get("MOUNT_MOON_TO_MOUNT_MOON_7_LINK")]
    )
#Mount Moon Square 
    HubNodes_Kanto['Mount Moon Square Node'] = Node(
        [kmd["Mount_Moon_Square_Links"].get(key) for key in kmd["Mount_Moon_Square_Links"]]
    )

#Fast Ship Hub
    HubNodes_Kanto['Fast Ship 1F Hub Node'] = Node(
        [kmd["Fast_Ship_1F_Links"].get(key) for key in kmd["Fast_Ship_1F_Links"] if key not in
         [kmd["Fast_Ship_1F_Links"].get("FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_1_LINK"),
          kmd["Fast_Ship_1F_Links"].get("FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5_LINK"),
          kmd["Fast_Ship_1F_Links"].get("FAST_SHIP_1F_TO_FAST_SHIP_B1F_1_LINK"),
          kmd["Fast_Ship_1F_Links"].get("FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_3_LINK"),
          kmd["Fast_Ship_1F_Links"].get("FAST_SHIP_1F_TO_FAST_SHIP_B1F_2_LINK"),
          kmd["Fast_Ship_1F_Links"].get("FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_3_LINK")]]
    )

#Celadon Dept Store Hub
    HubNodes_Kanto['Celadon Dept Store Hub Node'] = Node(
        [kmd["Celadon_Dept_Store_1F_Links"].get(key) for key in kmd["Celadon_Dept_Store_1F_Links"]] +
        [kmd["Celadon_Dept_Store_2F_Links"].get(key) for key in kmd["Celadon_Dept_Store_2F_Links"]] +
        [kmd["Celadon_Dept_Store_3F_Links"].get(key) for key in kmd["Celadon_Dept_Store_3F_Links"]] +
        [kmd["Celadon_Dept_Store_4F_Links"].get(key) for key in kmd["Celadon_Dept_Store_4F_Links"]] +
        [kmd["Celadon_Dept_Store_5F_Links"].get(key) for key in kmd["Celadon_Dept_Store_5F_Links"]] +
        [kmd["Celadon_Dept_Store_6F_Links"].get(key) for key in kmd["Celadon_Dept_Store_6F_Links"]]
    )

    return HubNodes_Kanto









  

# print("Printing Major Node Connection Numbers")
# for node in MajorNodes:
#     print(node["value.TOTAL_LINKS"]
#
# print("Printing Corridor Connection Numbers")
# for node in TwoWayCorridorNodes:
#     print(node["value.TOTAL_LINKS"]
#
# print("Printing Hub Node Connection Numbers")
# for node in HubNodes:
#     print(node["value.TOTAL_LINKS"]
#
# print("Printing Deadend Node Connection Numbers")
# for node in DeadEndNodes:
#     print(node["value.TOTAL_LINKS"]
