import itertools
from enum import Enum

from class_definitions import Node

#import links_and_nodes.get("kanto_all_Link")as kanto
from links_and_nodes import johto_all_warp_points_dict

johto = johto_all_warp_points_dict.buildJohtoWarpLinks()

def buildJohtoMajorNodes(excludeMart):
    MajorNodes_Johto = dict()
    MajorNodes_Johto['New Bark and Cherrygrove Node'] = Node(
        [johto["Cherrygrove_City_Links"].get(key) for key in johto["Cherrygrove_City_Links"] if key != "CHERRYGROVE_CITY_TO_CHERRYGROVE_MART_LINK"] +
        [johto["Cherrygrove_City_Links"].get(key) for key in johto["Cherrygrove_City_Links"] if key == "CHERRYGROVE_CITY_TO_CHERRYGROVE_MART_LINK" and not excludeMart] +
        [johto["Route_29_Links"].get(key) for key in johto["Route_29_Links"]] +
        [johto["Route_30_Links"].get(key) for key in johto["Route_30_Links"]]

    )

    MajorNodes_Johto['Violet City and Route 32 Node'] = Node(
            [johto["Violet_City_Links"].get(key) for key in johto["Violet_City_Links"]]
        +   [johto["Route_36_Links"].get("ROUTE_36_TO_ROUTE_36_RUINS_OF_ALPH_GATE_LINK")]
        +   [johto["Route_32_Links"].get(key) for key in johto["Route_32_Links"]]
    )

    MajorNodes_Johto['Azalea Town and Route 32 Node'] = Node(
        [johto["Azalea_Town_Links"].get(key) for key in johto["Azalea_Town_Links"]] +
        [johto["Route_33_Links"].get("ROUTE_33_TO_UNION_CAVE_1F_LINK")])

    MajorNodes_Johto['Goldenrod City and Route 34 Node'] = Node(
        [johto["Goldenrod_City_Links"].get(key) for key in johto["Goldenrod_City_Links"]] +
        [johto["Route_34_Links"].get(key) for key in johto["Route_34_Links"]]
    )

    MajorNodes_Johto['Ecruteak_City_Node'] = Node(
        [johto["Ecruteak_City_Links"].get(key) for key in johto["Ecruteak_City_Links"] if key not in
            ["ECRUTEAK_CITY_TO_TIN_TOWER_1F_LINK","ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_LINK"]
         ]
    )

    MajorNodes_Johto['Olivine City, Route 38 and Route 39 Node'] = Node(
        [johto["Route_38_Links"].get(key) for key in johto["Route_38_Links"]] +
        [johto["Route_39_Links"].get(key) for key in johto["Route_39_Links"]] +
        [johto["Olivine_City_Links"].get(key) for key in johto["Olivine_City_Links"] if key != "OLIVINE_CITY_TO_OLIVINE_PORT_PASSAGE_LINK"] +
        [johto["Route_40_Links"].get("ROUTE_40_TO_ROUTE_40_BATTLE_TOWER_GATE_1_LINK")]
    )

    MajorNodes_Johto['Cianwood City Node'] = Node(
        [johto["Cianwood_City_Links"].get(key) for key in johto["Cianwood_City_Links"]]
    )

    MajorNodes_Johto['Mahogany Town Node'] = Node(
        [johto["Mahogany_Town_Links"].get(key) for key in johto["Mahogany_Town_Links"]] +
        [johto["Route_42_Links"].get("ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_RIGHT_LINK")] +
        [johto["Route_44_Links"].get("ROUTE_44_TO_ICE_PATH_1F_LINK")]
    )

    MajorNodes_Johto['Blackthorn City Node'] = Node(
        [johto["Blackthorn_City_Links"].get(key) for key in johto["Blackthorn_City_Links"]] +
        [johto["Route_45_Links"].get(key) for key in johto["Route_45_Links"]]
    )

    return MajorNodes_Johto

