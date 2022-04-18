import itertools
from enum import Enum

from class_definitions import Node
import links_and_nodes.kanto_all_warp_points as kmd


class MajorNodes_Kanto(Enum):

#Pallet + Viridian + Pewter + Victoryroad Gate Entrance + Mount Moon Entrance(note: maybe split later?) 
    Pallet_Viridian_Pewter_Node = Node(
            [link for link in kmd.Pallet_Town_Links]
        +   [link for link in kmd.Viridian_City_Links]
        +   [kmd.Route_22_Links.ROUTE_22_TO_VICTORY_ROAD_GATE_1_LINK]
        +   [link for link in kmd.Pewter_City_Links]
        +   [kmd.Route_3_Links.ROUTE_3_TO_MOUNT_MOON_1_LINK])

#Cerulean (note: block on underground) (bikeshop closed) + route 5
    Cerulean_City_Node = Node(
            [link for link in kmd.Cerulean_City_Links]
        +   [kmd.Route_25_Links.ROUTE_25_TO_BILLS_HOUSE_1_LINK]
        +   [kmd.Route_5_Links.ROUTE_5_TO_ROUTE_5_CLEANSE_TAG_HOUSE_1_LINK]
        +   [kmd.Route_5_Links.ROUTE_5_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_1_LINK]
        +   [kmd.Route_5_Links.ROUTE_5_TO_ROUTE_5_SAFFRON_GATE_1_LINK])

#Vermillion (note: snorlax key) excluded gym + route 6
    Vermilion_City_Node = Node(
            [link for link in kmd.Vermilion_City_Links if link not in 
            [kmd.Vermilion_City_Links.VERMILION_CITY_TO_VERMILION_GYM_1_LINK]]
        +   [kmd.Route_6_Links.ROUTE_6_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_1_LINK]
        +   [kmd.Route_6_Links.ROUTE_6_TO_ROUTE_6_SAFFRON_GATE_3_LINK])


#Celadon + route 8 and 16 gates
    Celadon_City_Node = Node(
            [link for link in kmd.Celadon_City_Links if link not in 
            [kmd.Celadon_City_Links.CELADON_CITY_TO_CELADON_GYM_1_LINK]]
        +   [kmd.Route_8_Links.ROUTE_8_TO_ROUTE_8_SAFFRON_GATE_3_LINK]
        +   [kmd.Route_16_Links.ROUTE_16_TO_ROUTE_16_GATE_3_LINK])

#Lavender + rocktunnel entrance + route 7 gate + superrodhouse + route 15 gate
    Lavender_Town_Node = Node(
            [link for link in kmd.Lavender_Town_Links]
        +   [kmd.Route_10_South_Links.ROUTE_10_SOUTH_TO_ROCK_TUNNEL_1F_2_LINK]
        +   [kmd.Route_7_Links.ROUTE_7_TO_ROUTE_7_SAFFRON_GATE_1_LINK]
        +   [kmd.Route_12_Links.ROUTE_12_TO_ROUTE_12_SUPER_ROD_HOUSE_1_LINK]
        +   [kmd.Route_15_Links.ROUTE_15_TO_ROUTE_15_FUCHSIA_GATE_3_LINK]) #(#todo make this gate a dead end for less pain ?)

#Saffron 
    Saffron_City_Node = Node(
            [link for link in kmd.Saffron_City_Links])
     

#Fuchsia + gates
    Fuchsia_City_Node = Node(
            [link for link in kmd.Fuchsia_City_Links if link not in 
            [kmd.Fuchsia_City_Links.FUCHSIA_CITY_TO_FUCHSIA_MART_2_LINK]]
        +   [kmd.Route_18_Links.ROUTE_18_TO_ROUTE_17_ROUTE_18_GATE_3_LINK])



class ImportantDeadEndNodes_Kanto(Enum):

# Route 2 Gates Entrances bottom
    Route_2_Gate_Exterior_Bottom_Node = Node(
        [kmd.Route_2_Links.ROUTE_2_TO_ROUTE_2_GATE_3_LINK]
    ) 
# Route 2 Gates Entrances top
    Route_2_Gate_Exterior_Top_Node = Node(
        [kmd.Route_2_Links.ROUTE_2_TO_ROUTE_2_GATE_1_LINK]
    ) 
# Mount Moon Ledge (unimportant?) 
    Mount_Moon_Ledge_Node = Node(
        [kmd.Mount_Moon_Links.MOUNT_MOON_TO_MOUNT_MOON_8_LINK]
    ) 
# Route 4 Cerulean Ledge (unimportant?)
    Route_4_Ledge_Node = Node(
        [kmd.Route_4_Links.ROUTE_4_TO_MOUNT_MOON_2_LINK]
    ) 
# Powerplant Exterior 
    Power_Plant_Exterior_Node = Node(
        [kmd.Route_10_North_Links.ROUTE_10_NORTH_TO_POWER_PLANT_1_LINK]
    ) 
# Surge Exterior 
    Vermillion_Gym_Exterior_Node = Node(
        [kmd.Vermilion_City_Links.VERMILION_CITY_TO_VERMILION_GYM_1_LINK]
    )  
# Erika Exterior 
    Celadon_Gym_Exterior_Node = Node(
        [kmd.Celadon_City_Links.CELADON_CITY_TO_CELADON_GYM_1_LINK]
    ) 
