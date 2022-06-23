import itertools
from enum import Enum

from class_definitions import Node
import links_and_nodes.johto_all_warp_points as johto
#import links_and_nodes.kanto_all_Link as kanto


class MajorNodes_Johto(Enum):

    New_Bark_Town_Node = Node(list(itertools.chain(
        johto.Cherrygrove_City_Links,
        johto.Route_29_Links,
        johto.Route_30_Links)))

    Violet_City_Node = Node(
            [link for link in johto.Violet_City_Links]
        +   [johto.Route_36_Links.ROUTE_36_TO_ROUTE_36_RUINS_OF_ALPH_GATE_LINK]
        +   [johto.Route_32_Links.ROUTE_32_TO_ROUTE_32_RUINS_OF_ALPH_GATE_LINK])

    Azalea_Town_Node = Node([link for link in johto.Azalea_Town_Links] +
            [johto.Route_33_Links.ROUTE_33_TO_UNION_CAVE_1F_LINK])

    Goldenrod_City_Node = Node(list(itertools.chain(
        johto.Goldenrod_City_Links,
        johto.Route_34_Links
    )))

    Ecruteak_City_Node = Node(
        [link for link in johto.Ecruteak_City_Links if link not in
            [johto.Ecruteak_City_Links.ECRUTEAK_CITY_TO_TIN_TOWER_1F_LINK,
             johto.Ecruteak_City_Links.ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_LINK]
         ]
    )

    Olivine_City_Node = Node(
        [link for link in johto.Route_38_Links] +
        [link for link in johto.Route_39_Links] +
        [link for link in johto.Olivine_City_Links if link is not johto.Olivine_City_Links.OLIVINE_CITY_TO_OLIVINE_PORT_PASSAGE_LINK] +
        [johto.Route_40_Links.ROUTE_40_TO_ROUTE_40_BATTLE_TOWER_GATE_1_LINK]
    )

    Cianwood_City_Node = Node(
        [link for link in johto.Cianwood_City_Links]
    )

    Mahogany_Town_Node = Node(
        [link for link in johto.Mahogany_Town_Links] +
        [johto.Route_42_Links.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_RIGHT_LINK]
    )

    Blackthorn_City_Node = Node(list(itertools.chain(
        johto.Blackthorn_City_Links,
        johto.Route_45_Links
    )))

