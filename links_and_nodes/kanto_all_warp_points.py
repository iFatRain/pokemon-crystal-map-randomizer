import itertools
from enum import Enum

from class_definitions import WarpLink, Unlock_Keys
from logic.MemoryAddressReader import buildMemoryLocationsFromSym

from map_data.Celadon_Group.CeladonCafe_Map import Celadon_Cafe_Warp_Points
from map_data.Celadon_Group.CeladonCity_Map import Celadon_City_Warp_Points
from map_data.Celadon_Group.CeladonDeptStore1F_Map import Celadon_Dept_Store_1F_Warp_Points
from map_data.Celadon_Group.CeladonDeptStore2F_Map import Celadon_Dept_Store_2F_Warp_Points
from map_data.Celadon_Group.CeladonDeptStore3F_Map import Celadon_Dept_Store_3F_Warp_Points
from map_data.Celadon_Group.CeladonDeptStore4F_Map import Celadon_Dept_Store_4F_Warp_Points
from map_data.Celadon_Group.CeladonDeptStore5F_Map import Celadon_Dept_Store_5F_Warp_Points
from map_data.Celadon_Group.CeladonDeptStore6F_Map import Celadon_Dept_Store_6F_Warp_Points
from map_data.Celadon_Group.CeladonGameCorner_Map import Celadon_Game_Corner_Warp_Points
from map_data.Celadon_Group.CeladonGameCornerPrizeRoom_Map import Celadon_Game_Corner_Prize_Room_Warp_Points
from map_data.Celadon_Group.CeladonGym_Map import Celadon_Gym_Warp_Points
from map_data.Celadon_Group.CeladonMansion1F_Map import Celadon_Mansion_1F_Warp_Points
from map_data.Celadon_Group.CeladonMansion2F_Map import Celadon_Mansion_2F_Warp_Points
from map_data.Celadon_Group.CeladonMansion3F_Map import Celadon_Mansion_3F_Warp_Points
from map_data.Celadon_Group.CeladonMansionRoofHouse_Map import Celadon_Mansion_Roof_House_Warp_Points
from map_data.Celadon_Group.CeladonMansionRoof_Map import Celadon_Mansion_Roof_Warp_Points
from map_data.Celadon_Group.CeladonPokecenter1F_Map import Celadon_Pokecenter_1F_Warp_Points

from map_data.Cerulean_Group.BillsHouse_Map import Bills_House_Warp_Points
from map_data.Cerulean_Group.CeruleanCity_Map import Cerulean_City_Warp_Points
from map_data.Cerulean_Group.CeruleanGym_Map import Cerulean_Gym_Warp_Points
from map_data.Cerulean_Group.CeruleanGymBadgeSpeechHouse_Map import Cerulean_Gym_Badge_Speech_House_Warp_Points
from map_data.Cerulean_Group.CeruleanMart_Map import Cerulean_Mart_Warp_Points
from map_data.Cerulean_Group.CeruleanPokecenter1F_Map import Cerulean_Pokecenter_1F_Warp_Points
from map_data.Cerulean_Group.CeruleanPoliceStation_Map import Cerulean_Police_Station_Warp_Points
from map_data.Cerulean_Group.CeruleanTradeSpeechHouse_Map import Cerulean_Trade_Speech_House_Warp_Points
from map_data.Cerulean_Group.PowerPlant_Map import Power_Plant_Warp_Points

from map_data.Cinnabar_Group.CinnabarIsland_Map import Cinnabar_Island_Warp_Points
from map_data.Cinnabar_Group.CinnabarPokecenter1F_Map import Cinnabar_Pokecenter_1F_Warp_Points
from map_data.Cinnabar_Group.SeafoamGym_Map import Seafoam_Gym_Warp_Points
from map_data.Dungeons_Group.Pokecenter2F_Map import Pokecenter_2F_Warp_Points

from map_data.Fuchsia_Group.BillsBrothersHouse_Map import Bills_Brothers_House_Warp_Points
from map_data.Fuchsia_Group.FuchsiaCity_Map import Fuchsia_City_Warp_Points
from map_data.Fuchsia_Group.FuchsiaGym_Map import Fuchsia_Gym_Warp_Points
from map_data.Fuchsia_Group.FuchsiaMart_Map import Fuchsia_Mart_Warp_Points
from map_data.Fuchsia_Group.FuchsiaPokecenter1F_Map import Fuchsia_Pokecenter_1F_Warp_Points
from map_data.Fuchsia_Group.SafariZoneMainOffice_Map import Safari_Zone_Main_Office_Warp_Points
from map_data.Fuchsia_Group.SafariZoneWardensHome_Map import Safari_Zone_Wardens_Home_Warp_Points
from map_data.Gates.VictoryRoadGate_Map import Victory_Road_Gate_Warp_Points

from map_data.Lavender_Group.LavenderMart_Map import Lavender_Mart_Warp_Points
from map_data.Lavender_Group.LavenderNameRater_Map import Lavender_Name_Rater_Warp_Points
from map_data.Lavender_Group.LavenderPokecenter1F_Map import Lavender_Pokecenter_1F_Warp_Points
from map_data.Lavender_Group.LavenderSpeechHouse_Map import Lavender_Speech_House_Warp_Points
from map_data.Lavender_Group.LavenderTown_Map import Lavender_Town_Warp_Points
from map_data.Lavender_Group.LavRadioTower1F_Map import Lav_Radio_Tower_1F_Warp_Points
from map_data.Lavender_Group.MrFujisHouse_Map import Mr_Fujis_House_Warp_Points
from map_data.Lavender_Group.SoulHouse_Map import Soul_House_Warp_Points

from map_data.Pallet_Group.BluesHouse_Map import Blues_House_Warp_Points
from map_data.Pallet_Group.OaksLab_Map import Oaks_Lab_Warp_Points
from map_data.Pallet_Group.PalletTown_Map import Pallet_Town_Warp_Points
from map_data.Pallet_Group.RedsHouse1F_Map import Reds_House_1F_Warp_Points
from map_data.Pallet_Group.RedsHouse2F_Map import Reds_House_2F_Warp_Points

from map_data.Pewter_Group.PewterCity_Map import Pewter_City_Warp_Points
from map_data.Pewter_Group.PewterGym_Map import Pewter_Gym_Warp_Points
from map_data.Pewter_Group.PewterMart_Map import Pewter_Mart_Warp_Points
from map_data.Pewter_Group.PewterNidoranSpeechHouse_Map import Pewter_Nidoran_Speech_House_Warp_Points
from map_data.Pewter_Group.PewterPokecenter1F_Map import Pewter_Pokecenter_1F_Warp_Points
from map_data.Pewter_Group.PewterSnoozeSpeechHouse_Map import Pewter_Snooze_Speech_House_Warp_Points

from map_data.Saffron_Group.CopycatsHouse1F_Map import Copycats_House_1F_Warp_Points
from map_data.Saffron_Group.CopycatsHouse2F_Map import Copycats_House_2F_Warp_Points
from map_data.Saffron_Group.FightingDojo_Map import Fighting_Dojo_Warp_Points
from map_data.Saffron_Group.MrPsychicsHouse_Map import Mr_Psychics_House_Warp_Points
from map_data.Saffron_Group.SaffronCity_Map import Saffron_City_Warp_Points
from map_data.Saffron_Group.SaffronGym_Map import Saffron_Gym_Warp_Points
from map_data.Saffron_Group.SaffronMagnetTrainStation_Map import Saffron_Magnet_Train_Station_Warp_Points
from map_data.Saffron_Group.SaffronMart_Map import Saffron_Mart_Warp_Points
from map_data.Saffron_Group.SaffronPokecenter1F_Map import Saffron_Pokecenter_1F_Warp_Points
from map_data.Saffron_Group.SilphCo1F_Map import Silph_Co_1F_Warp_Points
from map_data.Silver_Group.Route28SteelWingHouse_Map import Route_28_Steel_Wing_House_Warp_Points
from map_data.Silver_Group.Route28_Map import Route_28_Warp_Points
from map_data.Silver_Group.SilverCaveItemRooms_Map import Silver_Cave_Item_Rooms_Warp_Points
from map_data.Silver_Group.SilverCaveOutside_Map import Silver_Cave_Outside_Warp_Points
from map_data.Silver_Group.SilverCavePokecenter1F_Map import Silver_Cave_Pokecenter_1F_Warp_Points
from map_data.Silver_Group.SilverCaveRoom1_Map import Silver_Cave_Room_1_Warp_Points
from map_data.Silver_Group.SilverCaveRoom2_Map import Silver_Cave_Room_2_Warp_Points
from map_data.Silver_Group.SilverCaveRoom3_Map import Silver_Cave_Room_3_Warp_Points

from map_data.Vermilion_Group.PokemonFanClub_Map import Pokemon_Fan_Club_Warp_Points
from map_data.Vermilion_Group.VermilionCity_Map import Vermilion_City_Warp_Points
from map_data.Vermilion_Group.VermilionDiglettsCaveSpeechHouse_Map import Vermilion_Digletts_Cave_Speech_House_Warp_Points
from map_data.Vermilion_Group.VermilionFishingSpeechHouse_Map import Vermilion_Fishing_Speech_House_Warp_Points
from map_data.Vermilion_Group.VermilionGym_Map import Vermilion_Gym_Warp_Points
from map_data.Vermilion_Group.VermilionMagnetTrainSpeechHouse_Map import Vermilion_Magnet_Train_Speech_House_Warp_Points
from map_data.Vermilion_Group.VermilionMart_Map import Vermilion_Mart_Warp_Points
from map_data.Vermilion_Group.VermilionPokecenter1F_Map import Vermilion_Pokecenter_1F_Warp_Points
from map_data.Vermilion_Group.VermilionPort_Map import Vermilion_Port_Warp_Points
from map_data.Vermilion_Group.VermilionPortPassage_Map import Vermilion_Port_Passage_Warp_Points

from map_data.Viridian_Group.Route2NuggetHouse_Map import Route_2_Nugget_House_Warp_Points
from map_data.Viridian_Group.TrainerHouse1F_Map import Trainer_House_1F_Warp_Points
from map_data.Viridian_Group.TrainerHouseB1F_Map import Trainer_House_B1F_Warp_Points
from map_data.Viridian_Group.ViridianCity_Map import Viridian_City_Warp_Points
from map_data.Viridian_Group.ViridianGym_Map import Viridian_Gym_Warp_Points
from map_data.Viridian_Group.ViridianMart_Map import Viridian_Mart_Warp_Points
from map_data.Viridian_Group.ViridianNicknameSpeechHouse_Map import Viridian_Nickname_Speech_House_Warp_Points
from map_data.Viridian_Group.ViridianPokecenter1F_Map import Viridian_Pokecenter_1F_Warp_Points

from map_data.Kanto_Dungeons.DiglettsCave_Map import Digletts_Cave_Warp_Points
from map_data.Kanto_Dungeons.MountMoonGiftShop_Map import Mount_Moon_Gift_Shop_Warp_Points
from map_data.Kanto_Dungeons.MountMoon_Map import Mount_Moon_Warp_Points
from map_data.Kanto_Dungeons.MountMoonSquare_Map import Mount_Moon_Square_Warp_Points
from map_data.Kanto_Dungeons.RockTunnel1F_Map import Rock_Tunnel_1F_Warp_Points
from map_data.Kanto_Dungeons.RockTunnelB1F_Map import Rock_Tunnel_B1F_Warp_Points
from map_data.Kanto_Dungeons.UndergroundPath_Map import Underground_Path_Warp_Points

from map_data.Kanto_Gates.Route17Route18Gate_Map import Route_17_Route_18_Gate_Warp_Points
from map_data.Kanto_Gates.Route19FuchsiaGate_Map import Route_19_Fuchsia_Gate_Warp_Points
from map_data.Kanto_Gates.Route2Gate_Map import Route_2_Gate_Warp_Points
from map_data.Kanto_Gates.Route5SaffronGate_Map import Route_5_Saffron_Gate_Warp_Points
from map_data.Kanto_Gates.Route6SaffronGate_Map import Route_6_Saffron_Gate_Warp_Points
from map_data.Kanto_Gates.Route7SaffronGate_Map import Route_7_Saffron_Gate_Warp_Points
from map_data.Kanto_Gates.Route8SaffronGate_Map import Route_8_Saffron_Gate_Warp_Points
from map_data.Kanto_Gates.Route15FuchsiaGate_Map import Route_15_Fuchsia_Gate_Warp_Points
from map_data.Kanto_Gates.Route16Gate_Map import Route_16_Gate_Warp_Points

from map_data.Kanto_Routes.Route2_Map import Route_2_Warp_Points
from map_data.Kanto_Routes.Route3_Map import Route_3_Warp_Points
from map_data.Kanto_Routes.Route4_Map import Route_4_Warp_Points
from map_data.Kanto_Routes.Route5CleanseTagHouse_Map import Route_5_Cleanse_Tag_House_Warp_Points
from map_data.Kanto_Routes.Route5_Map import Route_5_Warp_Points
from map_data.Kanto_Routes.Route5UndergroundPathEntrance_Map import Route_5_Underground_Path_Entrance_Warp_Points
from map_data.Kanto_Routes.Route6_Map import Route_6_Warp_Points
from map_data.Kanto_Routes.Route6UndergroundPathEntrance_Map import Route_6_Underground_Path_Entrance_Warp_Points
from map_data.Kanto_Routes.Route7_Map import Route_7_Warp_Points
from map_data.Kanto_Routes.Route8_Map import Route_8_Warp_Points
from map_data.Kanto_Routes.Route9_Map import Route_9_Warp_Points
from map_data.Kanto_Routes.Route10North_Map import Route_10_North_Warp_Points
from map_data.Kanto_Routes.Route10Pokecenter1F_Map import Route_10_Pokecenter_1F_Warp_Points
from map_data.Kanto_Routes.Route10South_Map import Route_10_South_Warp_Points
from map_data.Kanto_Routes.Route12_Map import Route_12_Warp_Points
from map_data.Kanto_Routes.Route12SuperRodHouse_Map import Route_12_Super_Rod_House_Warp_Points
from map_data.Kanto_Routes.Route15_Map import Route_15_Warp_Points
from map_data.Kanto_Routes.Route16FuchsiaSpeechHouse_Map import Route_16_Fuchsia_Speech_House_Warp_Points
from map_data.Kanto_Routes.Route16_Map import Route_16_Warp_Points
from map_data.Kanto_Routes.Route17_Map import Route_17_Warp_Points
from map_data.Kanto_Routes.Route18_Map import Route_18_Warp_Points
from map_data.Kanto_Routes.Route19_Map import Route_19_Warp_Points
from map_data.Kanto_Routes.Route20_Map import Route_20_Warp_Points
from map_data.Kanto_Routes.Route22_Map import Route_22_Warp_Points
from map_data.Kanto_Routes.Route25_Map import Route_25_Warp_Points

