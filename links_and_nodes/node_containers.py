import itertools
from enum import Enum

from class_definitions import Node
import links_and_nodes.all_warp_points as md


class MajorNodes(Enum):

    New_Bark_Town_Node = Node(list(itertools.chain(
        md.Cherrygrove_City_Links,
        md.Route_29_Links,
        md.Route_30_Links)))

    Violet_City_Node = Node(
            [link for link in md.Violet_City_Links]
        +   [md.Route_36_Links.ROUTE_36_TO_ROUTE_36_RUINS_OF_ALPH_GATE_LINK]
        +   [md.Route_32_Links.ROUTE_32_TO_ROUTE_32_RUINS_OF_ALPH_GATE_LINK])

    Azalea_Town_Node = Node([link for link in md.Azalea_Town_Links if link not in
            [md.Azalea_Town_Links.AZALEA_TOWN_TO_SLOWPOKE_WELL_B1F_LINK]] +
            [md.Route_33_Links.ROUTE_33_TO_UNION_CAVE_1F_LINK])

    Goldenrod_City_Node = Node(list(itertools.chain(
        md.Goldenrod_City_Links,
        md.Route_34_Links
    )))

    Ecruteak_City_Node = Node(
        [link for link in md.Ecruteak_City_Links if link not in
            [md.Ecruteak_City_Links.ECRUTEAK_CITY_TO_TIN_TOWER_1F_LINK,
             md.Ecruteak_City_Links.ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_LINK]
         ]
    )

    Olivine_City_Node = Node(list(itertools.chain(
        md.Olivine_City_Links,
        md.Route_38_Links)))

    Cianwood_City_Node = Node(list(itertools.chain(
        md.Cianwood_City_Links
    )))

    Mahogany_Town_Node = Node(list(itertools.chain(
        md.Mahogany_Town_Links
    )))

    Blackthorn_City_Node = Node(list(itertools.chain(
        md.Blackthorn_City_Links
    )))