def buildJohtoImportantDeadEnds(excludeMart):
    ImportantDeadEndNodes_Johto = dict()

    ImportantDeadEndNodes_Johto['Lighthouse 3F Middle Room Node'] = Node(
        [johto["Olivine_Lighthouse_3F_Links"].get("OLIVINE_LIGHTHOUSE_3F_TO_4F_MIDDLE_STAIR_LINK")]
    )

    ImportantDeadEndNodes_Johto['Tin Tower 5F NW Deadend Node'] = Node(
        [johto["Tin_Tower_5F_Links"].get("TIN_TOWER_5F_TO_TIN_TOWER_4F_1_LINK")]
    )
    # Tintower 5F Deadend SE
    ImportantDeadEndNodes_Johto['Tin Tower 5F SE Deadend Node'] = Node(
        [johto["Tin_Tower_5F_Links"].get("TIN_TOWER_5F_TO_TIN_TOWER_4F_4_LINK")]
    )
    # Tintower 5F Deadend S
    ImportantDeadEndNodes_Johto['Tin Tower 5F S Deadend Node'] = Node(
        [johto["Tin_Tower_5F_Links"].get("TIN_TOWER_5F_TO_TIN_TOWER_6F_2_LINK")]
    )
    # Tintower 5F Deadend SW
    ImportantDeadEndNodes_Johto['Tin Tower 5F Deadend SW Node'] = Node(
        [johto["Tin_Tower_5F_Links"].get("TIN_TOWER_5F_TO_TIN_TOWER_4F_3_LINK")]
    )

    # Tintower 8F Deadend Middle
    ImportantDeadEndNodes_Johto['Tin Tower 8F Middle Node'] = Node(
        [johto["Tin_Tower_8F_Links"].get("TIN_TOWER_8F_TO_TIN_TOWER_9F_7_LINK")]
    )
    # Tintower 8F Deadend S
    ImportantDeadEndNodes_Johto['Tin Tower 8F S Node'] = Node(
        [johto["Tin_Tower_8F_Links"].get("TIN_TOWER_8F_TO_TIN_TOWER_9F_6_LINK")]
    )

    ImportantDeadEndNodes_Johto['Route 46 Berry Tree Node'] = Node(
        [johto["Route_46_Links"].get("ROUTE_46_TO_DARK_CAVE_VIOLET_ENTRANCE_LINK")]
    )

    ImportantDeadEndNodes_Johto['Route 39 Barn Node'] = Node(
        [johto["Route_39_Barn_Links"].get(key) for key in johto["Route_39_Barn_Links"]]
    )

    ImportantDeadEndNodes_Johto['Route 39 Farmhouse Node'] = Node(
        [johto["Route_39_Farmhouse_Links"].get(key) for key in johto["Route_39_Farmhouse_Links"]]
    )

    ImportantDeadEndNodes_Johto['Sprout Tower 3F Node'] = Node(
        [johto["Sprout_Tower_3F_Links"].get("SPROUT_TOWER_3F_TO_SPROUT_TOWER_2F_LINK")]
    )

    ImportantDeadEndNodes_Johto['E4 Lances Room Node'] = Node(
        [johto["Lances_Room_Links"].get("LANCES_ROOM_TO_KARENS_ROOM_LINK")]
    )

    ImportantDeadEndNodes_Johto['Route 36 National Park Gate Node'] = Node(
        [johto["Route_36_Links"].get("ROUTE_36_TO_ROUTE_36_NATIONAL_PARK_GATE_LINK")]
    )

    ImportantDeadEndNodes_Johto['Olivine Cafe Node'] = Node(
        [johto["Olivine_Cafe_Links"].get(key) for key in johto["Olivine_Cafe_Links"]])

    ImportantDeadEndNodes_Johto['Olivine Good Rod House Node'] = Node(
        [johto["Olivine_Good_Rod_House_Links"].get(key) for key in johto["Olivine_Good_Rod_House_Links"]])

    ImportantDeadEndNodes_Johto['Olivine Gym Node'] = Node(
        [johto["Olivine_Gym_Links"].get(key) for key in johto["Olivine_Gym_Links"]])

    ImportantDeadEndNodes_Johto['Olivine Mart Node'] = Node(
        [johto["Olivine_Mart_Links"].get(key) for key in johto["Olivine_Mart_Links"]])

    ImportantDeadEndNodes_Johto['Olivine Tims House Node'] = Node(
        [johto["Olivine_Tims_House_Links"].get(key) for key in johto["Olivine_Tims_House_Links"]])

    ImportantDeadEndNodes_Johto['Cherrygrove Mart Node'] = Node(
        [johto["Cherrygrove_Mart_Links"].get(key) for key in johto["Cherrygrove_Mart_Links"]])

    ImportantDeadEndNodes_Johto['Route 30 Mr Pokemons House Node'] = Node(
        [johto["Mr_Pokemons_House_Links"].get(key) for key in johto["Mr_Pokemons_House_Links"]])

    ImportantDeadEndNodes_Johto['Route 30 Berry House Node'] = Node(
        [johto["Route_30_Berry_House_Links"].get(key) for key in johto["Route_30_Berry_House_Links"]])

    ImportantDeadEndNodes_Johto['Violet Mart Node'] = Node(
        [johto["Violet_City_Mart_Links"].get(key) for key in johto["Violet_City_Mart_Links"]])

    ImportantDeadEndNodes_Johto['Violet Gym Node'] = Node(
        [johto["Violet_City_Gym_Links"].get(key) for key in johto["Violet_City_Gym_Links"]])

    ImportantDeadEndNodes_Johto['Violet Kyles House Node'] = Node(
        [johto["Violet_City_Kyles_House_Links"].get(key) for key in johto["Violet_City_Kyles_House_Links"]])

    ImportantDeadEndNodes_Johto['Azalea Gym Node'] = Node(
        [johto["Azalea_Gym_Links"].get(key) for key in johto["Azalea_Gym_Links"]]
    )

    ImportantDeadEndNodes_Johto['Azalea Mart Node'] = Node(
        [johto["Azalea_Mart_Links"].get(key) for key in johto["Azalea_Mart_Links"]]
    )

    ImportantDeadEndNodes_Johto['Azalea Charcoal Kiln Node'] = Node(
        [johto["Charcoal_Kiln_Links"].get(key) for key in johto["Charcoal_Kiln_Links"]]
    )

    ImportantDeadEndNodes_Johto['Azalea Kurts House Node'] = Node(
        [johto["Kurts_House_Links"].get(key) for key in johto["Kurts_House_Links"]]
    )

    ImportantDeadEndNodes_Johto['Blackthorn Gym Node'] = Node(
        [johto["Blackthorn_Gym_Links"].get(key) for key in johto["Blackthorn_Gym_Links"]]
    )

    ImportantDeadEndNodes_Johto['Blackthorn Mart Node'] = Node(
        [johto["Blackthorn_Mart_Links"].get(key) for key in johto["Blackthorn_Mart_Links"]]
    )

    ImportantDeadEndNodes_Johto['Blackthorn Move Deleters House Node'] = Node(
        [johto["Move_Deleters_House_Links"].get(key) for key in johto["Move_Deleters_House_Links"]]
    )

    ImportantDeadEndNodes_Johto['Cianwood Gym Node'] = Node(
        [johto["Cianwood_Gym_Links"].get(key) for key in johto["Cianwood_Gym_Links"]]
    )

    ImportantDeadEndNodes_Johto['Cianwood Pharmacy Node'] = Node(
        [johto["Cianwood_Pharmacy_Links"].get(key) for key in johto["Cianwood_Pharmacy_Links"]]
    )

    ImportantDeadEndNodes_Johto['Cianwood Manias House Node'] = Node(
        [johto["Manias_House_Links"].get(key) for key in johto["Manias_House_Links"]]
    )

    ImportantDeadEndNodes_Johto['Cianwood Poke Seers House Node'] = Node(
        [johto["Poke_Seers_House_Links"].get(key) for key in johto["Poke_Seers_House_Links"]]
    )

    # TODO This is technically a corridor
    ImportantDeadEndNodes_Johto['Burned Tower 1F Node'] = Node(
        [johto["Burned_Tower_1F_Links"].get(key) for key in johto["Burned_Tower_1F_Links"]]
    )

    ImportantDeadEndNodes_Johto['Ilex Forest From Route 34 Gate (North Portion) Node'] = Node(
        [johto["Ilex_Forest_Links"].get("ILEX_FOREST_TO_ROUTE_34_ILEX_FOREST_GATE_LINK")]
    )

    ImportantDeadEndNodes_Johto['Ilex Forest From Azalea Gate (South Portion) Node'] = Node(
        [johto["Ilex_Forest_Links"].get("ILEX_FOREST_TO_ILEX_FOREST_AZALEA_GATE_LINK")]
    )

    ImportantDeadEndNodes_Johto['Slowpoke Well B1F (From Overworld) Node'] = Node(
        [johto["Slowpoke_Well_B1F_Links"].get("SLOWPOKE_WELL_B1F_TO_AZALEA_TOWN_LINK")]
    )

    ImportantDeadEndNodes_Johto['Slowpoke Well B2F Node'] = Node(
        [johto["Slowpoke_Well_B2F_Links"].get("SLOWPOKE_WELL_B2F_TO_SLOWPOKE_WELL_B1F_LINK")]
    )

    # TODO Technically a corridor
    ImportantDeadEndNodes_Johto['Tin Tower 1F Node'] = Node(
        [johto["Tin_Tower_1F_Links"].get("TIN_TOWER_1F_TO_ECRUTEAK_CITY_LINK")]
    )

    ImportantDeadEndNodes_Johto['Ecruteak Dance Theatre Node'] = Node(
        [johto["Dance_Theatre_Links"].get(key) for key in johto["Dance_Theatre_Links"]]
    )

    ImportantDeadEndNodes_Johto['Ecruteak Gym Node'] = Node(
        [johto["Ecruteak_Gym_Links"].get(key) for key in johto["Ecruteak_Gym_Links"]]
    )

    ImportantDeadEndNodes_Johto['Ecruteak Item Finder House Node'] = Node(
        [johto["Ecruteak_Item_Finder_House_Links"].get(key) for key in johto["Ecruteak_Item_Finder_House_Links"]]
    )

    ImportantDeadEndNodes_Johto['Lake of Rage Hidden Power House Node'] = Node(
        [johto["Lake_Of_Rage_Hidden_Power_House_Links"].get(key) for key in johto["Lake_Of_Rage_Hidden_Power_House_Links"]]
    )

    ImportantDeadEndNodes_Johto['Lake of Rage Magikarp House Node'] = Node(
        [johto["Lake_Of_Rage_Magikarp_House_Links"].get(key) for key in johto["Lake_Of_Rage_Magikarp_House_Links"]]
    )

    ImportantDeadEndNodes_Johto['Day Care Node'] = Node(
        [johto["Day_Care_Links"].get(key) for key in johto["Day_Care_Links"]]
    )

    ImportantDeadEndNodes_Johto['Goldenrod Bike Shop Node'] = Node(
        [johto["Goldenrod_Bike_Shop_Links"].get(key) for key in johto["Goldenrod_Bike_Shop_Links"]]
    )

    ImportantDeadEndNodes_Johto['Goldenrod Dept Store Roof Node'] = Node(
        [johto["Goldenrod_Dept_Store_Roof_Links"].get("GOLDENROD_DEPT_STORE_ROOF_TO_GOLDENROD_DEPT_STORE_6F_3_LINK")]
    )

    ImportantDeadEndNodes_Johto['Goldenrod Flower Shop Node'] = Node(
        [johto["Goldenrod_Flower_Shop_Links"].get(key) for key in johto["Goldenrod_Flower_Shop_Links"]]
    )

    ImportantDeadEndNodes_Johto['Goldenrod_Game_Corner_Node'] = Node(
        [johto["Goldenrod_Game_Corner_Links"].get(key) for key in johto["Goldenrod_Game_Corner_Links"]]
    )

    ImportantDeadEndNodes_Johto['Goldenrod Gym Node'] = Node(
        [johto["Goldenrod_Gym_Links"].get(key) for key in johto["Goldenrod_Gym_Links"]]
    )

    #TODO Technically a cooridor
    ImportantDeadEndNodes_Johto['Route 42 Middle Node'] = Node(
        [johto["Route_42_Links"].get("ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_MIDDLE_LINK")]
    )

    ImportantDeadEndNodes_Johto['Whirl Island Lugia Chamber Node'] = Node(
        [johto["Whirl_Island_Lugia_Chamber_Links"].get("WHIRL_ISLAND_LUGIA_CHAMBER_TO_WHIRL_ISLAND_B2F_LINK")]
    )

    ImportantDeadEndNodes_Johto['Whirl Island B1F Escape Rope Node'] = Node(
        [johto["Whirl_Island_B1F_Links"].get("WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_3_LINK")]
    )

    ImportantDeadEndNodes_Johto['Whirl Island B2F Single Item_Node'] = Node(
        [johto["Whirl_Island_B2F_Links"].get("WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_7_LINK")]
    )

    ImportantDeadEndNodes_Johto['Whirl Island B2F Double Item Node'] = Node(
        [johto["Whirl_Island_B2F_Links"].get("WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_8_LINK")]
    )

    ImportantDeadEndNodes_Johto['Whirl Island NE Middle Node'] = Node(
        [johto["Whirl_Island_NE_Links"].get("WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_3_LINK")]
    )

    ImportantDeadEndNodes_Johto['Whirl Island SW Item Node'] = Node(
        [johto["Whirl_Island_SW_Links"].get("WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_5_LINK")]
    )

    ImportantDeadEndNodes_Johto['Tin Tower Roof Node'] = Node(
        [johto["Tin_Tower_Roof_Links"].get("TIN_TOWER_ROOF_TO_TIN_TOWER_9F_LINK")]
    )

    ImportantDeadEndNodes_Johto['Goldenrod Magnet Train Station Node'] = Node(
        [johto["Goldenrod_Magnet_Train_Station_Links"].get(key) for key in johto["Goldenrod_Magnet_Train_Station_Links"]]
    )

    # TODO Technically Corridor
    ImportantDeadEndNodes_Johto['Goldenrod Radio Tower 1F Node'] = Node(
        [johto["Radio_Tower_1F_Links"].get(key) for key in johto["Radio_Tower_1F_Links"]]
    )

    # TODO Technically a corridor after trigger
    ImportantDeadEndNodes_Johto['Mahogany Mart Node'] = Node(
        [johto["Mahogany_Mart_Links"].get(key) for key in johto["Mahogany_Mart_Links"]]
    )

    ImportantDeadEndNodes_Johto['Mahogany Gym Node'] = Node(
        [johto["Mahogany_Gym_Links"].get(key) for key in johto["Mahogany_Gym_Links"]]
    )

    ImportantDeadEndNodes_Johto['Ecruteak Mart Node'] = Node(
        [johto["Ecruteak_Mart_Links"].get(key) for key in johto["Ecruteak_Mart_Links"]]
    )

    ImportantDeadEndNodes_Johto['Dragon Shrine Node'] = Node(
        [johto["Dragon_Shrine_Links"].get("DRAGON_SHRINE_TO_DRAGONS_DEN_B1F_2_LINK")]
    )

    ImportantDeadEndNodes_Johto['Mount Mortar 1F Outside Left Item Node'] = Node(
        [johto["Mount_Mortar_1F_Outside_Links"].get("MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_3_LINK")]
    )
    ImportantDeadEndNodes_Johto['Mount Mortar 1F Outside Right Item Node'] = Node(
        [johto["Mount_Mortar_1F_Outside_Links"].get("MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_4_LINK")]
    )

    ImportantDeadEndNodes_Johto['Mount Mortar B1F Upper Node'] = Node(
        [johto["Mount_Mortar_B1F_Links"].get("MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_INSIDE_5_LINK")]
    )

    ImportantDeadEndNodes_Johto['Mount Mortar 2F Inside Uppder Node'] = Node(
        [johto["Mount_Mortar_2F_Inside_Links"].get("MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_INSIDE_6_LINK")]
    )
    ImportantDeadEndNodes_Johto['Mount Mortar 2F Inside Lower Node'] = Node(
        [johto["Mount_Mortar_2F_Inside_Links"].get("MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_4_LINK")]
    )

    ImportantDeadEndNodes_Johto['Dark Cave Blackthorn Entrance (From Route 45) Node'] = Node(
        [johto["Dark_Cave_Blackthorn_Entrance_Links"].get("DARK_CAVE_BLACKTHORN_ENTRANCE_TO_ROUTE_45_LINK")]
    )

    ImportantDeadEndNodes_Johto['Dark Cave (From Route 31) Node'] = Node(
        [johto["Dark_Cave_Violet_Entrance_Links"].get("DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_31_LINK")]
    )
    ImportantDeadEndNodes_Johto['Dark Cave (From Route 46) Node'] = Node(
        [johto["Dark_Cave_Violet_Entrance_Links"].get("DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_46_LINK")]
    )

    ImportantDeadEndNodes_Johto['Dragons Den B1F North Shore Node'] = Node(
        [johto["Dragons_Den_B1F_Links"].get("DRAGONS_DEN_B1F_TO_DRAGONS_DEN_1F_3_LINK")]
    )

    ImportantDeadEndNodes_Johto['Dragons Den B1F Dragon Shrine Shore Node'] = Node(
        [johto["Dragons_Den_B1F_Links"].get("DRAGONS_DEN_B1F_TO_DRAGON_SHRINE_1_LINK")]
    )

    ImportantDeadEndNodes_Johto['Union Cave B1F Item Node'] = Node(
        [johto["Union_Cave_B1F_Links"].get("UNION_CAVE_B1F_TO_UNION_CAVE_1F_1_LINK")]
    )

    ImportantDeadEndNodes_Johto['Union Cave B2F Node'] = Node(
        [johto["Union_Cave_B2F_Links"].get("UNION_CAVE_B2F_TO_UNION_CAVE_B1F_5_LINK")]
    )
    # victory road gate bottom
    ImportantDeadEndNodes_Johto['Victory Road Gate (From Johto) Node'] = Node(
        [johto["Victory_Road_Gate_Links"].get("VICTORY_ROAD_GATE_TO_ROUTE_26_1_LINK")]
    )
    # tohjo fall interior left
    ImportantDeadEndNodes_Johto['Tohjo Falls Interior (West) Node'] = Node(
        [johto["Tohjo_Falls_Links"].get("TOHJO_FALLS_TO_ROUTE_27_2_LINK")]
    )