from map_data.Fast_Ship_Group.FastShip1F_Map import Fast_Ship_1F_Warp_Points
from map_data.Fast_Ship_Group.FastShipB1F_Map import Fast_Ship_B1F_Warp_Points
from map_data.Fast_Ship_Group.FastShipCabins_NNW_NNE_NE_Map import Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points
from map_data.Fast_Ship_Group.FastShipCabins_SE_SSE_CaptainsCabin_Map import Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points
from map_data.Fast_Ship_Group.FastShipCabins_SW_SSW_NW_Map import Fast_Ship_Cabins_SW_SSW_NW_Warp_Points

#######################################################################
#                                                                     #
#                Organized Linking is Below This Point                #
#                                                                     #
#######################################################################

#######################################################################
#                    Celadon Group                                    #
#######################################################################

class Celadon_Cafe_Links(Enum):

    CELADON_CAFE_TO_CELADON_CITY_9_LINK = WarpLink(
        Celadon_Cafe_Warp_Points.CELADON_CAFE_TO_CELADON_CITY_9_WP,
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_CAFE_1_WP,
        "CeladonCafe", dual_width= True
    )

class Celadon_Dept_Store_1F_Links(Enum):

    CELADON_DEPT_STORE_1F_TO_CELADON_CITY_1_LINK = WarpLink(
        Celadon_Dept_Store_1F_Warp_Points.CELADON_DEPT_STORE_1F_TO_CELADON_CITY_1_WP,
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_DEPT_STORE_1F_1_WP,
        "CeladonDeptStore1F", dual_width= True
    )

    CELADON_DEPT_STORE_1F_TO_CELADON_DEPT_STORE_2F_2_LINK = WarpLink(
        Celadon_Dept_Store_1F_Warp_Points.CELADON_DEPT_STORE_1F_TO_CELADON_DEPT_STORE_2F_2_WP,
        Celadon_Dept_Store_2F_Warp_Points.CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_1F_3_WP,
        "CeladonDeptStore1F", 10
    )


class Celadon_Dept_Store_2F_Links(Enum):

    CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_3F_1_LINK = WarpLink(
        Celadon_Dept_Store_2F_Warp_Points.CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_3F_1_WP,
        Celadon_Dept_Store_3F_Warp_Points.CELADON_DEPT_STORE_3F_TO_CELADON_DEPT_STORE_2F_1_WP,
        "CeladonDeptStore2F"
    )

    CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_1F_3_LINK = WarpLink(
        Celadon_Dept_Store_2F_Warp_Points.CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_1F_3_WP,
        Celadon_Dept_Store_1F_Warp_Points.CELADON_DEPT_STORE_1F_TO_CELADON_DEPT_STORE_2F_2_WP,
        "CeladonDeptStore2F", 5
    )


class Celadon_Dept_Store_3F_Links(Enum):

    CELADON_DEPT_STORE_3F_TO_CELADON_DEPT_STORE_2F_1_LINK = WarpLink(
        Celadon_Dept_Store_3F_Warp_Points.CELADON_DEPT_STORE_3F_TO_CELADON_DEPT_STORE_2F_1_WP,
        Celadon_Dept_Store_2F_Warp_Points.CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_3F_1_WP,
        "CeladonDeptStore3F"
    )

    CELADON_DEPT_STORE_3F_TO_CELADON_DEPT_STORE_4F_2_LINK = WarpLink(
        Celadon_Dept_Store_3F_Warp_Points.CELADON_DEPT_STORE_3F_TO_CELADON_DEPT_STORE_4F_2_WP,
        Celadon_Dept_Store_4F_Warp_Points.CELADON_DEPT_STORE_4F_TO_CELADON_DEPT_STORE_3F_2_WP,
        "CeladonDeptStore3F", 5
    )


class Celadon_Dept_Store_4F_Links(Enum):

    CELADON_DEPT_STORE_4F_TO_CELADON_DEPT_STORE_5F_1_LINK = WarpLink(
        Celadon_Dept_Store_4F_Warp_Points.CELADON_DEPT_STORE_4F_TO_CELADON_DEPT_STORE_5F_1_WP,
        Celadon_Dept_Store_5F_Warp_Points.CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_4F_1_WP,
        "CeladonDeptStore4F"
    )

    CELADON_DEPT_STORE_4F_TO_CELADON_DEPT_STORE_3F_2_LINK = WarpLink(
        Celadon_Dept_Store_4F_Warp_Points.CELADON_DEPT_STORE_4F_TO_CELADON_DEPT_STORE_3F_2_WP,
        Celadon_Dept_Store_3F_Warp_Points.CELADON_DEPT_STORE_3F_TO_CELADON_DEPT_STORE_4F_2_WP,
        "CeladonDeptStore4F", 5
    )


class Celadon_Dept_Store_5F_Links(Enum):

    CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_4F_1_LINK = WarpLink(
        Celadon_Dept_Store_5F_Warp_Points.CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_4F_1_WP,
        Celadon_Dept_Store_4F_Warp_Points.CELADON_DEPT_STORE_4F_TO_CELADON_DEPT_STORE_5F_1_WP,
        "CeladonDeptStore5F"
    )

    CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_6F_1_LINK = WarpLink(
        Celadon_Dept_Store_5F_Warp_Points.CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_6F_1_WP,
        Celadon_Dept_Store_6F_Warp_Points.CELADON_DEPT_STORE_6F_TO_CELADON_DEPT_STORE_5F_2_WP,
        "CeladonDeptStore5F", 5
    )


class Celadon_Dept_Store_6F_Links(Enum):

    CELADON_DEPT_STORE_6F_TO_CELADON_DEPT_STORE_5F_2_LINK = WarpLink(
        Celadon_Dept_Store_6F_Warp_Points.CELADON_DEPT_STORE_6F_TO_CELADON_DEPT_STORE_5F_2_WP,
        Celadon_Dept_Store_5F_Warp_Points.CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_6F_1_WP,
        "CeladonDeptStore6F"
    )


class Celadon_Game_Corner_Links(Enum):

    CELADON_GAME_CORNER_TO_CELADON_CITY_6_LINK = WarpLink(
        Celadon_Game_Corner_Warp_Points.CELADON_GAME_CORNER_TO_CELADON_CITY_6_WP,
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_GAME_CORNER_1_WP,
        "CeladonGameCorner", dual_width= True
    )

class Celadon_Game_Corner_Prize_Room_Links(Enum):

    CELADON_GAME_CORNER_PRIZE_ROOM_TO_CELADON_CITY_7_LINK = WarpLink(
        Celadon_Game_Corner_Prize_Room_Warp_Points.CELADON_GAME_CORNER_PRIZE_ROOM_TO_CELADON_CITY_7_WP,
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_GAME_CORNER_PRIZE_ROOM_1_WP,
        "CeladonGameCornerPrizeRoom", dual_width= True
    )

class Celadon_Gym_Links(Enum):

    CELADON_GYM_TO_CELADON_CITY_8_LINK = WarpLink(
        Celadon_Gym_Warp_Points.CELADON_GYM_TO_CELADON_CITY_8_WP,
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_GYM_1_WP,
        "CeladonGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_12]
    )

class Celadon_Mansion_1F_Links(Enum): # 1-4 ,2-3

    CELADON_MANSION_1F_TO_CELADON_CITY_2_LINK = WarpLink(
        Celadon_Mansion_1F_Warp_Points.CELADON_MANSION_1F_TO_CELADON_CITY_2_WP,
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_MANSION_1F_1_WP,
        "CeladonMansion1F", dual_width= True
    )

    CELADON_MANSION_1F_TO_CELADON_CITY_3_LINK = WarpLink(# backside
        Celadon_Mansion_1F_Warp_Points.CELADON_MANSION_1F_TO_CELADON_CITY_3_WP,
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_MANSION_1F_3_WP,
        "CeladonMansion1F", 10
    )

    CELADON_MANSION_1F_TO_CELADON_MANSION_2F_1_LINK = WarpLink( # 
        Celadon_Mansion_1F_Warp_Points.CELADON_MANSION_1F_TO_CELADON_MANSION_2F_1_WP,
        Celadon_Mansion_2F_Warp_Points.CELADON_MANSION_2F_TO_CELADON_MANSION_1F_4_WP,
        "CeladonMansion1F", 15
    )

    CELADON_MANSION_1F_TO_CELADON_MANSION_2F_4_LINK = WarpLink( 
        Celadon_Mansion_1F_Warp_Points.CELADON_MANSION_1F_TO_CELADON_MANSION_2F_4_WP,
        Celadon_Mansion_2F_Warp_Points.CELADON_MANSION_2F_TO_CELADON_MANSION_1F_5_WP,
        "CeladonMansion1F", 20
    )

class Celadon_Mansion_2F_Links(Enum): # 1-2,3-4

    CELADON_MANSION_2F_TO_CELADON_MANSION_1F_4_LINK = WarpLink(#
        Celadon_Mansion_2F_Warp_Points.CELADON_MANSION_2F_TO_CELADON_MANSION_1F_4_WP,
        Celadon_Mansion_1F_Warp_Points.CELADON_MANSION_1F_TO_CELADON_MANSION_2F_1_WP,
        "CeladonMansion2F"
    )

    CELADON_MANSION_2F_TO_CELADON_MANSION_3F_2_LINK = WarpLink(#
        Celadon_Mansion_2F_Warp_Points.CELADON_MANSION_2F_TO_CELADON_MANSION_3F_2_WP,
        Celadon_Mansion_3F_Warp_Points.CELADON_MANSION_3F_TO_CELADON_MANSION_2F_2_WP,
        "CeladonMansion2F", 5
    )

    CELADON_MANSION_2F_TO_CELADON_MANSION_3F_3_LINK = WarpLink(
        Celadon_Mansion_2F_Warp_Points.CELADON_MANSION_2F_TO_CELADON_MANSION_3F_3_WP,
        Celadon_Mansion_3F_Warp_Points.CELADON_MANSION_3F_TO_CELADON_MANSION_2F_3_WP,
        "CeladonMansion2F", 10
    )

    CELADON_MANSION_2F_TO_CELADON_MANSION_1F_5_LINK = WarpLink(
        Celadon_Mansion_2F_Warp_Points.CELADON_MANSION_2F_TO_CELADON_MANSION_1F_5_WP,
        Celadon_Mansion_1F_Warp_Points.CELADON_MANSION_1F_TO_CELADON_MANSION_2F_4_WP,
        "CeladonMansion2F", 15
    )

class Celadon_Mansion_3F_Links(Enum): # 1-2, 3-4

    CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_1_LINK = WarpLink(#
        Celadon_Mansion_3F_Warp_Points.CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_1_WP,
        Celadon_Mansion_Roof_Warp_Points.CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_1_WP,
        "CeladonMansion3F",  unlocks=[]
    )

    CELADON_MANSION_3F_TO_CELADON_MANSION_2F_2_LINK = WarpLink(#
        Celadon_Mansion_3F_Warp_Points.CELADON_MANSION_3F_TO_CELADON_MANSION_2F_2_WP,
        Celadon_Mansion_2F_Warp_Points.CELADON_MANSION_2F_TO_CELADON_MANSION_3F_2_WP,
        "CeladonMansion3F", 5
    )

    CELADON_MANSION_3F_TO_CELADON_MANSION_2F_3_LINK = WarpLink(
        Celadon_Mansion_3F_Warp_Points.CELADON_MANSION_3F_TO_CELADON_MANSION_2F_3_WP,
        Celadon_Mansion_2F_Warp_Points.CELADON_MANSION_2F_TO_CELADON_MANSION_3F_3_WP,
        "CeladonMansion3F", 10
    )

    CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_2_LINK = WarpLink(
        Celadon_Mansion_3F_Warp_Points.CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_2_WP,
        Celadon_Mansion_Roof_Warp_Points.CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_4_WP,
        "CeladonMansion3F", 15
    )

class Celadon_Mansion_Roof_House_Links(Enum):

    CELADON_MANSION_ROOF_HOUSE_TO_CELADON_MANSION_ROOF_3_LINK = WarpLink(#
        Celadon_Mansion_Roof_House_Warp_Points.CELADON_MANSION_ROOF_HOUSE_TO_CELADON_MANSION_ROOF_3_WP,
        Celadon_Mansion_Roof_Warp_Points.CELADON_MANSION_ROOF_TO_CELADON_MANSION_ROOF_HOUSE_1_WP,
        "CeladonMansionRoofHouse", dual_width= True
    )

class Celadon_Mansion_Roof_Links(Enum): # 1-3, 2x

    CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_1_LINK = WarpLink(#
        Celadon_Mansion_Roof_Warp_Points.CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_1_WP,
        Celadon_Mansion_3F_Warp_Points.CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_1_WP,
        "CeladonMansionRoof"
    )

    CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_4_LINK = WarpLink(
        Celadon_Mansion_Roof_Warp_Points.CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_4_WP,
        Celadon_Mansion_3F_Warp_Points.CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_2_WP,
        "CeladonMansionRoof", 5
    )

    CELADON_MANSION_ROOF_TO_CELADON_MANSION_ROOF_HOUSE_1_LINK = WarpLink(#
        Celadon_Mansion_Roof_Warp_Points.CELADON_MANSION_ROOF_TO_CELADON_MANSION_ROOF_HOUSE_1_WP,
        Celadon_Mansion_Roof_House_Warp_Points.CELADON_MANSION_ROOF_HOUSE_TO_CELADON_MANSION_ROOF_3_WP,
        "CeladonMansionRoof", 10
    )

class Celadon_Pokecenter_1F_Links(Enum):

    CELADON_POKECENTER_1F_TO_CELADON_CITY_5_LINK = WarpLink(
        Celadon_Pokecenter_1F_Warp_Points.CELADON_POKECENTER_1F_TO_CELADON_CITY_5_WP,
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_POKECENTER_1F_1_WP,
        "CeladonPokecenter1F", dual_width= True
    )

    CELADON_POKECENTER_1F_TO_POKECENTER_2F_1_LINK = WarpLink(
        Celadon_Pokecenter_1F_Warp_Points.CELADON_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "CeladonPokecenter1F", 10
    )


class Celadon_City_Links(Enum):

    CELADON_CITY_TO_CELADON_DEPT_STORE_1F_1_LINK = WarpLink(
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_DEPT_STORE_1F_1_WP,
        Celadon_Dept_Store_1F_Warp_Points.CELADON_DEPT_STORE_1F_TO_CELADON_CITY_1_WP,
        "CeladonCity"
    )

    CELADON_CITY_TO_CELADON_MANSION_1F_1LINK = WarpLink(
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_MANSION_1F_1_WP,
        Celadon_Mansion_1F_Warp_Points.CELADON_MANSION_1F_TO_CELADON_CITY_2_WP,
        "CeladonCity", 5
    )

    CELADON_CITY_TO_CELADON_MANSION_1F_3_LINK = WarpLink(
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_MANSION_1F_3_WP,
        Celadon_Mansion_1F_Warp_Points.CELADON_MANSION_1F_TO_CELADON_CITY_3_WP,
        "CeladonCity", 10, dual_width= True
    )

    CELADON_CITY_TO_CELADON_POKECENTER_1F_1_LINK = WarpLink(
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_POKECENTER_1F_1_WP,
        Celadon_Pokecenter_1F_Warp_Points.CELADON_POKECENTER_1F_TO_CELADON_CITY_5_WP,
        "CeladonCity", 20
    )

    CELADON_CITY_TO_CELADON_GAME_CORNER_1_LINK = WarpLink(
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_GAME_CORNER_1_WP,
        Celadon_Game_Corner_Warp_Points.CELADON_GAME_CORNER_TO_CELADON_CITY_6_WP,
        "CeladonCity", 25
    )

    CELADON_CITY_TO_CELADON_GAME_CORNER_PRIZE_ROOM_1_LINK = WarpLink(
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_GAME_CORNER_PRIZE_ROOM_1_WP,
        Celadon_Game_Corner_Prize_Room_Warp_Points.CELADON_GAME_CORNER_PRIZE_ROOM_TO_CELADON_CITY_7_WP,
        "CeladonCity", 30
    )

    CELADON_CITY_TO_CELADON_GYM_1_LINK = WarpLink(
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_GYM_1_WP,
        Celadon_Gym_Warp_Points.CELADON_GYM_TO_CELADON_CITY_8_WP,
        "CeladonCity", 35, locked_by=[Unlock_Keys.CAN_CUT]
    )

    CELADON_CITY_TO_CELADON_CAFE_1_LINK = WarpLink(
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_CAFE_1_WP,
        Celadon_Cafe_Warp_Points.CELADON_CAFE_TO_CELADON_CITY_9_WP,
        "CeladonCity", 40
    )