class ImportantDeadEndNodes(Enum):

    Sprout_Tower_3F_Node = Node(
        [md.Sprout_Tower_3F_Links.SPROUT_TOWER_3F_TO_SPROUT_TOWER_2F_LINK]
    )

    Lances_Room_Node = Node(
        [md.Lances_Room_Links.LANCES_ROOM_TO_KARENS_ROOM_LINK]
    )

    Route_36_National_Park_Gate_Node = Node(
        [md.Route_36_Links.ROUTE_36_TO_ROUTE_36_NATIONAL_PARK_GATE_LINK]
    )

    Olivine_Cafe_Node = Node(list(itertools.chain(
        md.Olivine_Cafe_Links)))

    Olivine_Good_Rod_House_Node = Node(list(itertools.chain(
        md.Olivine_Good_Rod_House_Links)))

    Olivine_Gym_Node = Node(list(itertools.chain(
        md.Olivine_Gym_Links)))

    Olivine_Mart_Node = Node(list(itertools.chain(
        md.Olivine_Mart_Links)))


    Olivine_Tims_House_Node = Node(list(itertools.chain(
        md.Olivine_Tims_House_Links)))



    Cherrygrove_Mart_Node = Node(list(itertools.chain(
        md.Cherrygrove_Mart_Links)))

    Mr_Pokemons_House_Node = Node(list(itertools.chain(
        md.Mr_Pokemons_House_Links)))

    Route_30_Berry_House_Node = Node(list(itertools.chain(
        md.Route_30_Berry_House_Links)))

    Earls_Pokemon_Academy_Node = Node(list(itertools.chain(
        md.Earls_Pokemon_Academy_Links)))

    Violet_Mart_Node = Node(list(itertools.chain(
        md.Violet_City_Mart_Links)))

    Violet_Gym_Node = Node(list(itertools.chain(
        md.Violet_City_Gym_Links)))

    Violet_Kyles_House_Node = Node(list(itertools.chain(
        md.Violet_City_Kyles_House_Links)))

    Azalea_Gym_Node = Node(
        [link for link in md.Azalea_Gym_Links]
    )

    Azalea_Mart_Node = Node(
        [link for link in md.Azalea_Mart_Links]
    )



    Charcoal_Kiln_Node = Node(
        [link for link in md.Charcoal_Kiln_Links]
    )

    Kurts_House_Node = Node(
        [link for link in md.Kurts_House_Links]
    )

    Blackthorn_Gym_Node = Node(
        [link for link in md.Blackthorn_Gym_Links]
    )

    Blackthorn_Mart_House_Node = Node(
        [link for link in md.Blackthorn_Mart_Links]
    )



    Move_Deleters_House_Node = Node(
        [link for link in md.Move_Deleters_House_Links]
    )

    Cianwood_Gym_Node = Node(
        [link for link in md.Cianwood_Gym_Links]
    )

    Cianwood_Pharmacy_Node = Node(
        [link for link in md.Cianwood_Pharmacy_Links]
    )

    Cianwood_Photo_Studio_Node = Node(
        [link for link in md.Cianwood_Photo_Studio_Links]
    )



    Manias_House_Node = Node(
        [link for link in md.Manias_House_Links]
    )

    Poke_Seers_House_Node = Node(
        [link for link in md.Poke_Seers_House_Links]
    )

    # TODO This is technically a corridor
    Burned_Tower_1F_Node = Node(
        [link for link in md.Burned_Tower_1F_Links]
    )

    Ilex_Forest_From_Route_34_Gate_Node = Node(
        [md.Ilex_Forest_Links.ILEX_FOREST_TO_ROUTE_34_ILEX_FOREST_GATE_LINK]
    )

    Ilex_Forest_From_Azalea_Gate_Node = Node(
        [md.Ilex_Forest_Links.ILEX_FOREST_TO_ILEX_FOREST_AZALEA_GATE_LINK]
    )

    Ruins_Of_Alph_Research_Center_Node = Node(
        [link for link in md.Ruins_Of_Alph_Research_Center_Links]
    )

    Slowpoke_Well_Overworld_Entrance_Node = Node(
        [md.Azalea_Town_Links.AZALEA_TOWN_TO_SLOWPOKE_WELL_B1F_LINK]
    )

    Slowpoke_Well_B1F_From_Overworld_Node = Node(
        [md.Slowpoke_Well_B1F_Links.SLOWPOKE_WELL_B1F_TO_AZALEA_TOWN_LINK]
    )

    # TODO Technically a corridor
    Tin_Tower_1F_Node = Node(
        [md.Tin_Tower_1F_Links.TIN_TOWER_1F_TO_ECRUTEAK_CITY_LINK]
    )

    Dance_Theatre_Node = Node(
        [link for link in md.Dance_Theatre_Links]
    )

    Ecruteak_Gym_Node = Node(
        [link for link in md.Ecruteak_Gym_Links]
    )

    Ecruteak_Item_Finder_House_Node = Node(
        [link for link in md.Ecruteak_Item_Finder_House_Links]
    )

    Lake_Of_Rage_Hidden_Power_House_Interior_Node = Node(
        [link for link in md.Lake_Of_Rage_Hidden_Power_House_Links]
    )

    Lake_Of_Rage_Magikarp_House_Node = Node(
        [link for link in md.Lake_Of_Rage_Magikarp_House_Links]
    )

    Day_Care_Node = Node(
        [link for link in md.Day_Care_Links]
    )

    Goldenrod_Bike_Shop_Node = Node(
        [link for link in md.Goldenrod_Bike_Shop_Links]
    )

    #Todo this is a cooridor
    Goldenrod_Dept_Store_1F_Node = Node(
        [link for link in md.Goldenrod_Dept_Store_1F_Links]
    )

    Goldenrod_Flower_Shop_Node = Node(
        [link for link in md.Goldenrod_Flower_Shop_Links]
    )

    Goldenrod_Game_Corner_Node = Node(
        [link for link in md.Goldenrod_Game_Corner_Links]
    )

    Goldenrod_Gym_Node = Node(
        [link for link in md.Goldenrod_Gym_Links]
    )

    #TODO Technically a cooridor
    Route_42_Left_Node = Node(
        [md.Route_42_Links.ROUTE_42_TO_ROUTE_42_ECRUTEAK_GATE_LINK]
    )

    Lugia_Chamber_Node = Node(
        [md.Whirl_Island_Lugia_Chamber_Links.WHIRL_ISLAND_LUGIA_CHAMBER_TO_WHIRL_ISLAND_B2F_LINK]
    )

    Tin_Tower_Roof_Node = Node(
        [md.Tin_Tower_Roof_Links.TIN_TOWER_ROOF_TO_TIN_TOWER_9F_LINK]
    )

    Goldenrod_Magnet_Train_Station_Node = Node(
        [link for link in md.Goldenrod_Magnet_Train_Station_Links]
    )



    Goldenrod_PP_Speech_House_Node = Node(
        [link for link in md.Goldenrod_PP_Speech_House_Links]
    )

    #TODO Technically Corridor
    Radio_Tower_1F_Node = Node(
        [link for link in md.Radio_Tower_1F_Links]
    )

    # TODO Technically a coridor after trigger
    Mahogany_Mart_Node = Node(
        [link for link in md.Mahogany_Mart_Links]
    )

    Mahogany_Gym_Node = Node(
        [link for link in md.Mahogany_Gym_Links]
    )


    Ecruteak_Mart_Node = Node(
        [link for link in md.Ecruteak_Mart_Links]
    )

    Dragon_Shrine_Node = Node(
        [md.Dragon_Shrine_Links.DRAGON_SHRINE_TO_DRAGONS_DEN_B1F_2_LINK]
    )