class ImportantDeadEndNodes_Johto(Enum):
    Lighthouse_3F_Middle_Item_Node = Node(
        [johto.Olivine_Lighthouse_3F_Links.OLIVINE_LIGHTHOUSE_3F_TO_4F_MIDDLE_STAIR_LINK]
    )

    Tin_Tower_5F_Deadend_N_Node = Node(
        [johto.Tin_Tower_5F_Links.TIN_TOWER_5F_TO_TIN_TOWER_4F_1_LINK]
    )
    # Tintower 5F Deadend SE
    Tin_Tower_5F_Deadend_SE_Node = Node(
        [johto.Tin_Tower_5F_Links.TIN_TOWER_5F_TO_TIN_TOWER_4F_4_LINK]
    )
    # Tintower 5F Deadend S
    Tin_Tower_5F_Deadend_S_Node = Node(
        [johto.Tin_Tower_5F_Links.TIN_TOWER_5F_TO_TIN_TOWER_6F_2_LINK]
    )
    # Tintower 5F Deadend SW
    Tin_Tower_5F_Deadend_SW_Node = Node(
        [johto.Tin_Tower_5F_Links.TIN_TOWER_5F_TO_TIN_TOWER_4F_3_LINK]
    )

    # Tintower 8F Deadend Middle
    Tin_Tower_8F_Deadend_Middle_Node = Node(
        [johto.Tin_Tower_8F_Links.TIN_TOWER_8F_TO_TIN_TOWER_9F_7_LINK]
    )
    # Tintower 8F Deadend S
    Tin_Tower_8F_Deadend_S_Node = Node(
        [johto.Tin_Tower_8F_Links.TIN_TOWER_8F_TO_TIN_TOWER_9F_6_LINK]
    )

    Route_46_Berry_Tree_Node = Node(
        [johto.Route_46_Links.ROUTE_46_TO_DARK_CAVE_VIOLET_ENTRANCE_LINK]
    )

    Route_39_Barn_Node = Node(
        [link for link in johto.Route_39_Barn_Links]
    )

    Route_39_Farmhouse_Node = Node(
        [link for link in johto.Route_39_Farmhouse_Links]
    )

    Sprout_Tower_3F_Node = Node(
        [johto.Sprout_Tower_3F_Links.SPROUT_TOWER_3F_TO_SPROUT_TOWER_2F_LINK]
    )

    Route_44_Node = Node(
        [johto.Route_44_Links.ROUTE_44_TO_ICE_PATH_1F_LINK]
    )

    Lances_Room_Node = Node(
        [johto.Lances_Room_Links.LANCES_ROOM_TO_KARENS_ROOM_LINK]
    )

    Route_36_National_Park_Gate_Node = Node(
        [johto.Route_36_Links.ROUTE_36_TO_ROUTE_36_NATIONAL_PARK_GATE_LINK]
    )

    Olivine_Cafe_Node = Node(list(itertools.chain(
        johto.Olivine_Cafe_Links)))

    Olivine_Good_Rod_House_Node = Node(list(itertools.chain(
        johto.Olivine_Good_Rod_House_Links)))

    Olivine_Gym_Node = Node(list(itertools.chain(
        johto.Olivine_Gym_Links)))

    Olivine_Mart_Node = Node(list(itertools.chain(
        johto.Olivine_Mart_Links)))


    Olivine_Tims_House_Node = Node(list(itertools.chain(
        johto.Olivine_Tims_House_Links)))

    Cherrygrove_Mart_Node = Node(list(itertools.chain(
        johto.Cherrygrove_Mart_Links)))

    Mr_Pokemons_House_Node = Node(list(itertools.chain(
        johto.Mr_Pokemons_House_Links)))

    Route_30_Berry_House_Node = Node(list(itertools.chain(
        johto.Route_30_Berry_House_Links)))

    Violet_Mart_Node = Node(list(itertools.chain(
        johto.Violet_City_Mart_Links)))

    Violet_Gym_Node = Node(list(itertools.chain(
        johto.Violet_City_Gym_Links)))

    Violet_Kyles_House_Node = Node(list(itertools.chain(
        johto.Violet_City_Kyles_House_Links)))

    Azalea_Gym_Node = Node(
        [link for link in johto.Azalea_Gym_Links]
    )

    Azalea_Mart_Node = Node(
        [link for link in johto.Azalea_Mart_Links]
    )

    Charcoal_Kiln_Node = Node(
        [link for link in johto.Charcoal_Kiln_Links]
    )

    Kurts_House_Node = Node(
        [link for link in johto.Kurts_House_Links]
    )

    Blackthorn_Gym_Node = Node(
        [link for link in johto.Blackthorn_Gym_Links]
    )

    Blackthorn_Mart_House_Node = Node(
        [link for link in johto.Blackthorn_Mart_Links]
    )

    Move_Deleters_House_Node = Node(
        [link for link in johto.Move_Deleters_House_Links]
    )

    Cianwood_Gym_Node = Node(
        [link for link in johto.Cianwood_Gym_Links]
    )

    Cianwood_Pharmacy_Node = Node(
        [link for link in johto.Cianwood_Pharmacy_Links]
    )


    Manias_House_Node = Node(
        [link for link in johto.Manias_House_Links]
    )

    Poke_Seers_House_Node = Node(
        [link for link in johto.Poke_Seers_House_Links]
    )

    # TODO This is technically a corridor
    Burned_Tower_1F_Node = Node(
        [link for link in johto.Burned_Tower_1F_Links]
    )

    Ilex_Forest_From_Route_34_Gate_Node = Node(
        [johto.Ilex_Forest_Links.ILEX_FOREST_TO_ROUTE_34_ILEX_FOREST_GATE_LINK]
    )

    Ilex_Forest_From_Azalea_Gate_Node = Node(
        [johto.Ilex_Forest_Links.ILEX_FOREST_TO_ILEX_FOREST_AZALEA_GATE_LINK]
    )

    Slowpoke_Well_B1F_From_Overworld_Node = Node(
        [johto.Slowpoke_Well_B1F_Links.SLOWPOKE_WELL_B1F_TO_AZALEA_TOWN_LINK]
    )

    Slowpoke_Well_B2F_Node = Node(
        [johto.Slowpoke_Well_B2F_Links.SLOWPOKE_WELL_B2F_TO_SLOWPOKE_WELL_B1F_LINK]
    )

    # TODO Technically a corridor
    Tin_Tower_1F_Node = Node(
        [johto.Tin_Tower_1F_Links.TIN_TOWER_1F_TO_ECRUTEAK_CITY_LINK]
    )

    Dance_Theatre_Node = Node(
        [link for link in johto.Dance_Theatre_Links]
    )

    Ecruteak_Gym_Node = Node(
        [link for link in johto.Ecruteak_Gym_Links]
    )

    Ecruteak_Item_Finder_House_Node = Node(
        [link for link in johto.Ecruteak_Item_Finder_House_Links]
    )

    Lake_Of_Rage_Hidden_Power_House_Interior_Node = Node(
        [link for link in johto.Lake_Of_Rage_Hidden_Power_House_Links]
    )

    Lake_Of_Rage_Magikarp_House_Node = Node(
        [link for link in johto.Lake_Of_Rage_Magikarp_House_Links]
    )

    Day_Care_Node = Node(
        [link for link in johto.Day_Care_Links]
    )

    Goldenrod_Bike_Shop_Node = Node(
        [link for link in johto.Goldenrod_Bike_Shop_Links]
    )

    Goldenrod_Dept_Store_Roof_Node = Node(
        [johto.Goldenrod_Dept_Store_Roof_Links.GOLDENROD_DEPT_STORE_ROOF_TO_GOLDENROD_DEPT_STORE_6F_3_LINK]
    )

    Goldenrod_Flower_Shop_Node = Node(
        [link for link in johto.Goldenrod_Flower_Shop_Links]
    )

    Goldenrod_Game_Corner_Node = Node(
        [link for link in johto.Goldenrod_Game_Corner_Links]
    )

    Goldenrod_Gym_Node = Node(
        [link for link in johto.Goldenrod_Gym_Links]
    )

    #TODO Technically a cooridor
    Route_42_Middle_Node = Node(
        [johto.Route_42_Links.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_MIDDLE_LINK]
    )

    Whirl_Island_Lugia_Chamber_Node = Node(
        [johto.Whirl_Island_Lugia_Chamber_Links.WHIRL_ISLAND_LUGIA_CHAMBER_TO_WHIRL_ISLAND_B2F_LINK]
    )

    Whirl_Island_B1F_Escape_Rope_Node = Node(
        [johto.Whirl_Island_B1F_Links.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_3_LINK]
    )

    Whirl_Island_B2F_Single_Item_Node = Node(
        [johto.Whirl_Island_B2F_Links.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_7_LINK]
    )

    Whirl_Island_B2F_Double_Item_Node = Node(
        [johto.Whirl_Island_B2F_Links.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_8_LINK]
    )

    Whirl_Island_NE_Middle_Node = Node(
        [johto.Whirl_Island_NE_Links.WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_3_LINK]
    )

    Whirl_Island_SW_Item_Node = Node(
        [johto.Whirl_Island_SW_Links.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_5_LINK]
    )

    Tin_Tower_Roof_Node = Node(
        [johto.Tin_Tower_Roof_Links.TIN_TOWER_ROOF_TO_TIN_TOWER_9F_LINK]
    )

    Goldenrod_Magnet_Train_Station_Node = Node(
        [link for link in johto.Goldenrod_Magnet_Train_Station_Links]
    )

    #TODO Technically Corridor
    Radio_Tower_1F_Node = Node(
        [link for link in johto.Radio_Tower_1F_Links]
    )

    # TODO Technically a coridor after trigger
    Mahogany_Mart_Node = Node(
        [link for link in johto.Mahogany_Mart_Links]
    )

    Mahogany_Gym_Node = Node(
        [link for link in johto.Mahogany_Gym_Links]
    )


    Ecruteak_Mart_Node = Node(
        [link for link in johto.Ecruteak_Mart_Links]
    )

    Dragon_Shrine_Node = Node(
        [johto.Dragon_Shrine_Links.DRAGON_SHRINE_TO_DRAGONS_DEN_B1F_2_LINK]
    )

    Mount_Mortar_1F_Outside_Left_Item_Node = Node(
        [johto.Mount_Mortar_1F_Outside_Links.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_3_LINK]
    )
    Mount_Mortar_1F_Outside_Right_Item_Node = Node(
        [johto.Mount_Mortar_1F_Outside_Links.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_4_LINK]
    )

    Mount_Mortar_B1F_Upper_Node = Node(
        [johto.Mount_Mortar_B1F_Links.MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_INSIDE_5_LINK]
    )

    Mount_Mortar_2F_Inside_Uppder_Node = Node(
        [johto.Mount_Mortar_2F_Inside_Links.MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_INSIDE_6_LINK]
    )
    Mount_Mortar_2F_Inside_Lower_Node = Node(
        [johto.Mount_Mortar_2F_Inside_Links.MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_4_LINK]
    )

    Dark_Cave_Blackthorn_Entrance_From_Route_45_Node = Node(
        [johto.Dark_Cave_Blackthorn_Entrance_Links.DARK_CAVE_BLACKTHORN_ENTRANCE_TO_ROUTE_45_LINK]
    )

    Dark_Cave_From_Route_31_Node = Node(
        [johto.Dark_Cave_Violet_Entrance_Links.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_31_LINK]
    )
    Dark_Cave_From_Route_46_Node = Node(
        [johto.Dark_Cave_Violet_Entrance_Links.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_46_LINK]
    )

    Dragons_Den_B1F_From_Above_Node = Node(
        [johto.Dragons_Den_B1F_Links.DRAGONS_DEN_B1F_TO_DRAGONS_DEN_1F_3_LINK]
    )

    Dragons_Den_B1F_From_Dragon_Shrine_Node = Node(
        [johto.Dragons_Den_B1F_Links.DRAGONS_DEN_B1F_TO_DRAGON_SHRINE_1_LINK]
    )

    Union_Cave_B1F_Item_Node = Node(
        [johto.Union_Cave_B1F_Links.UNION_CAVE_B1F_TO_UNION_CAVE_1F_1_LINK]
    )

    Union_Cave_B2F_Node = Node(
        [johto.Union_Cave_B2F_Links.UNION_CAVE_B2F_TO_UNION_CAVE_B1F_5_LINK]
    )
    # victory road gate bottom 
    Victory_Road_Gate_Bottom_Node = Node(
        [johto.Victory_Road_Gate_Links.VICTORY_ROAD_GATE_TO_ROUTE_26_1_LINK]
    )
    # tohjo fall interior left
    Tohjo_Falls_Left_Interior_Node = Node(
        [johto.Tohjo_Falls_Links.TOHJO_FALLS_TO_ROUTE_27_2_LINK]
    )