#######################################################################
#                    Cerulean Group                                   #
#######################################################################

class Bills_House_Links(Enum):

    BILLS_HOUSE_TO_ROUTE_25_1_LINK = WarpLink(
        Bills_House_Warp_Points.BILLS_HOUSE_TO_ROUTE_25_1_WP,
        Route_25_Warp_Points.ROUTE_25_TO_BILLS_HOUSE_1_WP,
        "BillsHouse", dual_width= True
    )

class Cerulean_Gym_Badge_Speech_House_Links(Enum):

    CERULEAN_GYM_BADGE_SPEECH_HOUSE_TO_CERULEAN_CITY_1_LINK = WarpLink(
        Cerulean_Gym_Badge_Speech_House_Warp_Points.CERULEAN_GYM_BADGE_SPEECH_HOUSE_TO_CERULEAN_CITY_1_WP,
        Cerulean_City_Warp_Points.CERULEAN_CITY_TO_CERULEAN_GYM_BADGE_SPEECH_HOUSE_1_WP,
        "CeruleanGymBadgeSpeechHouse", dual_width= True
    )

class Cerulean_Gym_Links(Enum):

    CERULEAN_GYM_TO_CERULEAN_CITY_5_LINK = WarpLink(
        Cerulean_Gym_Warp_Points.CERULEAN_GYM_TO_CERULEAN_CITY_5_WP,
        Cerulean_City_Warp_Points.CERULEAN_CITY_TO_CERULEAN_GYM_1_WP,
        "CeruleanGym", dual_width= True, unlocks=[Unlock_Keys.CERULEAN_GYM_ACCESS]
    )

class Cerulean_Mart_Links(Enum):

    CERULEAN_MART_TO_CERULEAN_CITY_6_LINK = WarpLink(
        Cerulean_Mart_Warp_Points.CERULEAN_MART_TO_CERULEAN_CITY_6_WP,
        Cerulean_City_Warp_Points.CERULEAN_CITY_TO_CERULEAN_MART_2_WP,  
        "CeruleanMart", dual_width= True
    )

class Cerulean_Pokecenter_1F_Links(Enum):

    CERULEAN_POKECENTER_1F_TO_CERULEAN_CITY_4_LINK = WarpLink(
        Cerulean_Pokecenter_1F_Warp_Points.CERULEAN_POKECENTER_1F_TO_CERULEAN_CITY_4_WP,
        Cerulean_City_Warp_Points.CERULEAN_CITY_TO_CERULEAN_POKECENTER_1F_1_WP,
        "CeruleanPokecenter1F", dual_width= True
    )

    CERULEAN_POKECENTER_1F_TO_POKECENTER_2F_1_LINK = WarpLink(
        Cerulean_Pokecenter_1F_Warp_Points.CERULEAN_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "CeruleanPokecenter1F", 10
    )


class Cerulean_Police_Station_Links(Enum):

    CERULEAN_POLICE_STATION_TO_CERULEAN_CITY_2_LINK = WarpLink(
        Cerulean_Police_Station_Warp_Points.CERULEAN_POLICE_STATION_TO_CERULEAN_CITY_2_WP,
        Cerulean_City_Warp_Points.CERULEAN_CITY_TO_CERULEAN_POLICE_STATION_1_WP,
        "CeruleanPoliceStation", dual_width= True
    )

class Cerulean_Trade_Speech_House_Links(Enum):

    CERULEAN_TRADE_SPEECH_HOUSE_TO_CERULEAN_CITY_3_LINK = WarpLink(
        Cerulean_Trade_Speech_House_Warp_Points.CERULEAN_TRADE_SPEECH_HOUSE_TO_CERULEAN_CITY_3_WP,
        Cerulean_City_Warp_Points.CERULEAN_CITY_TO_CERULEAN_TRADE_SPEECH_HOUSE_1_WP,
        "CeruleanTradeSpeechHouse", dual_width= True
    )

class Power_Plant_Links(Enum):

    POWER_PLANT_TO_ROUTE_10_NORTH_2_LINK = WarpLink( 
        Power_Plant_Warp_Points.POWER_PLANT_TO_ROUTE_10_NORTH_2_WP,
        Route_10_North_Warp_Points.ROUTE_10_NORTH_TO_POWER_PLANT_1_WP,
        "PowerPlant", dual_width= True, unlocks=[Unlock_Keys.POWER_PLANT_ACCESS]
    )


class Cerulean_City_Links(Enum):

    CERULEAN_CITY_TO_CERULEAN_GYM_BADGE_SPEECH_HOUSE_1_LINK = WarpLink(
        Cerulean_City_Warp_Points.CERULEAN_CITY_TO_CERULEAN_GYM_BADGE_SPEECH_HOUSE_1_WP,
        Cerulean_Gym_Badge_Speech_House_Warp_Points.CERULEAN_GYM_BADGE_SPEECH_HOUSE_TO_CERULEAN_CITY_1_WP,
        "CeruleanCity"
    )

    CERULEAN_CITY_TO_CERULEAN_POLICE_STATION_1_LINK = WarpLink(
        Cerulean_City_Warp_Points.CERULEAN_CITY_TO_CERULEAN_POLICE_STATION_1_WP,
        Cerulean_Police_Station_Warp_Points.CERULEAN_POLICE_STATION_TO_CERULEAN_CITY_2_WP,
        "CeruleanCity", 5
    )

    CERULEAN_CITY_TO_CERULEAN_TRADE_SPEECH_HOUSE_1_LINK = WarpLink(
        Cerulean_City_Warp_Points.CERULEAN_CITY_TO_CERULEAN_TRADE_SPEECH_HOUSE_1_WP,
        Cerulean_Trade_Speech_House_Warp_Points.CERULEAN_TRADE_SPEECH_HOUSE_TO_CERULEAN_CITY_3_WP,
        "CeruleanCity", 10
    )

    CERULEAN_CITY_TO_CERULEAN_POKECENTER_1F_1_LINK = WarpLink(
        Cerulean_City_Warp_Points.CERULEAN_CITY_TO_CERULEAN_POKECENTER_1F_1_WP,
        Cerulean_Pokecenter_1F_Warp_Points.CERULEAN_POKECENTER_1F_TO_CERULEAN_CITY_4_WP,
        "CeruleanCity", 15
    )

    CERULEAN_CITY_TO_CERULEAN_GYM_1_LINK = WarpLink(
        Cerulean_City_Warp_Points.CERULEAN_CITY_TO_CERULEAN_GYM_1_WP,
        Cerulean_Gym_Warp_Points.CERULEAN_GYM_TO_CERULEAN_CITY_5_WP,
        "CeruleanCity", 20
    )

    CERULEAN_CITY_TO_CERULEAN_MART_2_LINK = WarpLink(
        Cerulean_City_Warp_Points.CERULEAN_CITY_TO_CERULEAN_MART_2_WP,
        Cerulean_Mart_Warp_Points.CERULEAN_MART_TO_CERULEAN_CITY_6_WP,
        "CeruleanCity", 25
    )


#######################################################################
#                    Cinnabar Group                                   #
#######################################################################


class Cinnabar_Pokecenter_1F_Links(Enum):

    CINNABAR_POKECENTER_1F_TO_CINNABAR_ISLAND_1_LINK = WarpLink(
        Cinnabar_Pokecenter_1F_Warp_Points.CINNABAR_POKECENTER_1F_TO_CINNABAR_ISLAND_1_WP,
        Cinnabar_Island_Warp_Points.CINNABAR_ISLAND_TO_CINNABAR_POKECENTER_1F_1_WP,
        "CinnabarPokecenter1F", dual_width= True
    )

    CINNABAR_POKECENTER_1F_TO_POKECENTER_2F_1_LINK = WarpLink(
        Cinnabar_Pokecenter_1F_Warp_Points.CINNABAR_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "CinnabarPokecenter1F", 10
    )


class Seafoam_Gym_Links(Enum):

    SEAFOAM_GYM_TO_ROUTE_20_1_LINK = WarpLink(
        Seafoam_Gym_Warp_Points.SEAFOAM_GYM_TO_ROUTE_20_1_WP,
        Route_20_Warp_Points.ROUTE_20_TO_SEAFOAM_GYM_1_WP,
        "SeafoamGym", unlocks=[Unlock_Keys.BADGE_15]
    )

class Cinnabar_Island_Links(Enum):

    CINNABAR_ISLAND_TO_CINNABAR_POKECENTER_1F_1_LINK = WarpLink(
        Cinnabar_Island_Warp_Points.CINNABAR_ISLAND_TO_CINNABAR_POKECENTER_1F_1_WP,
        Cinnabar_Pokecenter_1F_Warp_Points.CINNABAR_POKECENTER_1F_TO_CINNABAR_ISLAND_1_WP,
        "CinnabarIsland", unlocks=[Unlock_Keys.FOUND_BLUE]
    )

#######################################################################
#                    Fuchsia Group                                    #
#######################################################################

class Bills_Brothers_House_Links(Enum):

    BILLS_BROTHERS_HOUSE_TO_FUCHSIA_CITY_4_LINK = WarpLink(
        Bills_Brothers_House_Warp_Points.BILLS_BROTHERS_HOUSE_TO_FUCHSIA_CITY_4_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_BILLS_BROTHERS_HOUSE_1_WP,
        "BillsBrothersHouse", dual_width= True
    )

class Fuchsia_Gym_Links(Enum):

    FUCHSIA_GYM_TO_FUCHSIA_CITY_3_LINK = WarpLink(
        Fuchsia_Gym_Warp_Points.FUCHSIA_GYM_TO_FUCHSIA_CITY_3_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_FUCHSIA_GYM_1_WP,
        "FuchsiaGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_13]
    )

class Fuchsia_Mart_Links(Enum):

    FUCHSIA_MART_TO_FUCHSIA_CITY_1_LINK = WarpLink(
        Fuchsia_Mart_Warp_Points.FUCHSIA_MART_TO_FUCHSIA_CITY_1_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_FUCHSIA_MART_2_WP,
        "FuchsiaMart", dual_width= True
    )

class Fuchsia_Pokecenter_1F_Links(Enum):

    FUCHSIA_POKECENTER_1F_TO_FUCHSIA_CITY_5_LINK = WarpLink(
        Fuchsia_Pokecenter_1F_Warp_Points.FUCHSIA_POKECENTER_1F_TO_FUCHSIA_CITY_5_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_FUCHSIA_POKECENTER_1F_1_WP,
        "FuchsiaPokecenter1F", dual_width= True
    )

    FUCHSIA_POKECENTER_1F_TO_POKECENTER_2F_1_LINK = WarpLink(
        Fuchsia_Pokecenter_1F_Warp_Points.FUCHSIA_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "FuchsiaPokecenter1F", 10
    )

class Safari_Zone_Main_Office_Links(Enum):

    SAFARI_ZONE_MAIN_OFFICE_TO_FUCHSIA_CITY_2_LINK = WarpLink(
        Safari_Zone_Main_Office_Warp_Points.SAFARI_ZONE_MAIN_OFFICE_TO_FUCHSIA_CITY_2_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_SAFARI_ZONE_MAIN_OFFICE_1_WP,
        "SafariZoneMainOffice", dual_width= True
    )

class Safari_Zone_Wardens_Home_Links(Enum):

    SAFARI_ZONE_WARDENS_HOME_TO_FUCHSIA_CITY_6_LINK = WarpLink(
        Safari_Zone_Wardens_Home_Warp_Points.SAFARI_ZONE_WARDENS_HOME_TO_FUCHSIA_CITY_6_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_SAFARI_ZONE_WARDENS_HOME_1_WP,
        "SafariZoneWardensHome", dual_width= True
    )


class Fuchsia_City_Links(Enum):

    FUCHSIA_CITY_TO_FUCHSIA_MART_2_LINK = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_FUCHSIA_MART_2_WP,
        Fuchsia_Mart_Warp_Points.FUCHSIA_MART_TO_FUCHSIA_CITY_1_WP,
        "FuchsiaCity"
    )

    FUCHSIA_CITY_TO_SAFARI_ZONE_MAIN_OFFICE_1_LINK = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_SAFARI_ZONE_MAIN_OFFICE_1_WP,
        Safari_Zone_Main_Office_Warp_Points.SAFARI_ZONE_MAIN_OFFICE_TO_FUCHSIA_CITY_2_WP,
        "FuchsiaCity", 5
    )

    FUCHSIA_CITY_TO_FUCHSIA_GYM_1_LINK = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_FUCHSIA_GYM_1_WP,
        Fuchsia_Gym_Warp_Points.FUCHSIA_GYM_TO_FUCHSIA_CITY_3_WP,
        "FuchsiaCity", 10
    )

    FUCHSIA_CITY_TO_BILLS_BROTHERS_HOUSE_1_LINK = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_BILLS_BROTHERS_HOUSE_1_WP,
        Bills_Brothers_House_Warp_Points.BILLS_BROTHERS_HOUSE_TO_FUCHSIA_CITY_4_WP,
        "FuchsiaCity", 15
    )

    FUCHSIA_CITY_TO_FUCHSIA_POKECENTER_1F_1_LINK = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_FUCHSIA_POKECENTER_1F_1_WP,
        Fuchsia_Pokecenter_1F_Warp_Points.FUCHSIA_POKECENTER_1F_TO_FUCHSIA_CITY_5_WP,
        "FuchsiaCity", 20
    )

    FUCHSIA_CITY_TO_SAFARI_ZONE_WARDENS_HOME_1_LINK = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_SAFARI_ZONE_WARDENS_HOME_1_WP,
        Safari_Zone_Wardens_Home_Warp_Points.SAFARI_ZONE_WARDENS_HOME_TO_FUCHSIA_CITY_6_WP,
        "FuchsiaCity", 25
    )

    #fuchsia beta safari zone - inaccessible

    FUCHSIA_CITY_TO_ROUTE_15_FUCHSIA_GATE_1_LINK = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_ROUTE_15_FUCHSIA_GATE_1_WP,
        Route_15_Fuchsia_Gate_Warp_Points.ROUTE_15_FUCHSIA_GATE_TO_FUCHSIA_CITY_8_WP,
        "FuchsiaCity", 35, dual_width= True
    )

    FUCHSIA_CITY_TO_ROUTE_19_FUCHSIA_GATE_1_LINK = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_ROUTE_19_FUCHSIA_GATE_1_WP,
        Route_19_Fuchsia_Gate_Warp_Points.ROUTE_19_FUCHSIA_GATE_TO_FUCHSIA_CITY_10_WP,
        "FuchsiaCity", 45, dual_width= True
    )