#sandstorm house interior
    ImportantDeadEndNodes_Johto['Route 27 Sandstorm House Node'] = Node(
        [johto["Route_27_Sandstorm_House_Links"].get("ROUTE_27_SANDSTORM_HOUSE_TO_ROUTE_27_1_LINK")]
    )
#route 26 heal house interior
    ImportantDeadEndNodes_Johto['Route 26 Heal House Node'] = Node(
        [johto["Route_26_Heal_House_Links"].get("ROUTE_26_HEAL_HOUSE_TO_ROUTE_26_2_LINK")]
    )

    ImportantDeadEndNodes_Johto['Victory Road Cave Middle Room Item Node'] = Node(
        [johto["Victory_Road_Links"].get("VICTORY_ROAD_TO_VICTORY_ROAD_7_LINK")]
    )

    return ImportantDeadEndNodes_Johto

def buildJohtoUselessDeadEnds():

    UnreachableUselessDeadEndNodes_Johto = dict()

    UnreachableUselessDeadEndNodes_Johto['Ruins Of Alph Research Center Node'] = Node(
        [johto["Ruins_Of_Alph_Research_Center_Links"].get(key) for key in johto["Ruins_Of_Alph_Research_Center_Links"]]
    )

    UnreachableUselessDeadEndNodes_Johto['Goldenrod PP Speech House Node'] = Node(
        [johto["Goldenrod_PP_Speech_House_Links"].get(key) for key in johto["Goldenrod_PP_Speech_House_Links"]]
    )

    # route 26 day of week sibling house interior
    UnreachableUselessDeadEndNodes_Johto['Route 26 Day Of Week Sibling House Node'] = Node(
        [johto["Day_Of_Week_Siblings_House_Links"].get("DAY_OF_WEEK_SIBLINGS_HOUSE_TO_ROUTE_26_3_LINK")]
    )

    UnreachableUselessDeadEndNodes_Johto['Violet Earls Pokemon Academy Node'] = Node(
        [johto["Earls_Pokemon_Academy_Links"].get(key) for key in johto["Earls_Pokemon_Academy_Links"]])

    UnreachableUselessDeadEndNodes_Johto['Olivine Punishment Speech House Node'] = Node(
        [johto["Olivine_Punishment_Speech_House_Links"].get(key) for key in johto["Olivine_Punishment_Speech_House_Links"]])

    UnreachableUselessDeadEndNodes_Johto['Cherrygrove Gym Speech House Node'] = Node(
        [johto["Cherrygrove_Gym_Speech_House_Links"].get(key) for key in johto["Cherrygrove_Gym_Speech_House_Links"]])

    UnreachableUselessDeadEndNodes_Johto['Cherrygrove Evolution Speech House Node'] = Node(
        [johto["Cherrygrove_Evolution_Speech_House_Links"].get(key) for key in johto["Cherrygrove_Evolution_Speech_House_Links"]])

    UnreachableUselessDeadEndNodes_Johto['Cherrygrove Guide Gents House Node'] = Node(
        [johto["Guide_Gents_House_Links"].get(key) for key in johto["Guide_Gents_House_Links"]])

    UnreachableUselessDeadEndNodes_Johto['Violet Nickname Speech House Node'] = Node(
        [johto["Violet_Nickname_Speech_House_Links"].get(key) for key in johto["Violet_Nickname_Speech_House_Links"]])

    UnreachableUselessDeadEndNodes_Johto['Blackthorn Emys House Node'] = Node(
        [johto["Blackthorn_Emys_House_Links"].get(key) for key in johto["Blackthorn_Emys_House_Links"]]
    )

    UnreachableUselessDeadEndNodes_Johto['Blackthorn Dragon Speech House Node'] = Node(
        [johto["Blackthorn_Dragon_Speech_House_Links"].get(key) for key in johto["Blackthorn_Dragon_Speech_House_Links"]]
    )

    UnreachableUselessDeadEndNodes_Johto['Cianwood Lugia Speech House Node'] = Node(
        [johto["Cianwood_Lugia_Speech_House_Links"].get(key) for key in johto["Cianwood_Lugia_Speech_House_Links"]]
    )

    UnreachableUselessDeadEndNodes_Johto['Goldenrod Happiness Rater Node'] = Node(
        [johto["Goldenrod_Happiness_Rater_Links"].get(key) for key in johto["Goldenrod_Happiness_Rater_Links"]]
    )

    UnreachableUselessDeadEndNodes_Johto['Ecruteak Lugia Speech House Node'] = Node(
        [johto["Ecruteak_Lugia_Speech_House_Links"].get(key) for key in johto["Ecruteak_Lugia_Speech_House_Links"]]
    )

    UnreachableUselessDeadEndNodes_Johto['Goldenrod Name Rater Node'] = Node(
        [johto["Goldenrod_Name_Rater_Links"].get(key) for key in johto["Goldenrod_Name_Rater_Links"]]
    )

    return UnreachableUselessDeadEndNodes_Johto