#sandstorm house interior
    Route_27_Sandstorm_House_Interior_Node = Node(
        [johto.Route_27_Sandstorm_House_Links.ROUTE_27_SANDSTORM_HOUSE_TO_ROUTE_27_1_LINK]
    )
#route 26 heal house interior
    Route_26_Heal_House_Interior_Node = Node(
        [johto.Route_26_Heal_House_Links.ROUTE_26_HEAL_HOUSE_TO_ROUTE_26_2_LINK]
    )
    
class UnreachableUselessDeadEndNodes_Johto(Enum):

    Ruins_Of_Alph_Research_Center_Node = Node(
        [link for link in johto.Ruins_Of_Alph_Research_Center_Links]
    )

    Goldenrod_PP_Speech_House_Node = Node(
        [link for link in johto.Goldenrod_PP_Speech_House_Links]
    )

    # route 26 day of week sibling house interior
    Route_26_Day_Of_Week_Sibling_House_Interior_Node = Node(
        [johto.Day_Of_Week_Siblings_House_Links.DAY_OF_WEEK_SIBLINGS_HOUSE_TO_ROUTE_26_3_LINK]
    )

    Earls_Pokemon_Academy_Node = Node(list(itertools.chain(
        johto.Earls_Pokemon_Academy_Links)))

    Olivine_Punishment_Speech_House_Node = Node(list(itertools.chain(
        johto.Olivine_Punishment_Speech_House_Links)))

    Cherrygrove_Gym_Speech_House_Node = Node(list(itertools.chain(
        johto.Cherrygrove_Gym_Speech_House_Links)))

    Cherrygrove_Evolution_Speech_House_Node = Node(list(itertools.chain(
        johto.Cherrygrove_Evolution_Speech_House_Links)))

    Guide_Gents_House_Node = Node(list(itertools.chain(
        johto.Guide_Gents_House_Links)))

    Violet_Nickname_Speech_House_Node = Node(list(itertools.chain(
        johto.Violet_Nickname_Speech_House_Links)))

    Blackthorn_Emys_House_Node = Node(
        [link for link in johto.Blackthorn_Emys_House_Links]
    )

    Blackthorn_Dragon_Speech_House_Node = Node(
        [link for link in johto.Blackthorn_Dragon_Speech_House_Links]
    )

    Cianwood_Lugia_Speech_House_Node = Node(
        [link for link in johto.Cianwood_Lugia_Speech_House_Links]
    )

    Goldenrod_Happiness_Rater_Node = Node(
        [link for link in johto.Goldenrod_Happiness_Rater_Links]
    )

    Ecruteak_Lugia_Speech_House_Node = Node(
        [link for link in johto.Ecruteak_Lugia_Speech_House_Links]
    )

    Goldenrod_Name_Rater_Node = Node(
        [link for link in johto.Goldenrod_Name_Rater_Links]
    )