# Route 16 Cycling Road House 
    Route_16_Fuchsia_Speech_House_Exterior_Node = Node(
        [kmd.Route_16_Links.ROUTE_16_TO_ROUTE_16_FUCHSIA_SPEECH_HOUSE_1_LINK]
    ) 
# Fuchsia Market 
    Fuchsia_Mart_Exterior_Node = Node(
        [kmd.Fuchsia_City_Links.FUCHSIA_CITY_TO_FUCHSIA_MART_2_LINK]
    ) 
# Route 19 Fuchsia Gate 
    Route_19_Gate_Exterior_Node = Node(
        [kmd.Route_19_Links.ROUTE_19_TO_ROUTE_19_FUCHSIA_GATE_3_LINK]
    ) 
# Cinnabar PokeCenter Exterior 
    Cinnabar_Pokecenter_Exterior_Node = Node(
        [kmd.Cinnabar_Island_Links.CINNABAR_ISLAND_TO_CINNABAR_POKECENTER_1F_1_LINK]
    ) 
# Cinnabar Blain Exterior 
    Seafoam_Gym_Exterior_Node = Node(
        [kmd.Route_20_Links.ROUTE_20_TO_SEAFOAM_GYM_1_LINK]
    ) 
# Vermillion Port Ship Entrance 
    Vermilion_Port_Node = Node(
        [kmd.Vermilion_Port_Links.VERMILION_PORT_TO_VERMILION_PORT_PASSAGE_5_LINK]
    ) 

#Interior Nodes
# Powerplant  
    Power_Plant_Node = Node(
        [kmd.Power_Plant_Links.POWER_PLANT_TO_ROUTE_10_NORTH_2_LINK]
    ) 
# Route 12 Superrod House  
    Route_12_Super_Rod_House_Node = Node(
        [kmd.Route_12_Super_Rod_House_Links.ROUTE_12_SUPER_ROD_HOUSE_TO_ROUTE_12_1_LINK]
    ) 
# Pallet Oaks Lab 
    Oaks_Lab_Node = Node(
        [kmd.Oaks_Lab_Links.OAKS_LAB_TO_PALLET_TOWN_3_LINK]
    ) 
# Mount Moon Mart 
    Mount_Moon_Gift_Shop_Node = Node(
        [kmd.Mount_Moon_Gift_Shop_Links.MOUNT_MOON_TO_ROUTE_3_1_LINK]
    ) 
# Route 2 Nugget House 
    Route_2_Nugget_House_Node = Node(
        [kmd.Route_2_Nugget_House_Links.ROUTE_2_NUGGET_HOUSE_TO_ROUTE_2_1_LINK]
    ) 
# Viridian TrainerHouse B1F 
    Trainer_House_B1F_Node = Node(
        [kmd.Trainer_House_B1F_Links.TRAINER_HOUSE_B1F_TO_TRAINER_HOUSE_1F_3_LINK]
    ) 
# Viridian Gym 
    Viridian_Gym_Node = Node(
        [kmd.Viridian_Gym_Links.VIRIDIAN_GYM_TO_VIRIDIAN_CITY_1_LINK]
    ) 
# Viridian Mart 
    Viridian_Mart_Node = Node(
        [kmd.Viridian_Mart_Links.VIRIDIAN_MART_TO_VIRIDIAN_CITY_4_LINK]
    ) 
# Pewter Gym  
    Pewter_Gym_Node = Node(
        [kmd.Pewter_Gym_Links.PEWTER_GYM_TO_PEWTER_CITY_2_LINK]
    ) 
# Pewter Mart 
    Pewter_Mart_Node = Node(
        [kmd.Pewter_Mart_Links.PEWTER_MART_TO_PEWTER_CITY_3_LINK]
    ) 
# Cerulean BillHouse 
    Bills_House_Node = Node(
        [kmd.Bills_House_Links.BILLS_HOUSE_TO_ROUTE_25_1_LINK]
    ) 
# Cerulean Gym 
    Cerulean_Gym_Node = Node(
        [kmd.Cerulean_Gym_Links.CERULEAN_GYM_TO_CERULEAN_CITY_5_LINK]
    ) 
# Cerulean Mart 
    Cerulean_Mart_Node = Node(
        [kmd.Cerulean_Mart_Links.CERULEAN_MART_TO_CERULEAN_CITY_6_LINK]
    ) 
# Route Route5CleanseTagHouse 
    Route_5_Cleanse_Tag_House_Node = Node(
        [kmd.Route_5_Cleanse_Tag_House_Links.ROUTE_5_CLEANSE_TAG_HOUSE_TO_ROUTE_5_4_LINK]
    ) 
# Vermillion Gym 
    Vermilion_Gym_Node = Node(
        [kmd.Vermilion_Gym_Links.VERMILION_GYM_TO_VERMILION_CITY_7_LINK]
    ) 
# Vermillion Mart 
    Vermilion_Mart_Node = Node(
        [kmd.Vermilion_Mart_Links.VERMILION_MART_TO_VERMILION_CITY_5_LINK]
    ) 
# Vermillion PokemonFanClub 
    Pokemon_Fan_Club_Node = Node(
        [kmd.Pokemon_Fan_Club_Links.POKEMON_FAN_CLUB_TO_VERMILION_CITY_3_LINK]
    ) 