#######################################################################
#                    Lavender Group                                   #
#######################################################################

class Lavender_Mart_Links(Enum):

    LAVENDER_MART_TO_LAVENDER_TOWN_5_LINK = WarpLink(
        Lavender_Mart_Warp_Points.LAVENDER_MART_TO_LAVENDER_TOWN_5_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_MART_2_WP,
        "LavenderMart", dual_width= True
    )

class Lavender_Name_Rater_Links(Enum):

    LAVENDER_NAME_RATER_TO_LAVENDER_TOWN_4_LINK = WarpLink(
        Lavender_Name_Rater_Warp_Points.LAVENDER_NAME_RATER_TO_LAVENDER_TOWN_4_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_NAME_RATER_1_WP,
        "LavenderNameRater", dual_width= True
    )

class Lavender_Pokecenter_1F_Links(Enum):

    LAVENDER_POKECENTER_1F_TO_LAVENDER_TOWN_1_LINK = WarpLink(
        Lavender_Pokecenter_1F_Warp_Points.LAVENDER_POKECENTER_1F_TO_LAVENDER_TOWN_1_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_POKECENTER_1F_1_WP,
        "LavenderPokecenter1F", dual_width= True
    )

    LAVENDER_POKECENTER_1F_TO_POKECENTER_2F_1_LINK = WarpLink(
        Lavender_Pokecenter_1F_Warp_Points.LAVENDER_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "LavenderPokecenter1F", 10
    )

class Lavender_Speech_House_Links(Enum):

    LAVENDER_SPEECH_HOUSE_TO_LAVENDER_TOWN_3_LINK = WarpLink(
        Lavender_Speech_House_Warp_Points.LAVENDER_SPEECH_HOUSE_TO_LAVENDER_TOWN_3_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_SPEECH_HOUSE_1_WP,
        "LavenderSpeechHouse", dual_width= True
    )

class Lav_Radio_Tower_1F_Links(Enum):

    LAV_RADIO_TOWER_1F_TO_LAVENDER_TOWN_7_LINK = WarpLink(
        Lav_Radio_Tower_1F_Warp_Points.LAV_RADIO_TOWER_1F_TO_LAVENDER_TOWN_7_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAV_RADIO_TOWER_1F_1_WP,
        "LavRadioTower1F", dual_width= True, unlocks=[Unlock_Keys.EXPN_CARD],
        locked_by=[Unlock_Keys.MACHINE_PART]
    )

class Mr_Fujis_House_Links(Enum):

    MR_FUJIS_HOUSE_TO_LAVENDER_TOWN_2_LINK = WarpLink(
        Mr_Fujis_House_Warp_Points.MR_FUJIS_HOUSE_TO_LAVENDER_TOWN_2_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_MR_FUJIS_HOUSE_1_WP,
        "MrFujisHouse", dual_width= True
    )

class Soul_House_Links(Enum):

    SOUL_HOUSE_TO_LAVENDER_TOWN_6_LINK = WarpLink(
        Soul_House_Warp_Points.SOUL_HOUSE_TO_LAVENDER_TOWN_6_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_SOUL_HOUSE_1_WP,
        "SoulHouse", dual_width= True
    )

class Lavender_Town_Links(Enum):

    LAVENDER_TOWN_TO_LAVENDER_POKECENTER_1F_1_LINK = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_POKECENTER_1F_1_WP,
        Lavender_Pokecenter_1F_Warp_Points.LAVENDER_POKECENTER_1F_TO_LAVENDER_TOWN_1_WP,
        "LavenderTown"
    )

    LAVENDER_TOWN_TO_MR_FUJIS_HOUSE_1_LINK = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_MR_FUJIS_HOUSE_1_WP,
        Mr_Fujis_House_Warp_Points.MR_FUJIS_HOUSE_TO_LAVENDER_TOWN_2_WP,
        "LavenderTown", 5
    )

    LAVENDER_TOWN_TO_LAVENDER_SPEECH_HOUSE_1_LINK = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_SPEECH_HOUSE_1_WP,
        Lavender_Speech_House_Warp_Points.LAVENDER_SPEECH_HOUSE_TO_LAVENDER_TOWN_3_WP,
        "LavenderTown", 10
    )

    LAVENDER_TOWN_TO_LAVENDER_NAME_RATER_1_LINK = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_NAME_RATER_1_WP,
        Lavender_Name_Rater_Warp_Points.LAVENDER_NAME_RATER_TO_LAVENDER_TOWN_4_WP,
        "LavenderTown", 15
    )

    LAVENDER_TOWN_TO_LAVENDER_MART_2_LINK = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_MART_2_WP,
        Lavender_Mart_Warp_Points.LAVENDER_MART_TO_LAVENDER_TOWN_5_WP,
        "LavenderTown", 20
    )

    LAVENDER_TOWN_TO_SOUL_HOUSE_1_LINK = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_SOUL_HOUSE_1_WP,
        Soul_House_Warp_Points.SOUL_HOUSE_TO_LAVENDER_TOWN_6_WP,
        "LavenderTown", 25
    )

    LAVENDER_TOWN_TO_LAV_RADIO_TOWER_1F_1_LINK = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAV_RADIO_TOWER_1F_1_WP,
        Lav_Radio_Tower_1F_Warp_Points.LAV_RADIO_TOWER_1F_TO_LAVENDER_TOWN_7_WP,
        "LavenderTown", 30
    )

#######################################################################
#                    Pallet Group                                     #
#######################################################################

class Blues_House_Links(Enum):

    BLUES_HOUSE_TO_PALLET_TOWN_2_LINK = WarpLink(
        Blues_House_Warp_Points.BLUES_HOUSE_TO_PALLET_TOWN_2_WP,
        Pallet_Town_Warp_Points.PALLET_TOWN_TO_BLUES_HOUSE_1_WP,
        "BluesHouse", dual_width= True
    )

class Oaks_Lab_Links(Enum):

    OAKS_LAB_TO_PALLET_TOWN_3_LINK = WarpLink(
        Oaks_Lab_Warp_Points.OAKS_LAB_TO_PALLET_TOWN_3_WP,
        Pallet_Town_Warp_Points.PALLET_TOWN_TO_OAKS_LAB_1_WP,
        "OaksLab", dual_width= True, unlocks=[Unlock_Keys.OAKS_LAB_ACCESS]
    )

class Reds_House_1F_Links(Enum):

    REDS_HOUSE_1F_TO_PALLET_TOWN_1_LINK = WarpLink(
        Reds_House_1F_Warp_Points.REDS_HOUSE_1F_TO_PALLET_TOWN_1_WP,
        Pallet_Town_Warp_Points.PALLET_TOWN_TO_REDS_HOUSE_1F_1_WP,
        "RedsHouse1F", dual_width= True
    )

    REDS_HOUSE_1F_TO_REDS_HOUSE_2F_1_LINK = WarpLink(
        Reds_House_1F_Warp_Points.REDS_HOUSE_1F_TO_REDS_HOUSE_2F_1_WP,
        Reds_House_2F_Warp_Points.REDS_HOUSE_2F_TO_REDS_HOUSE_1F_3_WP,
        "RedsHouse1F", 10
    )

class Reds_House_2F_Links(Enum):

    REDS_HOUSE_2F_TO_REDS_HOUSE_1F_3_LINK = WarpLink(
        Reds_House_2F_Warp_Points.REDS_HOUSE_2F_TO_REDS_HOUSE_1F_3_WP,
        Reds_House_1F_Warp_Points.REDS_HOUSE_1F_TO_REDS_HOUSE_2F_1_WP,
        "RedsHouse2F"
    )

class Pallet_Town_Links(Enum):

    PALLET_TOWN_TO_REDS_HOUSE_1F_1_LINK = WarpLink(
        Pallet_Town_Warp_Points.PALLET_TOWN_TO_REDS_HOUSE_1F_1_WP,
        Reds_House_1F_Warp_Points.REDS_HOUSE_1F_TO_PALLET_TOWN_1_WP,
        "PalletTown"
    )

    PALLET_TOWN_TO_BLUES_HOUSE_1_LINK = WarpLink(
        Pallet_Town_Warp_Points.PALLET_TOWN_TO_BLUES_HOUSE_1_WP,
        Blues_House_Warp_Points.BLUES_HOUSE_TO_PALLET_TOWN_2_WP,
        "PalletTown", 5
    )

    PALLET_TOWN_TO_OAKS_LAB_1_LINK = WarpLink(
        Pallet_Town_Warp_Points.PALLET_TOWN_TO_OAKS_LAB_1_WP,
        Oaks_Lab_Warp_Points.OAKS_LAB_TO_PALLET_TOWN_3_WP,
        "PalletTown", 10
    )


#######################################################################
#                    Pewter Group                                     #
#######################################################################

class Pewter_Gym_Links(Enum):

    PEWTER_GYM_TO_PEWTER_CITY_2_LINK = WarpLink(
        Pewter_Gym_Warp_Points.PEWTER_GYM_TO_PEWTER_CITY_2_WP,
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_GYM_1_WP,
        "PewterGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_14]
    )

class Pewter_Mart_Links(Enum):

    PEWTER_MART_TO_PEWTER_CITY_3_LINK = WarpLink(
        Pewter_Mart_Warp_Points.PEWTER_MART_TO_PEWTER_CITY_3_WP,
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_MART_2_WP,
        "PewterMart", dual_width= True
    )

class Pewter_Nidoran_Speech_House_Links(Enum):

    PEWTER_NIDORAN_SPEECH_HOUSE_TO_PEWTER_CITY_1_LINK = WarpLink(
        Pewter_Nidoran_Speech_House_Warp_Points.PEWTER_NIDORAN_SPEECH_HOUSE_TO_PEWTER_CITY_1_WP,
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_NIDORAN_SPEECH_HOUSE_1_WP,
        "PewterNidoranSpeechHouse", dual_width= True
    )

class Pewter_Snooze_Speech_House_Links(Enum):

    PEWTER_SNOOZE_SPEECH_HOUSE_TO_PEWTER_CITY_5_LINK = WarpLink(
        Pewter_Snooze_Speech_House_Warp_Points.PEWTER_SNOOZE_SPEECH_HOUSE_TO_PEWTER_CITY_5_WP,
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_SNOOZE_SPEECH_HOUSE_1_WP,
        "PewterSnoozeSpeechHouse", dual_width= True
    )

class Pewter_Pokecenter_1F_Links(Enum):

    PEWTER_POKECENTER_1F_TO_PEWTER_CITY_4_LINK = WarpLink(
        Pewter_Pokecenter_1F_Warp_Points.PEWTER_POKECENTER_1F_TO_PEWTER_CITY_4_WP,
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_POKECENTER_1F_1_WP,
        "PewterPokecenter1F", dual_width= True
    )

    PEWTER_POKECENTER_1F_TO_POKECENTER_2F_1_LINK = WarpLink(
        Pewter_Pokecenter_1F_Warp_Points.PEWTER_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "PewterPokecenter1F", 10
    )

class Pewter_City_Links(Enum):

    PEWTER_CITY_TO_PEWTER_NIDORAN_SPEECH_HOUSE_1_LINK = WarpLink(
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_NIDORAN_SPEECH_HOUSE_1_WP,
        Pewter_Nidoran_Speech_House_Warp_Points.PEWTER_NIDORAN_SPEECH_HOUSE_TO_PEWTER_CITY_1_WP,
        "PewterCity"
    )

    PEWTER_CITY_TO_PEWTER_GYM_1_LINK = WarpLink(
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_GYM_1_WP,
        Pewter_Gym_Warp_Points.PEWTER_GYM_TO_PEWTER_CITY_2_WP,
        "PewterCity", 5
    )

    PEWTER_CITY_TO_PEWTER_MART_2_LINK = WarpLink(
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_MART_2_WP,
        Pewter_Mart_Warp_Points.PEWTER_MART_TO_PEWTER_CITY_3_WP,
        "PewterCity", 10
    )

    PEWTER_CITY_TO_PEWTER_POKECENTER_1F_1_LINK = WarpLink(
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_POKECENTER_1F_1_WP,
        Pewter_Pokecenter_1F_Warp_Points.PEWTER_POKECENTER_1F_TO_PEWTER_CITY_4_WP,
        "PewterCity", 15
    )

    PEWTER_CITY_TO_PEWTER_SNOOZE_SPEECH_HOUSE_1_LINK = WarpLink(
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_SNOOZE_SPEECH_HOUSE_1_WP,
        Pewter_Snooze_Speech_House_Warp_Points.PEWTER_SNOOZE_SPEECH_HOUSE_TO_PEWTER_CITY_5_WP,
        "PewterCity", 20
    )


#######################################################################
#                    Saffron Group                                    #
#######################################################################

class Copycats_House_1F_Links(Enum):

    COPYCATS_HOUSE_1F_TO_SAFFRON_CITY_8_LINK = WarpLink(
        Copycats_House_1F_Warp_Points.COPYCATS_HOUSE_1F_TO_SAFFRON_CITY_8_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_COPYCATS_HOUSE_1F_1_WP,
        "CopycatsHouse1F", dual_width= True
    )

    COPYCATS_HOUSE_1F_TO_COPYCATS_HOUSE_2F_1_LINK = WarpLink(
        Copycats_House_1F_Warp_Points.COPYCATS_HOUSE_1F_TO_COPYCATS_HOUSE_2F_1_WP,
        Copycats_House_2F_Warp_Points.COPYCATS_HOUSE_2F_TO_COPYCATS_HOUSE_1F_3_WP,
        "CopycatsHouse1F", 10
    )

class Copycats_House_2F_Links(Enum):

    COPYCATS_HOUSE_2F_TO_COPYCATS_HOUSE_1F_3_LINK = WarpLink(
        Copycats_House_2F_Warp_Points.COPYCATS_HOUSE_2F_TO_COPYCATS_HOUSE_1F_3_WP,
        Copycats_House_1F_Warp_Points.COPYCATS_HOUSE_1F_TO_COPYCATS_HOUSE_2F_1_WP,
        "CopycatsHouse2F"
    )

class Fighting_Dojo_Links(Enum):

    FIGHTING_DOJO_TO_SAFFRON_CITY_1_LINK = WarpLink(
        Fighting_Dojo_Warp_Points.FIGHTING_DOJO_TO_SAFFRON_CITY_1_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_FIGHTING_DOJO_1_WP,
        "FightingDojo", dual_width= True
    )