class UselessDeadEndNodes(Enum):


    Olivine_Punishment_Speech_House_Node = Node(list(itertools.chain(
        md.Olivine_Punishment_Speech_House_Links)))

    Cherrygrove_Gym_Speech_House_Node = Node(list(itertools.chain(
        md.Cherrygrove_Gym_Speech_House_Links)))

    Cherrygrove_Evolution_Speech_House_Node = Node(list(itertools.chain(
        md.Cherrygrove_Evolution_Speech_House_Links)))

    Guide_Gents_House_Node = Node(list(itertools.chain(
        md.Guide_Gents_House_Links)))

    Violet_Nickname_Speech_House_Node = Node(list(itertools.chain(
        md.Violet_Nickname_Speech_House_Links)))

    Blackthorn_Emys_House_Node = Node(
        [link for link in md.Blackthorn_Emys_House_Links]
    )

    Blackthorn_Dragon_Speech_House_Node = Node(
        [link for link in md.Blackthorn_Dragon_Speech_House_Links]
    )

    Cianwood_Lugia_Speech_House_Node = Node(
        [link for link in md.Cianwood_Lugia_Speech_House_Links]
    )

    Dark_Cave_Violet_Entrance_From_Route_31_Node = Node(
        [md.Dark_Cave_Violet_Entrance_Links.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_31_LINK]
    )

    # Dark_Cave_Violet_Entrance_From_Route_46_Node = Node(
    #     [md.Dark_Cave_Violet_Entrance_Links.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_46_LINK]
    # )

    Lake_Of_Rage_Hidden_Power_House_Exterior_Node = Node(
        [md.Lake_Of_Rage_Links.LAKE_OF_RAGE_TO_LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_LINK]
    )

    Ecruteak_Lugia_Speech_House_Node = Node(
        [link for link in md.Ecruteak_Lugia_Speech_House_Links]
    )

    # Ecruteak_Tin_Tower_Entrance_To_Wise_Trio_Room_Node = Node(
    #     [md.Ecruteak_Tin_Tower_Entrance_Links.ECRUTEAK_TIN_TOWER_ENTRANCE_TO_WISE_TRIOS_ROOM_LINK]
    # )

    Route_43_Gate_Top_Node = Node(
        [md.Route_43_Gate_Links.ROUTE_43_GATE_TO_ROUTE_43_TOP_LINK]
    )

    Route_43_Gate_Bottom_Node = Node(
        [md.Route_43_Gate_Links.ROUTE_43_GATE_TO_ROUTE_43_BOTTOM_LINK]
    )

    Bills_Familys_House_Node = Node(
        [link for link in md.Bills_Familys_House_Links]
    )

    Goldenrod_Happiness_Rater_Node = Node(
        [link for link in md.Goldenrod_Happiness_Rater_Links]
    )

    Goldenrod_Name_Rater_Node = Node(
        [link for link in md.Goldenrod_Name_Rater_Links]
    )

    Mahogany_Red_Gyarados_Speech_House_Node = Node(
        [link for link in md.Mahogany_Red_Gyarados_Speech_House_Links]
    )