# Lavender Mart 
    Lavender_Mart_Node = Node(
        [kmd.Lavender_Mart_Links.LAVENDER_MART_TO_LAVENDER_TOWN_5_LINK]
    ) 
# Lavender NameRater 
    Lavender_Name_Rater_Node = Node(
        [kmd.Lavender_Name_Rater_Links.LAVENDER_NAME_RATER_TO_LAVENDER_TOWN_4_LINK]
    ) 
# Lavender RadioTower 
    Lav_Radio_Tower_1F_Node = Node(
        [kmd.Lav_Radio_Tower_1F_Links.LAV_RADIO_TOWER_1F_TO_LAVENDER_TOWN_7_LINK]
    ) 
# Celadon Cafe 
    Celadon_Cafe_Node = Node(
        [kmd.Celadon_Cafe_Links.CELADON_CAFE_TO_CELADON_CITY_9_LINK]
    ) 
# Celadon Game Corner 
    Celadon_Game_Corner_Node = Node(
        [kmd.Celadon_Game_Corner_Links.CELADON_GAME_CORNER_TO_CELADON_CITY_6_LINK]
    ) 
# Celadon Game Corner Prize 
    Celadon_Game_Corner_Prize_Room_Node = Node(
        [kmd.Celadon_Game_Corner_Prize_Room_Links.CELADON_GAME_CORNER_PRIZE_ROOM_TO_CELADON_CITY_7_LINK]
    ) 
# Celadon Gym 
    Celadon_Gym_Node = Node(
        [kmd.Celadon_Gym_Links.CELADON_GYM_TO_CELADON_CITY_8_LINK]
    ) 
# Celadon Store 6F
    Celadon_Dept_Store_6F_Node = Node(
        [kmd.Celadon_Dept_Store_6F_Links.CELADON_DEPT_STORE_6F_TO_CELADON_DEPT_STORE_5F_2_LINK]
    )
# Celadon Roof House Back 
    Celadon_Mansion_Roof_House_Node = Node(
        [kmd.Celadon_Mansion_Roof_House_Links.CELADON_MANSION_ROOF_HOUSE_TO_CELADON_MANSION_ROOF_3_LINK]
    ) 
# Saffron Copycat House 2F 
    Copycats_House_2F_Node = Node(
        [kmd.Copycats_House_2F_Links.COPYCATS_HOUSE_2F_TO_COPYCATS_HOUSE_1F_3_LINK]
    ) 
# Saffron Fighting Dojo 
    Fighting_Dojo_Node = Node(
        [kmd.Fighting_Dojo_Links.FIGHTING_DOJO_TO_SAFFRON_CITY_1_LINK]
    ) 
# Saffron Mr Psychic House 
    Mr_Psychics_House_Node = Node(
        [kmd.Mr_Psychics_House_Links.MR_PSYCHICS_HOUSE_TO_SAFFRON_CITY_5_LINK]
    ) 
# Saffron Gym 
    Saffron_Gym_Node = Node(
        [kmd.Saffron_Gym_Links.SAFFRON_GYM_TO_SAFFRON_CITY_2_LINK]
    ) 
# Saffron MagnetTrain 
    Saffron_Magnet_Train_Station_Node = Node(
        [kmd.Saffron_Magnet_Train_Station_Links.SAFFRON_MAGNET_TRAIN_STATION_TO_SAFFRON_CITY_6_LINK]
    ) 
# Saffron Mart 
    Saffron_Mart_Node = Node(
        [kmd.Saffron_Mart_Links.SAFFRON_MART_TO_SAFFRON_CITY_3_LINK]
    ) 
# Saffron SilphCo 
    Silph_Co_1F_Node = Node(
        [kmd.Silph_Co_1F_Links.SILPH_CO_1F_TO_SAFFRON_CITY_7_LINK]
    ) 
# Fuchsia Gym 
    Fuchsia_Gym_Node = Node(
        [kmd.Fuchsia_Gym_Links.FUCHSIA_GYM_TO_FUCHSIA_CITY_3_LINK]
    ) 
# Fuchsia Mart 
    Fuchsia_Mart_Node = Node(
        [kmd.Fuchsia_Mart_Links.FUCHSIA_MART_TO_FUCHSIA_CITY_1_LINK]
    ) 
# Cinnabar Gym 
    Seafoam_Gym_Node = Node(
        [kmd.Seafoam_Gym_Links.SEAFOAM_GYM_TO_ROUTE_20_1_LINK]
    ) 

#Fast Ship Cabin Warp 4 lazy sailor
    Fast_Ship_Cabins_NNW_NNE_NE_Cabin_4_Node = Node(
        [kmd.Fast_Ship_Cabins_NNW_NNE_NE_Links.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_4_LINK]
    ) 
#Fast Ship Cabin Warp 5 player cabin
    Fast_Ship_Cabins_SW_SSW_NW_Cabin_5_Node = Node(
        [kmd.Fast_Ship_Cabins_SW_SSW_NW_Links.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_5_LINK]
    ) 
#Fast Ship Cabin Warp 10 captain
    Fast_Ship_Cabins_SE_SSE_Captains_Cabin_10_Node = Node(
        [kmd.Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_10_LINK]
    ) 


class UselessDeadEndNodes_Kanto(Enum):