class Mr_Psychics_House_Links(Enum):

    MR_PSYCHICS_HOUSE_TO_SAFFRON_CITY_5_LINK = WarpLink(
        Mr_Psychics_House_Warp_Points.MR_PSYCHICS_HOUSE_TO_SAFFRON_CITY_5_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_MR_PSYCHICS_HOUSE_1_WP,
        "MrPsychicsHouse", dual_width= True
    )


# <here> warps in gym randomizable too if needed


class Saffron_Gym_Links(Enum): 

    SAFFRON_GYM_TO_SAFFRON_CITY_2_LINK = WarpLink(
        Saffron_Gym_Warp_Points.SAFFRON_GYM_TO_SAFFRON_CITY_2_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_GYM_1_WP,
        "SaffronGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_10]
    )

class Saffron_Magnet_Train_Station_Links(Enum):

    SAFFRON_MAGNET_TRAIN_STATION_TO_SAFFRON_CITY_6_LINK = WarpLink(
        Saffron_Magnet_Train_Station_Warp_Points.SAFFRON_MAGNET_TRAIN_STATION_TO_SAFFRON_CITY_6_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_MAGNET_TRAIN_STATION_2_WP,
        "SaffronMagnetTrainStation", dual_width= True
    )

#We don't randomize magnet train
    #SAFFRON_MAGNET_TRAIN_STATION_TO_GOLDENROD_MAGNET_TRAIN_STATION_4_LINK = WarpLink(
    #    Saffron_Magnet_Train_Station_Warp_Points.SAFFRON_MAGNET_TRAIN_STATION_TO_GOLDENROD_MAGNET_TRAIN_STATION_4_WP,
    #    Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_CAFE_1_WP,
    #    "SaffronMagnetTrainStation", 10, dual_width= True
    #)

class Saffron_Mart_Links(Enum):

    SAFFRON_MART_TO_SAFFRON_CITY_3_LINK = WarpLink(
        Saffron_Mart_Warp_Points.SAFFRON_MART_TO_SAFFRON_CITY_3_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_MART_2_WP,
        "SaffronMart", dual_width= True
    )

class Saffron_Pokecenter_1F_Links(Enum):

    SAFFRON_POKECENTER_1F_TO_SAFFRON_CITY_4_LINK = WarpLink(
        Saffron_Pokecenter_1F_Warp_Points.SAFFRON_POKECENTER_1F_TO_SAFFRON_CITY_4_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_POKECENTER_1F_1_WP,
        "SaffronPokecenter1F", dual_width= True
    )

    SAFFRON_POKECENTER_1F_TO_POKECENTER_2F_1_LINK = WarpLink(
        Saffron_Pokecenter_1F_Warp_Points.SAFFRON_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "SaffronPokecenter1F", 10
    )

class Silph_Co_1F_Links(Enum):

    SILPH_CO_1F_TO_SAFFRON_CITY_7_LINK = WarpLink(
        Silph_Co_1F_Warp_Points.SILPH_CO_1F_TO_SAFFRON_CITY_7_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SILPH_CO_1F_1_WP,
        "SilphCo1F", dual_width= True
    )

class Saffron_City_Links(Enum):

    SAFFRON_CITY_TO_FIGHTING_DOJO_1_LINK = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_FIGHTING_DOJO_1_WP,
        Fighting_Dojo_Warp_Points.FIGHTING_DOJO_TO_SAFFRON_CITY_1_WP,
        "SaffronCity"
    )

    SAFFRON_CITY_TO_SAFFRON_GYM_1_LINK = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_GYM_1_WP,
        Saffron_Gym_Warp_Points.SAFFRON_GYM_TO_SAFFRON_CITY_2_WP,
        "SaffronCity", 5
    )

    SAFFRON_CITY_TO_SAFFRON_MART_2_LINK = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_MART_2_WP,
        Saffron_Mart_Warp_Points.SAFFRON_MART_TO_SAFFRON_CITY_3_WP,
        "SaffronCity", 10
    )

    SAFFRON_CITY_TO_SAFFRON_POKECENTER_1F_1_LINK = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_POKECENTER_1F_1_WP,
        Saffron_Pokecenter_1F_Warp_Points.SAFFRON_POKECENTER_1F_TO_SAFFRON_CITY_4_WP,
        "SaffronCity", 15
    )

    SAFFRON_CITY_TO_MR_PSYCHICS_HOUSE_1_LINK = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_MR_PSYCHICS_HOUSE_1_WP,
        Mr_Psychics_House_Warp_Points.MR_PSYCHICS_HOUSE_TO_SAFFRON_CITY_5_WP,
        "SaffronCity", 20
    )

    SAFFRON_CITY_TO_SAFFRON_MAGNET_TRAIN_STATION_2_LINK = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_MAGNET_TRAIN_STATION_2_WP,
        Saffron_Magnet_Train_Station_Warp_Points.SAFFRON_MAGNET_TRAIN_STATION_TO_SAFFRON_CITY_6_WP,
        "SaffronCity", 25
    )

    SAFFRON_CITY_TO_SILPH_CO_1F_1_LINK = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SILPH_CO_1F_1_WP,
        Silph_Co_1F_Warp_Points.SILPH_CO_1F_TO_SAFFRON_CITY_7_WP,
        "SaffronCity", 30
    )

    SAFFRON_CITY_TO_COPYCATS_HOUSE_1F_1_LINK = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_COPYCATS_HOUSE_1F_1_WP,
        Copycats_House_1F_Warp_Points.COPYCATS_HOUSE_1F_TO_SAFFRON_CITY_8_WP,
        "SaffronCity", 35
    )

    SAFFRON_CITY_TO_ROUTE_5_SAFFRON_GATE_3_LINK = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_5_SAFFRON_GATE_3_WP,
        Route_5_Saffron_Gate_Warp_Points.ROUTE_5_SAFFRON_GATE_TO_SAFFRON_CITY_9_WP,
        "SaffronCity", 40
    )

    SAFFRON_CITY_TO_ROUTE_7_SAFFRON_GATE_3_LINK = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_7_SAFFRON_GATE_3_WP,
        Route_7_Saffron_Gate_Warp_Points.ROUTE_7_SAFFRON_GATE_TO_SAFFRON_CITY_10_WP,
        "SaffronCity", 45, dual_width= True
    )

    SAFFRON_CITY_TO_ROUTE_6_SAFFRON_GATE_1_LINK = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_6_SAFFRON_GATE_1_WP,
        Route_6_Saffron_Gate_Warp_Points.ROUTE_6_SAFFRON_GATE_TO_SAFFRON_CITY_12_WP,
        "SaffronCity", 55, dual_width= True
    )

    SAFFRON_CITY_TO_ROUTE_8_SAFFRON_GATE_1_LINK = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_8_SAFFRON_GATE_1_WP,
        Route_8_Saffron_Gate_Warp_Points.ROUTE_8_SAFFRON_GATE_TO_SAFFRON_CITY_14_WP,
        "SaffronCity", 65, dual_width= True
    )
    

#######################################################################
#                    Vermillion Group                                 #
#######################################################################

class Pokemon_Fan_Club_Links(Enum):

    POKEMON_FAN_CLUB_TO_VERMILION_CITY_3_LINK = WarpLink(
        Pokemon_Fan_Club_Warp_Points.POKEMON_FAN_CLUB_TO_VERMILION_CITY_3_WP,
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_POKEMON_FAN_CLUB_1_WP,
        "PokemonFanClub", dual_width= True
    )

class Vermilion_Digletts_Cave_Speech_House_Links(Enum):

    VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_TO_VERMILION_CITY_6_LINK = WarpLink(
        Vermilion_Digletts_Cave_Speech_House_Warp_Points.VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_TO_VERMILION_CITY_6_WP,
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_1_WP,
        "VermilionDiglettsCaveSpeechHouse", dual_width= True
    )

class Vermilion_Fishing_Speech_House_Links(Enum):

    VERMILION_FISHING_SPEECH_HOUSE_TO_VERMILION_CITY_1_LINK = WarpLink(
        Vermilion_Fishing_Speech_House_Warp_Points.VERMILION_FISHING_SPEECH_HOUSE_TO_VERMILION_CITY_1_WP,
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_FISHING_SPEECH_HOUSE_1_WP,
        "VermilionFishingSpeechHouse", dual_width= True
    )

class Vermilion_Gym_Links(Enum):

    VERMILION_GYM_TO_VERMILION_CITY_7_LINK = WarpLink(
        Vermilion_Gym_Warp_Points.VERMILION_GYM_TO_VERMILION_CITY_7_WP,
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_GYM_1_WP,
        "VermilionGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_9]
    )

class Vermilion_Magnet_Train_Speech_House_Links(Enum):

    VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_TO_VERMILION_CITY_4_LINK = WarpLink(
        Vermilion_Magnet_Train_Speech_House_Warp_Points.VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_TO_VERMILION_CITY_4_WP,
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_1_WP,
        "VermilionMagnetTrainSpeechHouse", dual_width= True
    )

class Vermilion_Mart_Links(Enum):

    VERMILION_MART_TO_VERMILION_CITY_5_LINK = WarpLink(
        Vermilion_Mart_Warp_Points.VERMILION_MART_TO_VERMILION_CITY_5_WP,
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_MART_2_WP,
        "VermilionMart", dual_width= True
    )

class Vermilion_Pokecenter_1F_Links(Enum):

    VERMILION_POKECENTER_1F_TO_VERMILION_CITY_2_LINK = WarpLink(
        Vermilion_Pokecenter_1F_Warp_Points.VERMILION_POKECENTER_1F_TO_VERMILION_CITY_2_WP,
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_POKECENTER_1F_1_WP,
        "VermilionPokecenter1F", dual_width= True
    )

    VERMILION_POKECENTER_1F_TO_POKECENTER_2F_1_LINK = WarpLink(
        Vermilion_Pokecenter_1F_Warp_Points.VERMILION_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "VermilionPokecenter1F", 10
    )

class Vermilion_Port_Links(Enum):

    VERMILION_PORT_TO_VERMILION_PORT_PASSAGE_5_LINK = WarpLink(
        Vermilion_Port_Warp_Points.VERMILION_PORT_TO_VERMILION_PORT_PASSAGE_5_WP,
        Vermilion_Port_Passage_Warp_Points.VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_1_WP,
        "VermilionPort"
    )

#We dont randomize ship entrance/exit
    #VERMILION_PORT_TO_FAST_SHIP_1F_1_LINK = WarpLink(
    #    Vermilion_Port_Warp_Points.VERMILION_PORT_TO_FAST_SHIP_1F_1_WP,
    #    Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_POKECENTER_1F_1_WP,
    #    "VermilionPort", 5
    #)


class Vermilion_Port_Passage_Links(Enum): # 1-3,4-5

    VERMILION_PORT_PASSAGE_TO_VERMILION_CITY_8_LINK = WarpLink(
        Vermilion_Port_Passage_Warp_Points.VERMILION_PORT_PASSAGE_TO_VERMILION_CITY_8_WP,
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_PORT_PASSAGE_1_WP,
        "VermilionPortPassage", dual_width= True
    )

    VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_PASSAGE_4_LINK = WarpLink(
        Vermilion_Port_Passage_Warp_Points.VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_PASSAGE_4_WP,
        Vermilion_Port_Passage_Warp_Points.VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_PASSAGE_3_WP,
        "VermilionPortPassage", 10
    )

    VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_PASSAGE_3_LINK = WarpLink(
        Vermilion_Port_Passage_Warp_Points.VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_PASSAGE_3_WP,
        Vermilion_Port_Passage_Warp_Points.VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_PASSAGE_4_WP,
        "VermilionPortPassage", 15
    )

    VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_1_LINK = WarpLink(
        Vermilion_Port_Passage_Warp_Points.VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_1_WP,
        Vermilion_Port_Warp_Points.VERMILION_PORT_TO_VERMILION_PORT_PASSAGE_5_WP,
        "VermilionPortPassage", 20
    )



class Vermilion_City_Links(Enum):

    VERMILION_CITY_TO_VERMILION_FISHING_SPEECH_HOUSE_1_LINK = WarpLink(
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_FISHING_SPEECH_HOUSE_1_WP,
        Vermilion_Fishing_Speech_House_Warp_Points.VERMILION_FISHING_SPEECH_HOUSE_TO_VERMILION_CITY_1_WP,
        "VermilionCity"
    )

    VERMILION_CITY_TO_VERMILION_POKECENTER_1F_1_LINK = WarpLink(
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_POKECENTER_1F_1_WP,
        Vermilion_Pokecenter_1F_Warp_Points.VERMILION_POKECENTER_1F_TO_VERMILION_CITY_2_WP,
        "VermilionCity", 5
    )

    VERMILION_CITY_TO_POKEMON_FAN_CLUB_1_LINK = WarpLink(
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_POKEMON_FAN_CLUB_1_WP,
        Pokemon_Fan_Club_Warp_Points.POKEMON_FAN_CLUB_TO_VERMILION_CITY_3_WP,
        "VermilionCity", 10
    )

    VERMILION_CITY_TO_VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_1_LINK = WarpLink(
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_1_WP,
        Vermilion_Magnet_Train_Speech_House_Warp_Points.VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_TO_VERMILION_CITY_4_WP,
        "VermilionCity", 15
    )

    VERMILION_CITY_TO_VERMILION_MART_2_LINK = WarpLink(
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_MART_2_WP,
        Vermilion_Mart_Warp_Points.VERMILION_MART_TO_VERMILION_CITY_5_WP,
        "VermilionCity", 20
    )

    VERMILION_CITY_TO_VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_1_LINK = WarpLink(
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_1_WP,
        Vermilion_Digletts_Cave_Speech_House_Warp_Points.VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_TO_VERMILION_CITY_6_WP,
        "VermilionCity", 25
    )

    VERMILION_CITY_TO_VERMILION_GYM_1_LINK = WarpLink(
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_GYM_1_WP,
        Vermilion_Gym_Warp_Points.VERMILION_GYM_TO_VERMILION_CITY_7_WP,
        "VermilionCity", 30, locked_by=[Unlock_Keys.CAN_SURF_OR_CUT]
    )

    VERMILION_CITY_TO_VERMILION_PORT_PASSAGE_1_LINK = WarpLink(
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_PORT_PASSAGE_1_WP,
        Vermilion_Port_Passage_Warp_Points.VERMILION_PORT_PASSAGE_TO_VERMILION_CITY_8_WP,
        "VermilionCity", 35, dual_width= True
    )

    VERMILION_CITY_TO_DIGLETTS_CAVE_1_LINK = WarpLink(
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_DIGLETTS_CAVE_1_WP,
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_VERMILION_CITY_10_WP,
        "VermilionCity", 45, locked_by=[Unlock_Keys.EXPN_CARD, Unlock_Keys.RADIO_CARD]
    )
    

#######################################################################
#                    Viridian Group                                   #
#######################################################################

class Route_2_Nugget_House_Links(Enum):

    ROUTE_2_NUGGET_HOUSE_TO_ROUTE_2_1_LINK = WarpLink(
        Route_2_Nugget_House_Warp_Points.ROUTE_2_NUGGET_HOUSE_TO_ROUTE_2_1_WP,
        Route_2_Warp_Points.ROUTE_2_TO_ROUTE_2_NUGGET_HOUSE_1_WP,
        "Route2NuggetHouse", dual_width= True
    )