class ReachableUselessDeadEndNodes_Johto(Enum):



    # route 27 tohjo fall entrance left
    Tohjo_Falls_Left_Node = Node(
        [johto.Route_27_Links.ROUTE_27_TO_TOHJO_FALLS_1_LINK]
    )
    
    # tohjo fall interior right
    Tohjo_Falls_Right_Interior_Node = Node(
        [johto.Tohjo_Falls_Links.TOHJO_FALLS_TO_ROUTE_27_3_LINK]
    )
    # route 41 whirl entrance nw
    Route_41_To_Whirl_Island_NW_Node = Node(
        [johto.Route_41_Links.ROUTE_41_TO_WHIRL_ISLAND_NW_LINK]
    )
    # route 41 whirl entrance ne
    Route_41_To_Whirl_Island_NE_Node = Node(
        [johto.Route_41_Links.ROUTE_41_TO_WHIRL_ISLAND_NE_LINK]
    )
    # route 41 whirl entrance sw
    Route_41_To_Whirl_Island_SW_Node = Node(
        [johto.Route_41_Links.ROUTE_41_TO_WHIRL_ISLAND_SW_LINK]
    )
    # route 41 whirl entrance se
    Route_41_To_Whirl_Island_SE_Node = Node(
        [johto.Route_41_Links.ROUTE_41_TO_WHIRL_ISLAND_SE_LINK]
    )
    Union_Cave_B1F_Useless_Alph_Node1 = Node(
        [johto.Union_Cave_B1F_Links.UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_8_LINK]
    )

    Union_Cave_B1F_Useless_Alph_Node2 = Node(
        [johto.Union_Cave_B1F_Links.UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_7_LINK]
    )

    Whirl_Island_B1F_Useless_Node = Node(
        [johto.Whirl_Island_B1F_Links.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_CAVE_1_LINK]
    )

    Union_Cave_B1F_Useless_Trainer_Node1 = Node(
        [johto.Union_Cave_B1F_Links.UNION_CAVE_B1F_TO_UNION_CAVE_1F_2_LINK]
    )

    Union_Cave_B1F_Useless_Trainer_Node2 = Node(
        [johto.Union_Cave_B1F_Links.UNION_CAVE_B1F_TO_UNION_CAVE_B2F_1_LINK]
    )

    Slowpoke_Well_B1F_To_B2F_Useless_Node = Node(
        [johto.Slowpoke_Well_B1F_Links.SLOWPOKE_WELL_B1F_TO_SLOWPOKE_WELL_B2F_LINK]
    )

    Dark_Cave_Violet_Entrance_From_Blackthorn_Side_Useless_Node = Node(
        [johto.Dark_Cave_Violet_Entrance_Links.DARK_CAVE_VIOLET_ENTRANCE_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_LINK]
    )

    Dark_Cave_Blackthorn_Entrance_From_Violet_Side_Useless_Node = Node(
        [johto.Dark_Cave_Blackthorn_Entrance_Links.DARK_CAVE_BLACKTHORN_ENTRANCE_TO_DARK_CAVE_VIOLET_ENTRANCE_LINK]
    )


    Route_46_Route_29_Gate_Node = Node(
        [johto.Route_46_Links.ROUTE_46_TO_ROUTE_29_ROUTE_46_GATE_LINK]
    )

    Mount_Mortar_B1F_Lower_Node = Node(
        [johto.Mount_Mortar_B1F_Links.MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_OUTSIDE_7_LINK]
    )

    Mount_Mortar_1F_Outside_Center_Upper_Node = Node(
        [johto.Mount_Mortar_1F_Outside_Links.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_2F_INSIDE_1_LINK]
    )

    Lake_Of_Rage_Hidden_Power_House_Exterior_Node = Node(
        [johto.Lake_Of_Rage_Links.LAKE_OF_RAGE_TO_LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_LINK]
    )

    # Ecruteak_Tin_Tower_Entrance_To_Wise_Trio_Room_Node = Node(
    #     [johto.Ecruteak_Tin_Tower_Entrance_Links.ECRUTEAK_TIN_TOWER_ENTRANCE_TO_WISE_TRIOS_ROOM_LINK]
    # )

    Bills_Familys_House_Node = Node(
        [link for link in johto.Bills_Familys_House_Links]
    )


    Whirl_Island_B2F_Useless_Ladder_Node = Node(
        [johto.Whirl_Island_B2F_Links.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_SW_5_LINK]
    )

    Whirl_Island_B2F_Useless_Cave_Node = Node(
        [johto.Whirl_Island_B2F_Links.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_LUGIA_CHAMBER_1_LINK]
    )

    Whirl_Island_NE_Left_Node = Node(
        [johto.Whirl_Island_NE_Links.WHIRL_ISLAND_N_E_TO_ROUTE_41_2_LINK]
    )

    Whirl_Island_NE_Right_Node = Node(
        [johto.Whirl_Island_NE_Links.WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_2_LINK]
    )

    Whirl_Island_SW_Lower_Left_Useless_Node = Node(
        [johto.Whirl_Island_SW_Links.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_NW_3_LINK]
    )

    Whirl_Island_SW_Lower_Right_Useless_Node = Node(
        [johto.Whirl_Island_SW_Links.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B2F_4_LINK]
    )

    Union_Cave_1F_Useless_Node = Node(
        [johto.Union_Cave_1F_Links.UNION_CAVE_1F_TO_UNION_CAVE_B1FB_LINK]
    )