#All Interiors
# Route 16 Cycling Road House  
    Route_16_Fuchsia_Speech_House_Node = Node(
        [kmd.Route_16_Fuchsia_Speech_House_Links.ROUTE_16_FUCHSIA_SPEECH_HOUSE_TO_ROUTE_16_1_LINK]
    )
# Pallet Blues House
    Blues_House_Node = Node(
        [kmd.Blues_House_Links.BLUES_HOUSE_TO_PALLET_TOWN_2_LINK]
    )
# Pallet Reds House 2F
    Reds_House_2F_Node = Node(
        [kmd.Reds_House_2F_Links.REDS_HOUSE_2F_TO_REDS_HOUSE_1F_3_LINK]
    )
# Viridian NicknameSpeechHouse
    Viridian_Nickname_Speech_House_Node = Node(
        [kmd.Viridian_Nickname_Speech_House_Links.VIRIDIAN_NICKNAME_SPEECH_HOUSE_TO_VIRIDIAN_CITY_2_LINK]
    )
# Pewter NidoranSpeechHouse
    Pewter_Nidoran_Speech_House_Node = Node(
        [kmd.Pewter_Nidoran_Speech_House_Links.PEWTER_NIDORAN_SPEECH_HOUSE_TO_PEWTER_CITY_1_LINK]
    )
# Pewter SnoozeSpeechHouse
    Pewter_Snooze_Speech_House_Node = Node(
        [kmd.Pewter_Snooze_Speech_House_Links.PEWTER_SNOOZE_SPEECH_HOUSE_TO_PEWTER_CITY_5_LINK]
    )
# Cerulean GymBadgeSpeechHouse
    Cerulean_Gym_Badge_Speech_House_Node = Node(
        [kmd.Cerulean_Gym_Badge_Speech_House_Links.CERULEAN_GYM_BADGE_SPEECH_HOUSE_TO_CERULEAN_CITY_1_LINK]
    )
# Cerulean PoliceStation
    Cerulean_Police_Station_Node = Node(
        [kmd.Cerulean_Police_Station_Links.CERULEAN_POLICE_STATION_TO_CERULEAN_CITY_2_LINK]
    )
# Cerulean TradespeechHouse
    Cerulean_Trade_Speech_House_Node = Node(
        [kmd.Cerulean_Trade_Speech_House_Links.CERULEAN_TRADE_SPEECH_HOUSE_TO_CERULEAN_CITY_3_LINK]
    )
# Vermillion DiglettCaveSpeechHouse
    Vermilion_Digletts_Cave_Speech_House_Node = Node(
        [kmd.Vermilion_Digletts_Cave_Speech_House_Links.VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_TO_VERMILION_CITY_6_LINK]
    )
# Vermillion FishingSpeechHouse
    Vermilion_Fishing_Speech_House_Node = Node(
        [kmd.Vermilion_Fishing_Speech_House_Links.VERMILION_FISHING_SPEECH_HOUSE_TO_VERMILION_CITY_1_LINK]
    )
# Vermillion MagnetTrainSpeechHouse
    Vermilion_Magnet_Train_Speech_House_Node = Node(
        [kmd.Vermilion_Magnet_Train_Speech_House_Links.VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_TO_VERMILION_CITY_4_LINK]
    )
# Lavender SpeechHouse
    Lavender_Speech_House_Node = Node(
        [kmd.Lavender_Speech_House_Links.LAVENDER_SPEECH_HOUSE_TO_LAVENDER_TOWN_3_LINK]
    )
# Lavender MrFujiHouse
    Mr_Fujis_House_Node = Node(
        [kmd.Mr_Fujis_House_Links.MR_FUJIS_HOUSE_TO_LAVENDER_TOWN_2_LINK]
    )
# Lavender SoulHouse
    Soul_House_Node = Node(
        [kmd.Soul_House_Links.SOUL_HOUSE_TO_LAVENDER_TOWN_6_LINK]
    )
# Celadon Roof Front
    Celadon_Mansion_Roof_Node = Node(
        [kmd.Celadon_Mansion_Roof_Links.CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_4_LINK]
    )
# Fuchsia BillsBrother House
    Bills_Brothers_House_Node = Node(
        [kmd.Bills_Brothers_House_Links.BILLS_BROTHERS_HOUSE_TO_FUCHSIA_CITY_4_LINK]
    )
# Fuchsia SafariZone Main Office
    Safari_Zone_Main_Office_Node = Node(
        [kmd.Safari_Zone_Main_Office_Links.SAFARI_ZONE_MAIN_OFFICE_TO_FUCHSIA_CITY_2_LINK]
    )
# Fuchsia SafariZone Wardens Home
    Safari_Zone_Wardens_Home_Node = Node(
        [kmd.Safari_Zone_Wardens_Home_Links.SAFARI_ZONE_WARDENS_HOME_TO_FUCHSIA_CITY_6_LINK]
    )

#Fast Ship Cabin Warp 2
    Fast_Ship_Cabins_NNW_NNE_NE_Cabin_2_Node = Node(
        [kmd.Fast_Ship_Cabins_NNW_NNE_NE_Links.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_2_LINK]
    )
#Fast Ship Cabin Warp 3
    Fast_Ship_Cabins_NNW_NNE_NE_Cabin_3_Node = Node(
        [kmd.Fast_Ship_Cabins_NNW_NNE_NE_Links.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_3_LINK]
    )