class Trainer_House_1F_Links(Enum):

    TRAINER_HOUSE_1F_TO_VIRIDIAN_CITY_3_LINK = WarpLink(
        Trainer_House_1F_Warp_Points.TRAINER_HOUSE_1F_TO_VIRIDIAN_CITY_3_WP,
        Viridian_City_Warp_Points.VIRIDIAN_CITY_TO_TRAINER_HOUSE_1F_1_WP,
        "TrainerHouse1F", dual_width= True
    )

    TRAINER_HOUSE_1F_TO_TRAINER_HOUSE_B1F_1_LINK = WarpLink(
        Trainer_House_1F_Warp_Points.TRAINER_HOUSE_1F_TO_TRAINER_HOUSE_B1F_1_WP,
        Trainer_House_B1F_Warp_Points.TRAINER_HOUSE_B1F_TO_TRAINER_HOUSE_1F_3_WP,
        "TrainerHouse1F", 10
    )

class Trainer_House_B1F_Links(Enum):

    TRAINER_HOUSE_B1F_TO_TRAINER_HOUSE_1F_3_LINK = WarpLink(
        Trainer_House_B1F_Warp_Points.TRAINER_HOUSE_B1F_TO_TRAINER_HOUSE_1F_3_WP,
        Trainer_House_1F_Warp_Points.TRAINER_HOUSE_1F_TO_TRAINER_HOUSE_B1F_1_WP,
        "TrainerHouseB1F"
    )

class Viridian_Gym_Links(Enum):

    VIRIDIAN_GYM_TO_VIRIDIAN_CITY_1_LINK = WarpLink(
        Viridian_Gym_Warp_Points.VIRIDIAN_GYM_TO_VIRIDIAN_CITY_1_WP,
        Viridian_City_Warp_Points.VIRIDIAN_CITY_TO_VIRIDIAN_GYM_1_WP,
        "ViridianGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_16],
        locked_by=[Unlock_Keys.FOUND_BLUE]
    )

class Viridian_Mart_Links(Enum):

    VIRIDIAN_MART_TO_VIRIDIAN_CITY_4_LINK = WarpLink(
        Viridian_Mart_Warp_Points.VIRIDIAN_MART_TO_VIRIDIAN_CITY_4_WP,
        Viridian_City_Warp_Points.VIRIDIAN_CITY_TO_VIRIDIAN_MART_2_WP,
        "ViridianMart", dual_width= True
    )

class Viridian_Nickname_Speech_House_Links(Enum):

    VIRIDIAN_NICKNAME_SPEECH_HOUSE_TO_VIRIDIAN_CITY_2_LINK = WarpLink(
        Viridian_Nickname_Speech_House_Warp_Points.VIRIDIAN_NICKNAME_SPEECH_HOUSE_TO_VIRIDIAN_CITY_2_WP,
        Viridian_City_Warp_Points.VIRIDIAN_CITY_TO_VIRIDIAN_NICKNAME_SPEECH_HOUSE_1_WP,
        "ViridianNicknameSpeechHouse", dual_width= True
    )

class Viridian_Pokecenter_1F_Links(Enum):

    VIRIDIAN_POKECENTER_1F_TO_VIRIDIAN_CITY_5_LINK = WarpLink(
        Viridian_Pokecenter_1F_Warp_Points.VIRIDIAN_POKECENTER_1F_TO_VIRIDIAN_CITY_5_WP,
        Viridian_City_Warp_Points.VIRIDIAN_CITY_TO_VIRIDIAN_POKECENTER_1F_1_WP,
        "ViridianPokecenter1F", dual_width= True
    )

    VIRIDIAN_POKECENTER_1F_TO_POKECENTER_2F_1_LINK = WarpLink(
        Viridian_Pokecenter_1F_Warp_Points.VIRIDIAN_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "ViridianPokecenter1F", 10
    )

class Viridian_City_Links(Enum):

    VIRIDIAN_CITY_TO_VIRIDIAN_GYM_1_LINK = WarpLink(
        Viridian_City_Warp_Points.VIRIDIAN_CITY_TO_VIRIDIAN_GYM_1_WP,
        Viridian_Gym_Warp_Points.VIRIDIAN_GYM_TO_VIRIDIAN_CITY_1_WP,
        "ViridianCity"
    )

    VIRIDIAN_CITY_TO_VIRIDIAN_NICKNAME_SPEECH_HOUSE_1_LINK = WarpLink(
        Viridian_City_Warp_Points.VIRIDIAN_CITY_TO_VIRIDIAN_NICKNAME_SPEECH_HOUSE_1_WP,
        Viridian_Nickname_Speech_House_Warp_Points.VIRIDIAN_NICKNAME_SPEECH_HOUSE_TO_VIRIDIAN_CITY_2_WP,
        "ViridianCity", 5
    )

    VIRIDIAN_CITY_TO_TRAINER_HOUSE_1F_1_LINK = WarpLink(
        Viridian_City_Warp_Points.VIRIDIAN_CITY_TO_TRAINER_HOUSE_1F_1_WP,
        Trainer_House_1F_Warp_Points.TRAINER_HOUSE_1F_TO_VIRIDIAN_CITY_3_WP,
        "ViridianCity", 10
    )

    VIRIDIAN_CITY_TO_VIRIDIAN_MART_2_LINK = WarpLink(
        Viridian_City_Warp_Points.VIRIDIAN_CITY_TO_VIRIDIAN_MART_2_WP,
        Viridian_Mart_Warp_Points.VIRIDIAN_MART_TO_VIRIDIAN_CITY_4_WP,
        "ViridianCity", 15
    )

    VIRIDIAN_CITY_TO_VIRIDIAN_POKECENTER_1F_1_LINK = WarpLink(
        Viridian_City_Warp_Points.VIRIDIAN_CITY_TO_VIRIDIAN_POKECENTER_1F_1_WP,
        Viridian_Pokecenter_1F_Warp_Points.VIRIDIAN_POKECENTER_1F_TO_VIRIDIAN_CITY_5_WP,
        "ViridianCity", 20
    )



#######################################################################
#                    Kanto_Dungeons Group                             #
#######################################################################


class Digletts_Cave_Links(Enum): # 1-2,3-4,5-6

    DIGLETTS_CAVE_TO_VERMILION_CITY_10_LINK = WarpLink(
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_VERMILION_CITY_10_WP,
        Vermilion_City_Warp_Points.VERMILION_CITY_TO_DIGLETTS_CAVE_1_WP,
        "DiglettsCave"
    )

    DIGLETTS_CAVE_TO_DIGLETTS_CAVE_5_LINK = WarpLink(
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_5_WP,
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_2_WP,
        "DiglettsCave", 5
    )

    DIGLETTS_CAVE_TO_ROUTE_2_5_LINK = WarpLink(
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_ROUTE_2_5_WP,
        Route_2_Warp_Points.ROUTE_2_TO_DIGLETTS_CAVE_3_WP,
        "DiglettsCave", 10
    )

    DIGLETTS_CAVE_TO_DIGLETTS_CAVE_6_LINK = WarpLink(
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_6_WP,
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_4_WP,
        "DiglettsCave", 15
    )

    DIGLETTS_CAVE_TO_DIGLETTS_CAVE_2_LINK = WarpLink(
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_2_WP,
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_5_WP,
        "DiglettsCave", 20
    )

    DIGLETTS_CAVE_TO_DIGLETTS_CAVE_4_LINK = WarpLink(
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_4_WP,
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_6_WP,
        "DiglettsCave", 25
    )



class Mount_Moon_Gift_Shop_Links(Enum):

    MOUNT_MOON_TO_ROUTE_3_1_LINK = WarpLink(
        Mount_Moon_Gift_Shop_Warp_Points.MOUNT_MOON_GIFT_SHOP_TO_MOUNT_MOON_SQUARE_3_WP,
        Mount_Moon_Square_Warp_Points.MOUNT_MOON_SQUARE_TO_MOUNT_MOON_GIFT_SHOP_1_WP,
        "MountMoonGiftShop", dual_width= True
    )


class Mount_Moon_Links(Enum): # 1-2-3 hub, 4 ledge, 5-7, 6-8

    MOUNT_MOON_TO_ROUTE_3_1_LINK = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_ROUTE_3_1_WP,
        Route_3_Warp_Points.ROUTE_3_TO_MOUNT_MOON_1_WP,
        "MountMoon"
    )

    MOUNT_MOON_TO_ROUTE_4_1_LINK = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_ROUTE_4_1_WP,
        Route_4_Warp_Points.ROUTE_4_TO_MOUNT_MOON_2_WP,
        "MountMoon", 5
    )

    MOUNT_MOON_TO_MOUNT_MOON_7_LINK = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_7_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_3_WP,
        "MountMoon", 10
    )

    MOUNT_MOON_TO_MOUNT_MOON_8_LINK = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_8_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_4_WP,
        "MountMoon", 15
    )

    MOUNT_MOON_TO_MOUNT_MOON_SQUARE_1_LINK = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_SQUARE_1_WP,
        Mount_Moon_Square_Warp_Points.MOUNT_MOON_SQUARE_TO_MOUNT_MOON_5_WP,
        "MountMoon", 20
    )

    MOUNT_MOON_TO_MOUNT_MOON_SQUARE_2_LINK = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_SQUARE_2_WP,
        Mount_Moon_Square_Warp_Points.MOUNT_MOON_SQUARE_TO_MOUNT_MOON_6_WP,
        "MountMoon", 25
    )

    MOUNT_MOON_TO_MOUNT_MOON_3_LINK = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_3_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_7_WP,
        "MountMoon", 30
    )

    MOUNT_MOON_TO_MOUNT_MOON_4_LINK = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_4_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_8_WP,
        "MountMoon", 35
    )


class Mount_Moon_Square_Links(Enum):

    MOUNT_MOON_SQUARE_TO_MOUNT_MOON_5_LINK = WarpLink(
        Mount_Moon_Square_Warp_Points.MOUNT_MOON_SQUARE_TO_MOUNT_MOON_5_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_SQUARE_1_WP,
        "MountMoonSquare"
    )

    MOUNT_MOON_SQUARE_TO_MOUNT_MOON_6_LINK = WarpLink(
        Mount_Moon_Square_Warp_Points.MOUNT_MOON_SQUARE_TO_MOUNT_MOON_6_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_SQUARE_2_WP,
        "MountMoonSquare", 5
    )

    MOUNT_MOON_SQUARE_TO_MOUNT_MOON_GIFT_SHOP_1_LINK = WarpLink(
        Mount_Moon_Square_Warp_Points.MOUNT_MOON_SQUARE_TO_MOUNT_MOON_GIFT_SHOP_1_WP,
        Mount_Moon_Gift_Shop_Warp_Points.MOUNT_MOON_GIFT_SHOP_TO_MOUNT_MOON_SQUARE_3_WP,
        "MountMoonSquare", 10
    )


class Rock_Tunnel_1F_Links(Enum): # 1-5, 2-6, 3,4

    ROCK_TUNNEL_1F_TO_ROUTE_9_1_LINK = WarpLink(
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROUTE_9_1_WP,
        Route_9_Warp_Points.ROUTE_9_TO_ROCK_TUNNEL_1F_1_WP,
        "RockTunnel1F"
    )

    ROCK_TUNNEL_1F_TO_ROUTE_10_SOUTH_1_LINK = WarpLink(
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROUTE_10_SOUTH_1_WP,
        Route_10_South_Warp_Points.ROUTE_10_SOUTH_TO_ROCK_TUNNEL_1F_2_WP,
        "RockTunnel1F", 5
    )

    ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_3_LINK = WarpLink(
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_3_WP,
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_3_WP,
        "RockTunnel1F", 10
    )

    ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_2_LINK = WarpLink(
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_2_WP,
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_4_WP,
        "RockTunnel1F", 15
    )

    ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_4_LINK = WarpLink(
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_4_WP,
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_5_WP,
        "RockTunnel1F", 20
    )

    ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_1_LINK = WarpLink(
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_1_WP,
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_6_WP,
        "RockTunnel1F", 25
    )


class Rock_Tunnel_B1F_Links(Enum): # 1-2, 3-4

    ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_6_LINK = WarpLink(
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_6_WP,
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_1_WP,
        "RockTunnelB1F"
    )

    ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_4_LINK = WarpLink(
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_4_WP,
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_2_WP,
        "RockTunnelB1F", 5
    )

    ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_3_LINK = WarpLink(
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_3_WP,
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_3_WP,
        "RockTunnelB1F", 10
    )

    ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_5_LINK = WarpLink(
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_5_WP,
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_4_WP,
        "RockTunnelB1F", 15
    )

class Underground_Path_Links(Enum):

    UNDERGROUND_PATH_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_3_LINK = WarpLink(
        Underground_Path_Warp_Points.UNDERGROUND_PATH_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_3_WP,
        Route_5_Underground_Path_Entrance_Warp_Points.ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_1_WP,
        "UndergroundPath"
    )

    UNDERGROUND_PATH_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_3_LINK = WarpLink(
        Underground_Path_Warp_Points.UNDERGROUND_PATH_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_3_WP,
        Route_6_Underground_Path_Entrance_Warp_Points.ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_2_WP,
        "UndergroundPath", 5
    )



#######################################################################
#                    Kanto_Gates Group                                      #
#######################################################################

class Route_2_Gate_Links(Enum): # 1 top, 2 bottom

    ROUTE_2_GATE_TO_ROUTE_2_3_LINK = WarpLink(
        Route_2_Gate_Warp_Points.ROUTE_2_GATE_TO_ROUTE_2_3_WP,
        Route_2_Warp_Points.ROUTE_2_TO_ROUTE_2_GATE_1_WP,
        "Route2Gate", dual_width= True
    )

    ROUTE_2_GATE_TO_ROUTE_2_2_LINK = WarpLink(
        Route_2_Gate_Warp_Points.ROUTE_2_GATE_TO_ROUTE_2_2_WP,
        Route_2_Warp_Points.ROUTE_2_TO_ROUTE_2_GATE_3_WP,
        "Route2Gate", 10, dual_width= True
    )

class Route_5_Saffron_Gate_Links(Enum): # 1 top 2 bottom

    ROUTE_5_SAFFRON_GATE_TO_ROUTE_5_2_LINK = WarpLink(
        Route_5_Saffron_Gate_Warp_Points.ROUTE_5_SAFFRON_GATE_TO_ROUTE_5_2_WP,
        Route_5_Warp_Points.ROUTE_5_TO_ROUTE_5_SAFFRON_GATE_1_WP,
        "Route5SaffronGate", dual_width= True
    )

    ROUTE_5_SAFFRON_GATE_TO_SAFFRON_CITY_9_LINK = WarpLink(
        Route_5_Saffron_Gate_Warp_Points.ROUTE_5_SAFFRON_GATE_TO_SAFFRON_CITY_9_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_5_SAFFRON_GATE_3_WP,
        "Route5SaffronGate", 10, dual_width= True
    )