def buildJohtoReachableDeadEnds():

    ReachableUselessDeadEndNodes_Johto = dict()

    ReachableUselessDeadEndNodes_Johto['Victory Road Cave Upper Room (Below Ledge) Node'] = Node(
        [johto["Victory_Road_Links"].get("VICTORY_ROAD_TO_VICTORY_ROAD_6_LINK")]
    )

    # route 27 tohjo fall entrance left
    ReachableUselessDeadEndNodes_Johto['Route 27 (To Tohjo Falls West) Node'] = Node(
        [johto["Route_27_Links"].get("ROUTE_27_TO_TOHJO_FALLS_1_LINK")]
    )

    # tohjo fall interior right
    ReachableUselessDeadEndNodes_Johto['Tohjo Falls (East) Node'] = Node(
        [johto["Tohjo_Falls_Links"].get("TOHJO_FALLS_TO_ROUTE_27_3_LINK")]
    )
    # route 41 whirl entrance nw
    ReachableUselessDeadEndNodes_Johto['Route 41 (Whirl Island NW) Node'] = Node(
        [johto["Route_41_Links"].get("ROUTE_41_TO_WHIRL_ISLAND_NW_LINK")]
    )
    # route 41 whirl entrance ne
    ReachableUselessDeadEndNodes_Johto['Route 41 (Whirl Island NE) Node'] = Node(
        [johto["Route_41_Links"].get("ROUTE_41_TO_WHIRL_ISLAND_NE_LINK")]
    )
    # route 41 whirl entrance sw
    ReachableUselessDeadEndNodes_Johto['Route 41 To (Whirl Island SW) Node'] = Node(
        [johto["Route_41_Links"].get("ROUTE_41_TO_WHIRL_ISLAND_SW_LINK")]
    )
    # route 41 whirl entrance se
    ReachableUselessDeadEndNodes_Johto['Route 41 (Whirl Island SE) Node'] = Node(
        [johto["Route_41_Links"].get("ROUTE_41_TO_WHIRL_ISLAND_SE_LINK")]
    )
    ReachableUselessDeadEndNodes_Johto['Union Cave B1F North (Lower Half, Blocked by Boulder) Node'] = Node(
        [johto["Union_Cave_B1F_Links"].get("UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_8_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Union Cave B1F North (Upper Half, Blocked by Boulder) Node'] = Node(
        [johto["Union_Cave_B1F_Links"].get("UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_7_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Whirl Island B1F (Central, Above Ledge) Node'] = Node(
        [johto["Whirl_Island_B1F_Links"].get("WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_CAVE_1_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Union Cave B1F S (West Half) Node'] = Node(
        [johto["Union_Cave_B1F_Links"].get("UNION_CAVE_B1F_TO_UNION_CAVE_1F_2_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Union Cave B1F S (East Half) Node'] = Node(
        [johto["Union_Cave_B1F_Links"].get("UNION_CAVE_B1F_TO_UNION_CAVE_B2F_1_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Slowpoke Well B1F To B2F Useless Node'] = Node(
        [johto["Slowpoke_Well_B1F_Links"].get("SLOWPOKE_WELL_B1F_TO_SLOWPOKE_WELL_B2F_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Dark Cave Violet Entrance From Blackthorn Side Node'] = Node(
        [johto["Dark_Cave_Violet_Entrance_Links"].get("DARK_CAVE_VIOLET_ENTRANCE_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Dark Cave Blackthorn Entrance From Violet Side Node'] = Node(
        [johto["Dark_Cave_Blackthorn_Entrance_Links"].get("DARK_CAVE_BLACKTHORN_ENTRANCE_TO_DARK_CAVE_VIOLET_ENTRANCE_LINK")]
    )


    ReachableUselessDeadEndNodes_Johto['Route 46 Route 29 Gate Node'] = Node(
        [johto["Route_46_Links"].get("ROUTE_46_TO_ROUTE_29_ROUTE_46_GATE_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Mount Mortar B1F (Lower) Node'] = Node(
        [johto["Mount_Mortar_B1F_Links"].get("MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_OUTSIDE_7_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Mount Mortar 1F Outside Center Upper Node'] = Node(
        [johto["Mount_Mortar_1F_Outside_Links"].get("MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_2F_INSIDE_1_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Lake Of Rage Maze Node'] = Node(
        [johto["Lake_Of_Rage_Links"].get("LAKE_OF_RAGE_TO_LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_LINK")]
    )

    # Ecruteak_Tin_Tower_Entrance_To_Wise_Trio_Room_Node = Node(
    #     [johto["Ecruteak_Tin_Tower_Entrance_Links"]ECRUTEAK_TIN_TOWER_ENTRANCE_TO_WISE_TRIOS_ROOM_LINK]
    # )

    ReachableUselessDeadEndNodes_Johto['Goldenrod Bills Familys House Node'] = Node(
        [johto["Bills_Familys_House_Links"].get(key) for key in johto["Bills_Familys_House_Links"]]
    )


    ReachableUselessDeadEndNodes_Johto['Whirl Island B2F (Ladder) Node'] = Node(
        [johto["Whirl_Island_B2F_Links"].get("WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_SW_5_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Whirl Island B2F (Cave) Node'] = Node(
        [johto["Whirl_Island_B2F_Links"].get("WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_LUGIA_CHAMBER_1_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Whirl Island NE (East Half) Node'] = Node(
        [johto["Whirl_Island_NE_Links"].get("WHIRL_ISLAND_N_E_TO_ROUTE_41_2_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Whirl Island NE (West Half) Node'] = Node(
        [johto["Whirl_Island_NE_Links"].get("WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_2_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Whirl Island SW (SW Portion) Node'] = Node(
        [johto["Whirl_Island_SW_Links"].get("WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_NW_3_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Whirl Island SW (SE Portion) Node'] = Node(
        [johto["Whirl_Island_SW_Links"].get("WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B2F_4_LINK")]
    )

    ReachableUselessDeadEndNodes_Johto['Union Cave 1F (Isolated Ladder) Node'] = Node(
        [johto["Union_Cave_1F_Links"].get("UNION_CAVE_1F_TO_UNION_CAVE_B1FB_LINK")]
    )

    return ReachableUselessDeadEndNodes_Johto

def buildJohtoCorridors():

    TwoWayCorridorNodes_Johto = dict()

    TwoWayCorridorNodes_Johto['Victory Road Cave (Lower J Room) Node'] = Node(
        [johto["Victory_Road_Links"].get("VICTORY_ROAD_TO_VICTORY_ROAD_GATE_5_LINK"),
         johto["Victory_Road_Links"].get("VICTORY_ROAD_TO_VICTORY_ROAD_3_LINK")]
    )

    TwoWayCorridorNodes_Johto['Victory Road Cave (Middle Room) Node'] = Node(
        [johto["Victory_Road_Links"].get("VICTORY_ROAD_TO_VICTORY_ROAD_2_LINK"),
         johto["Victory_Road_Links"].get("VICTORY_ROAD_TO_VICTORY_ROAD_5_LINK")]
    )

    # route 27 tohjo fall entrance right to sandstorm house
    TwoWayCorridorNodes_Johto['Tohjo Falls (East Half) Node'] = Node(
         [johto["Route_27_Links"].get("ROUTE_27_TO_TOHJO_FALLS_2_LINK"),
         johto["Route_27_Links"].get("ROUTE_27_TO_ROUTE_27_SANDSTORM_HOUSE_1_LINK")]
    )

    TwoWayCorridorNodes_Johto['Mount Mortar 1F Outside (SW Portion) Node'] = Node(
        [johto["Mount_Mortar_1F_Outside_Links"].get("MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_3_LINK"),
         johto["Mount_Mortar_1F_Outside_Links"].get("MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_1_LINK")]
    )
    TwoWayCorridorNodes_Johto['Mount Mortar 1F Outside (S Portion) Node'] = Node(
        [johto["Mount_Mortar_1F_Outside_Links"].get("MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_4_LINK"),
         johto["Mount_Mortar_1F_Outside_Links"].get("MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_B1F_2_LINK")]
    )
    TwoWayCorridorNodes_Johto['Mount Mortar 1F Outside (SE Portion) Node'] = Node(
        [johto["Mount_Mortar_1F_Outside_Links"].get("MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_5_LINK"),
         johto["Mount_Mortar_1F_Outside_Links"].get("MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_2_LINK")]
    )

    TwoWayCorridorNodes_Johto['Ice Path B2F (Lower Boulder Area) Node'] = Node(
        [johto["Ice_Path_B2F_Mahogany_Side_Links"].get("ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_2_LINK"),
         johto["Ice_Path_B2F_Mahogany_Side_Links"].get("ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B3F_1_LINK")]
    )

    TwoWayCorridorNodes_Johto['Ice Path B3F Node'] = Node(
        [johto["Ice_Path_B3F_Links"].get("ICE_PATH_B3F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_2_LINK"),
         johto["Ice_Path_B3F_Links"].get("ICE_PATH_B3F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_2_LINK")]
    )

    TwoWayCorridorNodes_Johto['Ice Path B2F Blackthorn Side Node'] = Node(
        [johto["Ice_Path_B2F_Blackthorn_Side_Links"].get("ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B1F_8_LINK"),
         johto["Ice_Path_B2F_Blackthorn_Side_Links"].get("ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B3F_2_LINK")]
    )

    TwoWayCorridorNodes_Johto['Ice Path B1F Blackthorn Side Node'] = Node(
        [johto["Ice_Path_B1F_Links"].get("ICE_PATH_B1F_TO_ICE_PATH_1F_4_LINK"),
         johto["Ice_Path_B1F_Links"].get("ICE_PATH_B1F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_1_LINK")]
    )

    TwoWayCorridorNodes_Johto['Ice Path 1F (Route 44 Side) Node'] = Node(
        [johto["Ice_Path_1F_Links"].get("ICE_PATH_1F_TO_ROUTE_44_1_LINK"),
         johto["Ice_Path_1F_Links"].get("ICE_PATH_1F_TO_ICE_PATH_B1F_1_LINK")]
    )

    TwoWayCorridorNodes_Johto['Ice Path 1F (Blackthorn Side) Node'] = Node(
        [johto["Ice_Path_1F_Links"].get("ICE_PATH_1F_TO_ICE_PATH_B1F_7_LINK"),
         johto["Ice_Path_1F_Links"].get("ICE_PATH_1F_TO_BLACKTHORN_CITY_7_LINK")]
    )

    TwoWayCorridorNodes_Johto['Route 42 (West Portion) Node'] = Node(
        [johto["Route_42_Links"].get("ROUTE_42_TO_ROUTE_42_ECRUTEAK_GATE_LINK"),
         johto["Route_42_Links"].get("ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_LEFT_LINK")]
    )

    TwoWayCorridorNodes_Johto['Sprout Tower 1F (Inner) Node'] = Node(
        [johto["Sprout_Tower_1F_Links"].get("SPROUT_TOWER_1F_TO_VIOLET_CITY_LINK"),
         johto["Sprout_Tower_1F_Links"].get("SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FA_LINK")]
    )

    TwoWayCorridorNodes_Johto['Sprout Tower 1F (Outer) Node'] = Node(
        [johto["Sprout_Tower_1F_Links"].get("SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FB_LINK"),
         johto["Sprout_Tower_1F_Links"].get("SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FC_LINK")]
    )

    TwoWayCorridorNodes_Johto['Sprout Tower 2F (NE) Node'] = Node(
        [johto["Sprout_Tower_2F_Links"].get("SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_5_LINK"),
         johto["Sprout_Tower_2F_Links"].get("SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_3_LINK")]
    )
    TwoWayCorridorNodes_Johto['Sprout Tower 2F (SW) Node'] = Node(
        [johto["Sprout_Tower_2F_Links"].get("SPROUT_TOWER_2F_TO_SPROUT_TOWER_3F_1_LINK"),
         johto["Sprout_Tower_2F_Links"].get("SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_4_LINK")]
    )

    TwoWayCorridorNodes_Johto['Goldenrod Underground Warehouse Node'] = Node(
        [johto["Goldenrod_Underground_Switch_Room_Entrance_Links"].get("GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_LINK"),
         johto["Goldenrod_Underground_Warehouse_Links"].get("GOLDENROD_UNDERGROUND_WAREHOUSE_TO_GOLDENROD_DEPT_STORE_B1F_LINK")]
    )

    TwoWayCorridorNodes_Johto['Goldenrod Switch Room Entrance (North) Node'] = Node(
        [johto["Goldenrod_Underground_Switch_Room_Entrance_Links"].get("GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_NORTH_LINK"),
         johto["Goldenrod_Underground_Switch_Room_Entrance_Links"].get("GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_NORTH_LINK")]
    )

    TwoWayCorridorNodes_Johto['Goldenrod Switch Room Entrance (South) Node'] = Node(
        [johto["Goldenrod_Underground_Switch_Room_Entrance_Links"].get("GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_SOUTH_LINK"),
         johto["Goldenrod_Underground_Switch_Room_Entrance_Links"].get("GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_SOUTH_LINK")]
    )

    TwoWayCorridorNodes_Johto['E4 Kogas Room Node'] = Node(
        [johto["Kogas_Room_Links"].get(key) for key in johto["Kogas_Room_Links"]]
    )

    TwoWayCorridorNodes_Johto['E4 Wills Room Node'] = Node(
        [johto["Wills_Room_Links"].get(key) for key in johto["Wills_Room_Links"]]
    )

    TwoWayCorridorNodes_Johto['E4 Karens Room Node'] = Node(
        [johto["Karens_Room_Links"].get(key) for key in johto["Karens_Room_Links"]]
    )

    TwoWayCorridorNodes_Johto['E4 Brunos Room Node'] = Node(
        [johto["Brunos_Room_Links"].get(key) for key in johto["Brunos_Room_Links"]]
    )

    TwoWayCorridorNodes_Johto['Ecruteak Pokecenter Node'] = Node(
        [johto["Ecruteak_Pokecenter_Links"].get(key) for key in johto["Ecruteak_Pokecenter_Links"]]
    )

    TwoWayCorridorNodes_Johto['Route 32 Pokecenter Node'] = Node(
        [johto["Route_32_Pokecenter_Links"].get(key) for key in johto["Route_32_Pokecenter_Links"]]
    )

    TwoWayCorridorNodes_Johto['Mahogany Pokecenter Node'] = Node(
        [johto["Mahogany_Pokecenter_Links"].get(key) for key in johto["Mahogany_Pokecenter_Links"]]
    )

    TwoWayCorridorNodes_Johto['Goldenrod Pokecenter Node'] = Node(
        [johto["Goldenrod_Pokecenter_Links"].get(key) for key in johto["Goldenrod_Pokecenter_Links"]]
    )

    TwoWayCorridorNodes_Johto['Cianwood Pokecenter Node'] = Node(
        [johto["Cianwood_Pokecenter_Links"].get(key) for key in johto["Cianwood_Pokecenter_Links"]]
    )

    TwoWayCorridorNodes_Johto['Blackthorn Pokecenter Node'] = Node(
        [johto["Blackthorn_Pokecenter_Links"].get(key) for key in johto["Blackthorn_Pokecenter_Links"]]
    )

    TwoWayCorridorNodes_Johto['Azalea Pokecenter Node'] = Node(
        [johto["Azalea_Pokecenter_Links"].get(key) for key in johto["Azalea_Pokecenter_Links"]]
    )

    TwoWayCorridorNodes_Johto['Violet Pokecenter Node'] = Node(
        [johto["Violet_City_Pokecenter_Links"].get(key) for key in johto["Violet_City_Pokecenter_Links"]]
    )

    TwoWayCorridorNodes_Johto['Cherrygrove Pokecenter Node'] = Node(
        [johto["Cherrygrove_Pokecenter_Links"].get(key) for key in johto["Cherrygrove_Pokecenter_Links"]])

    TwoWayCorridorNodes_Johto['Olivine Pokecenter Node'] = Node(
        [johto["Olivine_Pokecenter_Links"].get(key) for key in johto["Olivine_Pokecenter_Links"]])

    TwoWayCorridorNodes_Johto['Route 31 Node'] = Node(
        [johto["Route_31_Links"].get(key) for key in johto["Route_31_Links"]])

    TwoWayCorridorNodes_Johto['Ecruteak Wise Trio Room To Tin Tower Node'] = Node(
        [johto["Ecruteak_City_Links"].get(key) for key in johto["Ecruteak_City_Links"] if key in
         ["ECRUTEAK_CITY_TO_TIN_TOWER_1F_LINK","ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_LINK"]
         ]
    )

    TwoWayCorridorNodes_Johto['Lighthouse 1F Node'] = Node(
        [johto["Olivine_Lighthouse_1F_Links"].get(key) for key in johto["Olivine_Lighthouse_1F_Links"]]
    )

    TwoWayCorridorNodes_Johto['Lighthouse 5F (Outer) Node'] = Node(
        [johto["Olivine_Lighthouse_5F_Links"].get("OLIVINE_LIGHTHOUSE_5F_TO_4F_OUTER_STAIR_LINK"),
         johto["Olivine_Lighthouse_5F_Links"].get("OLIVINE_LIGHTHOUSE_5F_TO_4F_PITFALL_LINK")]
    )

    TwoWayCorridorNodes_Johto['Lighthouse 5F (Inner) Node'] = Node(
        [johto["Olivine_Lighthouse_5F_Links"].get("OLIVINE_LIGHTHOUSE_5F_TO_4F_INNER_STAIR_LINK"),
         johto["Olivine_Lighthouse_5F_Links"].get("OLIVINE_LIGHTHOUSE_5F_TO_6F_STAIR_LINK")]
    )

    TwoWayCorridorNodes_Johto['Lighthouse 6F Node'] = Node(
        [johto["Olivine_Lighthouse_6F_Links"].get(key) for key in johto["Olivine_Lighthouse_6F_Links"]]
    )

    TwoWayCorridorNodes_Johto['National Park Node'] = Node(
        [johto["National_Park_Links"].get(key) for key in johto["National_Park_Links"]]
    )

    TwoWayCorridorNodes_Johto['Gate - Route 29 Route 46 Node'] = Node(
        [johto["Route_29_Route_46_Gate_Links"].get(key) for key in johto["Route_29_Route_46_Gate_Links"]]
    )

    TwoWayCorridorNodes_Johto['Gate - Route 31 Violet Node'] = Node(
        [johto["Route_31_Violet_Gate_Links"].get(key) for key in johto["Route_31_Violet_Gate_Links"]]
    )

    TwoWayCorridorNodes_Johto['Gate - Route 32 Ruins Of Alph Node'] = Node(
        [johto["Route_32_Ruins_Of_Alph_Gate_Links"].get(key) for key in johto["Route_32_Ruins_Of_Alph_Gate_Links"]]
    )

    TwoWayCorridorNodes_Johto['Gate - Route 34 Ilex Forest Node'] = Node(
        [johto["Route_34_Ilex_Forest_Gate_Links"].get(key) for key in johto["Route_34_Ilex_Forest_Gate_Links"]]
    )

    TwoWayCorridorNodes_Johto['Gate - Ilex Forest Azalea Node'] = Node(
        [johto["Ilex_Forest_Azalea_Gate_Links"].get(key) for key in johto["Ilex_Forest_Azalea_Gate_Links"]]
    )


    TwoWayCorridorNodes_Johto['Gate - Route 35 Goldenrod  Node'] = Node(
        [johto["Route_35_Goldenrod_Gate_Links"].get(key) for key in johto["Route_35_Goldenrod_Gate_Links"]]
    )

    # Removed rt 35 national park gate so that bug contest only has a single entry point.
    # Route_35_National_Park_Gate_Node = Node(
    #     [johto[""].get(key) for key in johto["Route_35_National_Park_Gate_Links"]
    # )

    TwoWayCorridorNodes_Johto['Gate - Route 36 National Park Node'] = Node(
        [johto["Route_36_National_Park_Gate_Links"].get(key) for key in johto["Route_36_National_Park_Gate_Links"]]
    )

    TwoWayCorridorNodes_Johto['Gate - Route 36 Ruins Of Alph Node'] = Node(
        [johto["Route_36_Ruins_Of_Alph_Gate_Links"].get(key) for key in johto["Route_36_Ruins_Of_Alph_Gate_Links"]]
    )

    TwoWayCorridorNodes_Johto['Gate - Route 38 Ecruteak Node'] = Node(
        [johto["Route_38_Ecruteak_Gate_Links"].get(key) for key in johto["Route_38_Ecruteak_Gate_Links"]]
    )

    TwoWayCorridorNodes_Johto['Gate - Route 42 Ecruteak Node'] = Node(
        [johto["Route_42_Ecruteak_Gate_Links"].get(key) for key in johto["Route_42_Ecruteak_Gate_Links"]]
    )

    TwoWayCorridorNodes_Johto['Gate - Route 43 Mahogany Node'] = Node(
        [johto["Route_43_Mahogany_Gate_Links"].get(key) for key in johto["Route_43_Mahogany_Gate_Links"]]
    )

    TwoWayCorridorNodes_Johto['Gate - Route 43 (Rockets) Node'] = Node(
        [johto["Route_43_Gate_Links"].get(key) for key in johto["Route_43_Gate_Links"]]
    )

    TwoWayCorridorNodes_Johto['Route 35 Node'] = Node(
        [johto["Route_35_Links"].get(key) for key in johto["Route_35_Links"]]
    )
    #
    # Route_32_Node = Node(
    #     [johto["Route_32_Links"]ROUTE_32_TO_ROUTE_32_POKECENTER_LINK,
    #      johto["Route_32_Links"]ROUTE_32_TO_UNION_CAVE_LINK]
    # )



    TwoWayCorridorNodes_Johto['Goldenrod Underground (Director, Corridor) Node'] = Node(
        [johto["Goldenrod_Underground_Links"].get("GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_STAIR_LINK"),
         johto["Goldenrod_Underground_Links"].get("GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_LINK")]
    )

    TwoWayCorridorNodes_Johto['Mount Mortar 1F Inside (Corridor) Node'] = Node(
        [johto["Mount_Mortar_1F_Inside_Links"].get("MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_2F_INSIDE_2_LINK"),
         johto["Mount_Mortar_1F_Inside_Links"].get("MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_B1F_1_LINK")]
    )

    TwoWayCorridorNodes_Johto['Dragons Den 1F (Transition From Blackthorn) Node'] = Node(
        [johto["Dragons_Den_1F_Links"].get("DRAGONS_DEN_1F_TO_BLACKTHORN_CITY_8_LINK"),
         johto["Dragons_Den_1F_Links"].get("DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_4_LINK")]
    )

    TwoWayCorridorNodes_Johto['Dragons Den 1F (Transition From Dragons Den) Node'] = Node(
        [johto["Dragons_Den_1F_Links"].get("DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_2_LINK"),
         johto["Dragons_Den_1F_Links"].get("DRAGONS_DEN_1F_TO_DRAGONS_DEN_B1F_1_LINK")]
    )

    TwoWayCorridorNodes_Johto['Ruins Of Alph (Middle Portion) Node'] = Node(
        [johto["Ruins_Of_Alph_Outside_Links"].get("RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_1_LINK"),
         johto["Ruins_Of_Alph_Outside_Links"].get("RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_1_LINK")]
    )

    TwoWayCorridorNodes_Johto['Ruins Of AlphAerodactyl Chamber Node'] = Node(
        [johto["Ruins_Of_Alph_Aerodactyl_Chamber_Links"].get(key) for key in johto["Ruins_Of_Alph_Aerodactyl_Chamber_Links"]]
    )
    TwoWayCorridorNodes_Johto['Ruins Of Alph Ho Oh Chamber Node'] = Node(
        [johto["Ruins_Of_Alph_Ho_Oh_Chamber_Links"].get(key) for key in johto["Ruins_Of_Alph_Ho_Oh_Chamber_Links"]]
    )
    TwoWayCorridorNodes_Johto['Ruins Of Alph Kabuto Chamber Node'] = Node(
        [johto["Ruins_Of_Alph_Kabuto_Chamber_Links"].get(key) for key in johto["Ruins_Of_Alph_Kabuto_Chamber_Links"]]
    )
    TwoWayCorridorNodes_Johto['Ruins Of Alph Omanyte Chamber Node'] = Node(
        [johto["Ruins_Of_Alph_Omanyte_Chamber_Links"].get(key) for key in johto["Ruins_Of_Alph_Omanyte_Chamber_Links"]]
    )

    TwoWayCorridorNodes_Johto['Whirl Island B1F (Raised Path Corridor) Node'] = Node(
        [johto["Whirl_Island_B1F_Links"].get("WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_1_LINK"),
         johto["Whirl_Island_B1F_Links"].get("WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_2_LINK")]
    )

    TwoWayCorridorNodes_Johto['Whirl Island B1F (SE Corridor) Node'] = Node(
        [johto["Whirl_Island_B1F_Links"].get("WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SE_2_LINK"),
         johto["Whirl_Island_B1F_Links"].get("WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_2_LINK")]
    )

    TwoWayCorridorNodes_Johto['Whirl Island Cave (Corridor) Node'] = Node(
        [johto["Whirl_Island_Cave_Links"].get("WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_NW_4_LINK"),
         johto["Whirl_Island_Cave_Links"].get("WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_B1F_9_LINK")]
    )

    TwoWayCorridorNodes_Johto['Whirl Island NW (Upper Corridor) Node'] = Node(
        [johto["Whirl_Island_NW_Links"].get("WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_B1F_1_LINK"),
         johto["Whirl_Island_NW_Links"].get("WHIRL_ISLAND_N_W_TO_ROUTE_41_1_LINK")]
    )

    TwoWayCorridorNodes_Johto['Whirl Island NW (Lower Corridor) Node'] = Node(
        [johto["Whirl_Island_NW_Links"].get("WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_SW_4_LINK"),
         johto["Whirl_Island_NW_Links"].get("WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_CAVE_2_LINK")]
    )

    TwoWayCorridorNodes_Johto['Whirl Island SE (Corridor) Node'] = Node(
        [johto["Whirl_Island_SE_Links"].get("WHIRL_ISLAND_S_E_TO_WHIRL_ISLAND_B1F_6_LINK"),
         johto["Whirl_Island_SE_Links"].get("WHIRL_ISLAND_S_E_TO_ROUTE_41_4_LINK")]
    )

    TwoWayCorridorNodes_Johto['Whirl Island SW (Corridor) Node'] = Node(
        [johto["Whirl_Island_SW_Links"].get("WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_4_LINK"),
         johto["Whirl_Island_SW_Links"].get("WHIRL_ISLAND_S_W_TO_ROUTE_41_3_LINK")]
    )


    # Dark_Cave_Violet_Entrance_From_Route_31_Node = Node(
    #     [johto["Dark_Cave_Violet_Entrance_Links"]DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_31_LINK,
    #      johto["Dark_Cave_Violet_Entrance_Links"]DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_46_LINK]
    # )
    TwoWayCorridorNodes_Johto['Tin Tower 2F Node'] = Node(
        [johto["Tin_Tower_2F_Links"].get("TIN_TOWER_2F_TO_TIN_TOWER_3F_1_LINK"),
         johto["Tin_Tower_2F_Links"].get("TIN_TOWER_2F_TO_TIN_TOWER_1F_3_LINK")]
    )

    TwoWayCorridorNodes_Johto['Tin Tower 3F Node'] = Node(
       [johto["Tin_Tower_3F_Links"].get("TIN_TOWER_3F_TO_TIN_TOWER_2F_1_LINK"),
         johto["Tin_Tower_3F_Links"].get("TIN_TOWER_3F_TO_TIN_TOWER_4F_2_LINK")]
    )

    TwoWayCorridorNodes_Johto['Tin Tower 6F Node'] = Node(
        [johto["Tin_Tower_6F_Links"].get("TIN_TOWER_6F_TO_TIN_TOWER_7F_1_LINK"),
         johto["Tin_Tower_6F_Links"].get("TIN_TOWER_6F_TO_TIN_TOWER_5F_1_LINK")]
    )

    TwoWayCorridorNodes_Johto['Tin Tower 7F (Corridor) Node'] = Node(
        [johto["Tin_Tower_7F_Links"].get("TIN_TOWER_7F_TO_TIN_TOWER_7F_4_LINK"),
         johto["Tin_Tower_7F_Links"].get("TIN_TOWER_7F_TO_TIN_TOWER_9F_5_LINK")]
    )

    TwoWayCorridorNodes_Johto['Tin Tower 8F (NE Corridor) Node'] = Node(
        [johto["Tin_Tower_8F_Links"].get("TIN_TOWER_8F_TO_TIN_TOWER_9F_2_LINK"),
         johto["Tin_Tower_8F_Links"].get("TIN_TOWER_8F_TO_TIN_TOWER_9F_3_LINK")]
    )

    TwoWayCorridorNodes_Johto['Tin Tower 8F (West Corridor) Node'] = Node(
        [johto["Tin_Tower_8F_Links"].get("TIN_TOWER_8F_TO_TIN_TOWER_7F_2_LINK"),
         johto["Tin_Tower_8F_Links"].get("TIN_TOWER_8F_TO_TIN_TOWER_9F_1_LINK")]
    )

    TwoWayCorridorNodes_Johto['Tin Tower 9F (North Corridor) Node'] = Node(
        [johto["Tin_Tower_9F_Links"].get("TIN_TOWER_9F_TO_TIN_TOWER_8F_2_LINK"),
         johto["Tin_Tower_9F_Links"].get("TIN_TOWER_9F_TO_TIN_TOWER_8F_3_LINK")]
    )

    TwoWayCorridorNodes_Johto['Tin Tower 9F (Central Corridor) Node'] = Node(
        [johto["Tin_Tower_9F_Links"].get("TIN_TOWER_9F_TO_TIN_TOWER_8F_4_LINK"),
         johto["Tin_Tower_9F_Links"].get("TIN_TOWER_9F_TO_TIN_TOWER_ROOF_1_LINK")]
    )

    TwoWayCorridorNodes_Johto['Battle Tower Outside Node'] = Node(
        [johto["Battle_Tower_Outside_Links"].get("BATTLE_TOWER_OUTSIDE_TO_BATTLE_TOWER_1F_1_LINK"),
         johto["Battle_Tower_Outside_Links"].get("BATTLE_TOWER_OUTSIDE_TO_ROUTE_40_BATTLE_TOWER_GATE_3_LINK")]
    )

    TwoWayCorridorNodes_Johto['Gate - Route 40 Battle Tower Node'] = Node(
        [johto["Route_40_Battle_Tower_Gate_Links"].get("ROUTE_40_BATTLE_TOWER_GATE_TO_ROUTE_40_1_LINK"),
         johto["Route_40_Battle_Tower_Gate_Links"].get("ROUTE_40_BATTLE_TOWER_GATE_TO_BATTLE_TOWER_OUTSIDE_1_LINK")]
    )

    return TwoWayCorridorNodes_Johto


def buildJohtoHubs():

    HubNodes_Johto = dict()

    HubNodes_Johto['Victory Road Cave (Upper Room, Hub) Node'] = Node(
        [johto["Victory_Road_Links"].get("VICTORY_ROAD_TO_VICTORY_ROAD_4_LINK"),
         johto["Victory_Road_Links"].get("VICTORY_ROAD_TO_ROUTE_23_3_LINK"),
         johto["Victory_Road_Links"].get("VICTORY_ROAD_TO_VICTORY_ROAD_9_LINK")]
    )

    HubNodes_Johto['Tin Tower 4F Node'] = Node(
        [johto["Tin_Tower_4F_Links"].get(key) for key in johto["Tin_Tower_4F_Links"]]
    )

    HubNodes_Johto['Tin Tower 7F (Hub) Node'] = Node(
        [johto["Tin_Tower_7F_Links"].get("TIN_TOWER_7F_TO_TIN_TOWER_6F_1_LINK"),
         johto["Tin_Tower_7F_Links"].get("TIN_TOWER_7F_TO_TIN_TOWER_8F_1_LINK"),
         johto["Tin_Tower_7F_Links"].get("TIN_TOWER_7F_TO_TIN_TOWER_7F_3_LINK")]
    )

    HubNodes_Johto['Tin Tower 9F (Hub) Node'] = Node(
        [johto["Tin_Tower_9F_Links"].get("TIN_TOWER_9F_TO_TIN_TOWER_7F_5_LINK"),
         johto["Tin_Tower_9F_Links"].get("TIN_TOWER_9F_TO_TIN_TOWER_8F_5_LINK"),
         johto["Tin_Tower_9F_Links"].get("TIN_TOWER_9F_TO_TIN_TOWER_8F_6_LINK")]
    )

    HubNodes_Johto['Whirl Island B1F (Hub) Node'] = Node(
        [johto["Whirl_Island_B1F_Links"].get("WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_2_LINK"),
         johto["Whirl_Island_B1F_Links"].get("WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NW_2_LINK"),
         johto["Whirl_Island_B1F_Links"].get("WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_3_LINK")]
    )

    HubNodes_Johto['Goldenrod Underground (Hub) Node'] = Node(
        [johto["Goldenrod_Underground_Links"].get("GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_KEY_DOOR_LINK"),
         johto["Goldenrod_Underground_Links"].get("GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_NORTH_LINK"),
         johto["Goldenrod_Underground_Links"].get("GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH_LINK")]
    )

    HubNodes_Johto['Mount Mortar 1F Inside (Hub) Node'] = Node(
        [johto["Mount_Mortar_1F_Inside_Links"].get("MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_5_LINK"),
         johto["Mount_Mortar_1F_Inside_Links"].get("MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_6_LINK"),
         johto["Mount_Mortar_1F_Inside_Links"].get("MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_8_LINK"),
         johto["Mount_Mortar_1F_Inside_Links"].get("MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_9_LINK")]
    )


    HubNodes_Johto['Lighthouse 2F Node'] = Node(
        [johto["Olivine_Lighthouse_2F_Links"].get(key) for key in johto["Olivine_Lighthouse_2F_Links"]]
    )

    HubNodes_Johto['Lighthouse 3F Node'] = Node(
        [johto["Olivine_Lighthouse_3F_Links"].get(key) for key in johto["Olivine_Lighthouse_3F_Links"] if key != "OLIVINE_LIGHTHOUSE_3F_TO_4F_MIDDLE_STAIR_LINK"]
    )

    HubNodes_Johto['Lighthouse 4F Node'] = Node(
        [johto["Olivine_Lighthouse_4F_Links"].get(key) for key in johto["Olivine_Lighthouse_4F_Links"]]
    )

    HubNodes_Johto['Lake Of Rage (Hub) Node'] = Node(
        [johto["Route_43_Links"].get(key) for key in johto["Route_43_Links"]] +
        [johto["Lake_Of_Rage_Links"].get("LAKE_OF_RAGE_TO_LAKE_OF_RAGE_MAGIKARP_HOUSE_LINK")]

    )

    HubNodes_Johto['Ruins Of Alph Outside (Upper Portion) Node'] = Node(
        [johto["Ruins_Of_Alph_Outside_Links"].get("RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_32_RUINS_OF_ALPH_GATE_1_LINK"),
         johto["Ruins_Of_Alph_Outside_Links"].get("RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_36_RUINS_OF_ALPH_GATE_3_LINK"),
         johto["Ruins_Of_Alph_Outside_Links"].get("RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_INNER_CHAMBER_1_LINK"),
         johto["Ruins_Of_Alph_Outside_Links"].get("RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_KABUTO_CHAMBER_1_LINK"),
         johto["Ruins_Of_Alph_Outside_Links"].get("RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_RESEARCH_CENTER_1_LINK")]
    )

    HubNodes_Johto['Union Cave 1F (Hub) Node'] = Node(
        [johto["Union_Cave_1F_Links"].get(key) for key in johto["Union_Cave_1F_Links"]
         if key != "UNION_CAVE_1F_TO_UNION_CAVE_B1FB_LINK"]
    )
    HubNodes_Johto['Indigo Plateau Pokecenter 1F Node'] = Node(
        [johto["Indigo_Plateau_Pokecenter_1F_Links"].get("INDIGO_PLATEAU_POKECENTER_1F_TO_ROUTE_23_1_LINK"),
         johto["Indigo_Plateau_Pokecenter_1F_Links"].get("INDIGO_PLATEAU_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"),
         johto["Indigo_Plateau_Pokecenter_1F_Links"].get("INDIGO_PLATEAU_POKECENTER_1F_TO_WILLS_ROOM_1_LINK")]
    )

    HubNodes_Johto['Ruins Of Alph Lower (Modified, Hub) Node'] = Node(
        [johto["Ruins_Of_Alph_Outside_Links"].get("RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_2_LINK"),
         johto["Ruins_Of_Alph_Outside_Links"].get("RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_AERODACTYL_CHAMBER_1_LINK"),
         johto["Ruins_Of_Alph_Outside_Links"].get("RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_OMANYTE_CHAMBER_1_LINK")]
    )

    HubNodes_Johto['Ice Path B1F (Holes, Hub) Node'] = Node(
        [johto["Ice_Path_B1F_Links"].get(key) for key in johto["Ice_Path_B1F_Links"] if key not in
         ["ICE_PATH_B1F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_1_LINK","ICE_PATH_B1F_TO_ICE_PATH_1F_4_LINK"]
         ]
    )

    HubNodes_Johto['Goldenrod Dept Store Hub Node'] = Node(
        [johto["Goldenrod_Dept_Store_B1F_Links"].get("GOLDENROD_DEPT_STORE_B1F_TO_UNDERGROUND_WAREHOUSE_LINK")] +
        [johto["Goldenrod_Dept_Store_1F_Links"].get(key) for key in johto["Goldenrod_Dept_Store_1F_Links"]] +
        [johto["Goldenrod_Dept_Store_2F_Links"].get(key) for key in johto["Goldenrod_Dept_Store_2F_Links"]] +
        [johto["Goldenrod_Dept_Store_3F_Links"].get(key) for key in johto["Goldenrod_Dept_Store_3F_Links"]] +
        [johto["Goldenrod_Dept_Store_4F_Links"].get(key) for key in johto["Goldenrod_Dept_Store_4F_Links"]] +
        [johto["Goldenrod_Dept_Store_5F_Links"].get(key) for key in johto["Goldenrod_Dept_Store_5F_Links"]] +
        [johto["Goldenrod_Dept_Store_6F_Links"].get(key) for key in johto["Goldenrod_Dept_Store_6F_Links"]]
    )

    HubNodes_Johto['Route 26 Hub'] = Node(
        [johto["Route_26_Links"].get(key) for key in johto["Route_26_Links"]]
    )

    return HubNodes_Johto



# print("Printing Major Node Connection Numbers")
# for node in MajorNodes_Johto:
#     print(node.get("value.TOTAL_LINK"))
#
# print("Printing Corridor Connection Numbers")
# for node in TwoWayCorridorNodes_Johto:
#     print(node.get("value.TOTAL_LINK"))
#
# print("Printing Hub Node Connection Numbers")
# for node in HubNodes:
#     print(node.get("value.TOTAL_LINK"))
#
# print("Printing Deadend Node Connection Numbers")
# for node in DeadEndNodes:
#     print(node.get("value.TOTAL_LINK"))