#Fast Ship Cabin Warp 6
    Fast_Ship_Cabins_SW_SSW_NW_Cabin_6_Node = Node(
        [kmd.Fast_Ship_Cabins_SW_SSW_NW_Links.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_6_LINK]
    )
#Fast Ship Cabin Warp 7
    Fast_Ship_Cabins_SW_SSW_NW_Cabin_7_Node = Node(
        [kmd.Fast_Ship_Cabins_SW_SSW_NW_Links.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_7_LINK]
    )
#Fast Ship Cabin Warp 8
    Fast_Ship_Cabins_SE_SSE_Captains_Cabin_8_Node = Node(
        [kmd.Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_8_LINK]
    )
#Fast Ship Cabin Warp 9
    Fast_Ship_Cabins_SE_SSE_Captains_Cabin_9_Node = Node(
        [kmd.Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_9_LINK]
    )


class TwoWayCorridorNodes_Kanto(Enum):

#Outside Diglett - Pewter 
    Route_2_Diglett_Cave_To_Nugget_House_Node = Node(
        [kmd.Route_2_Links.ROUTE_2_TO_ROUTE_2_NUGGET_HOUSE_1_LINK,
         kmd.Route_2_Links.ROUTE_2_TO_DIGLETTS_CAVE_3_LINK]
    )
#Diglett Cave
    Digletts_Cave_Vermillion_Side_Node = Node(
        [kmd.Digletts_Cave_Links.DIGLETTS_CAVE_TO_VERMILION_CITY_10_LINK,
         kmd.Digletts_Cave_Links.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_5_LINK]
    )
#Diglett Cave
    Digletts_Cave_Route_2_Side_Node = Node(
        [kmd.Digletts_Cave_Links.DIGLETTS_CAVE_TO_ROUTE_2_5_LINK, 
         kmd.Digletts_Cave_Links.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_6_LINK]
    )
#Diglett Cave
    Digletts_Cave_Main_Tunnel_Node = Node(
        [kmd.Digletts_Cave_Links.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_2_LINK, 
         kmd.Digletts_Cave_Links.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_4_LINK]
    )
#Pkmcenter - Rocktunnel Route 9,10
    Route_10_Pokecenter_To_Rock_Tunnel_Node = Node(
        [kmd.Route_10_North_Links.ROUTE_10_NORTH_TO_ROUTE_10_POKECENTER_1F_1_LINK,
         kmd.Route_9_Links.ROUTE_9_TO_ROCK_TUNNEL_1F_1_LINK]
    )
#Cycling Road Route 17
    Route_16_Route_17_Node = Node(
        [kmd.Route_17_Links.ROUTE_17_TO_ROUTE_17_ROUTE_18_GATE_1_LINK,
         kmd.Route_16_Links.ROUTE_16_TO_ROUTE_16_GATE_1_LINK]
    )
#Kanto Underground
    Underground_Path_Node = Node(
        [kmd.Underground_Path_Links.UNDERGROUND_PATH_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_3_LINK,
         kmd.Underground_Path_Links.UNDERGROUND_PATH_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_3_LINK]
    )
#Vermillion Port Passage
    Vermilion_Port_Passage_Entrance_Node = Node(
        [kmd.Vermilion_Port_Passage_Links.VERMILION_PORT_PASSAGE_TO_VERMILION_CITY_8_LINK,
         kmd.Vermilion_Port_Passage_Links.VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_PASSAGE_4_LINK]
    )
#Vermillion Port Passage
    Vermilion_Port_Passage_Tunnel_Node = Node(
        [kmd.Vermilion_Port_Passage_Links.VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_PASSAGE_3_LINK,
         kmd.Vermilion_Port_Passage_Links.VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_1_LINK]
    )
#Rocktunnel 1F
    Rock_Tunnel_1F_Route_9_Side_Node = Node(
        [kmd.Rock_Tunnel_1F_Links.ROCK_TUNNEL_1F_TO_ROUTE_9_1_LINK, 
         kmd.Rock_Tunnel_1F_Links.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_4_LINK]
    )
#Rocktunnel 1F
    Rock_Tunnel_1F_Lavender_Side_Node = Node(
        [kmd.Rock_Tunnel_1F_Links.ROCK_TUNNEL_1F_TO_ROUTE_10_SOUTH_1_LINK, 
         kmd.Rock_Tunnel_1F_Links.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_1_LINK]
    )
#Rocktunnel 1F
    Rock_Tunnel_1F_Middle_Part_Node = Node(
        [kmd.Rock_Tunnel_1F_Links.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_3_LINK, 
         kmd.Rock_Tunnel_1F_Links.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_2_LINK]
    )
#Rocktunnel B1F
    Rock_Tunnel_B1F_NW_Node = Node(
        [kmd.Rock_Tunnel_B1F_Links.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_6_LINK, 
         kmd.Rock_Tunnel_B1F_Links.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_4_LINK]
    )
#Rocktunnel B1F
    Rock_Tunnel_B1F_SE_Node = Node(
        [kmd.Rock_Tunnel_B1F_Links.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_3_LINK, 
         kmd.Rock_Tunnel_B1F_Links.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_5_LINK]
    )