class Route_6_Saffron_Gate_Links(Enum): # 1 top, 2 bottom

    ROUTE_6_SAFFRON_GATE_TO_SAFFRON_CITY_12_LINK = WarpLink(
        Route_6_Saffron_Gate_Warp_Points.ROUTE_6_SAFFRON_GATE_TO_SAFFRON_CITY_12_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_6_SAFFRON_GATE_1_WP,
        "Route6SaffronGate", dual_width= True
    )

    ROUTE_6_SAFFRON_GATE_TO_ROUTE_6_2_LINK = WarpLink(
        Route_6_Saffron_Gate_Warp_Points.ROUTE_6_SAFFRON_GATE_TO_ROUTE_6_2_WP,
        Route_6_Warp_Points.ROUTE_6_TO_ROUTE_6_SAFFRON_GATE_3_WP,
        "Route6SaffronGate", 10, dual_width= True
    )

class Route_7_Saffron_Gate_Links(Enum): # 1 right, 2 left

    ROUTE_7_SAFFRON_GATE_TO_ROUTE_7_1_LINK = WarpLink(
        Route_7_Saffron_Gate_Warp_Points.ROUTE_7_SAFFRON_GATE_TO_ROUTE_7_1_WP,
        Route_7_Warp_Points.ROUTE_7_TO_ROUTE_7_SAFFRON_GATE_1_WP,
        "Route7SaffronGate", dual_width= True
    )

    ROUTE_7_SAFFRON_GATE_TO_SAFFRON_CITY_10_LINK = WarpLink(
        Route_7_Saffron_Gate_Warp_Points.ROUTE_7_SAFFRON_GATE_TO_SAFFRON_CITY_10_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_7_SAFFRON_GATE_3_WP,
        "Route7SaffronGate", 10, dual_width= True
    )

class Route_8_Saffron_Gate_Links(Enum): # 1 right, 2 left

    ROUTE_8_SAFFRON_GATE_TO_SAFFRON_CITY_14_LINK = WarpLink(
        Route_8_Saffron_Gate_Warp_Points.ROUTE_8_SAFFRON_GATE_TO_SAFFRON_CITY_14_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_8_SAFFRON_GATE_1_WP,
        "Route8SaffronGate", dual_width= True
    )

    ROUTE_8_SAFFRON_GATE_TO_ROUTE_8_1_LINK = WarpLink(
        Route_8_Saffron_Gate_Warp_Points.ROUTE_8_SAFFRON_GATE_TO_ROUTE_8_1_WP,
        Route_8_Warp_Points.ROUTE_8_TO_ROUTE_8_SAFFRON_GATE_3_WP,
        "Route8SaffronGate", 10, dual_width= True
    )

class Route_15_Fuchsia_Gate_Links(Enum): # 1 left, 2 right

    ROUTE_15_FUCHSIA_GATE_TO_FUCHSIA_CITY_8_LINK = WarpLink(
        Route_15_Fuchsia_Gate_Warp_Points.ROUTE_15_FUCHSIA_GATE_TO_FUCHSIA_CITY_8_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_ROUTE_15_FUCHSIA_GATE_1_WP,
        "Route15FuchsiaGate", dual_width= True
    )

    ROUTE_15_FUCHSIA_GATE_TO_ROUTE_15_1_LINK = WarpLink(
        Route_15_Fuchsia_Gate_Warp_Points.ROUTE_15_FUCHSIA_GATE_TO_ROUTE_15_1_WP,
        Route_15_Warp_Points.ROUTE_15_TO_ROUTE_15_FUCHSIA_GATE_3_WP,
        "Route15FuchsiaGate", 10, dual_width= True
    )

class Route_16_Gate_Links(Enum): # 1 left, 2 right

    ROUTE_16_GATE_TO_ROUTE_16_4_LINK = WarpLink(
        Route_16_Gate_Warp_Points.ROUTE_16_GATE_TO_ROUTE_16_4_WP,
        Route_16_Warp_Points.ROUTE_16_TO_ROUTE_16_GATE_1_WP,
        "Route16Gate", dual_width= True
    )

    ROUTE_16_GATE_TO_ROUTE_16_2_LINK = WarpLink(
        Route_16_Gate_Warp_Points.ROUTE_16_GATE_TO_ROUTE_16_2_WP,
        Route_16_Warp_Points.ROUTE_16_TO_ROUTE_16_GATE_3_WP,
        "Route16Gate", 10, dual_width= True
    )


class Route_17_Route_18_Gate_Links(Enum): # 1 left, 2 right

    ROUTE_17_ROUTE_18_GATE_TO_ROUTE_17_1_LINK = WarpLink(
        Route_17_Route_18_Gate_Warp_Points.ROUTE_17_ROUTE_18_GATE_TO_ROUTE_17_1_WP,
        Route_17_Warp_Points.ROUTE_17_TO_ROUTE_17_ROUTE_18_GATE_1_WP,
        "Route17Route18Gate", dual_width= True
    )

    ROUTE_17_ROUTE_18_GATE_TO_ROUTE_18_1_LINK = WarpLink(
        Route_17_Route_18_Gate_Warp_Points.ROUTE_17_ROUTE_18_GATE_TO_ROUTE_18_1_WP,
        Route_18_Warp_Points.ROUTE_18_TO_ROUTE_17_ROUTE_18_GATE_3_WP,
        "Route17Route18Gate", 10, dual_width= True
    )

class Route_19_Fuchsia_Gate_Links(Enum):

    ROUTE_19_FUCHSIA_GATE_TO_FUCHSIA_CITY_10_LINK = WarpLink(
        Route_19_Fuchsia_Gate_Warp_Points.ROUTE_19_FUCHSIA_GATE_TO_FUCHSIA_CITY_10_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_ROUTE_19_FUCHSIA_GATE_1_WP,
        "Route19FuchsiaGate", dual_width= True
    )

    ROUTE_19_FUCHSIA_GATE_TO_ROUTE_19_1_LINK = WarpLink(
        Route_19_Fuchsia_Gate_Warp_Points.ROUTE_19_FUCHSIA_GATE_TO_ROUTE_19_1_WP,
        Route_19_Warp_Points.ROUTE_19_TO_ROUTE_19_FUCHSIA_GATE_3_WP,
        "Route19FuchsiaGate", 10, dual_width= True
    )


#######################################################################
#                    Kanto_Routes Group                               #
#######################################################################

class Route_2_Links(Enum):

    ROUTE_2_TO_ROUTE_2_NUGGET_HOUSE_1_LINK = WarpLink(
        Route_2_Warp_Points.ROUTE_2_TO_ROUTE_2_NUGGET_HOUSE_1_WP,
        Route_2_Nugget_House_Warp_Points.ROUTE_2_NUGGET_HOUSE_TO_ROUTE_2_1_WP,
        "Route2"
    )

    ROUTE_2_TO_ROUTE_2_GATE_3_LINK = WarpLink(
        Route_2_Warp_Points.ROUTE_2_TO_ROUTE_2_GATE_3_WP,
        Route_2_Gate_Warp_Points.ROUTE_2_GATE_TO_ROUTE_2_2_WP,
        "Route2", 5
    )

    ROUTE_2_TO_ROUTE_2_GATE_1_LINK = WarpLink(
        Route_2_Warp_Points.ROUTE_2_TO_ROUTE_2_GATE_1_WP,
        Route_2_Gate_Warp_Points.ROUTE_2_GATE_TO_ROUTE_2_3_WP,
        "Route2", 10, dual_width= True
    )

    ROUTE_2_TO_DIGLETTS_CAVE_3_LINK = WarpLink(
        Route_2_Warp_Points.ROUTE_2_TO_DIGLETTS_CAVE_3_WP,
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_ROUTE_2_5_WP,
        "Route2", 20
    )

class Route_3_Links(Enum):

    ROUTE_3_TO_MOUNT_MOON_1_LINK = WarpLink(
        Route_3_Warp_Points.ROUTE_3_TO_MOUNT_MOON_1_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_ROUTE_3_1_WP,
        "Route3"
    )

class Route_4_Links(Enum):

    ROUTE_4_TO_MOUNT_MOON_2_LINK = WarpLink(
        Route_4_Warp_Points.ROUTE_4_TO_MOUNT_MOON_2_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_ROUTE_4_1_WP,
        "Route4"
    )

class Route_5_Cleanse_Tag_House_Links(Enum):

    ROUTE_5_CLEANSE_TAG_HOUSE_TO_ROUTE_5_4_LINK = WarpLink(
        Route_5_Cleanse_Tag_House_Warp_Points.ROUTE_5_CLEANSE_TAG_HOUSE_TO_ROUTE_5_4_WP,
        Route_5_Warp_Points.ROUTE_5_TO_ROUTE_5_CLEANSE_TAG_HOUSE_1_WP,
        "Route5CleanseTagHouse", dual_width= True
    )

class Route_5_Links(Enum):

    ROUTE_5_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_1_LINK = WarpLink(
        Route_5_Warp_Points.ROUTE_5_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_1_WP,
        Route_5_Underground_Path_Entrance_Warp_Points.ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_5_1_WP,
        "Route5", locked_by=[Unlock_Keys.MACHINE_PART]
    )

    ROUTE_5_TO_ROUTE_5_SAFFRON_GATE_1_LINK = WarpLink(
        Route_5_Warp_Points.ROUTE_5_TO_ROUTE_5_SAFFRON_GATE_1_WP,
        Route_5_Saffron_Gate_Warp_Points.ROUTE_5_SAFFRON_GATE_TO_ROUTE_5_2_WP,
        "Route5", 5, dual_width= True
    )

    ROUTE_5_TO_ROUTE_5_CLEANSE_TAG_HOUSE_1_LINK = WarpLink(
        Route_5_Warp_Points.ROUTE_5_TO_ROUTE_5_CLEANSE_TAG_HOUSE_1_WP,
        Route_5_Cleanse_Tag_House_Warp_Points.ROUTE_5_CLEANSE_TAG_HOUSE_TO_ROUTE_5_4_WP,
        "Route5", 15
    )

class Route_5_Underground_Path_Entrance_Links(Enum):

    ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_5_1_LINK = WarpLink(
        Route_5_Underground_Path_Entrance_Warp_Points.ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_5_1_WP,
        Route_5_Warp_Points.ROUTE_5_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_1_WP,
        "Route5UndergroundPathEntrance", dual_width= True
    )

    ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_1_LINK = WarpLink(
        Route_5_Underground_Path_Entrance_Warp_Points.ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_1_WP,
        Underground_Path_Warp_Points.UNDERGROUND_PATH_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_3_WP,
        "Route5UndergroundPathEntrance", 10
    )

class Route_6_Links(Enum):

    ROUTE_6_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_1_LINK = WarpLink(
        Route_6_Warp_Points.ROUTE_6_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_1_WP,
        Route_6_Underground_Path_Entrance_Warp_Points.ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_6_1_WP,
        "Route6", locked_by=[Unlock_Keys.MACHINE_PART]
    )

    ROUTE_6_TO_ROUTE_6_SAFFRON_GATE_3_LINK = WarpLink(
        Route_6_Warp_Points.ROUTE_6_TO_ROUTE_6_SAFFRON_GATE_3_WP,
        Route_6_Saffron_Gate_Warp_Points.ROUTE_6_SAFFRON_GATE_TO_ROUTE_6_2_WP,
        "Route6", 5
    )

class Route_6_Underground_Path_Entrance_Links(Enum):

    ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_6_1_LINK = WarpLink(
        Route_6_Underground_Path_Entrance_Warp_Points.ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_6_1_WP,
        Route_6_Warp_Points.ROUTE_6_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_1_WP,
        "Route6UndergroundPathEntrance", dual_width= True
    )

    ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_2_LINK = WarpLink(
        Route_6_Underground_Path_Entrance_Warp_Points.ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_2_WP,
        Underground_Path_Warp_Points.UNDERGROUND_PATH_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_3_WP,
        "Route6UndergroundPathEntrance", 10
    )

class Route_7_Links(Enum):

    ROUTE_7_TO_ROUTE_7_SAFFRON_GATE_1_LINK = WarpLink(
        Route_7_Warp_Points.ROUTE_7_TO_ROUTE_7_SAFFRON_GATE_1_WP,
        Route_7_Saffron_Gate_Warp_Points.ROUTE_7_SAFFRON_GATE_TO_ROUTE_7_1_WP,
        "Route7", dual_width= True
    )

class Route_8_Links(Enum):

    ROUTE_8_TO_ROUTE_8_SAFFRON_GATE_3_LINK = WarpLink(
        Route_8_Warp_Points.ROUTE_8_TO_ROUTE_8_SAFFRON_GATE_3_WP,
        Route_8_Saffron_Gate_Warp_Points.ROUTE_8_SAFFRON_GATE_TO_ROUTE_8_1_WP,
        "Route8", dual_width= True
    )

class Route_9_Links(Enum):

    ROUTE_9_TO_ROCK_TUNNEL_1F_1_LINK = WarpLink(
        Route_9_Warp_Points.ROUTE_9_TO_ROCK_TUNNEL_1F_1_WP,
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROUTE_9_1_WP,
        "Route9"
    )

class Route_10_North_Links(Enum):

    ROUTE_10_NORTH_TO_ROUTE_10_POKECENTER_1F_1_LINK = WarpLink(
        Route_10_North_Warp_Points.ROUTE_10_NORTH_TO_ROUTE_10_POKECENTER_1F_1_WP,
        Route_10_Pokecenter_1F_Warp_Points.ROUTE_10_POKECENTER_1F_TO_ROUTE_10_NORTH_1_WP,
        "Route10North"
    )

    ROUTE_10_NORTH_TO_POWER_PLANT_1_LINK = WarpLink(
        Route_10_North_Warp_Points.ROUTE_10_NORTH_TO_POWER_PLANT_1_WP,
        Power_Plant_Warp_Points.POWER_PLANT_TO_ROUTE_10_NORTH_2_WP,
        "Route10North", 5
    )

class Route_10_Pokecenter_1F_Links(Enum):

    ROUTE_10_POKECENTER_1F_TO_ROUTE_10_NORTH_1_LINK = WarpLink(
        Route_10_Pokecenter_1F_Warp_Points.ROUTE_10_POKECENTER_1F_TO_ROUTE_10_NORTH_1_WP,
        Route_10_North_Warp_Points.ROUTE_10_NORTH_TO_ROUTE_10_POKECENTER_1F_1_WP,
        "Route10Pokecenter1F", dual_width= True
    )

    ROUTE_10_POKECENTER_1F_TO_POKECENTER_2F_1_LINK = WarpLink(
        Route_10_Pokecenter_1F_Warp_Points.ROUTE_10_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "Route10Pokecenter1F", 10
    )

class Route_10_South_Links(Enum):

    ROUTE_10_SOUTH_TO_ROCK_TUNNEL_1F_2_LINK = WarpLink(
        Route_10_South_Warp_Points.ROUTE_10_SOUTH_TO_ROCK_TUNNEL_1F_2_WP,
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROUTE_10_SOUTH_1_WP,
        "Route10South"
    )

class Route_12_Links(Enum):

    ROUTE_12_TO_ROUTE_12_SUPER_ROD_HOUSE_1_LINK = WarpLink(
        Route_12_Warp_Points.ROUTE_12_TO_ROUTE_12_SUPER_ROD_HOUSE_1_WP,
        Route_12_Super_Rod_House_Warp_Points.ROUTE_12_SUPER_ROD_HOUSE_TO_ROUTE_12_1_WP,
        "Route12"
    )