class TwoWayCorridorNodes_Johto(Enum):

    Victory_Road_Cave_Node = Node(
        [link for link in johto.Victory_Road_Links]
    )

    # route 27 tohjo fall entrance right to sandstorm house
    Tohjo_Falls_Right_To_Route_27_Sandstorm_House_Node = Node(
         [johto.Route_27_Links.ROUTE_27_TO_TOHJO_FALLS_2_LINK,
         johto.Route_27_Links.ROUTE_27_TO_ROUTE_27_SANDSTORM_HOUSE_1_LINK]
    )



    Mount_Mortar_1F_Outside_Lower_Left_Node = Node(
        [johto.Mount_Mortar_1F_Outside_Links.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_3_LINK,
         johto.Mount_Mortar_1F_Outside_Links.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_1_LINK]
    )
    Mount_Mortar_1F_Outside_Lower_Middle_Node = Node(
        [johto.Mount_Mortar_1F_Outside_Links.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_4_LINK,
         johto.Mount_Mortar_1F_Outside_Links.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_B1F_2_LINK]
    )
    Mount_Mortar_1F_Outside_Lower_Right_Node = Node(
        [johto.Mount_Mortar_1F_Outside_Links.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_5_LINK,
         johto.Mount_Mortar_1F_Outside_Links.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_2_LINK]
    )

    Ice_Path_B2F_Ice_Rock_Room_Node = Node(
        [johto.Ice_Path_B2F_Mahogany_Side_Links.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_2_LINK,
         johto.Ice_Path_B2F_Mahogany_Side_Links.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B3F_1_LINK]
    )

    Ice_Path_B3F_Node = Node(
        [johto.Ice_Path_B3F_Links.ICE_PATH_B3F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_2_LINK,
         johto.Ice_Path_B3F_Links.ICE_PATH_B3F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_2_LINK]
    )

    Ice_Path_B2F_Blackthorn_Side_Node = Node(
        [johto.Ice_Path_B2F_Blackthorn_Side_Links.ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B1F_8_LINK,
         johto.Ice_Path_B2F_Blackthorn_Side_Links.ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B3F_2_LINK]
    )

    Ice_Path_B1F_Blackthorn_Side_Node = Node(
        [johto.Ice_Path_B1F_Links.ICE_PATH_B1F_TO_ICE_PATH_1F_4_LINK,
         johto.Ice_Path_B1F_Links.ICE_PATH_B1F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_1_LINK]
    )

    Ice_Path_1F_Route_44_Side_Node = Node(
        [johto.Ice_Path_1F_Links.ICE_PATH_1F_TO_ROUTE_44_1_LINK,
         johto.Ice_Path_1F_Links.ICE_PATH_1F_TO_ICE_PATH_B1F_1_LINK]
    )

    Ice_Path_1F_Blackthorn_Side_Node = Node(
        [johto.Ice_Path_1F_Links.ICE_PATH_1F_TO_ICE_PATH_B1F_7_LINK,
         johto.Ice_Path_1F_Links.ICE_PATH_1F_TO_BLACKTHORN_CITY_7_LINK]
    )

    Route_42_Left_Node = Node(
        [johto.Route_42_Links.ROUTE_42_TO_ROUTE_42_ECRUTEAK_GATE_LINK,
         johto.Route_42_Links.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_LEFT_LINK]
    )

    Sprout_Tower_1F_Inner_Node = Node(
        [johto.Sprout_Tower_1F_Links.SPROUT_TOWER_1F_TO_VIOLET_CITY_LINK,
         johto.Sprout_Tower_1F_Links.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FA_LINK]
    )

    Sprout_Tower_1F_Outer_Node = Node(
        [johto.Sprout_Tower_1F_Links.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FB_LINK,
         johto.Sprout_Tower_1F_Links.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FC_LINK]
    )

    Sprout_Tower_2F_NE_Node = Node(
        [johto.Sprout_Tower_2F_Links.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_5_LINK,
         johto.Sprout_Tower_2F_Links.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_3_LINK]
    )
    Sprout_Tower_2F_SW_Node = Node(
        [johto.Sprout_Tower_2F_Links.SPROUT_TOWER_2F_TO_SPROUT_TOWER_3F_1_LINK,
         johto.Sprout_Tower_2F_Links.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_4_LINK]
    )

    Goldenrod_Underground_Warehouse_Node = Node(
        [johto.Goldenrod_Underground_Switch_Room_Entrance_Links.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_LINK,
         johto.Goldenrod_Underground_Warehouse_Links.GOLDENROD_UNDERGROUND_WAREHOUSE_TO_GOLDENROD_DEPT_STORE_B1F_LINK]
    )

    Goldenrod_Switch_Room_Entrance_North_Node = Node(
        [johto.Goldenrod_Underground_Switch_Room_Entrance_Links.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_NORTH_LINK,
         johto.Goldenrod_Underground_Switch_Room_Entrance_Links.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_NORTH_LINK]
    )

    Goldenrod_Switch_Room_Entrance_South_Node = Node(
        [johto.Goldenrod_Underground_Switch_Room_Entrance_Links.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_SOUTH_LINK,
         johto.Goldenrod_Underground_Switch_Room_Entrance_Links.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_SOUTH_LINK]
    )

    Kogas_Room_Node = Node(
        [link for link in johto.Kogas_Room_Links]
    )

    Wills_Room_Node = Node(
        [link for link in johto.Wills_Room_Links]
    )

    Karens_Room_Node = Node(
        [link for link in johto.Karens_Room_Links]
    )

    Brunos_Room_Node = Node(
        [link for link in johto.Brunos_Room_Links]
    )

    Ecruteak_Pokecenter_Node = Node(
        [link for link in johto.Ecruteak_Pokecenter_Links]
    )

    Route_32_Pokecenter_Node = Node(
        [link for link in johto.Route_32_Pokecenter_Links]
    )

    Mahogany_Pokecenter_Node = Node(
        [link for link in johto.Mahogany_Pokecenter_Links]
    )

    Goldenrod_Pokecenter_Node = Node(
        [link for link in johto.Goldenrod_Pokecenter_Links]
    )

    Cianwood_Pokecenter_Node = Node(
        [link for link in johto.Cianwood_Pokecenter_Links]
    )

    Blackthorn_Pokecenter_Node = Node(
        [link for link in johto.Blackthorn_Pokecenter_Links]
    )

    Azalea_Pokecenter_Node = Node(
        [link for link in johto.Azalea_Pokecenter_Links]
    )

    Violet_Pokecenter_Node = Node(
        [link for link in johto.Violet_City_Pokecenter_Links]
    )

    Cherrygrove_Pokecenter_Node = Node(
        [link for link in johto.Cherrygrove_Pokecenter_Links])

    Olivine_Pokecenter_Node = Node(
        [link for link in johto.Olivine_Pokecenter_Links])

    Route31_Node = Node([link for link in johto.Route_31_Links])

    Wise_Trio_To_Tin_Tower_Overworld_Node = Node(
        [link for link in johto.Ecruteak_City_Links if link in
         [johto.Ecruteak_City_Links.ECRUTEAK_CITY_TO_TIN_TOWER_1F_LINK,
          johto.Ecruteak_City_Links.ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_LINK]
         ]
    )

    Lighthouse_1F_Node = Node(
        [link for link in johto.Olivine_Lighthouse_1F_Links]
    )

    Lighthouse_5F_Outer_Node = Node(
        [johto.Olivine_Lighthouse_5F_Links.OLIVINE_LIGHTHOUSE_5F_TO_4F_OUTER_STAIR_LINK,
         johto.Olivine_Lighthouse_5F_Links.OLIVINE_LIGHTHOUSE_5F_TO_4F_PITFALL_LINK]
    )

    Lighthouse_5F_Inner_Node = Node(
        [johto.Olivine_Lighthouse_5F_Links.OLIVINE_LIGHTHOUSE_5F_TO_4F_INNER_STAIR_LINK,
         johto.Olivine_Lighthouse_5F_Links.OLIVINE_LIGHTHOUSE_5F_TO_6F_STAIR_LINK]
    )

    Lighthouse_6F_Node = Node(
        [link for link in johto.Olivine_Lighthouse_6F_Links]
    )

    National_Park_Node = Node(
        [link for link in johto.National_Park_Links]
    )

    Route_29_Route_46_Gate_Node = Node(
        [link for link in johto.Route_29_Route_46_Gate_Links]
    )

    Route_31_Violet_Gate_Node = Node(
        [link for link in johto.Route_31_Violet_Gate_Links]
    )

    Route_32_Ruins_Of_Alph_Gate_Node = Node(
        [link for link in johto.Route_32_Ruins_Of_Alph_Gate_Links]
    )

    Route_34_Ilex_Forest_Gate_Node = Node(
        [link for link in johto.Route_34_Ilex_Forest_Gate_Links]
    )

    Ilex_Forest_Azalea_Gate_Node = Node(
        [link for link in johto.Ilex_Forest_Azalea_Gate_Links]
    )


    Route_35_Goldenrod_Gate_Node = Node(
        [link for link in johto.Route_35_Goldenrod_Gate_Links]
    )

    # Removed rt 35 national park gate so that bug contest only has a single entry point.
    # Route_35_National_Park_Gate_Node = Node(
    #     [link for link in johto.Route_35_National_Park_Gate_Links]
    # )

    Route_36_National_Park_Gate_Node = Node(
        [link for link in johto.Route_36_National_Park_Gate_Links]
    )

    Route_36_Ruins_Of_Alph_Gate_Node = Node(
        [link for link in johto.Route_36_Ruins_Of_Alph_Gate_Links]
    )

    Route_38_Ecruteak_Gate_Node = Node(
        [link for link in johto.Route_38_Ecruteak_Gate_Links]
    )

    Route_42_Ecruteak_Gate_Node = Node(
        [link for link in johto.Route_42_Ecruteak_Gate_Links]
    )

    Route_43_Mahogany_Gate_Node = Node(
        [link for link in johto.Route_43_Mahogany_Gate_Links]
    )

    Route_43_Gate_Node = Node(
        [link for link in johto.Route_43_Gate_Links]
    )

    Route_35_Node = Node(
        [link for link in johto.Route_35_Links]
    )

    Route_32_Node = Node(
        [johto.Route_32_Links.ROUTE_32_TO_ROUTE_32_POKECENTER_LINK,
         johto.Route_32_Links.ROUTE_32_TO_UNION_CAVE_LINK]
    )

    Goldenrod_Underground_Corridor_Node = Node(
        [johto.Goldenrod_Underground_Links.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_STAIR_LINK,
         johto.Goldenrod_Underground_Links.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_LINK]
    )

    Mount_Mortar_1F_Inside_Corridor_Node = Node(
        [johto.Mount_Mortar_1F_Inside_Links.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_2F_INSIDE_2_LINK,
         johto.Mount_Mortar_1F_Inside_Links.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_B1F_1_LINK]
    )

    Dragons_Den_1F_From_Blackthorn_Node = Node(
        [johto.Dragons_Den_1F_Links.DRAGONS_DEN_1F_TO_BLACKTHORN_CITY_8_LINK,
         johto.Dragons_Den_1F_Links.DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_4_LINK]
    )

    Dragons_Den_1F_From_Dragons_Den_Node = Node(
        [johto.Dragons_Den_1F_Links.DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_2_LINK,
         johto.Dragons_Den_1F_Links.DRAGONS_DEN_1F_TO_DRAGONS_DEN_B1F_1_LINK]
    )

    Ruins_Of_Alph_Middle_Node = Node(
        [johto.Ruins_Of_Alph_Outside_Links.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_1_LINK,
         johto.Ruins_Of_Alph_Outside_Links.RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_1_LINK]
    )

    Aerodactyl_Chamber_Node = Node(
        [link for link in johto.Ruins_Of_Alph_Aerodactyl_Chamber_Links]
    )
    Ho_Oh_Chamber_Node = Node(
        [link for link in johto.Ruins_Of_Alph_Ho_Oh_Chamber_Links]
    )
    Kabuto_Chamber_Node = Node(
        [link for link in johto.Ruins_Of_Alph_Kabuto_Chamber_Links]
    )
    Omanyte_Chamber_Node = Node(
        [link for link in johto.Ruins_Of_Alph_Omanyte_Chamber_Links]
    )

    Whirl_Island_B1F_Raised_Path_Corridor_Node = Node(
        [johto.Whirl_Island_B1F_Links.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_1_LINK,
         johto.Whirl_Island_B1F_Links.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_2_LINK]
    )

    Whirl_Island_B1F_Lower_Right_Corridor_Node = Node(
        [johto.Whirl_Island_B1F_Links.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SE_2_LINK,
         johto.Whirl_Island_B1F_Links.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_2_LINK]
    )

    Whirl_Island_Cave_Corridor_Node = Node(
        [johto.Whirl_Island_Cave_Links.WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_NW_4_LINK,
         johto.Whirl_Island_Cave_Links.WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_B1F_9_LINK]
    )

    Whirl_Island_NW_Upper_Corridor_Node = Node(
        [johto.Whirl_Island_NW_Links.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_B1F_1_LINK,
         johto.Whirl_Island_NW_Links.WHIRL_ISLAND_N_W_TO_ROUTE_41_1_LINK]
    )

    Whirl_Island_NW_Lower_Corridor_Node = Node(
        [johto.Whirl_Island_NW_Links.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_SW_4_LINK,
         johto.Whirl_Island_NW_Links.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_CAVE_2_LINK]
    )

    Whirl_Island_SE_Corridor_Node = Node(
        [johto.Whirl_Island_SE_Links.WHIRL_ISLAND_S_E_TO_WHIRL_ISLAND_B1F_6_LINK,
         johto.Whirl_Island_SE_Links.WHIRL_ISLAND_S_E_TO_ROUTE_41_4_LINK]
    )

    Whirl_Island_SW_Corridor_Node = Node(
        [johto.Whirl_Island_SW_Links.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_4_LINK,
         johto.Whirl_Island_SW_Links.WHIRL_ISLAND_S_W_TO_ROUTE_41_3_LINK]
    )


    # Dark_Cave_Violet_Entrance_From_Route_31_Node = Node(
    #     [johto.Dark_Cave_Violet_Entrance_Links.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_31_LINK,
    #      johto.Dark_Cave_Violet_Entrance_Links.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_46_LINK]
    # )
    Tin_Tower_2F_Node = Node(
        [johto.Tin_Tower_2F_Links.TIN_TOWER_2F_TO_TIN_TOWER_3F_1_LINK,
         johto.Tin_Tower_2F_Links.TIN_TOWER_2F_TO_TIN_TOWER_1F_3_LINK]
    )

    Tin_Tower_3F_Node = Node(
        [johto.Tin_Tower_3F_Links.TIN_TOWER_3F_TO_TIN_TOWER_2F_1_LINK,
         johto.Tin_Tower_3F_Links.TIN_TOWER_3F_TO_TIN_TOWER_4F_2_LINK]
    )

    Tin_Tower_6F_Node = Node(
        [johto.Tin_Tower_6F_Links.TIN_TOWER_6F_TO_TIN_TOWER_7F_1_LINK,
         johto.Tin_Tower_6F_Links.TIN_TOWER_6F_TO_TIN_TOWER_5F_1_LINK]
    )

    Tin_Tower_7F_Corridor_Node = Node(
        [johto.Tin_Tower_7F_Links.TIN_TOWER_7F_TO_TIN_TOWER_7F_4_LINK,
         johto.Tin_Tower_7F_Links.TIN_TOWER_7F_TO_TIN_TOWER_9F_5_LINK]
    )

    Tin_Tower_8F_Corridor_NE_Node = Node(
        [johto.Tin_Tower_8F_Links.TIN_TOWER_8F_TO_TIN_TOWER_9F_2_LINK,
         johto.Tin_Tower_8F_Links.TIN_TOWER_8F_TO_TIN_TOWER_9F_3_LINK]
    )

    Tin_Tower_8F_Corridor_W_Node = Node(
        [johto.Tin_Tower_8F_Links.TIN_TOWER_8F_TO_TIN_TOWER_7F_2_LINK,
         johto.Tin_Tower_8F_Links.TIN_TOWER_8F_TO_TIN_TOWER_9F_1_LINK]
    )

    Tin_Tower_9F_Corridor_N_Node = Node(
        [johto.Tin_Tower_9F_Links.TIN_TOWER_9F_TO_TIN_TOWER_8F_2_LINK,
         johto.Tin_Tower_9F_Links.TIN_TOWER_9F_TO_TIN_TOWER_8F_3_LINK]
    )

    Tin_Tower_9F_Corridor_Middle_Node = Node(
        [johto.Tin_Tower_9F_Links.TIN_TOWER_9F_TO_TIN_TOWER_8F_4_LINK,
         johto.Tin_Tower_9F_Links.TIN_TOWER_9F_TO_TIN_TOWER_ROOF_1_LINK]
    )

    Battle_Tower_Outside_Corridor_Node = Node(
        [johto.Battle_Tower_Outside_Links.BATTLE_TOWER_OUTSIDE_TO_BATTLE_TOWER_1F_1_LINK,
         johto.Battle_Tower_Outside_Links.BATTLE_TOWER_OUTSIDE_TO_ROUTE_40_BATTLE_TOWER_GATE_3_LINK]
    )

    Route_40_Battle_Tower_Gate_Corridor_Node = Node(
        [johto.Route_40_Battle_Tower_Gate_Links.ROUTE_40_BATTLE_TOWER_GATE_TO_ROUTE_40_1_LINK,
         johto.Route_40_Battle_Tower_Gate_Links.ROUTE_40_BATTLE_TOWER_GATE_TO_BATTLE_TOWER_OUTSIDE_1_LINK]
    )