#Mount Moon inbetween 
    Mount_Moon_Entrance_NE_Node = Node(
        [kmd.Mount_Moon_Links.MOUNT_MOON_TO_MOUNT_MOON_SQUARE_1_LINK, 
         kmd.Mount_Moon_Links.MOUNT_MOON_TO_MOUNT_MOON_3_LINK]
    )
#Mount Moon inbetween
    Mount_Moon_Entrance_SE_Node = Node(
        [kmd.Mount_Moon_Links.MOUNT_MOON_TO_MOUNT_MOON_SQUARE_2_LINK,
         kmd.Mount_Moon_Links.MOUNT_MOON_TO_MOUNT_MOON_4_LINK]
    )
#PokemonCenter Route 10 Inside
    Route_10_Pokecenter_1F_Node = Node(
        [kmd.Route_10_Pokecenter_1F_Links.ROUTE_10_POKECENTER_1F_TO_ROUTE_10_NORTH_1_LINK,
         kmd.Route_10_Pokecenter_1F_Links.ROUTE_10_POKECENTER_1F_TO_POKECENTER_2F_1_LINK]
    )
#PokemonCenter Viridian
    Viridian_Pokecenter_1F_Node = Node(
        [kmd.Viridian_Pokecenter_1F_Links.VIRIDIAN_POKECENTER_1F_TO_VIRIDIAN_CITY_5_LINK,
         kmd.Viridian_Pokecenter_1F_Links.VIRIDIAN_POKECENTER_1F_TO_POKECENTER_2F_1_LINK]
    )
#PokemonCenter Pewter
    Pewter_Pokecenter_1F_Node = Node(
        [kmd.Pewter_Pokecenter_1F_Links.PEWTER_POKECENTER_1F_TO_PEWTER_CITY_4_LINK,
         kmd.Pewter_Pokecenter_1F_Links.PEWTER_POKECENTER_1F_TO_POKECENTER_2F_1_LINK]
    )
#PokemonCenter Cerulean
    Cerulean_Pokecenter_1F_Node = Node(
        [kmd.Cerulean_Pokecenter_1F_Links.CERULEAN_POKECENTER_1F_TO_CERULEAN_CITY_4_LINK,
         kmd.Cerulean_Pokecenter_1F_Links.CERULEAN_POKECENTER_1F_TO_POKECENTER_2F_1_LINK]
    )
#PokemonCenter Vermilion
    Vermilion_Pokecenter_1F_Node = Node(
        [kmd.Vermilion_Pokecenter_1F_Links.VERMILION_POKECENTER_1F_TO_VERMILION_CITY_2_LINK,
         kmd.Vermilion_Pokecenter_1F_Links.VERMILION_POKECENTER_1F_TO_POKECENTER_2F_1_LINK]
    )
#PokemonCenter Lavender
    Lavender_Pokecenter_1F_Node = Node(
        [kmd.Lavender_Pokecenter_1F_Links.LAVENDER_POKECENTER_1F_TO_LAVENDER_TOWN_1_LINK,
         kmd.Lavender_Pokecenter_1F_Links.LAVENDER_POKECENTER_1F_TO_POKECENTER_2F_1_LINK]
    )
#PokemonCenter Celadon
    Celadon_Pokecenter_1F_Node = Node(
        [kmd.Celadon_Pokecenter_1F_Links.CELADON_POKECENTER_1F_TO_CELADON_CITY_5_LINK,
         kmd.Celadon_Pokecenter_1F_Links.CELADON_POKECENTER_1F_TO_POKECENTER_2F_1_LINK]
    )
#PokemonCenter Saffron
    Saffron_Pokecenter_1F_Node = Node(
        [kmd.Saffron_Pokecenter_1F_Links.SAFFRON_POKECENTER_1F_TO_SAFFRON_CITY_4_LINK,
         kmd.Saffron_Pokecenter_1F_Links.SAFFRON_POKECENTER_1F_TO_POKECENTER_2F_1_LINK]
    )
#PokemonCenter Fuchsia
    Fuchsia_Pokecenter_1F_Node = Node(
        [kmd.Fuchsia_Pokecenter_1F_Links.FUCHSIA_POKECENTER_1F_TO_FUCHSIA_CITY_5_LINK,
         kmd.Fuchsia_Pokecenter_1F_Links.FUCHSIA_POKECENTER_1F_TO_POKECENTER_2F_1_LINK]
    )
#PokemonCenter Cinnabar
    Cinnabar_Pokecenter_1F_Node = Node(
        [kmd.Cinnabar_Pokecenter_1F_Links.CINNABAR_POKECENTER_1F_TO_CINNABAR_ISLAND_1_LINK,
         kmd.Cinnabar_Pokecenter_1F_Links.CINNABAR_POKECENTER_1F_TO_POKECENTER_2F_1_LINK]
    )
#Gate Route2
    Route_2_Gate_Node = Node(
        [kmd.Route_2_Gate_Links.ROUTE_2_GATE_TO_ROUTE_2_3_LINK,
         kmd.Route_2_Gate_Links.ROUTE_2_GATE_TO_ROUTE_2_2_LINK]
    )
#Gate Route5 - Saffron
    Route_5_Saffron_Gate_Node = Node(
        [kmd.Route_5_Saffron_Gate_Links.ROUTE_5_SAFFRON_GATE_TO_ROUTE_5_2_LINK,
         kmd.Route_5_Saffron_Gate_Links.ROUTE_5_SAFFRON_GATE_TO_SAFFRON_CITY_9_LINK]
    )