class TwoWayCorridorNodes(Enum):
    Sprout_Tower_1F_Inner_Node = Node(
        [md.Sprout_Tower_1F_Links.SPROUT_TOWER_1F_TO_VIOLET_CITY_LINK,
         md.Sprout_Tower_1F_Links.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FA_LINK]
    )

    Sprout_Tower_1F_Outer_Node = Node(
        [md.Sprout_Tower_1F_Links.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FB_LINK,
         md.Sprout_Tower_1F_Links.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FC_LINK]
    )

    Sprout_Tower_2F_NE_Node = Node(
        [md.Sprout_Tower_2F_Links.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_5_LINK,
         md.Sprout_Tower_2F_Links.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_3_LINK]
    )
    Sprout_Tower_2F_SW_Node = Node(
        [md.Sprout_Tower_2F_Links.SPROUT_TOWER_2F_TO_SPROUT_TOWER_3F_1_LINK,
         md.Sprout_Tower_2F_Links.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_4_LINK]
    )

    Goldenrod_Underground_Warehouse_Node = Node(
        [md.Goldenrod_Underground_Switch_Room_Entrance_Links.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_LINK,
         md.Goldenrod_Underground_Warehouse_Links.GOLDENROD_UNDERGROUND_WAREHOUSE_TO_GOLDENROD_DEPT_STORE_B1F_LINK]
    )

    Goldenrod_Switch_Room_Entrance_North_Node = Node(
        [md.Goldenrod_Underground_Switch_Room_Entrance_Links.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_NORTH_LINK,
         md.Goldenrod_Underground_Switch_Room_Entrance_Links.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_NORTH_LINK]
    )

    Goldenrod_Switch_Room_Entrance_South_Node = Node(
        [md.Goldenrod_Underground_Switch_Room_Entrance_Links.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_SOUTH_LINK,
         md.Goldenrod_Underground_Switch_Room_Entrance_Links.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_SOUTH_LINK]
    )

    Kogas_Room_Node = Node(
        [link for link in md.Kogas_Room_Links]
    )

    Wills_Room_Node = Node(
        [link for link in md.Wills_Room_Links]
    )

    Karens_Room_Node = Node(
        [link for link in md.Karens_Room_Links]
    )

    Brunos_Room_Node = Node(
        [link for link in md.Brunos_Room_Links]
    )

    Ecruteak_Pokecenter_Node = Node(
        [link for link in md.Ecruteak_Pokecenter_Links]
    )

    Route_32_Pokecenter_Node = Node(
        [link for link in md.Route_32_Pokecenter_Links]
    )

    Mahogany_Pokecenter_Node = Node(
        [link for link in md.Mahogany_Pokecenter_Links]
    )

    Goldenrod_Pokecenter_Node = Node(
        [link for link in md.Goldenrod_Pokecenter_Links]
    )

    Cianwood_Pokecenter_Node = Node(
        [link for link in md.Cianwood_Pokecenter_Links]
    )

    Blackthorn_Pokecenter_Node = Node(
        [link for link in md.Blackthorn_Pokecenter_Links]
    )

    Azalea_Pokecenter_Node = Node(
        [link for link in md.Azalea_Pokecenter_Links]
    )

    Violet_Pokecenter_Node = Node(
        [link for link in md.Violet_City_Pokecenter_Links]
    )

    Cherrygrove_Pokecenter_Node = Node(
        [link for link in md.Cherrygrove_Pokecenter_Links])

    Olivine_Pokecenter_Node = Node(
        [link for link in md.Olivine_Pokecenter_Links])

    Route31_Node = Node([link for link in md.Route_31_Links])

    Wise_Trio_To_Tin_Tower_Overworld_Node = Node(
        [link for link in md.Ecruteak_City_Links if link in
         [md.Ecruteak_City_Links.ECRUTEAK_CITY_TO_TIN_TOWER_1F_LINK,
          md.Ecruteak_City_Links.ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_LINK]
         ]
    )

    Lighthouse_1F_Node = Node(
        [link for link in md.Olivine_Lighthouse_1F_Links]
    )

    Lighthouse_5F_Outer_Node = Node(
        [md.Olivine_Lighthouse_5F_Links.OLIVINE_LIGHTHOUSE_5F_TO_4F_OUTER_STAIR_LINK,
         md.Olivine_Lighthouse_5F_Links.OLIVINE_LIGHTHOUSE_5F_TO_4F_PITFALL_LINK]
    )

    Lighthouse_5F_Inner_Node = Node(
        [md.Olivine_Lighthouse_5F_Links.OLIVINE_LIGHTHOUSE_5F_TO_4F_INNER_STAIR_LINK,
         md.Olivine_Lighthouse_5F_Links.OLIVINE_LIGHTHOUSE_5F_TO_6F_STAIR_LINK]
    )

    Lighthouse_6F_Node = Node(
        [link for link in md.Olivine_Lighthouse_6F_Links]
    )

    National_Park_Node = Node(
        [link for link in md.National_Park_Links]
    )

    Union_Cave_1F_Node = Node(
        [link for link in md.Union_Cave_1F_Links]
    )

    Route_29_Route_46_Gate_Node = Node(
        [link for link in md.Route_29_Route_46_Gate_Links]
    )

    Route_31_Violet_Gate_Node = Node(
        [link for link in md.Route_31_Violet_Gate_Links]
    )

    Route_32_Ruins_Of_Alph_Gate_Node = Node(
        [link for link in md.Route_32_Ruins_Of_Alph_Gate_Links]
    )

    Route_34_Ilex_Forest_Gate_Node = Node(
        [link for link in md.Route_34_Ilex_Forest_Gate_Links]
    )

    Ilex_Forest_Azalea_Gate_Node = Node(
        [link for link in md.Ilex_Forest_Azalea_Gate_Links]
    )


    Route_35_Goldenrod_Gate_Node = Node(
        [link for link in md.Route_35_Goldenrod_Gate_Links]
    )

    Route_35_National_Park_Gate_Node = Node(
        [link for link in md.Route_35_National_Park_Gate_Links]
    )

    Route_36_National_Park_Gate_Node = Node(
        [link for link in md.Route_36_National_Park_Gate_Links]
    )

    Route_36_Ruins_Of_Alph_Gate_Node = Node(
        [link for link in md.Route_36_Ruins_Of_Alph_Gate_Links]
    )

    Route_38_Ecruteak_Gate_Node = Node(
        [link for link in md.Route_38_Ecruteak_Gate_Links]
    )

    Route_42_Ecruteak_Gate_Node = Node(
        [link for link in md.Route_42_Ecruteak_Gate_Links]
    )

    Route_43_Mahogany_Gate_Node = Node(
        [link for link in md.Route_43_Mahogany_Gate_Links]
    )


    Route_35_Node = Node(
        [link for link in md.Route_35_Links]
    )

    Route_32_Node = Node(
        [md.Route_32_Links.ROUTE_32_TO_ROUTE_32_POKECENTER_LINK,
         md.Route_32_Links.ROUTE_32_TO_UNION_CAVE_LINK]
    )

    Goldenrod_Underground_Corridor_Node = Node(
        [md.Goldenrod_Underground_Links.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_STAIR_LINK,
         md.Goldenrod_Underground_Links.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_LINK]
    )

class HubNodes(Enum):

    Goldenrod_Underground_Hub_Node = Node(
        [md.Goldenrod_Underground_Links.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_KEY_DOOR_LINK,
         md.Goldenrod_Underground_Links.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_NORTH_LINK,
         md.Goldenrod_Underground_Links.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH_LINK]
    )


    Lighthouse_2F_Node = Node(
        [link for link in md.Olivine_Lighthouse_2F_Links]
    )

    Lighthouse_3F_Node = Node(
        [link for link in md.Olivine_Lighthouse_3F_Links if link not in
         [md.Olivine_Lighthouse_3F_Links.OLIVINE_LIGHTHOUSE_3F_TO_4F_MIDDLE_STAIR_LINK]]
    )

    Lighthouse_4F_Node = Node(
        [link for link in md.Olivine_Lighthouse_4F_Links]
    )

    Lake_Of_Rage_Area_Node = Node(
        [link for link in md.Route_43_Links] +
        [md.Lake_Of_Rage_Links.LAKE_OF_RAGE_TO_LAKE_OF_RAGE_MAGIKARP_HOUSE_LINK]

    )

    Ruins_Of_Alph_Outside_Node = Node(
        [link for link in md.Ruins_Of_Alph_Outside_Links]
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