class HubNodes_Johto(Enum):

    Tin_Tower_4F_Node = Node(
        [link for link in johto.Tin_Tower_4F_Links]
    )

    Tin_Tower_7F_Hub_Node = Node(
        [johto.Tin_Tower_7F_Links.TIN_TOWER_7F_TO_TIN_TOWER_6F_1_LINK,
         johto.Tin_Tower_7F_Links.TIN_TOWER_7F_TO_TIN_TOWER_8F_1_LINK,
         johto.Tin_Tower_7F_Links.TIN_TOWER_7F_TO_TIN_TOWER_7F_3_LINK]
    )

    Tin_Tower_9F_Hub_Node = Node(
        [johto.Tin_Tower_9F_Links.TIN_TOWER_9F_TO_TIN_TOWER_7F_5_LINK,
         johto.Tin_Tower_9F_Links.TIN_TOWER_9F_TO_TIN_TOWER_8F_5_LINK,
         johto.Tin_Tower_9F_Links.TIN_TOWER_9F_TO_TIN_TOWER_8F_6_LINK]
    )

    Whirl_Island_B1F_Hub_Node = Node(
        [johto.Whirl_Island_B1F_Links.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_2_LINK,
         johto.Whirl_Island_B1F_Links.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NW_2_LINK,
         johto.Whirl_Island_B1F_Links.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_3_LINK]
    )

    Goldenrod_Underground_Hub_Node = Node(
        [johto.Goldenrod_Underground_Links.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_KEY_DOOR_LINK,
         johto.Goldenrod_Underground_Links.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_NORTH_LINK,
         johto.Goldenrod_Underground_Links.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH_LINK]
    )

    Mount_Mortar_1F_Inside_Hub_Node = Node(
        [johto.Mount_Mortar_1F_Inside_Links.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_5_LINK,
         johto.Mount_Mortar_1F_Inside_Links.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_6_LINK,
         johto.Mount_Mortar_1F_Inside_Links.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_8_LINK,
         johto.Mount_Mortar_1F_Inside_Links.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_9_LINK]
    )


    Lighthouse_2F_Node = Node(
        [link for link in johto.Olivine_Lighthouse_2F_Links]
    )

    Lighthouse_3F_Node = Node(
        [link for link in johto.Olivine_Lighthouse_3F_Links if link not in
         [johto.Olivine_Lighthouse_3F_Links.OLIVINE_LIGHTHOUSE_3F_TO_4F_MIDDLE_STAIR_LINK]]
    )

    Lighthouse_4F_Node = Node(
        [link for link in johto.Olivine_Lighthouse_4F_Links]
    )

    Lake_Of_Rage_Area_Node = Node(
        [link for link in johto.Route_43_Links] +
        [johto.Lake_Of_Rage_Links.LAKE_OF_RAGE_TO_LAKE_OF_RAGE_MAGIKARP_HOUSE_LINK]

    )

    Ruins_Of_Alph_Outside_Upper_Node = Node(
        [johto.Ruins_Of_Alph_Outside_Links.RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_32_RUINS_OF_ALPH_GATE_1_LINK,
         johto.Ruins_Of_Alph_Outside_Links.RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_36_RUINS_OF_ALPH_GATE_3_LINK,
         johto.Ruins_Of_Alph_Outside_Links.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_INNER_CHAMBER_1_LINK,
         johto.Ruins_Of_Alph_Outside_Links.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_KABUTO_CHAMBER_1_LINK,
         johto.Ruins_Of_Alph_Outside_Links.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_RESEARCH_CENTER_1_LINK]
    )

    Union_Cave_1F_Node = Node(
        [link for link in johto.Union_Cave_1F_Links
         if link is not johto.Union_Cave_1F_Links.UNION_CAVE_1F_TO_UNION_CAVE_B1FB_LINK]
    )
    Indigo_Plateau_Pokecenter_1F_Node = Node(
        [johto.Indigo_Plateau_Pokecenter_1F_Links.INDIGO_PLATEAU_POKECENTER_1F_TO_ROUTE_23_1_LINK,
         johto.Indigo_Plateau_Pokecenter_1F_Links.INDIGO_PLATEAU_POKECENTER_1F_TO_POKECENTER_2F_1_LINK,
         johto.Indigo_Plateau_Pokecenter_1F_Links.INDIGO_PLATEAU_POKECENTER_1F_TO_WILLS_ROOM_1_LINK]
    )

    Ruins_Of_Alph_Lower_Node = Node(
        [johto.Ruins_Of_Alph_Outside_Links.RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_2_LINK,
         johto.Ruins_Of_Alph_Outside_Links.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_AERODACTYL_CHAMBER_1_LINK,
         johto.Ruins_Of_Alph_Outside_Links.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_OMANYTE_CHAMBER_1_LINK]
    )

    Ice_Path_B1F_Hub_Node = Node(
        [link for link in johto.Ice_Path_B1F_Links if link not in
         [johto.Ice_Path_B1F_Links.ICE_PATH_B1F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_1_LINK,
          johto.Ice_Path_B1F_Links.ICE_PATH_B1F_TO_ICE_PATH_1F_4_LINK]
         ]
    )

    Goldenrod_Dept_Store_Hub_Node = Node(
        [johto.Goldenrod_Dept_Store_B1F_Links.GOLDENROD_DEPT_STORE_B1F_TO_UNDERGROUND_WAREHOUSE_LINK] +
        [link for link in johto.Goldenrod_Dept_Store_1F_Links] +
        [link for link in johto.Goldenrod_Dept_Store_2F_Links] +
        [link for link in johto.Goldenrod_Dept_Store_3F_Links] +
        [link for link in johto.Goldenrod_Dept_Store_4F_Links] +
        [link for link in johto.Goldenrod_Dept_Store_5F_Links] +
        [link for link in johto.Goldenrod_Dept_Store_6F_Links]
    )

    Route_26_Hub = Node(
        [link for link in johto.Route_26_Links]
    )



# print("Printing Major Node Connection Numbers")
# for node in MajorNodes_Johto:
#     print(node.value.TOTAL_LINKS)
#
# print("Printing Corridor Connection Numbers")
# for node in TwoWayCorridorNodes_Johto:
#     print(node.value.TOTAL_LINKS)
#
# print("Printing Hub Node Connection Numbers")
# for node in HubNodes:
#     print(node.value.TOTAL_LINKS)
#
# print("Printing Deadend Node Connection Numbers")
# for node in DeadEndNodes:
#     print(node.value.TOTAL_LINKS)