#Gate Route6 - Saffron
    Route_6_Saffron_Gate_Node = Node(
        [kmd.Route_6_Saffron_Gate_Links.ROUTE_6_SAFFRON_GATE_TO_SAFFRON_CITY_12_LINK,
         kmd.Route_6_Saffron_Gate_Links.ROUTE_6_SAFFRON_GATE_TO_ROUTE_6_2_LINK]
    )
#Gate Route7 - Saffron
    Route_7_Saffron_Gate_Node = Node(
        [kmd.Route_7_Saffron_Gate_Links.ROUTE_7_SAFFRON_GATE_TO_ROUTE_7_1_LINK,
         kmd.Route_7_Saffron_Gate_Links.ROUTE_7_SAFFRON_GATE_TO_SAFFRON_CITY_10_LINK]
    )
#Gate Route8 - Saffron
    Route_8_Saffron_Gate_Node = Node(
        [kmd.Route_8_Saffron_Gate_Links.ROUTE_8_SAFFRON_GATE_TO_SAFFRON_CITY_14_LINK,
         kmd.Route_8_Saffron_Gate_Links.ROUTE_8_SAFFRON_GATE_TO_ROUTE_8_1_LINK]
    )
#Gate Route15 - Fuchsia
    Route_15_Fuchsia_Gate_Node = Node(
        [kmd.Route_15_Fuchsia_Gate_Links.ROUTE_15_FUCHSIA_GATE_TO_FUCHSIA_CITY_8_LINK,
         kmd.Route_15_Fuchsia_Gate_Links.ROUTE_15_FUCHSIA_GATE_TO_ROUTE_15_1_LINK]
    )
#Gate Route16
    Route_16_Gate_Node = Node(
        [kmd.Route_16_Gate_Links.ROUTE_16_GATE_TO_ROUTE_16_4_LINK,
         kmd.Route_16_Gate_Links.ROUTE_16_GATE_TO_ROUTE_16_2_LINK]
    )
#Gate Route17 - 18
    Route_17_Route_18_Gate_Node = Node(
        [kmd.Route_17_Route_18_Gate_Links.ROUTE_17_ROUTE_18_GATE_TO_ROUTE_17_1_LINK,
         kmd.Route_17_Route_18_Gate_Links.ROUTE_17_ROUTE_18_GATE_TO_ROUTE_18_1_LINK]
    )
#Gate Route19 - Fuchsia
    Route_19_Fuchsia_Gate_Node = Node(
        [kmd.Route_19_Fuchsia_Gate_Links.ROUTE_19_FUCHSIA_GATE_TO_FUCHSIA_CITY_10_LINK,
         kmd.Route_19_Fuchsia_Gate_Links.ROUTE_19_FUCHSIA_GATE_TO_ROUTE_19_1_LINK]
    )
#Reds House 1F
    Reds_House_1F_Node = Node(
        [kmd.Reds_House_1F_Links.REDS_HOUSE_1F_TO_PALLET_TOWN_1_LINK,
         kmd.Reds_House_1F_Links.REDS_HOUSE_1F_TO_REDS_HOUSE_2F_1_LINK]
    )
#Viridian Trainer School
    Trainer_House_1F_Node = Node(
        [kmd.Trainer_House_1F_Links.TRAINER_HOUSE_1F_TO_VIRIDIAN_CITY_3_LINK,
         kmd.Trainer_House_1F_Links.TRAINER_HOUSE_1F_TO_TRAINER_HOUSE_B1F_1_LINK]
    )
#Celadon Store 1F
    Celadon_Dept_Store_1F_Node = Node(
        [kmd.Celadon_Dept_Store_1F_Links.CELADON_DEPT_STORE_1F_TO_CELADON_CITY_1_LINK,
         kmd.Celadon_Dept_Store_1F_Links.CELADON_DEPT_STORE_1F_TO_CELADON_DEPT_STORE_2F_2_LINK]
    )
#Celadon Store 2F
    Celadon_Dept_Store_2F_Node = Node(
        [kmd.Celadon_Dept_Store_2F_Links.CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_3F_1_LINK,
         kmd.Celadon_Dept_Store_2F_Links.CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_1F_3_LINK]
    )
#Celadon Store 3F
    Celadon_Dept_Store_3F_Node = Node(
        [kmd.Celadon_Dept_Store_3F_Links.CELADON_DEPT_STORE_3F_TO_CELADON_DEPT_STORE_2F_1_LINK,
         kmd.Celadon_Dept_Store_3F_Links.CELADON_DEPT_STORE_3F_TO_CELADON_DEPT_STORE_4F_2_LINK]
    )
#Celadon Store 4F
    Celadon_Dept_Store_4F_Node = Node(
        [kmd.Celadon_Dept_Store_4F_Links.CELADON_DEPT_STORE_4F_TO_CELADON_DEPT_STORE_5F_1_LINK,
         kmd.Celadon_Dept_Store_4F_Links.CELADON_DEPT_STORE_4F_TO_CELADON_DEPT_STORE_3F_2_LINK]
    )
#Celadon Store 5F
    Celadon_Dept_Store_5F_Node = Node(
        [kmd.Celadon_Dept_Store_5F_Links.CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_4F_1_LINK,
         kmd.Celadon_Dept_Store_5F_Links.CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_6F_1_LINK]
    )