class Route_12_Super_Rod_House_Links(Enum):

    ROUTE_12_SUPER_ROD_HOUSE_TO_ROUTE_12_1_LINK = WarpLink(
        Route_12_Super_Rod_House_Warp_Points.ROUTE_12_SUPER_ROD_HOUSE_TO_ROUTE_12_1_WP,
        Route_12_Warp_Points.ROUTE_12_TO_ROUTE_12_SUPER_ROD_HOUSE_1_WP,
        "Route12SuperRodHouse", dual_width= True
    )

class Route_15_Links(Enum):

    ROUTE_15_TO_ROUTE_15_FUCHSIA_GATE_3_LINK = WarpLink(
        Route_15_Warp_Points.ROUTE_15_TO_ROUTE_15_FUCHSIA_GATE_3_WP,
        Route_15_Fuchsia_Gate_Warp_Points.ROUTE_15_FUCHSIA_GATE_TO_ROUTE_15_1_WP,
        "Route15", dual_width= True
    )


class Route_16_Fuchsia_Speech_House_Links(Enum):

    ROUTE_16_FUCHSIA_SPEECH_HOUSE_TO_ROUTE_16_1_LINK = WarpLink(
        Route_16_Fuchsia_Speech_House_Warp_Points.ROUTE_16_FUCHSIA_SPEECH_HOUSE_TO_ROUTE_16_1_WP,
        Route_16_Warp_Points.ROUTE_16_TO_ROUTE_16_FUCHSIA_SPEECH_HOUSE_1_WP,
        "Route16FuchsiaSpeechHouse", dual_width= True
    )

class Route_16_Links(Enum):

    ROUTE_16_TO_ROUTE_16_FUCHSIA_SPEECH_HOUSE_1_LINK = WarpLink(
        Route_16_Warp_Points.ROUTE_16_TO_ROUTE_16_FUCHSIA_SPEECH_HOUSE_1_WP,
        Route_16_Fuchsia_Speech_House_Warp_Points.ROUTE_16_FUCHSIA_SPEECH_HOUSE_TO_ROUTE_16_1_WP,
        "Route16"
    )

    ROUTE_16_TO_ROUTE_16_GATE_3_LINK = WarpLink(
        Route_16_Warp_Points.ROUTE_16_TO_ROUTE_16_GATE_3_WP,
        Route_16_Gate_Warp_Points.ROUTE_16_GATE_TO_ROUTE_16_2_WP,
        "Route16", 5, dual_width= True
    )

    ROUTE_16_TO_ROUTE_16_GATE_1_LINK = WarpLink(
        Route_16_Warp_Points.ROUTE_16_TO_ROUTE_16_GATE_1_WP,
        Route_16_Gate_Warp_Points.ROUTE_16_GATE_TO_ROUTE_16_4_WP,
        "Route16", 15, dual_width= True
    )

class Route_17_Links(Enum):

    ROUTE_17_TO_ROUTE_17_ROUTE_18_GATE_1_LINK = WarpLink(
        Route_17_Warp_Points.ROUTE_17_TO_ROUTE_17_ROUTE_18_GATE_1_WP,
        Route_17_Route_18_Gate_Warp_Points.ROUTE_17_ROUTE_18_GATE_TO_ROUTE_17_1_WP,
        "Route17", dual_width= True
    )


class Route_18_Links(Enum):

    ROUTE_18_TO_ROUTE_17_ROUTE_18_GATE_3_LINK = WarpLink(
        Route_18_Warp_Points.ROUTE_18_TO_ROUTE_17_ROUTE_18_GATE_3_WP,
        Route_17_Route_18_Gate_Warp_Points.ROUTE_17_ROUTE_18_GATE_TO_ROUTE_18_1_WP,
        "Route18", dual_width= True
    )


class Route_19_Links(Enum):

    ROUTE_19_TO_ROUTE_19_FUCHSIA_GATE_3_LINK = WarpLink(
        Route_19_Warp_Points.ROUTE_19_TO_ROUTE_19_FUCHSIA_GATE_3_WP,
        Route_19_Fuchsia_Gate_Warp_Points.ROUTE_19_FUCHSIA_GATE_TO_ROUTE_19_1_WP,
        "Route19"
    )

class Route_20_Links(Enum):

    ROUTE_20_TO_SEAFOAM_GYM_1_LINK = WarpLink(
        Route_20_Warp_Points.ROUTE_20_TO_SEAFOAM_GYM_1_WP,
        Seafoam_Gym_Warp_Points.SEAFOAM_GYM_TO_ROUTE_20_1_WP,
        "Route20"
    )

class Route_22_Links(Enum):

    ROUTE_22_TO_VICTORY_ROAD_GATE_1_LINK = WarpLink(
        Route_22_Warp_Points.ROUTE_22_TO_VICTORY_ROAD_GATE_1_WP, #todo victory road gate
        Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_DEPT_STORE_1F_1_WP,
        "Route22"
    )

class Route_25_Links(Enum):

    ROUTE_25_TO_BILLS_HOUSE_1_LINK = WarpLink(
        Route_25_Warp_Points.ROUTE_25_TO_BILLS_HOUSE_1_WP,
        Bills_House_Warp_Points.BILLS_HOUSE_TO_ROUTE_25_1_WP,
        "Route25"
    )


#######################################################################
#                    Fast ship Group                                  #
#######################################################################

class Fast_Ship_1F_Links(Enum): #10-11 corridor, rest except 1 is hub

#We don't randomize ship entrance/exit
    #FAST_SHIP_1F_TO_FAST_SHIP_1F_-1_LINK = WarpLink(
    #    Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_1F_-1_WP,
    #    <return warp>
    #    "FastShip1F"
    #)

    FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_1_LINK = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_1_WP,
        Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_2_WP,
        "FastShip1F", 5
    )

    FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_2_LINK = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_2_WP,
        Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_3_WP,
        "FastShip1F", 10
    )

    FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_3_LINK = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_3_WP,
        Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_4_WP,
        "FastShip1F", 15
    )

    FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_1_LINK = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_1_WP,
        Fast_Ship_Cabins_SW_SSW_NW_Warp_Points.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_5_WP,
        "FastShip1F", 20
    )

    FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_2_LINK = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_2_WP,
        Fast_Ship_Cabins_SW_SSW_NW_Warp_Points.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_6_WP,
        "FastShip1F", 25
    )

    FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_4_LINK = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_4_WP,
        Fast_Ship_Cabins_SW_SSW_NW_Warp_Points.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_7_WP,
        "FastShip1F", 30
    )

    FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_1_LINK = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_1_WP,
        Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_8_WP,
        "FastShip1F", 35
    )

    FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_3_LINK = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_3_WP,
        Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_9_WP,
        "FastShip1F", 40
    )

    FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5_LINK = WarpLink( #1011
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5_WP,
        Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_10_WP,
        "FastShip1F", 45
    )

    FAST_SHIP_1F_TO_FAST_SHIP_B1F_1_LINK = WarpLink( #1011
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_B1F_1_WP,
        Fast_Ship_B1F_Warp_Points.FAST_SHIP_B1F_TO_FAST_SHIP_1F_11_WP,
        "FastShip1F", 50
    )

    FAST_SHIP_1F_TO_FAST_SHIP_B1F_2_LINK = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_B1F_2_WP,
        Fast_Ship_B1F_Warp_Points.FAST_SHIP_B1F_TO_FAST_SHIP_1F_12_WP,
        "FastShip1F", 55
    )

class Fast_Ship_B1F_Links(Enum):

    FAST_SHIP_B1F_TO_FAST_SHIP_1F_11_LINK = WarpLink(
        Fast_Ship_B1F_Warp_Points.FAST_SHIP_B1F_TO_FAST_SHIP_1F_11_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_B1F_1_WP,
        "FastShipB1F"
    )

    FAST_SHIP_B1F_TO_FAST_SHIP_1F_12_LINK = WarpLink(
        Fast_Ship_B1F_Warp_Points.FAST_SHIP_B1F_TO_FAST_SHIP_1F_12_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_B1F_2_WP,
        "FastShipB1F", 5
    )

class Fast_Ship_Cabins_NNW_NNE_NE_Links(Enum): 

    FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_2_LINK = WarpLink(
        Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_2_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_1_WP,
        "FastShipCabins_NNW_NNE_NE" 
    )

    FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_3_LINK = WarpLink(
        Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_3_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_2_WP,
        "FastShipCabins_NNW_NNE_NE", 5 
    )

    FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_4_LINK = WarpLink( #lazy sailor
        Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_4_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_3_WP,
        "FastShipCabins_NNW_NNE_NE", 10 
    )

class Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links(Enum): 

    FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_8_LINK = WarpLink(
        Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_8_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_1_WP,
        "FastShipCabins_SE_SSE_CaptainsCabin", dual_width= True
    )

    FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_9_LINK = WarpLink(
        Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_9_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_3_WP,
        "FastShipCabins_SE_SSE_CaptainsCabin", 10, dual_width= True
    )

    FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_10_LINK = WarpLink( # captain
        Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_10_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5_WP,
        "FastShipCabins_SE_SSE_CaptainsCabin", 20, dual_width= True
    )

class Fast_Ship_Cabins_SW_SSW_NW_Links(Enum):

    FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_5_LINK = WarpLink( #player cabin
        Fast_Ship_Cabins_SW_SSW_NW_Warp_Points.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_5_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_1_WP,
        "FastShipCabins_SW_SSW_NW"
    )

    FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_6_LINK = WarpLink(
        Fast_Ship_Cabins_SW_SSW_NW_Warp_Points.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_6_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_2_WP,
        "FastShipCabins_SW_SSW_NW", 5, dual_width= True
    )

    FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_7_LINK = WarpLink(
        Fast_Ship_Cabins_SW_SSW_NW_Warp_Points.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_7_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_4_WP,
        "FastShipCabins_SW_SSW_NW", 15, dual_width= True
    )

class Route_28_Links(Enum):
    ROUTE_28_TO_ROUTE_28_STEEL_WING_HOUSE_1_LINK = WarpLink(
        Route_28_Warp_Points.ROUTE_28_TO_ROUTE_28_STEEL_WING_HOUSE_1_WP,
        Route_28_Steel_Wing_House_Warp_Points.ROUTE_28_STEEL_WING_HOUSE_TO_ROUTE_28_1_WP,
        "Route28"
    )
    ROUTE_28_TO_VICTORY_ROAD_GATE_7_LINK = WarpLink(
        Route_28_Warp_Points.ROUTE_28_TO_VICTORY_ROAD_GATE_7_WP,
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_ROUTE_28_2_WP,
        "Route28", 5
    )

class Route_28_Steel_Wing_House_Links(Enum):
    ROUTE_28_STEEL_WING_HOUSE_TO_ROUTE_28_1_LINK = WarpLink(
        Route_28_Steel_Wing_House_Warp_Points.ROUTE_28_STEEL_WING_HOUSE_TO_ROUTE_28_1_WP,
        Route_28_Warp_Points.ROUTE_28_TO_ROUTE_28_STEEL_WING_HOUSE_1_WP,
        "Route28SteelWingHouse", dual_width=True
    )

class Silver_Cave_Outside_Links(Enum):
    SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_POKECENTER_1F_1_LINK = WarpLink(
        Silver_Cave_Outside_Warp_Points.SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_POKECENTER_1F_1_WP,
        Silver_Cave_Pokecenter_1F_Warp_Points.SILVER_CAVE_POKECENTER_1F_TO_SILVER_CAVE_OUTSIDE_1_WP,
        "SilverCaveOutside"
    )
    SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_ROOM_1_1_LINK = WarpLink(
        Silver_Cave_Outside_Warp_Points.SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_ROOM_1_1_WP,
        Silver_Cave_Room_1_Warp_Points.SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_OUTSIDE_2_WP,
        "SilverCaveOutside", 5
    )

class Silver_Cave_Pokecenter_1F_Links(Enum):
    SILVER_CAVE_POKECENTER_1F_TO_SILVER_CAVE_OUTSIDE_1_LINK = WarpLink(
        Silver_Cave_Pokecenter_1F_Warp_Points.SILVER_CAVE_POKECENTER_1F_TO_SILVER_CAVE_OUTSIDE_1_WP,
        Silver_Cave_Outside_Warp_Points.SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_POKECENTER_1F_1_WP,
        "SilverCavePokecenter1F", dual_width=True
    )
    SILVER_CAVE_POKECENTER_1F_TO_POKECENTER_2F_1_LINK = WarpLink(
        Silver_Cave_Pokecenter_1F_Warp_Points.SILVER_CAVE_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "SilverCavePokecenter1F", 10
    )

class Silver_Cave_Room_1_Links(Enum):
    SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_OUTSIDE_2_LINK = WarpLink(
        Silver_Cave_Room_1_Warp_Points.SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_OUTSIDE_2_WP,
        Silver_Cave_Outside_Warp_Points.SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_ROOM_1_1_WP,
        "SilverCaveRoom1"
    )
    SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_ROOM_2_1_LINK = WarpLink(
        Silver_Cave_Room_1_Warp_Points.SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_ROOM_2_1_WP,
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_1_2_WP,
        "SilverCaveRoom1", 5
    )

class Silver_Cave_Room_2_Links(Enum):
    SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_1_2_LINK = WarpLink(
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_1_2_WP,
        Silver_Cave_Room_1_Warp_Points.SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_ROOM_2_1_WP,
        "SilverCaveRoom2"
    )
    SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_3_1_LINK = WarpLink(
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_3_1_WP,
        Silver_Cave_Room_3_Warp_Points.SILVER_CAVE_ROOM_3_TO_SILVER_CAVE_ROOM_2_2_WP,
        "SilverCaveRoom2", 5
    )
    SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_1_LINK = WarpLink(
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_1_WP,
        Silver_Cave_Item_Rooms_Warp_Points.SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_3_WP,
        "SilverCaveRoom2", 10
    )
    SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_2_LINK = WarpLink(
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_2_WP,
        Silver_Cave_Item_Rooms_Warp_Points.SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_4_WP,
        "SilverCaveRoom2", 15
    )
class Silver_Cave_Room_3_Links(Enum):
    SILVER_CAVE_ROOM_3_TO_SILVER_CAVE_ROOM_2_2_LINK = WarpLink(
        Silver_Cave_Room_3_Warp_Points.SILVER_CAVE_ROOM_3_TO_SILVER_CAVE_ROOM_2_2_WP,
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_ROUTE_28_2_WP,
        "SilverCaveRoom3"
    )

class Silver_Cave_Item_Rooms_Links(Enum):
    SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_3_LINK = WarpLink(
        Silver_Cave_Item_Rooms_Warp_Points.SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_3_WP,
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_1_WP,
        "SilverCaveItemRooms"
    )
    SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_4_LINK = WarpLink(
        Silver_Cave_Item_Rooms_Warp_Points.SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_4_WP,
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_2_WP,
        "SilverCaveItemRooms", 5
    )


#######################################################################
#                    END OF GROUPS                                    #
#######################################################################