#Celadon Mansion Front 1F
    Celadon_Mansion_1F_Front_Node = Node(
        [kmd.Celadon_Mansion_1F_Links.CELADON_MANSION_1F_TO_CELADON_CITY_2_LINK,
         kmd.Celadon_Mansion_1F_Links.CELADON_MANSION_1F_TO_CELADON_MANSION_2F_4_LINK]
    )
#Celadon Mansion Back 1F
    Celadon_Mansion_1F_Back_Node = Node(
        [kmd.Celadon_Mansion_1F_Links.CELADON_MANSION_1F_TO_CELADON_CITY_3_LINK,
         kmd.Celadon_Mansion_1F_Links.CELADON_MANSION_1F_TO_CELADON_MANSION_2F_1_LINK]
    )
#Celadon Mansion Front 2F
    Celadon_Mansion_2F_Front_Node = Node(
        [kmd.Celadon_Mansion_2F_Links.CELADON_MANSION_2F_TO_CELADON_MANSION_3F_3_LINK,
         kmd.Celadon_Mansion_2F_Links.CELADON_MANSION_2F_TO_CELADON_MANSION_1F_5_LINK]
    )
#Celadon Mansion Back 2F
    Celadon_Mansion_2F_Back_Node = Node(
        [kmd.Celadon_Mansion_2F_Links.CELADON_MANSION_2F_TO_CELADON_MANSION_1F_4_LINK, 
         kmd.Celadon_Mansion_2F_Links.CELADON_MANSION_2F_TO_CELADON_MANSION_3F_2_LINK]
    )
#Celadon Mansion Front 3F
    Celadon_Mansion_3F_Front_Node = Node(
        [kmd.Celadon_Mansion_3F_Links.CELADON_MANSION_3F_TO_CELADON_MANSION_2F_3_LINK,
         kmd.Celadon_Mansion_3F_Links.CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_2_LINK]
    )
#Celadon Mansion Back 3F
    Celadon_Mansion_3F_Back_Node = Node(
        [kmd.Celadon_Mansion_3F_Links.CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_1_LINK,
         kmd.Celadon_Mansion_3F_Links.CELADON_MANSION_3F_TO_CELADON_MANSION_2F_2_LINK]
    )
#Celadon Mansion Roof Back 
    Celadon_Mansion_Roof_Node = Node(
        [kmd.Celadon_Mansion_Roof_Links.CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_1_LINK, 
         kmd.Celadon_Mansion_Roof_Links.CELADON_MANSION_ROOF_TO_CELADON_MANSION_ROOF_HOUSE_1_LINK]
    )
#Saffron CopyCat 1F
    Copycats_House_1F_Node = Node(
        [kmd.Copycats_House_1F_Links.COPYCATS_HOUSE_1F_TO_SAFFRON_CITY_8_LINK, 
         kmd.Copycats_House_1F_Links.COPYCATS_HOUSE_1F_TO_COPYCATS_HOUSE_2F_1_LINK]
    )
#Fast Ship F1 Corridor
    Fast_Ship_1F_Corridor_Node = Node(
        [kmd.Fast_Ship_1F_Links.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5_LINK, 
         kmd.Fast_Ship_1F_Links.FAST_SHIP_1F_TO_FAST_SHIP_B1F_1_LINK]
    )
#Fast Ship B1F Corridor
    Fast_Ship_B1F_Node = Node(
        [kmd.Fast_Ship_B1F_Links.FAST_SHIP_B1F_TO_FAST_SHIP_1F_11_LINK, 
         kmd.Fast_Ship_B1F_Links.FAST_SHIP_B1F_TO_FAST_SHIP_1F_12_LINK]
    )


class HubNodes_Kanto(Enum):

#Mount Moon 
    Mount_Moon_Node = Node(
        [kmd.Mount_Moon_Links.MOUNT_MOON_TO_ROUTE_3_1_LINK,
         kmd.Mount_Moon_Links.MOUNT_MOON_TO_ROUTE_4_1_LINK,
         kmd.Mount_Moon_Links.MOUNT_MOON_TO_MOUNT_MOON_7_LINK]
    )
#Mount Moon Square 
    Mount_Moon_Square_Node = Node(
        [link for link in kmd.Mount_Moon_Square_Links]
    )

#Fast Ship Hub
    Fast_Ship_1F_Hub_Node = Node(
        [link for link in kmd.Fast_Ship_1F_Links if link not in
         [kmd.Fast_Ship_1F_Links.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5_LINK,
         kmd.Fast_Ship_1F_Links.FAST_SHIP_1F_TO_FAST_SHIP_B1F_1_LINK]]
    )









  

# print("Printing Major Node Connection Numbers")
# for node in MajorNodes:
#     print(node.value.TOTAL_LINKS)
#
# print("Printing Corridor Connection Numbers")
# for node in TwoWayCorridorNodes:
#     print(node.value.TOTAL_LINKS)
#
# print("Printing Hub Node Connection Numbers")
# for node in HubNodes:
#     print(node.value.TOTAL_LINKS)
#
# print("Printing Deadend Node Connection Numbers")
# for node in DeadEndNodes:
#     print(node.value.TOTAL_LINKS)
