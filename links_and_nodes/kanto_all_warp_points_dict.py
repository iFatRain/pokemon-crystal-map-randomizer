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
def buildKantoWarpLinks():

    Celadon_Cafe_Links = dict()
    Celadon_Dept_Store_1F_Links = dict()
    Celadon_Dept_Store_2F_Links = dict()
    Celadon_Dept_Store_3F_Links = dict()
    Celadon_Dept_Store_4F_Links = dict()
    Celadon_Dept_Store_5F_Links = dict()
    Celadon_Dept_Store_6F_Links = dict()
    Celadon_Game_Corner_Links = dict()
    Celadon_Game_Corner_Prize_Room_Links = dict()
    Celadon_Gym_Links = dict()
    Celadon_Mansion_1F_Links = dict()
    Celadon_Mansion_2F_Links = dict()
    Celadon_Mansion_3F_Links = dict()
    Celadon_Mansion_Roof_House_Links = dict()
    Celadon_Mansion_Roof_Links = dict()
    Celadon_Pokecenter_1F_Links = dict()
    Celadon_City_Links = dict()
    Bills_House_Links = dict()
    Cerulean_Gym_Badge_Speech_House_Links = dict()
    Cerulean_Gym_Links = dict()
    Cerulean_Mart_Links = dict()
    Cerulean_Pokecenter_1F_Links = dict()
    Cerulean_Police_Station_Links = dict()
    Cerulean_Trade_Speech_House_Links = dict()
    Power_Plant_Links = dict()
    Cerulean_City_Links = dict()
    Cinnabar_Pokecenter_1F_Links = dict()
    Seafoam_Gym_Links = dict()
    Cinnabar_Island_Links = dict()
    Bills_Brothers_House_Links = dict()
    Fuchsia_Gym_Links = dict()
    Fuchsia_Mart_Links = dict()
    Fuchsia_Pokecenter_1F_Links = dict()
    Safari_Zone_Main_Office_Links = dict()
    Safari_Zone_Wardens_Home_Links = dict()
    Fuchsia_City_Links = dict()
    Lavender_Mart_Links = dict()
    Lavender_Name_Rater_Links = dict()
    Lavender_Pokecenter_1F_Links = dict()
    Lavender_Speech_House_Links = dict()
    Lav_Radio_Tower_1F_Links = dict()
    Mr_Fujis_House_Links = dict()
    Soul_House_Links = dict()
    Lavender_Town_Links = dict()
    Blues_House_Links = dict()
    Oaks_Lab_Links = dict()
    Reds_House_1F_Links = dict()
    Reds_House_2F_Links = dict()
    Pallet_Town_Links = dict()
    Pewter_Gym_Links = dict()
    Pewter_Mart_Links = dict()
    Pewter_Nidoran_Speech_House_Links = dict()
    Pewter_Snooze_Speech_House_Links = dict()
    Pewter_Pokecenter_1F_Links = dict()
    Pewter_City_Links = dict()
    Copycats_House_1F_Links = dict()
    Copycats_House_2F_Links = dict()
    Fighting_Dojo_Links = dict()
    Mr_Psychics_House_Links = dict()
    Saffron_Gym_Links = dict()
    Saffron_Magnet_Train_Station_Links = dict()
    Saffron_Mart_Links = dict()
    Saffron_Pokecenter_1F_Links = dict()
    Silph_Co_1F_Links = dict()
    Saffron_City_Links = dict()
    Pokemon_Fan_Club_Links = dict()
    Vermilion_Digletts_Cave_Speech_House_Links = dict()
    Vermilion_Fishing_Speech_House_Links = dict()
    Vermilion_Gym_Links = dict()
    Vermilion_Magnet_Train_Speech_House_Links = dict()
    Vermilion_Mart_Links = dict()
    Vermilion_Pokecenter_1F_Links = dict()
    Vermilion_Port_Links = dict()
    Vermilion_Port_Passage_Links = dict()
    Vermilion_City_Links = dict()
    Route_2_Nugget_House_Links = dict()
    Trainer_House_1F_Links = dict()
    Trainer_House_B1F_Links = dict()
    Viridian_Gym_Links = dict()
    Viridian_Mart_Links = dict()
    Viridian_Nickname_Speech_House_Links = dict()
    Viridian_Pokecenter_1F_Links = dict()
    Viridian_City_Links = dict()
    Digletts_Cave_Links = dict()
    Mount_Moon_Gift_Shop_Links = dict()
    Mount_Moon_Links = dict()
    Mount_Moon_Square_Links = dict()
    Rock_Tunnel_1F_Links = dict()
    Rock_Tunnel_B1F_Links = dict()
    Underground_Path_Links = dict()
    Route_2_Gate_Links = dict()
    Route_5_Saffron_Gate_Links = dict()
    Route_6_Saffron_Gate_Links = dict()
    Route_7_Saffron_Gate_Links = dict()
    Route_8_Saffron_Gate_Links = dict()
    Route_15_Fuchsia_Gate_Links = dict()
    Route_16_Gate_Links = dict()
    Route_17_Route_18_Gate_Links = dict()
    Route_19_Fuchsia_Gate_Links = dict()
    Route_2_Links = dict()
    Route_3_Links = dict()
    Route_4_Links = dict()
    Route_5_Cleanse_Tag_House_Links = dict()
    Route_5_Links = dict()
    Route_5_Underground_Path_Entrance_Links = dict()
    Route_6_Links = dict()
    Route_6_Underground_Path_Entrance_Links = dict()
    Route_7_Links = dict()
    Route_8_Links = dict()
    Route_9_Links = dict()
    Route_10_North_Links = dict()
    Route_10_Pokecenter_1F_Links = dict()
    Route_10_South_Links = dict()
    Route_12_Links = dict()
    Route_12_Super_Rod_House_Links = dict()
    Route_15_Links = dict()
    Route_16_Fuchsia_Speech_House_Links = dict()
    Route_16_Links = dict()
    Route_17_Links = dict()
    Route_18_Links = dict()
    Route_19_Links = dict()
    Route_20_Links = dict()
    Route_22_Links = dict()
    Route_25_Links = dict()
    Fast_Ship_1F_Links = dict()
    Fast_Ship_B1F_Links = dict()
    Fast_Ship_Cabins_NNW_NNE_NE_Links = dict()
    Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links = dict()
    Fast_Ship_Cabins_SW_SSW_NW_Links = dict()
    Route_28_Links = dict()
    Route_28_Steel_Wing_House_Links = dict()
    Silver_Cave_Outside_Links = dict()
    Silver_Cave_Pokecenter_1F_Links = dict()
    Silver_Cave_Room_1_Links = dict()
    Silver_Cave_Room_2_Links = dict()
    Silver_Cave_Room_3_Links = dict()
    Silver_Cave_Item_Rooms_Links = dict()

    Celadon_Cafe_Links["CELADON_CAFE_TO_CELADON_CITY_9_LINK"] = WarpLink(
        Celadon_Cafe_Warp_Points.Celadon_City_Cafe_Exit_WP,
        Celadon_City_Warp_Points.Celadon_City_Cafe_Entrance_WP,
        "CeladonCafe", dual_width= True
    )



    Celadon_Dept_Store_1F_Links["CELADON_DEPT_STORE_1F_TO_CELADON_CITY_1_LINK"] = WarpLink(
        Celadon_Dept_Store_1F_Warp_Points.Celadon_City_Dept_Store_1F_Exit_WP,
        Celadon_City_Warp_Points.Celadon_City_Dept_Store_1F_Entrance_WP,
        "CeladonDeptStore1F", dual_width= True
    )

    Celadon_Dept_Store_1F_Links["CELADON_DEPT_STORE_1F_TO_CELADON_DEPT_STORE_2F_2_LINK"] = WarpLink(
        Celadon_Dept_Store_1F_Warp_Points.Celadon_City_Dept_Store_1F_Stairs_WP,
        Celadon_Dept_Store_2F_Warp_Points.Celadon_City_Dept_Store_2F_Right_Stairs_WP,
        "CeladonDeptStore1F", 10
    )




    Celadon_Dept_Store_2F_Links["CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_3F_1_LINK"] = WarpLink(
        Celadon_Dept_Store_2F_Warp_Points.Celadon_City_Dept_Store_2F_Left_Stairs_WP,
        Celadon_Dept_Store_3F_Warp_Points.Celadon_City_Dept_Store_3F_Left_Stairs_WP,
        "CeladonDeptStore2F"
    )

    Celadon_Dept_Store_2F_Links["CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_1F_3_LINK"] = WarpLink(
        Celadon_Dept_Store_2F_Warp_Points.Celadon_City_Dept_Store_2F_Right_Stairs_WP,
        Celadon_Dept_Store_1F_Warp_Points.Celadon_City_Dept_Store_1F_Stairs_WP,
        "CeladonDeptStore2F", 5
    )




    Celadon_Dept_Store_3F_Links["CELADON_DEPT_STORE_3F_TO_CELADON_DEPT_STORE_2F_1_LINK"] = WarpLink(
        Celadon_Dept_Store_3F_Warp_Points.Celadon_City_Dept_Store_3F_Left_Stairs_WP,
        Celadon_Dept_Store_2F_Warp_Points.Celadon_City_Dept_Store_2F_Left_Stairs_WP,
        "CeladonDeptStore3F"
    )

    Celadon_Dept_Store_3F_Links["CELADON_DEPT_STORE_3F_TO_CELADON_DEPT_STORE_4F_2_LINK"] = WarpLink(
        Celadon_Dept_Store_3F_Warp_Points.Celadon_City_Dept_Store_3F_Right_Stairs_WP,
        Celadon_Dept_Store_4F_Warp_Points.Celadon_City_Dept_Store_4F_Right_Stairs_WP,
        "CeladonDeptStore3F", 5
    )




    Celadon_Dept_Store_4F_Links["CELADON_DEPT_STORE_4F_TO_CELADON_DEPT_STORE_5F_1_LINK"] = WarpLink(
        Celadon_Dept_Store_4F_Warp_Points.Celadon_City_Dept_Store_4F_Left_Stairs_WP,
        Celadon_Dept_Store_5F_Warp_Points.Celadon_City_Dept_Store_5F_Left_Stairs_WP,
        "CeladonDeptStore4F"
    )

    Celadon_Dept_Store_4F_Links["CELADON_DEPT_STORE_4F_TO_CELADON_DEPT_STORE_3F_2_LINK"] = WarpLink(
        Celadon_Dept_Store_4F_Warp_Points.Celadon_City_Dept_Store_4F_Right_Stairs_WP,
        Celadon_Dept_Store_3F_Warp_Points.Celadon_City_Dept_Store_3F_Right_Stairs_WP,
        "CeladonDeptStore4F", 5
    )




    Celadon_Dept_Store_5F_Links["CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_4F_1_LINK"] = WarpLink(
        Celadon_Dept_Store_5F_Warp_Points.Celadon_City_Dept_Store_5F_Left_Stairs_WP,
        Celadon_Dept_Store_4F_Warp_Points.Celadon_City_Dept_Store_4F_Left_Stairs_WP,
        "CeladonDeptStore5F"
    )

    Celadon_Dept_Store_5F_Links["CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_6F_1_LINK"] = WarpLink(
        Celadon_Dept_Store_5F_Warp_Points.Celadon_City_Dept_Store_5F_Right_Stairs_WP,
        Celadon_Dept_Store_6F_Warp_Points.Celadon_City_Dept_Store_6F_Stairs_WP,
        "CeladonDeptStore5F", 5
    )




    Celadon_Dept_Store_6F_Links["CELADON_DEPT_STORE_6F_TO_CELADON_DEPT_STORE_5F_2_LINK"] = WarpLink(
        Celadon_Dept_Store_6F_Warp_Points.Celadon_City_Dept_Store_6F_Stairs_WP,
        Celadon_Dept_Store_5F_Warp_Points.Celadon_City_Dept_Store_5F_Right_Stairs_WP,
        "CeladonDeptStore6F"
    )




    Celadon_Game_Corner_Links["CELADON_GAME_CORNER_TO_CELADON_CITY_6_LINK"] = WarpLink(
        Celadon_Game_Corner_Warp_Points.Celadon_City_Game_Corner_Exit_WP,
        Celadon_City_Warp_Points.Celadon_City_Game_Corner_Entrance_WP,
        "CeladonGameCorner", dual_width= True
    )



    Celadon_Game_Corner_Prize_Room_Links["CELADON_GAME_CORNER_PRIZE_ROOM_TO_CELADON_CITY_7_LINK"] = WarpLink(
        Celadon_Game_Corner_Prize_Room_Warp_Points.Celadon_City_Game_Corner_Prize_Room_Exit_WP,
        Celadon_City_Warp_Points.Celadon_City_Game_Corner_Prize_Room_Entrance_WP,
        "CeladonGameCornerPrizeRoom", dual_width= True
    )



    Celadon_Gym_Links["CELADON_GYM_TO_CELADON_CITY_8_LINK"] = WarpLink(
        Celadon_Gym_Warp_Points.Celadon_City_Gym_Exit_WP,
        Celadon_City_Warp_Points.Celadon_City_Gym_Entrance_WP,
        "CeladonGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_12]
    )

 # 1-4 ,2-3

    Celadon_Mansion_1F_Links["CELADON_MANSION_1F_TO_CELADON_CITY_2_LINK"] = WarpLink(
        Celadon_Mansion_1F_Warp_Points.Celadon_City_Mansion_1F_Front_Exit_WP,
        Celadon_City_Warp_Points.Celadon_City_Mansion_1F_Front_Entrance_WP,
        "CeladonMansion1F", dual_width= True
    )

    Celadon_Mansion_1F_Links["CELADON_MANSION_1F_TO_CELADON_CITY_3_LINK"] = WarpLink(# backside
        Celadon_Mansion_1F_Warp_Points.Celadon_City_Mansion_1F_Rear_Exit_Central_Stairs_WP,
        Celadon_City_Warp_Points.Celadon_City_Mansion_1F_Rear_Entrance_WP,
        "CeladonMansion1F", 10
    )

    Celadon_Mansion_1F_Links["CELADON_MANSION_1F_TO_CELADON_MANSION_2F_1_LINK"] = WarpLink( #
        Celadon_Mansion_1F_Warp_Points.Celadon_City_Mansion_1F_Left_Stairs_WP,
        Celadon_Mansion_2F_Warp_Points.Celadon_City_Mansion_2F_Far_Left_Stairs_WP,
        "CeladonMansion1F", 15
    )

    Celadon_Mansion_1F_Links["CELADON_MANSION_1F_TO_CELADON_MANSION_2F_4_LINK"] = WarpLink(
        Celadon_Mansion_1F_Warp_Points.Celadon_City_Mansion_1F_Right_Stairs_WP,
        Celadon_Mansion_2F_Warp_Points.Celadon_City_Mansion_2F_Far_Right_Stairs_WP,
        "CeladonMansion1F", 20
    )

 # 1-2,3-4

    Celadon_Mansion_2F_Links["CELADON_MANSION_2F_TO_CELADON_MANSION_1F_4_LINK"] = WarpLink(#
        Celadon_Mansion_2F_Warp_Points.Celadon_City_Mansion_2F_Far_Left_Stairs_WP,
        Celadon_Mansion_1F_Warp_Points.Celadon_City_Mansion_1F_Left_Stairs_WP,
        "CeladonMansion2F"
    )

    Celadon_Mansion_2F_Links["CELADON_MANSION_2F_TO_CELADON_MANSION_3F_2_LINK"] = WarpLink(#
        Celadon_Mansion_2F_Warp_Points.Celadon_City_Mansion_2F_Far_Left_Stairs_WP,
        Celadon_Mansion_3F_Warp_Points.Celadon_City_Mansion_3F_Left_Center_Stairs_WP,
        "CeladonMansion2F", 5
    )

    Celadon_Mansion_2F_Links["CELADON_MANSION_2F_TO_CELADON_MANSION_3F_3_LINK"] = WarpLink(
        Celadon_Mansion_2F_Warp_Points.Celadon_City_Mansion_2F_Right_Center_Stairs_WP,
        Celadon_Mansion_3F_Warp_Points.Celadon_City_Mansion_3F_Right_Center_Stairs_WP,
        "CeladonMansion2F", 10
    )

    Celadon_Mansion_2F_Links["CELADON_MANSION_2F_TO_CELADON_MANSION_1F_5_LINK"] = WarpLink(
        Celadon_Mansion_2F_Warp_Points.Celadon_City_Mansion_2F_Far_Right_Stairs_WP,
        Celadon_Mansion_1F_Warp_Points.Celadon_City_Mansion_1F_Right_Stairs_WP,
        "CeladonMansion2F", 15
    )

 # 1-2, 3-4

    Celadon_Mansion_3F_Links["CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_1_LINK"] = WarpLink(#
        Celadon_Mansion_3F_Warp_Points.Celadon_City_Mansion_3F_Far_Left_Stairs_WP,
        Celadon_Mansion_Roof_Warp_Points.Celadon_City_Mansion_Roof_Left_Stairs_WP,
        "CeladonMansion3F",  unlocks=[]
    )

    Celadon_Mansion_3F_Links["CELADON_MANSION_3F_TO_CELADON_MANSION_2F_2_LINK"] = WarpLink(#
        Celadon_Mansion_3F_Warp_Points.Celadon_City_Mansion_3F_Left_Center_Stairs_WP,
        Celadon_Mansion_2F_Warp_Points.Celadon_City_Mansion_2F_Far_Left_Stairs_WP,
        "CeladonMansion3F", 5
    )

    Celadon_Mansion_3F_Links["CELADON_MANSION_3F_TO_CELADON_MANSION_2F_3_LINK"] = WarpLink(
        Celadon_Mansion_3F_Warp_Points.Celadon_City_Mansion_3F_Right_Center_Stairs_WP,
        Celadon_Mansion_2F_Warp_Points.Celadon_City_Mansion_2F_Right_Center_Stairs_WP,
        "CeladonMansion3F", 10
    )

    Celadon_Mansion_3F_Links["CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_2_LINK"] = WarpLink(
        Celadon_Mansion_3F_Warp_Points.Celadon_City_Mansion_3F_Far_Right_Stairs_WP,
        Celadon_Mansion_Roof_Warp_Points.Celadon_City_Mansion_Roof_Left_Stairs_WP,
        "CeladonMansion3F", 15
    )

    Celadon_Mansion_Roof_House_Links["CELADON_MANSION_ROOF_HOUSE_TO_CELADON_MANSION_ROOF_3_LINK"] = WarpLink(
        Celadon_Mansion_Roof_House_Warp_Points.Celadon_City_Mansion_Roof_House_Exit_WP,
        Celadon_Mansion_Roof_Warp_Points.Celadon_City_Mansion_Roof_House_Entrance_WP,
        "CeladonMansionRoofHouse", dual_width= True
    )

 # 1-3, 2x

    Celadon_Mansion_Roof_Links["CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_1_LINK"] = WarpLink(#
        Celadon_Mansion_Roof_Warp_Points.Celadon_City_Mansion_Roof_Left_Stairs_WP,
        Celadon_Mansion_3F_Warp_Points.Celadon_City_Mansion_3F_Far_Left_Stairs_WP,
        "CeladonMansionRoof"
    )

    Celadon_Mansion_Roof_Links["CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_4_LINK"] = WarpLink(
        Celadon_Mansion_Roof_Warp_Points.Celadon_City_Mansion_Roof_Left_Stairs_WP,
        Celadon_Mansion_3F_Warp_Points.Celadon_City_Mansion_3F_Far_Right_Stairs_WP,
        "CeladonMansionRoof", 5
    )

    Celadon_Mansion_Roof_Links["CELADON_MANSION_ROOF_TO_CELADON_MANSION_ROOF_HOUSE_1_LINK"] = WarpLink(#
        Celadon_Mansion_Roof_Warp_Points.Celadon_City_Mansion_Roof_House_Entrance_WP,
        Celadon_Mansion_Roof_House_Warp_Points.Celadon_City_Mansion_Roof_House_Exit_WP,
        "CeladonMansionRoof", 10
    )



    Celadon_Pokecenter_1F_Links["CELADON_POKECENTER_1F_TO_CELADON_CITY_5_LINK"] = WarpLink(
        Celadon_Pokecenter_1F_Warp_Points.Celadon_City_Pokecenter_Exit_WP,
        Celadon_City_Warp_Points.Celadon_City_Pokecenter_Entrance_WP,
        "CeladonPokecenter1F", dual_width= True
    )

    Celadon_Pokecenter_1F_Links["CELADON_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"] = WarpLink(
        Celadon_Pokecenter_1F_Warp_Points.Celadon_City_Pokecenter_Stairs_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "CeladonPokecenter1F", 10
    )




    Celadon_City_Links["CELADON_CITY_TO_CELADON_DEPT_STORE_1F_1_LINK"] = WarpLink(
        Celadon_City_Warp_Points.Celadon_City_Dept_Store_1F_Entrance_WP,
        Celadon_Dept_Store_1F_Warp_Points.Celadon_City_Dept_Store_1F_Exit_WP,
        "CeladonCity"
    )

    Celadon_City_Links["CELADON_CITY_TO_CELADON_MANSION_1F_1LINK"] = WarpLink(
        Celadon_City_Warp_Points.Celadon_City_Mansion_1F_Front_Entrance_WP,
        Celadon_Mansion_1F_Warp_Points.Celadon_City_Mansion_1F_Front_Exit_WP,
        "CeladonCity", 5
    )

    Celadon_City_Links["CELADON_CITY_TO_CELADON_MANSION_1F_3_LINK"] = WarpLink(
        Celadon_City_Warp_Points.Celadon_City_Mansion_1F_Rear_Entrance_WP,
        Celadon_Mansion_1F_Warp_Points.Celadon_City_Mansion_1F_Rear_Exit_Central_Stairs_WP,
        "CeladonCity", 10, dual_width= True
    )

    Celadon_City_Links["CELADON_CITY_TO_CELADON_POKECENTER_1F_1_LINK"] = WarpLink(
        Celadon_City_Warp_Points.Celadon_City_Pokecenter_Entrance_WP,
        Celadon_Pokecenter_1F_Warp_Points.Celadon_City_Pokecenter_Exit_WP,
        "CeladonCity", 20
    )

    Celadon_City_Links["CELADON_CITY_TO_CELADON_GAME_CORNER_1_LINK"] = WarpLink(
        Celadon_City_Warp_Points.Celadon_City_Game_Corner_Entrance_WP,
        Celadon_Game_Corner_Warp_Points.Celadon_City_Game_Corner_Exit_WP,
        "CeladonCity", 25
    )

    Celadon_City_Links["CELADON_CITY_TO_CELADON_GAME_CORNER_PRIZE_ROOM_1_LINK"] = WarpLink(
        Celadon_City_Warp_Points.Celadon_City_Game_Corner_Prize_Room_Entrance_WP,
        Celadon_Game_Corner_Prize_Room_Warp_Points.Celadon_City_Game_Corner_Prize_Room_Exit_WP,
        "CeladonCity", 30
    )

    Celadon_City_Links["CELADON_CITY_TO_CELADON_GYM_1_LINK"] = WarpLink(
        Celadon_City_Warp_Points.Celadon_City_Gym_Entrance_WP,
        Celadon_Gym_Warp_Points.Celadon_City_Gym_Exit_WP,
        "CeladonCity", 35, locked_by=[Unlock_Keys.CAN_CUT]
    )

    Celadon_City_Links["CELADON_CITY_TO_CELADON_CAFE_1_LINK"] = WarpLink(
        Celadon_City_Warp_Points.Celadon_City_Cafe_Entrance_WP,
        Celadon_Cafe_Warp_Points.Celadon_City_Cafe_Exit_WP,
        "CeladonCity", 40
    )


#######################################################################
#                    Cerulean Group                                   #
#######################################################################



    Bills_House_Links["BILLS_HOUSE_TO_ROUTE_25_1_LINK"] = WarpLink(
        Bills_House_Warp_Points.Bills_House_Exit_WP,
        Route_25_Warp_Points.ROUTE_25_TO_BILLS_HOUSE_1_WP,
        "BillsHouse", dual_width= True
    )



    Cerulean_Gym_Badge_Speech_House_Links["CERULEAN_GYM_BADGE_SPEECH_HOUSE_TO_CERULEAN_CITY_1_LINK"] = WarpLink(
        Cerulean_Gym_Badge_Speech_House_Warp_Points.Cerulean_City_Gym_Badge_Speech_House_Exit_WP,
        Cerulean_City_Warp_Points.Cerulean_City_Gym_Badge_Speech_House_Entrance_WP,
        "CeruleanGymBadgeSpeechHouse", dual_width= True
    )



    Cerulean_Gym_Links["CERULEAN_GYM_TO_CERULEAN_CITY_5_LINK"] = WarpLink(
        Cerulean_Gym_Warp_Points.Cerulean_City_Gym_Exit_WP,
        Cerulean_City_Warp_Points.Cerulean_City_Gym_Entrance_WP,
        "CeruleanGym", dual_width= True, unlocks=[Unlock_Keys.CERULEAN_GYM_ACCESS]
    )



    Cerulean_Mart_Links["CERULEAN_MART_TO_CERULEAN_CITY_6_LINK"] = WarpLink(
        Cerulean_Mart_Warp_Points.Cerulean_City_Mart_Exit_WP,
        Cerulean_City_Warp_Points.Cerulean_City_Mart_Entrance_WP,
        "CeruleanMart", dual_width= True
    )



    Cerulean_Pokecenter_1F_Links["CERULEAN_POKECENTER_1F_TO_CERULEAN_CITY_4_LINK"] = WarpLink(
        Cerulean_Pokecenter_1F_Warp_Points.Cerulean_City_Pokecenter_Exit_WP,
        Cerulean_City_Warp_Points.Cerulean_City_Pokecenter_Entrance_WP,
        "CeruleanPokecenter1F", dual_width= True
    )

    Cerulean_Pokecenter_1F_Links["CERULEAN_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"] = WarpLink(
        Cerulean_Pokecenter_1F_Warp_Points.Cerulean_City_Pokecenter_Stairs_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "CeruleanPokecenter1F", 10
    )




    Cerulean_Police_Station_Links["CERULEAN_POLICE_STATION_TO_CERULEAN_CITY_2_LINK"] = WarpLink(
        Cerulean_Police_Station_Warp_Points.Cerulean_City_Police_Station_Exit_WP,
        Cerulean_City_Warp_Points.Cerulean_City_Police_Station_Entrance_WP,
        "CeruleanPoliceStation", dual_width= True
    )



    Cerulean_Trade_Speech_House_Links["CERULEAN_TRADE_SPEECH_HOUSE_TO_CERULEAN_CITY_3_LINK"] = WarpLink(
        Cerulean_Trade_Speech_House_Warp_Points.Cerulean_City_Trade_Speech_House_Exit_WP,
        Cerulean_City_Warp_Points.Cerulean_City_Trade_Speech_House_Entrance_WP,
        "CeruleanTradeSpeechHouse", dual_width= True
    )



    Power_Plant_Links["POWER_PLANT_TO_ROUTE_10_NORTH_2_LINK"] = WarpLink(
        Power_Plant_Warp_Points.Power_Plant_Exit_WP,
        Route_10_North_Warp_Points.ROUTE_10_NORTH_TO_POWER_PLANT_1_WP,
        "PowerPlant", dual_width= True, unlocks=[Unlock_Keys.POWER_PLANT_ACCESS]
    )




    Cerulean_City_Links["CERULEAN_CITY_TO_CERULEAN_GYM_BADGE_SPEECH_HOUSE_1_LINK"] = WarpLink(
        Cerulean_City_Warp_Points.Cerulean_City_Gym_Badge_Speech_House_Entrance_WP,
        Cerulean_Gym_Badge_Speech_House_Warp_Points.Cerulean_City_Gym_Badge_Speech_House_Exit_WP,
        "CeruleanCity"
    )

    Cerulean_City_Links["CERULEAN_CITY_TO_CERULEAN_POLICE_STATION_1_LINK"] = WarpLink(
        Cerulean_City_Warp_Points.Cerulean_City_Police_Station_Entrance_WP,
        Cerulean_Police_Station_Warp_Points.Cerulean_City_Police_Station_Exit_WP,
        "CeruleanCity", 5
    )

    Cerulean_City_Links["CERULEAN_CITY_TO_CERULEAN_TRADE_SPEECH_HOUSE_1_LINK"] = WarpLink(
        Cerulean_City_Warp_Points.Cerulean_City_Trade_Speech_House_Entrance_WP,
        Cerulean_Trade_Speech_House_Warp_Points.Cerulean_City_Trade_Speech_House_Exit_WP,
        "CeruleanCity", 10
    )

    Cerulean_City_Links["CERULEAN_CITY_TO_CERULEAN_POKECENTER_1F_1_LINK"] = WarpLink(
        Cerulean_City_Warp_Points.Cerulean_City_Pokecenter_Entrance_WP,
        Cerulean_Pokecenter_1F_Warp_Points.Cerulean_City_Pokecenter_Exit_WP,
        "CeruleanCity", 15
    )

    Cerulean_City_Links["CERULEAN_CITY_TO_CERULEAN_GYM_1_LINK"] = WarpLink(
        Cerulean_City_Warp_Points.Cerulean_City_Gym_Entrance_WP,
        Cerulean_Gym_Warp_Points.Cerulean_City_Gym_Exit_WP,
        "CeruleanCity", 20
    )

    Cerulean_City_Links["CERULEAN_CITY_TO_CERULEAN_MART_2_LINK"] = WarpLink(
        Cerulean_City_Warp_Points.Cerulean_City_Mart_Entrance_WP,
        Cerulean_Mart_Warp_Points.Cerulean_City_Mart_Exit_WP,
        "CeruleanCity", 25
    )


#######################################################################
#                    Cinnabar Group                                   #
#######################################################################




    Cinnabar_Pokecenter_1F_Links["CINNABAR_POKECENTER_1F_TO_CINNABAR_ISLAND_1_LINK"] = WarpLink(
        Cinnabar_Pokecenter_1F_Warp_Points.Cinnabar_Island_Pokecenter_Exit_WP,
        Cinnabar_Island_Warp_Points.Cinnabar_Island_Pokecenter_Entrance_WP,
        "CinnabarPokecenter1F", dual_width= True
    )

    Cinnabar_Pokecenter_1F_Links["CINNABAR_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"] = WarpLink(
        Cinnabar_Pokecenter_1F_Warp_Points.Cinnabar_Island_Pokecenter_Stairs_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "CinnabarPokecenter1F", 10
    )




    Seafoam_Gym_Links["SEAFOAM_GYM_TO_ROUTE_20_1_LINK"] = WarpLink(
        Seafoam_Gym_Warp_Points.Seafoam_Gym_Exit_WP,
        Route_20_Warp_Points.ROUTE_20_TO_SEAFOAM_GYM_1_WP,
        "SeafoamGym", unlocks=[Unlock_Keys.BADGE_15]
    )



    Cinnabar_Island_Links["CINNABAR_ISLAND_TO_CINNABAR_POKECENTER_1F_1_LINK"] = WarpLink(
        Cinnabar_Island_Warp_Points.Cinnabar_Island_Pokecenter_Entrance_WP,
        Cinnabar_Pokecenter_1F_Warp_Points.Cinnabar_Island_Pokecenter_Exit_WP,
        "CinnabarIsland", unlocks=[Unlock_Keys.FOUND_BLUE]
    )

#######################################################################
#                    Fuchsia Group                                    #
#######################################################################



    Bills_Brothers_House_Links["BILLS_BROTHERS_HOUSE_TO_FUCHSIA_CITY_4_LINK"] = WarpLink(
        Bills_Brothers_House_Warp_Points.BILLS_BROTHERS_HOUSE_TO_FUCHSIA_CITY_4_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_BILLS_BROTHERS_HOUSE_1_WP,
        "BillsBrothersHouse", dual_width= True
    )



    Fuchsia_Gym_Links["FUCHSIA_GYM_TO_FUCHSIA_CITY_3_LINK"] = WarpLink(
        Fuchsia_Gym_Warp_Points.FUCHSIA_GYM_TO_FUCHSIA_CITY_3_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_FUCHSIA_GYM_1_WP,
        "FuchsiaGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_13]
    )



    Fuchsia_Mart_Links["FUCHSIA_MART_TO_FUCHSIA_CITY_1_LINK"] = WarpLink(
        Fuchsia_Mart_Warp_Points.FUCHSIA_MART_TO_FUCHSIA_CITY_1_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_FUCHSIA_MART_2_WP,
        "FuchsiaMart", dual_width= True
    )



    Fuchsia_Pokecenter_1F_Links["FUCHSIA_POKECENTER_1F_TO_FUCHSIA_CITY_5_LINK"] = WarpLink(
        Fuchsia_Pokecenter_1F_Warp_Points.FUCHSIA_POKECENTER_1F_TO_FUCHSIA_CITY_5_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_FUCHSIA_POKECENTER_1F_1_WP,
        "FuchsiaPokecenter1F", dual_width= True
    )

    Fuchsia_Pokecenter_1F_Links["FUCHSIA_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"] = WarpLink(
        Fuchsia_Pokecenter_1F_Warp_Points.FUCHSIA_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "FuchsiaPokecenter1F", 10
    )



    Safari_Zone_Main_Office_Links["SAFARI_ZONE_MAIN_OFFICE_TO_FUCHSIA_CITY_2_LINK"] = WarpLink(
        Safari_Zone_Main_Office_Warp_Points.SAFARI_ZONE_MAIN_OFFICE_TO_FUCHSIA_CITY_2_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_SAFARI_ZONE_MAIN_OFFICE_1_WP,
        "SafariZoneMainOffice", dual_width= True
    )



    Safari_Zone_Wardens_Home_Links["SAFARI_ZONE_WARDENS_HOME_TO_FUCHSIA_CITY_6_LINK"] = WarpLink(
        Safari_Zone_Wardens_Home_Warp_Points.SAFARI_ZONE_WARDENS_HOME_TO_FUCHSIA_CITY_6_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_SAFARI_ZONE_WARDENS_HOME_1_WP,
        "SafariZoneWardensHome", dual_width= True
    )




    Fuchsia_City_Links["FUCHSIA_CITY_TO_FUCHSIA_MART_2_LINK"] = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_FUCHSIA_MART_2_WP,
        Fuchsia_Mart_Warp_Points.FUCHSIA_MART_TO_FUCHSIA_CITY_1_WP,
        "FuchsiaCity"
    )

    Fuchsia_City_Links["FUCHSIA_CITY_TO_SAFARI_ZONE_MAIN_OFFICE_1_LINK"] = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_SAFARI_ZONE_MAIN_OFFICE_1_WP,
        Safari_Zone_Main_Office_Warp_Points.SAFARI_ZONE_MAIN_OFFICE_TO_FUCHSIA_CITY_2_WP,
        "FuchsiaCity", 5
    )

    Fuchsia_City_Links["FUCHSIA_CITY_TO_FUCHSIA_GYM_1_LINK"] = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_FUCHSIA_GYM_1_WP,
        Fuchsia_Gym_Warp_Points.FUCHSIA_GYM_TO_FUCHSIA_CITY_3_WP,
        "FuchsiaCity", 10
    )

    Fuchsia_City_Links["FUCHSIA_CITY_TO_BILLS_BROTHERS_HOUSE_1_LINK"] = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_BILLS_BROTHERS_HOUSE_1_WP,
        Bills_Brothers_House_Warp_Points.BILLS_BROTHERS_HOUSE_TO_FUCHSIA_CITY_4_WP,
        "FuchsiaCity", 15
    )

    Fuchsia_City_Links["FUCHSIA_CITY_TO_FUCHSIA_POKECENTER_1F_1_LINK"] = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_FUCHSIA_POKECENTER_1F_1_WP,
        Fuchsia_Pokecenter_1F_Warp_Points.FUCHSIA_POKECENTER_1F_TO_FUCHSIA_CITY_5_WP,
        "FuchsiaCity", 20
    )

    Fuchsia_City_Links["FUCHSIA_CITY_TO_SAFARI_ZONE_WARDENS_HOME_1_LINK"] = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_SAFARI_ZONE_WARDENS_HOME_1_WP,
        Safari_Zone_Wardens_Home_Warp_Points.SAFARI_ZONE_WARDENS_HOME_TO_FUCHSIA_CITY_6_WP,
        "FuchsiaCity", 25
    )

    #fuchsia beta safari zone - inaccessible

    Fuchsia_City_Links["FUCHSIA_CITY_TO_ROUTE_15_FUCHSIA_GATE_1_LINK"] = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_ROUTE_15_FUCHSIA_GATE_1_WP,
        Route_15_Fuchsia_Gate_Warp_Points.ROUTE_15_FUCHSIA_GATE_TO_FUCHSIA_CITY_8_WP,
        "FuchsiaCity", 35, dual_width= True
    )

    Fuchsia_City_Links["FUCHSIA_CITY_TO_ROUTE_19_FUCHSIA_GATE_1_LINK"] = WarpLink(
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_ROUTE_19_FUCHSIA_GATE_1_WP,
        Route_19_Fuchsia_Gate_Warp_Points.ROUTE_19_FUCHSIA_GATE_TO_FUCHSIA_CITY_10_WP,
        "FuchsiaCity", 45, dual_width= True
    )



#######################################################################
#                    Lavender Group                                   #
#######################################################################



    Lavender_Mart_Links["LAVENDER_MART_TO_LAVENDER_TOWN_5_LINK"] = WarpLink(
        Lavender_Mart_Warp_Points.LAVENDER_MART_TO_LAVENDER_TOWN_5_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_MART_2_WP,
        "LavenderMart", dual_width= True
    )



    Lavender_Name_Rater_Links["LAVENDER_NAME_RATER_TO_LAVENDER_TOWN_4_LINK"] = WarpLink(
        Lavender_Name_Rater_Warp_Points.LAVENDER_NAME_RATER_TO_LAVENDER_TOWN_4_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_NAME_RATER_1_WP,
        "LavenderNameRater", dual_width= True
    )



    Lavender_Pokecenter_1F_Links["LAVENDER_POKECENTER_1F_TO_LAVENDER_TOWN_1_LINK"] = WarpLink(
        Lavender_Pokecenter_1F_Warp_Points.LAVENDER_POKECENTER_1F_TO_LAVENDER_TOWN_1_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_POKECENTER_1F_1_WP,
        "LavenderPokecenter1F", dual_width= True
    )

    Lavender_Pokecenter_1F_Links["LAVENDER_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"] = WarpLink(
        Lavender_Pokecenter_1F_Warp_Points.LAVENDER_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "LavenderPokecenter1F", 10
    )



    Lavender_Speech_House_Links["LAVENDER_SPEECH_HOUSE_TO_LAVENDER_TOWN_3_LINK"] = WarpLink(
        Lavender_Speech_House_Warp_Points.LAVENDER_SPEECH_HOUSE_TO_LAVENDER_TOWN_3_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_SPEECH_HOUSE_1_WP,
        "LavenderSpeechHouse", dual_width= True
    )



    Lav_Radio_Tower_1F_Links["LAV_RADIO_TOWER_1F_TO_LAVENDER_TOWN_7_LINK"] = WarpLink(
        Lav_Radio_Tower_1F_Warp_Points.LAV_RADIO_TOWER_1F_TO_LAVENDER_TOWN_7_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAV_RADIO_TOWER_1F_1_WP,
        "LavRadioTower1F", dual_width= True, unlocks=[Unlock_Keys.EXPN_CARD],
        locked_by=[Unlock_Keys.MACHINE_PART]
    )



    Mr_Fujis_House_Links["MR_FUJIS_HOUSE_TO_LAVENDER_TOWN_2_LINK"] = WarpLink(
        Mr_Fujis_House_Warp_Points.MR_FUJIS_HOUSE_TO_LAVENDER_TOWN_2_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_MR_FUJIS_HOUSE_1_WP,
        "MrFujisHouse", dual_width= True
    )



    Soul_House_Links["SOUL_HOUSE_TO_LAVENDER_TOWN_6_LINK"] = WarpLink(
        Soul_House_Warp_Points.SOUL_HOUSE_TO_LAVENDER_TOWN_6_WP,
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_SOUL_HOUSE_1_WP,
        "SoulHouse", dual_width= True
    )



    Lavender_Town_Links["LAVENDER_TOWN_TO_LAVENDER_POKECENTER_1F_1_LINK"] = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_POKECENTER_1F_1_WP,
        Lavender_Pokecenter_1F_Warp_Points.LAVENDER_POKECENTER_1F_TO_LAVENDER_TOWN_1_WP,
        "LavenderTown"
    )

    Lavender_Town_Links["LAVENDER_TOWN_TO_MR_FUJIS_HOUSE_1_LINK"] = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_MR_FUJIS_HOUSE_1_WP,
        Mr_Fujis_House_Warp_Points.MR_FUJIS_HOUSE_TO_LAVENDER_TOWN_2_WP,
        "LavenderTown", 5
    )

    Lavender_Town_Links["LAVENDER_TOWN_TO_LAVENDER_SPEECH_HOUSE_1_LINK"] = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_SPEECH_HOUSE_1_WP,
        Lavender_Speech_House_Warp_Points.LAVENDER_SPEECH_HOUSE_TO_LAVENDER_TOWN_3_WP,
        "LavenderTown", 10
    )

    Lavender_Town_Links["LAVENDER_TOWN_TO_LAVENDER_NAME_RATER_1_LINK"] = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_NAME_RATER_1_WP,
        Lavender_Name_Rater_Warp_Points.LAVENDER_NAME_RATER_TO_LAVENDER_TOWN_4_WP,
        "LavenderTown", 15
    )

    Lavender_Town_Links["LAVENDER_TOWN_TO_LAVENDER_MART_2_LINK"] = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAVENDER_MART_2_WP,
        Lavender_Mart_Warp_Points.LAVENDER_MART_TO_LAVENDER_TOWN_5_WP,
        "LavenderTown", 20
    )

    Lavender_Town_Links["LAVENDER_TOWN_TO_SOUL_HOUSE_1_LINK"] = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_SOUL_HOUSE_1_WP,
        Soul_House_Warp_Points.SOUL_HOUSE_TO_LAVENDER_TOWN_6_WP,
        "LavenderTown", 25
    )

    Lavender_Town_Links["LAVENDER_TOWN_TO_LAV_RADIO_TOWER_1F_1_LINK"] = WarpLink(
        Lavender_Town_Warp_Points.LAVENDER_TOWN_TO_LAV_RADIO_TOWER_1F_1_WP,
        Lav_Radio_Tower_1F_Warp_Points.LAV_RADIO_TOWER_1F_TO_LAVENDER_TOWN_7_WP,
        "LavenderTown", 30
    )

#######################################################################
#                    Pallet Group                                     #
#######################################################################



    Blues_House_Links["BLUES_HOUSE_TO_PALLET_TOWN_2_LINK"] = WarpLink(
        Blues_House_Warp_Points.BLUES_HOUSE_TO_PALLET_TOWN_2_WP,
        Pallet_Town_Warp_Points.PALLET_TOWN_TO_BLUES_HOUSE_1_WP,
        "BluesHouse", dual_width= True
    )



    Oaks_Lab_Links["OAKS_LAB_TO_PALLET_TOWN_3_LINK"] = WarpLink(
        Oaks_Lab_Warp_Points.OAKS_LAB_TO_PALLET_TOWN_3_WP,
        Pallet_Town_Warp_Points.PALLET_TOWN_TO_OAKS_LAB_1_WP,
        "OaksLab", dual_width= True, unlocks=[Unlock_Keys.OAKS_LAB_ACCESS]
    )



    Reds_House_1F_Links["REDS_HOUSE_1F_TO_PALLET_TOWN_1_LINK"] = WarpLink(
        Reds_House_1F_Warp_Points.REDS_HOUSE_1F_TO_PALLET_TOWN_1_WP,
        Pallet_Town_Warp_Points.PALLET_TOWN_TO_REDS_HOUSE_1F_1_WP,
        "RedsHouse1F", dual_width= True
    )

    Reds_House_1F_Links["REDS_HOUSE_1F_TO_REDS_HOUSE_2F_1_LINK"] = WarpLink(
        Reds_House_1F_Warp_Points.REDS_HOUSE_1F_TO_REDS_HOUSE_2F_1_WP,
        Reds_House_2F_Warp_Points.REDS_HOUSE_2F_TO_REDS_HOUSE_1F_3_WP,
        "RedsHouse1F", 10
    )



    Reds_House_2F_Links["REDS_HOUSE_2F_TO_REDS_HOUSE_1F_3_LINK"] = WarpLink(
        Reds_House_2F_Warp_Points.REDS_HOUSE_2F_TO_REDS_HOUSE_1F_3_WP,
        Reds_House_1F_Warp_Points.REDS_HOUSE_1F_TO_REDS_HOUSE_2F_1_WP,
        "RedsHouse2F"
    )



    Pallet_Town_Links["PALLET_TOWN_TO_REDS_HOUSE_1F_1_LINK"] = WarpLink(
        Pallet_Town_Warp_Points.PALLET_TOWN_TO_REDS_HOUSE_1F_1_WP,
        Reds_House_1F_Warp_Points.REDS_HOUSE_1F_TO_PALLET_TOWN_1_WP,
        "PalletTown"
    )

    Pallet_Town_Links["PALLET_TOWN_TO_BLUES_HOUSE_1_LINK"] = WarpLink(
        Pallet_Town_Warp_Points.PALLET_TOWN_TO_BLUES_HOUSE_1_WP,
        Blues_House_Warp_Points.BLUES_HOUSE_TO_PALLET_TOWN_2_WP,
        "PalletTown", 5
    )

    Pallet_Town_Links["PALLET_TOWN_TO_OAKS_LAB_1_LINK"] = WarpLink(
        Pallet_Town_Warp_Points.PALLET_TOWN_TO_OAKS_LAB_1_WP,
        Oaks_Lab_Warp_Points.OAKS_LAB_TO_PALLET_TOWN_3_WP,
        "PalletTown", 10
    )


#######################################################################
#                    Pewter Group                                     #
#######################################################################



    Pewter_Gym_Links["PEWTER_GYM_TO_PEWTER_CITY_2_LINK"] = WarpLink(
        Pewter_Gym_Warp_Points.PEWTER_GYM_TO_PEWTER_CITY_2_WP,
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_GYM_1_WP,
        "PewterGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_14]
    )



    Pewter_Mart_Links["PEWTER_MART_TO_PEWTER_CITY_3_LINK"] = WarpLink(
        Pewter_Mart_Warp_Points.PEWTER_MART_TO_PEWTER_CITY_3_WP,
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_MART_2_WP,
        "PewterMart", dual_width= True
    )



    Pewter_Nidoran_Speech_House_Links["PEWTER_NIDORAN_SPEECH_HOUSE_TO_PEWTER_CITY_1_LINK"] = WarpLink(
        Pewter_Nidoran_Speech_House_Warp_Points.PEWTER_NIDORAN_SPEECH_HOUSE_TO_PEWTER_CITY_1_WP,
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_NIDORAN_SPEECH_HOUSE_1_WP,
        "PewterNidoranSpeechHouse", dual_width= True
    )



    Pewter_Snooze_Speech_House_Links["PEWTER_SNOOZE_SPEECH_HOUSE_TO_PEWTER_CITY_5_LINK"] = WarpLink(
        Pewter_Snooze_Speech_House_Warp_Points.PEWTER_SNOOZE_SPEECH_HOUSE_TO_PEWTER_CITY_5_WP,
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_SNOOZE_SPEECH_HOUSE_1_WP,
        "PewterSnoozeSpeechHouse", dual_width= True
    )



    Pewter_Pokecenter_1F_Links["PEWTER_POKECENTER_1F_TO_PEWTER_CITY_4_LINK"] = WarpLink(
        Pewter_Pokecenter_1F_Warp_Points.PEWTER_POKECENTER_1F_TO_PEWTER_CITY_4_WP,
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_POKECENTER_1F_1_WP,
        "PewterPokecenter1F", dual_width= True
    )

    Pewter_Pokecenter_1F_Links["PEWTER_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"] = WarpLink(
        Pewter_Pokecenter_1F_Warp_Points.PEWTER_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "PewterPokecenter1F", 10
    )



    Pewter_City_Links["PEWTER_CITY_TO_PEWTER_NIDORAN_SPEECH_HOUSE_1_LINK"] = WarpLink(
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_NIDORAN_SPEECH_HOUSE_1_WP,
        Pewter_Nidoran_Speech_House_Warp_Points.PEWTER_NIDORAN_SPEECH_HOUSE_TO_PEWTER_CITY_1_WP,
        "PewterCity"
    )

    Pewter_City_Links["PEWTER_CITY_TO_PEWTER_GYM_1_LINK"] = WarpLink(
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_GYM_1_WP,
        Pewter_Gym_Warp_Points.PEWTER_GYM_TO_PEWTER_CITY_2_WP,
        "PewterCity", 5
    )

    Pewter_City_Links["PEWTER_CITY_TO_PEWTER_MART_2_LINK"] = WarpLink(
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_MART_2_WP,
        Pewter_Mart_Warp_Points.PEWTER_MART_TO_PEWTER_CITY_3_WP,
        "PewterCity", 10
    )

    Pewter_City_Links["PEWTER_CITY_TO_PEWTER_POKECENTER_1F_1_LINK"] = WarpLink(
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_POKECENTER_1F_1_WP,
        Pewter_Pokecenter_1F_Warp_Points.PEWTER_POKECENTER_1F_TO_PEWTER_CITY_4_WP,
        "PewterCity", 15
    )

    Pewter_City_Links["PEWTER_CITY_TO_PEWTER_SNOOZE_SPEECH_HOUSE_1_LINK"] = WarpLink(
        Pewter_City_Warp_Points.PEWTER_CITY_TO_PEWTER_SNOOZE_SPEECH_HOUSE_1_WP,
        Pewter_Snooze_Speech_House_Warp_Points.PEWTER_SNOOZE_SPEECH_HOUSE_TO_PEWTER_CITY_5_WP,
        "PewterCity", 20
    )


#######################################################################
#                    Saffron Group                                    #
#######################################################################



    Copycats_House_1F_Links["COPYCATS_HOUSE_1F_TO_SAFFRON_CITY_8_LINK"] = WarpLink(
        Copycats_House_1F_Warp_Points.COPYCATS_HOUSE_1F_TO_SAFFRON_CITY_8_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_COPYCATS_HOUSE_1F_1_WP,
        "CopycatsHouse1F", dual_width= True
    )

    Copycats_House_1F_Links["COPYCATS_HOUSE_1F_TO_COPYCATS_HOUSE_2F_1_LINK"] = WarpLink(
        Copycats_House_1F_Warp_Points.COPYCATS_HOUSE_1F_TO_COPYCATS_HOUSE_2F_1_WP,
        Copycats_House_2F_Warp_Points.COPYCATS_HOUSE_2F_TO_COPYCATS_HOUSE_1F_3_WP,
        "CopycatsHouse1F", 10
    )



    Copycats_House_2F_Links["COPYCATS_HOUSE_2F_TO_COPYCATS_HOUSE_1F_3_LINK"] = WarpLink(
        Copycats_House_2F_Warp_Points.COPYCATS_HOUSE_2F_TO_COPYCATS_HOUSE_1F_3_WP,
        Copycats_House_1F_Warp_Points.COPYCATS_HOUSE_1F_TO_COPYCATS_HOUSE_2F_1_WP,
        "CopycatsHouse2F"
    )



    Fighting_Dojo_Links["FIGHTING_DOJO_TO_SAFFRON_CITY_1_LINK"] = WarpLink(
        Fighting_Dojo_Warp_Points.FIGHTING_DOJO_TO_SAFFRON_CITY_1_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_FIGHTING_DOJO_1_WP,
        "FightingDojo", dual_width= True
    )



    Mr_Psychics_House_Links["MR_PSYCHICS_HOUSE_TO_SAFFRON_CITY_5_LINK"] = WarpLink(
        Mr_Psychics_House_Warp_Points.MR_PSYCHICS_HOUSE_TO_SAFFRON_CITY_5_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_MR_PSYCHICS_HOUSE_1_WP,
        "MrPsychicsHouse", dual_width= True
    )


# <here> warps in gym randomizable too if needed




    Saffron_Gym_Links["SAFFRON_GYM_TO_SAFFRON_CITY_2_LINK"] = WarpLink(
        Saffron_Gym_Warp_Points.SAFFRON_GYM_TO_SAFFRON_CITY_2_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_GYM_1_WP,
        "SaffronGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_10]
    )



    Saffron_Magnet_Train_Station_Links["SAFFRON_MAGNET_TRAIN_STATION_TO_SAFFRON_CITY_6_LINK"] = WarpLink(
        Saffron_Magnet_Train_Station_Warp_Points.SAFFRON_MAGNET_TRAIN_STATION_TO_SAFFRON_CITY_6_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_MAGNET_TRAIN_STATION_2_WP,
        "SaffronMagnetTrainStation", dual_width= True
    )

#We don't randomize magnet train
    #["SAFFRON_MAGNET_TRAIN_STATION_TO_GOLDENROD_MAGNET_TRAIN_STATION_4_LINK"]= WarpLink(
    #    Saffron_Magnet_Train_Station_Warp_Points.SAFFRON_MAGNET_TRAIN_STATION_TO_GOLDENROD_MAGNET_TRAIN_STATION_4_WP,
    #    Celadon_City_Warp_Points.CELADON_CITY_TO_CELADON_CAFE_1_WP,
    #    "SaffronMagnetTrainStation", 10, dual_width= True
    #)



    Saffron_Mart_Links["SAFFRON_MART_TO_SAFFRON_CITY_3_LINK"] = WarpLink(
        Saffron_Mart_Warp_Points.SAFFRON_MART_TO_SAFFRON_CITY_3_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_MART_2_WP,
        "SaffronMart", dual_width= True
    )



    Saffron_Pokecenter_1F_Links["SAFFRON_POKECENTER_1F_TO_SAFFRON_CITY_4_LINK"] = WarpLink(
        Saffron_Pokecenter_1F_Warp_Points.SAFFRON_POKECENTER_1F_TO_SAFFRON_CITY_4_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_POKECENTER_1F_1_WP,
        "SaffronPokecenter1F", dual_width= True
    )

    Saffron_Pokecenter_1F_Links["SAFFRON_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"] = WarpLink(
        Saffron_Pokecenter_1F_Warp_Points.SAFFRON_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "SaffronPokecenter1F", 10
    )



    Silph_Co_1F_Links["SILPH_CO_1F_TO_SAFFRON_CITY_7_LINK"] = WarpLink(
        Silph_Co_1F_Warp_Points.SILPH_CO_1F_TO_SAFFRON_CITY_7_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SILPH_CO_1F_1_WP,
        "SilphCo1F", dual_width= True
    )



    Saffron_City_Links["SAFFRON_CITY_TO_FIGHTING_DOJO_1_LINK"] = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_FIGHTING_DOJO_1_WP,
        Fighting_Dojo_Warp_Points.FIGHTING_DOJO_TO_SAFFRON_CITY_1_WP,
        "SaffronCity"
    )

    Saffron_City_Links["SAFFRON_CITY_TO_SAFFRON_GYM_1_LINK"] = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_GYM_1_WP,
        Saffron_Gym_Warp_Points.SAFFRON_GYM_TO_SAFFRON_CITY_2_WP,
        "SaffronCity", 5
    )

    Saffron_City_Links["SAFFRON_CITY_TO_SAFFRON_MART_2_LINK"] = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_MART_2_WP,
        Saffron_Mart_Warp_Points.SAFFRON_MART_TO_SAFFRON_CITY_3_WP,
        "SaffronCity", 10
    )

    Saffron_City_Links["SAFFRON_CITY_TO_SAFFRON_POKECENTER_1F_1_LINK"] = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_POKECENTER_1F_1_WP,
        Saffron_Pokecenter_1F_Warp_Points.SAFFRON_POKECENTER_1F_TO_SAFFRON_CITY_4_WP,
        "SaffronCity", 15
    )

    Saffron_City_Links["SAFFRON_CITY_TO_MR_PSYCHICS_HOUSE_1_LINK"] = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_MR_PSYCHICS_HOUSE_1_WP,
        Mr_Psychics_House_Warp_Points.MR_PSYCHICS_HOUSE_TO_SAFFRON_CITY_5_WP,
        "SaffronCity", 20
    )

    Saffron_City_Links["SAFFRON_CITY_TO_SAFFRON_MAGNET_TRAIN_STATION_2_LINK"] = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SAFFRON_MAGNET_TRAIN_STATION_2_WP,
        Saffron_Magnet_Train_Station_Warp_Points.SAFFRON_MAGNET_TRAIN_STATION_TO_SAFFRON_CITY_6_WP,
        "SaffronCity", 25
    )

    Saffron_City_Links["SAFFRON_CITY_TO_SILPH_CO_1F_1_LINK"] = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_SILPH_CO_1F_1_WP,
        Silph_Co_1F_Warp_Points.SILPH_CO_1F_TO_SAFFRON_CITY_7_WP,
        "SaffronCity", 30
    )

    Saffron_City_Links["SAFFRON_CITY_TO_COPYCATS_HOUSE_1F_1_LINK"] = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_COPYCATS_HOUSE_1F_1_WP,
        Copycats_House_1F_Warp_Points.COPYCATS_HOUSE_1F_TO_SAFFRON_CITY_8_WP,
        "SaffronCity", 35
    )

    Saffron_City_Links["SAFFRON_CITY_TO_ROUTE_5_SAFFRON_GATE_3_LINK"] = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_5_SAFFRON_GATE_3_WP,
        Route_5_Saffron_Gate_Warp_Points.ROUTE_5_SAFFRON_GATE_TO_SAFFRON_CITY_9_WP,
        "SaffronCity", 40
    )

    Saffron_City_Links["SAFFRON_CITY_TO_ROUTE_7_SAFFRON_GATE_3_LINK"] = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_7_SAFFRON_GATE_3_WP,
        Route_7_Saffron_Gate_Warp_Points.ROUTE_7_SAFFRON_GATE_TO_SAFFRON_CITY_10_WP,
        "SaffronCity", 45, dual_width= True
    )

    Saffron_City_Links["SAFFRON_CITY_TO_ROUTE_6_SAFFRON_GATE_1_LINK"] = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_6_SAFFRON_GATE_1_WP,
        Route_6_Saffron_Gate_Warp_Points.ROUTE_6_SAFFRON_GATE_TO_SAFFRON_CITY_12_WP,
        "SaffronCity", 55, dual_width= True
    )

    Saffron_City_Links["SAFFRON_CITY_TO_ROUTE_8_SAFFRON_GATE_1_LINK"] = WarpLink(
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_8_SAFFRON_GATE_1_WP,
        Route_8_Saffron_Gate_Warp_Points.ROUTE_8_SAFFRON_GATE_TO_SAFFRON_CITY_14_WP,
        "SaffronCity", 65, dual_width= True
    )


#######################################################################
#                    Vermillion Group                                 #
#######################################################################



    Pokemon_Fan_Club_Links["POKEMON_FAN_CLUB_TO_VERMILION_CITY_3_LINK"] = WarpLink(
        Pokemon_Fan_Club_Warp_Points.Pokemon_Fan_Club_Exit_WP,
        Vermilion_City_Warp_Points.Pokemon_Fan_Club_Entrance_WP,
        "PokemonFanClub", dual_width= True
    )



    Vermilion_Digletts_Cave_Speech_House_Links["VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_TO_VERMILION_CITY_6_LINK"] = WarpLink(
        Vermilion_Digletts_Cave_Speech_House_Warp_Points.Vermilion_City_Digletts_Cave_Speech_House_Exit_WP,
        Vermilion_City_Warp_Points.Vermilion_City_Digletts_Cave_Speech_House_Entrance_WP,
        "VermilionDiglettsCaveSpeechHouse", dual_width= True
    )



    Vermilion_Fishing_Speech_House_Links["VERMILION_FISHING_SPEECH_HOUSE_TO_VERMILION_CITY_1_LINK"] = WarpLink(
        Vermilion_Fishing_Speech_House_Warp_Points.Vermilion_City_Fishing_Speech_House_Exit_WP,
        Vermilion_City_Warp_Points.Vermilion_City_Fishing_Speech_House_Entrance_WP,
        "VermilionFishingSpeechHouse", dual_width= True
    )



    Vermilion_Gym_Links["VERMILION_GYM_TO_VERMILION_CITY_7_LINK"] = WarpLink(
        Vermilion_Gym_Warp_Points.Vermilion_City_Gym_Exit_WP,
        Vermilion_City_Warp_Points.Vermilion_City_Gym_Entrance_WP,
        "VermilionGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_9]
    )



    Vermilion_Magnet_Train_Speech_House_Links["VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_TO_VERMILION_CITY_4_LINK"] = WarpLink(
        Vermilion_Magnet_Train_Speech_House_Warp_Points.Vermilion_City_Magnet_Train_Speech_House_Exit_WP,
        Vermilion_City_Warp_Points.Vermilion_City_Magnet_Train_Speech_House_Entrance_WP,
        "VermilionMagnetTrainSpeechHouse", dual_width= True
    )



    Vermilion_Mart_Links["VERMILION_MART_TO_VERMILION_CITY_5_LINK"] = WarpLink(
        Vermilion_Mart_Warp_Points.Vermilion_City_Mart_Exit_WP,
        Vermilion_City_Warp_Points.Vermilion_City_Mart_Entrance_WP,
        "VermilionMart", dual_width= True
    )



    Vermilion_Pokecenter_1F_Links["VERMILION_POKECENTER_1F_TO_VERMILION_CITY_2_LINK"] = WarpLink(
        Vermilion_Pokecenter_1F_Warp_Points.Vermilion_City_Pokecenter_Exit_WP,
        Vermilion_City_Warp_Points.Vermilion_City_Pokecenter_Entrance_WP,
        "VermilionPokecenter1F", dual_width= True
    )

    Vermilion_Pokecenter_1F_Links["VERMILION_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"] = WarpLink(
        Vermilion_Pokecenter_1F_Warp_Points.Vermilion_City_Pokecenter_Stairs_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "VermilionPokecenter1F", 10
    )



    Vermilion_Port_Links["VERMILION_PORT_TO_VERMILION_PORT_PASSAGE_5_LINK"] = WarpLink(
        Vermilion_Port_Warp_Points.Vermilion_Port_To_Port_Passage_WP,
        Vermilion_Port_Passage_Warp_Points.Vermilion_Port_Passage_To_Vermilion_Port_WP,
        "VermilionPort"
    )

#We dont randomize ship entrance/exit
    #["VERMILION_PORT_TO_FAST_SHIP_1F_1_LINK"]= WarpLink(
    #    Vermilion_Port_Warp_Points.Vermilion_Port_To_Fast_Ship_WP,
    #    Vermilion_City_Warp_Points.VERMILION_CITY_TO_VERMILION_POKECENTER_1F_1_WP,
    #    "VermilionPort", 5
    #)


 # 1-3,4-5

    Vermilion_Port_Passage_Links["VERMILION_PORT_PASSAGE_TO_VERMILION_CITY_8_LINK"] = WarpLink(
        Vermilion_Port_Passage_Warp_Points.Vermilion_Upper_Port_Passage_To_Vermilion_City_WP,
        Vermilion_City_Warp_Points.Vermilion_City_To_Port_Passage_WP,
        "VermilionPortPassage", dual_width= True
    )

    Vermilion_Port_Passage_Links["VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_PASSAGE_4_LINK"] = WarpLink(
        Vermilion_Port_Passage_Warp_Points.Vermilion_Upper_Port_Passage_To_Underground_Passage_North_WP,
        Vermilion_Port_Passage_Warp_Points.Vermilion_Underground_Passage_North_To_Upper_Port_Passage_WP,
        "VermilionPortPassage", 10
    )

    Vermilion_Port_Passage_Links["VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_PASSAGE_3_LINK"] = WarpLink(
        Vermilion_Port_Passage_Warp_Points.Vermilion_Underground_Passage_North_To_Upper_Port_Passage_WP,
        Vermilion_Port_Passage_Warp_Points.Vermilion_Upper_Port_Passage_To_Underground_Passage_North_WP,
        "VermilionPortPassage", 15
    )

    Vermilion_Port_Passage_Links["VERMILION_PORT_PASSAGE_TO_VERMILION_PORT_1_LINK"] = WarpLink(
        Vermilion_Port_Passage_Warp_Points.Vermilion_Port_Passage_To_Vermilion_Port_WP,
        Vermilion_Port_Warp_Points.Vermilion_Port_To_Port_Passage_WP,
        "VermilionPortPassage", 20
    )





    Vermilion_City_Links["VERMILION_CITY_TO_VERMILION_FISHING_SPEECH_HOUSE_1_LINK"] = WarpLink(
        Vermilion_City_Warp_Points.Vermilion_City_Fishing_Speech_House_Entrance_WP,
        Vermilion_Fishing_Speech_House_Warp_Points.Vermilion_City_Fishing_Speech_House_Exit_WP,
        "VermilionCity"
    )

    Vermilion_City_Links["VERMILION_CITY_TO_VERMILION_POKECENTER_1F_1_LINK"] = WarpLink(
        Vermilion_City_Warp_Points.Vermilion_City_Pokecenter_Entrance_WP,
        Vermilion_Pokecenter_1F_Warp_Points.Vermilion_City_Pokecenter_Exit_WP,
        "VermilionCity", 5
    )

    Vermilion_City_Links["VERMILION_CITY_TO_POKEMON_FAN_CLUB_1_LINK"] = WarpLink(
        Vermilion_City_Warp_Points.Pokemon_Fan_Club_Entrance_WP,
        Pokemon_Fan_Club_Warp_Points.Pokemon_Fan_Club_Exit_WP,
        "VermilionCity", 10
    )

    Vermilion_City_Links["VERMILION_CITY_TO_VERMILION_MAGNET_TRAIN_SPEECH_HOUSE_1_LINK"] = WarpLink(
        Vermilion_City_Warp_Points.Vermilion_City_Magnet_Train_Speech_House_Entrance_WP,
        Vermilion_Magnet_Train_Speech_House_Warp_Points.Vermilion_City_Magnet_Train_Speech_House_Exit_WP,
        "VermilionCity", 15
    )

    Vermilion_City_Links["VERMILION_CITY_TO_VERMILION_MART_2_LINK"] = WarpLink(
        Vermilion_City_Warp_Points.Vermilion_City_Mart_Entrance_WP,
        Vermilion_Mart_Warp_Points.Vermilion_City_Mart_Exit_WP,
        "VermilionCity", 20
    )

    Vermilion_City_Links["VERMILION_CITY_TO_VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE_1_LINK"] = WarpLink(
        Vermilion_City_Warp_Points.Vermilion_City_Digletts_Cave_Speech_House_Entrance_WP,
        Vermilion_Digletts_Cave_Speech_House_Warp_Points.Vermilion_City_Digletts_Cave_Speech_House_Exit_WP,
        "VermilionCity", 25
    )

    Vermilion_City_Links["VERMILION_CITY_TO_VERMILION_GYM_1_LINK"] = WarpLink(
        Vermilion_City_Warp_Points.Vermilion_City_Gym_Entrance_WP,
        Vermilion_Gym_Warp_Points.Vermilion_City_Gym_Exit_WP,
        "VermilionCity", 30, locked_by=[Unlock_Keys.CAN_SURF_OR_CUT]
    )

    Vermilion_City_Links["VERMILION_CITY_TO_VERMILION_PORT_PASSAGE_1_LINK"] = WarpLink(
        Vermilion_City_Warp_Points.Vermilion_City_To_Port_Passage_WP,
        Vermilion_Port_Passage_Warp_Points.Vermilion_Upper_Port_Passage_To_Vermilion_City_WP,
        "VermilionCity", 35, dual_width= True
    )

    Vermilion_City_Links["VERMILION_CITY_TO_DIGLETTS_CAVE_1_LINK"] = WarpLink(
        Vermilion_City_Warp_Points.Vermilion_City_Digletts_Cave_Entrance_WP,
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_VERMILION_CITY_10_WP,
        "VermilionCity", 45, locked_by=[Unlock_Keys.EXPN_CARD, Unlock_Keys.RADIO_CARD]
    )


#######################################################################
#                    Viridian Group                                   #
#######################################################################



    Route_2_Nugget_House_Links["ROUTE_2_NUGGET_HOUSE_TO_ROUTE_2_1_LINK"] = WarpLink(
        Route_2_Nugget_House_Warp_Points.Route_2_Nugget_House_Exit_WP,
        Route_2_Warp_Points.ROUTE_2_TO_ROUTE_2_NUGGET_HOUSE_1_WP,
        "Route2NuggetHouse", dual_width= True
    )



    Trainer_House_1F_Links["TRAINER_HOUSE_1F_TO_VIRIDIAN_CITY_3_LINK"] = WarpLink(
        Trainer_House_1F_Warp_Points.Trainer_House_1F_Exit_WP,
        Viridian_City_Warp_Points.Trainer_House_Entrance_WP,
        "TrainerHouse1F", dual_width= True
    )

    Trainer_House_1F_Links["TRAINER_HOUSE_1F_TO_TRAINER_HOUSE_B1F_1_LINK"] = WarpLink(
        Trainer_House_1F_Warp_Points.Trainer_House_1F_Stairs_WP,
        Trainer_House_B1F_Warp_Points.Trainer_House_B1F_Stairs_WP,
        "TrainerHouse1F", 10
    )



    Trainer_House_B1F_Links["TRAINER_HOUSE_B1F_TO_TRAINER_HOUSE_1F_3_LINK"] = WarpLink(
        Trainer_House_B1F_Warp_Points.Trainer_House_B1F_Stairs_WP,
        Trainer_House_1F_Warp_Points.Trainer_House_1F_Stairs_WP,
        "TrainerHouseB1F"
    )



    Viridian_Gym_Links["VIRIDIAN_GYM_TO_VIRIDIAN_CITY_1_LINK"] = WarpLink(
        Viridian_Gym_Warp_Points.Viridian_City_Gym_Exit_WP,
        Viridian_City_Warp_Points.Viridian_City_Gym_Entrance_WP,
        "ViridianGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_16],
        locked_by=[Unlock_Keys.FOUND_BLUE]
    )



    Viridian_Mart_Links["VIRIDIAN_MART_TO_VIRIDIAN_CITY_4_LINK"] = WarpLink(
        Viridian_Mart_Warp_Points.Viridian_City_Mart_Exit_WP,
        Viridian_City_Warp_Points.Viridian_City_Mart_Entrance_WP,
        "ViridianMart", dual_width= True
    )



    Viridian_Nickname_Speech_House_Links["VIRIDIAN_NICKNAME_SPEECH_HOUSE_TO_VIRIDIAN_CITY_2_LINK"] = WarpLink(
        Viridian_Nickname_Speech_House_Warp_Points.Viridian_City_Nickname_Speech_House_Exit_WP,
        Viridian_City_Warp_Points.Viridian_City_Nickname_Speech_House_Entrance_WP,
        "ViridianNicknameSpeechHouse", dual_width= True
    )



    Viridian_Pokecenter_1F_Links["VIRIDIAN_POKECENTER_1F_TO_VIRIDIAN_CITY_5_LINK"] = WarpLink(
        Viridian_Pokecenter_1F_Warp_Points.Viridian_City_Pokecenter_Exit_WP,
        Viridian_City_Warp_Points.Viridian_City_Pokecenter_Entrance_WP,
        "ViridianPokecenter1F", dual_width= True
    )

    Viridian_Pokecenter_1F_Links["VIRIDIAN_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"] = WarpLink(
        Viridian_Pokecenter_1F_Warp_Points.Viridian_City_Pokecenter_Stairs_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "ViridianPokecenter1F", 10
    )



    Viridian_City_Links["VIRIDIAN_CITY_TO_VIRIDIAN_GYM_1_LINK"] = WarpLink(
        Viridian_City_Warp_Points.Viridian_City_Gym_Entrance_WP,
        Viridian_Gym_Warp_Points.Viridian_City_Gym_Exit_WP,
        "ViridianCity"
    )

    Viridian_City_Links["VIRIDIAN_CITY_TO_VIRIDIAN_NICKNAME_SPEECH_HOUSE_1_LINK"] = WarpLink(
        Viridian_City_Warp_Points.Viridian_City_Nickname_Speech_House_Entrance_WP,
        Viridian_Nickname_Speech_House_Warp_Points.Viridian_City_Nickname_Speech_House_Exit_WP,
        "ViridianCity", 5
    )

    Viridian_City_Links["VIRIDIAN_CITY_TO_TRAINER_HOUSE_1F_1_LINK"] = WarpLink(
        Viridian_City_Warp_Points.Trainer_House_Entrance_WP,
        Trainer_House_1F_Warp_Points.Trainer_House_1F_Exit_WP,
        "ViridianCity", 10
    )

    Viridian_City_Links["VIRIDIAN_CITY_TO_VIRIDIAN_MART_2_LINK"] = WarpLink(
        Viridian_City_Warp_Points.Viridian_City_Mart_Entrance_WP,
        Viridian_Mart_Warp_Points.Viridian_City_Mart_Exit_WP,
        "ViridianCity", 15
    )

    Viridian_City_Links["VIRIDIAN_CITY_TO_VIRIDIAN_POKECENTER_1F_1_LINK"] = WarpLink(
        Viridian_City_Warp_Points.Viridian_City_Pokecenter_Entrance_WP,
        Viridian_Pokecenter_1F_Warp_Points.Viridian_City_Pokecenter_Exit_WP,
        "ViridianCity", 20
    )



#######################################################################
#                    Kanto_Dungeons Group                             #
#######################################################################


 # 1-2,3-4,5-6

    Digletts_Cave_Links["DIGLETTS_CAVE_TO_VERMILION_CITY_10_LINK"] = WarpLink(
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_VERMILION_CITY_10_WP,
        Vermilion_City_Warp_Points.Vermilion_City_Digletts_Cave_Entrance_WP,
        "DiglettsCave"
    )

    Digletts_Cave_Links["DIGLETTS_CAVE_TO_DIGLETTS_CAVE_5_LINK"] = WarpLink(
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_5_WP,
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_2_WP,
        "DiglettsCave", 5
    )

    Digletts_Cave_Links["DIGLETTS_CAVE_TO_ROUTE_2_5_LINK"] = WarpLink(
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_ROUTE_2_5_WP,
        Route_2_Warp_Points.ROUTE_2_TO_DIGLETTS_CAVE_3_WP,
        "DiglettsCave", 10
    )

    Digletts_Cave_Links["DIGLETTS_CAVE_TO_DIGLETTS_CAVE_6_LINK"] = WarpLink(
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_6_WP,
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_4_WP,
        "DiglettsCave", 15
    )

    Digletts_Cave_Links["DIGLETTS_CAVE_TO_DIGLETTS_CAVE_2_LINK"] = WarpLink(
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_2_WP,
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_5_WP,
        "DiglettsCave", 20
    )

    Digletts_Cave_Links["DIGLETTS_CAVE_TO_DIGLETTS_CAVE_4_LINK"] = WarpLink(
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_4_WP,
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_DIGLETTS_CAVE_6_WP,
        "DiglettsCave", 25
    )





    Mount_Moon_Gift_Shop_Links["MOUNT_MOON_TO_ROUTE_3_1_LINK"] = WarpLink(
        Mount_Moon_Gift_Shop_Warp_Points.MOUNT_MOON_GIFT_SHOP_TO_MOUNT_MOON_SQUARE_3_WP,
        Mount_Moon_Square_Warp_Points.MOUNT_MOON_SQUARE_TO_MOUNT_MOON_GIFT_SHOP_1_WP,
        "MountMoonGiftShop", dual_width= True
    )


 # 1-2-3 hub, 4 ledge, 5-7, 6-8

    Mount_Moon_Links["MOUNT_MOON_TO_ROUTE_3_1_LINK"] = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_ROUTE_3_1_WP,
        Route_3_Warp_Points.ROUTE_3_TO_MOUNT_MOON_1_WP,
        "MountMoon"
    )

    Mount_Moon_Links["MOUNT_MOON_TO_ROUTE_4_1_LINK"] = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_ROUTE_4_1_WP,
        Route_4_Warp_Points.ROUTE_4_TO_MOUNT_MOON_2_WP,
        "MountMoon", 5
    )

    Mount_Moon_Links["MOUNT_MOON_TO_MOUNT_MOON_7_LINK"] = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_7_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_3_WP,
        "MountMoon", 10
    )

    Mount_Moon_Links["MOUNT_MOON_TO_MOUNT_MOON_8_LINK"] = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_8_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_4_WP,
        "MountMoon", 15
    )

    Mount_Moon_Links["MOUNT_MOON_TO_MOUNT_MOON_SQUARE_1_LINK"] = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_SQUARE_1_WP,
        Mount_Moon_Square_Warp_Points.MOUNT_MOON_SQUARE_TO_MOUNT_MOON_5_WP,
        "MountMoon", 20
    )

    Mount_Moon_Links["MOUNT_MOON_TO_MOUNT_MOON_SQUARE_2_LINK"] = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_SQUARE_2_WP,
        Mount_Moon_Square_Warp_Points.MOUNT_MOON_SQUARE_TO_MOUNT_MOON_6_WP,
        "MountMoon", 25
    )

    Mount_Moon_Links["MOUNT_MOON_TO_MOUNT_MOON_3_LINK"] = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_3_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_7_WP,
        "MountMoon", 30
    )

    Mount_Moon_Links["MOUNT_MOON_TO_MOUNT_MOON_4_LINK"] = WarpLink(
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_4_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_8_WP,
        "MountMoon", 35
    )




    Mount_Moon_Square_Links["MOUNT_MOON_SQUARE_TO_MOUNT_MOON_5_LINK"] = WarpLink(
        Mount_Moon_Square_Warp_Points.MOUNT_MOON_SQUARE_TO_MOUNT_MOON_5_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_SQUARE_1_WP,
        "MountMoonSquare"
    )

    Mount_Moon_Square_Links["MOUNT_MOON_SQUARE_TO_MOUNT_MOON_6_LINK"] = WarpLink(
        Mount_Moon_Square_Warp_Points.MOUNT_MOON_SQUARE_TO_MOUNT_MOON_6_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_MOUNT_MOON_SQUARE_2_WP,
        "MountMoonSquare", 5
    )

    Mount_Moon_Square_Links["MOUNT_MOON_SQUARE_TO_MOUNT_MOON_GIFT_SHOP_1_LINK"] = WarpLink(
        Mount_Moon_Square_Warp_Points.MOUNT_MOON_SQUARE_TO_MOUNT_MOON_GIFT_SHOP_1_WP,
        Mount_Moon_Gift_Shop_Warp_Points.MOUNT_MOON_GIFT_SHOP_TO_MOUNT_MOON_SQUARE_3_WP,
        "MountMoonSquare", 10
    )


 # 1-5, 2-6, 3,4

    Rock_Tunnel_1F_Links["ROCK_TUNNEL_1F_TO_ROUTE_9_1_LINK"] = WarpLink(
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROUTE_9_1_WP,
        Route_9_Warp_Points.ROUTE_9_TO_ROCK_TUNNEL_1F_1_WP,
        "RockTunnel1F"
    )

    Rock_Tunnel_1F_Links["ROCK_TUNNEL_1F_TO_ROUTE_10_SOUTH_1_LINK"] = WarpLink(
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROUTE_10_SOUTH_1_WP,
        Route_10_South_Warp_Points.ROUTE_10_SOUTH_TO_ROCK_TUNNEL_1F_2_WP,
        "RockTunnel1F", 5
    )

    Rock_Tunnel_1F_Links["ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_3_LINK"] = WarpLink(
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_3_WP,
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_3_WP,
        "RockTunnel1F", 10
    )

    Rock_Tunnel_1F_Links["ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_2_LINK"] = WarpLink(
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_2_WP,
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_4_WP,
        "RockTunnel1F", 15
    )

    Rock_Tunnel_1F_Links["ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_4_LINK"] = WarpLink(
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_4_WP,
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_5_WP,
        "RockTunnel1F", 20
    )

    Rock_Tunnel_1F_Links["ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_1_LINK"] = WarpLink(
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_1_WP,
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_6_WP,
        "RockTunnel1F", 25
    )


 # 1-2, 3-4

    Rock_Tunnel_B1F_Links["ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_6_LINK"] = WarpLink(
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_6_WP,
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_1_WP,
        "RockTunnelB1F"
    )

    Rock_Tunnel_B1F_Links["ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_4_LINK"] = WarpLink(
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_4_WP,
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_2_WP,
        "RockTunnelB1F", 5
    )

    Rock_Tunnel_B1F_Links["ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_3_LINK"] = WarpLink(
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_3_WP,
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_3_WP,
        "RockTunnelB1F", 10
    )

    Rock_Tunnel_B1F_Links["ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_5_LINK"] = WarpLink(
        Rock_Tunnel_B1F_Warp_Points.ROCK_TUNNEL_B1F_TO_ROCK_TUNNEL_1F_5_WP,
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROCK_TUNNEL_B1F_4_WP,
        "RockTunnelB1F", 15
    )



    Underground_Path_Links["UNDERGROUND_PATH_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_3_LINK"] = WarpLink(
        Underground_Path_Warp_Points.UNDERGROUND_PATH_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_3_WP,
        Route_5_Underground_Path_Entrance_Warp_Points.ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_1_WP,
        "UndergroundPath"
    )

    Underground_Path_Links["UNDERGROUND_PATH_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_3_LINK"] = WarpLink(
        Underground_Path_Warp_Points.UNDERGROUND_PATH_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_3_WP,
        Route_6_Underground_Path_Entrance_Warp_Points.ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_2_WP,
        "UndergroundPath", 5
    )



#######################################################################
#                    Kanto_Gates Group                                      #
#######################################################################

 # 1 top, 2 bottom

    Route_2_Gate_Links["ROUTE_2_GATE_TO_ROUTE_2_3_LINK"] = WarpLink(
        Route_2_Gate_Warp_Points.ROUTE_2_GATE_TO_ROUTE_2_3_WP,
        Route_2_Warp_Points.ROUTE_2_TO_ROUTE_2_GATE_1_WP,
        "Route2Gate", dual_width= True
    )

    Route_2_Gate_Links["ROUTE_2_GATE_TO_ROUTE_2_2_LINK"] = WarpLink(
        Route_2_Gate_Warp_Points.ROUTE_2_GATE_TO_ROUTE_2_2_WP,
        Route_2_Warp_Points.ROUTE_2_TO_ROUTE_2_GATE_3_WP,
        "Route2Gate", 10, dual_width= True
    )

 # 1 top 2 bottom

    Route_5_Saffron_Gate_Links["ROUTE_5_SAFFRON_GATE_TO_ROUTE_5_2_LINK"] = WarpLink(
        Route_5_Saffron_Gate_Warp_Points.ROUTE_5_SAFFRON_GATE_TO_ROUTE_5_2_WP,
        Route_5_Warp_Points.ROUTE_5_TO_ROUTE_5_SAFFRON_GATE_1_WP,
        "Route5SaffronGate", dual_width= True
    )

    Route_5_Saffron_Gate_Links["ROUTE_5_SAFFRON_GATE_TO_SAFFRON_CITY_9_LINK"] = WarpLink(
        Route_5_Saffron_Gate_Warp_Points.ROUTE_5_SAFFRON_GATE_TO_SAFFRON_CITY_9_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_5_SAFFRON_GATE_3_WP,
        "Route5SaffronGate", 10, dual_width= True
    )

 # 1 top, 2 bottom

    Route_6_Saffron_Gate_Links["ROUTE_6_SAFFRON_GATE_TO_SAFFRON_CITY_12_LINK"] = WarpLink(
        Route_6_Saffron_Gate_Warp_Points.ROUTE_6_SAFFRON_GATE_TO_SAFFRON_CITY_12_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_6_SAFFRON_GATE_1_WP,
        "Route6SaffronGate", dual_width= True
    )

    Route_6_Saffron_Gate_Links["ROUTE_6_SAFFRON_GATE_TO_ROUTE_6_2_LINK"] = WarpLink(
        Route_6_Saffron_Gate_Warp_Points.ROUTE_6_SAFFRON_GATE_TO_ROUTE_6_2_WP,
        Route_6_Warp_Points.ROUTE_6_TO_ROUTE_6_SAFFRON_GATE_3_WP,
        "Route6SaffronGate", 10, dual_width= True
    )

 # 1 right, 2 left

    Route_7_Saffron_Gate_Links["ROUTE_7_SAFFRON_GATE_TO_ROUTE_7_1_LINK"] = WarpLink(
        Route_7_Saffron_Gate_Warp_Points.ROUTE_7_SAFFRON_GATE_TO_ROUTE_7_1_WP,
        Route_7_Warp_Points.ROUTE_7_TO_ROUTE_7_SAFFRON_GATE_1_WP,
        "Route7SaffronGate", dual_width= True
    )

    Route_7_Saffron_Gate_Links["ROUTE_7_SAFFRON_GATE_TO_SAFFRON_CITY_10_LINK"] = WarpLink(
        Route_7_Saffron_Gate_Warp_Points.ROUTE_7_SAFFRON_GATE_TO_SAFFRON_CITY_10_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_7_SAFFRON_GATE_3_WP,
        "Route7SaffronGate", 10, dual_width= True
    )

 # 1 right, 2 left

    Route_8_Saffron_Gate_Links["ROUTE_8_SAFFRON_GATE_TO_SAFFRON_CITY_14_LINK"] = WarpLink(
        Route_8_Saffron_Gate_Warp_Points.ROUTE_8_SAFFRON_GATE_TO_SAFFRON_CITY_14_WP,
        Saffron_City_Warp_Points.SAFFRON_CITY_TO_ROUTE_8_SAFFRON_GATE_1_WP,
        "Route8SaffronGate", dual_width= True
    )

    Route_8_Saffron_Gate_Links["ROUTE_8_SAFFRON_GATE_TO_ROUTE_8_1_LINK"] = WarpLink(
        Route_8_Saffron_Gate_Warp_Points.ROUTE_8_SAFFRON_GATE_TO_ROUTE_8_1_WP,
        Route_8_Warp_Points.ROUTE_8_TO_ROUTE_8_SAFFRON_GATE_3_WP,
        "Route8SaffronGate", 10, dual_width= True
    )

 # 1 left, 2 right

    Route_15_Fuchsia_Gate_Links["ROUTE_15_FUCHSIA_GATE_TO_FUCHSIA_CITY_8_LINK"] = WarpLink(
        Route_15_Fuchsia_Gate_Warp_Points.ROUTE_15_FUCHSIA_GATE_TO_FUCHSIA_CITY_8_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_ROUTE_15_FUCHSIA_GATE_1_WP,
        "Route15FuchsiaGate", dual_width= True
    )

    Route_15_Fuchsia_Gate_Links["ROUTE_15_FUCHSIA_GATE_TO_ROUTE_15_1_LINK"] = WarpLink(
        Route_15_Fuchsia_Gate_Warp_Points.ROUTE_15_FUCHSIA_GATE_TO_ROUTE_15_1_WP,
        Route_15_Warp_Points.ROUTE_15_TO_ROUTE_15_FUCHSIA_GATE_3_WP,
        "Route15FuchsiaGate", 10, dual_width= True
    )

 # 1 left, 2 right

    Route_16_Gate_Links["ROUTE_16_GATE_TO_ROUTE_16_4_LINK"] = WarpLink(
        Route_16_Gate_Warp_Points.ROUTE_16_GATE_TO_ROUTE_16_4_WP,
        Route_16_Warp_Points.ROUTE_16_TO_ROUTE_16_GATE_1_WP,
        "Route16Gate", dual_width= True
    )

    Route_16_Gate_Links["ROUTE_16_GATE_TO_ROUTE_16_2_LINK"] = WarpLink(
        Route_16_Gate_Warp_Points.ROUTE_16_GATE_TO_ROUTE_16_2_WP,
        Route_16_Warp_Points.ROUTE_16_TO_ROUTE_16_GATE_3_WP,
        "Route16Gate", 10, dual_width= True
    )


 # 1 left, 2 right

    Route_17_Route_18_Gate_Links["ROUTE_17_ROUTE_18_GATE_TO_ROUTE_17_1_LINK"] = WarpLink(
        Route_17_Route_18_Gate_Warp_Points.ROUTE_17_ROUTE_18_GATE_TO_ROUTE_17_1_WP,
        Route_17_Warp_Points.ROUTE_17_TO_ROUTE_17_ROUTE_18_GATE_1_WP,
        "Route17Route18Gate", dual_width= True
    )

    Route_17_Route_18_Gate_Links["ROUTE_17_ROUTE_18_GATE_TO_ROUTE_18_1_LINK"] = WarpLink(
        Route_17_Route_18_Gate_Warp_Points.ROUTE_17_ROUTE_18_GATE_TO_ROUTE_18_1_WP,
        Route_18_Warp_Points.ROUTE_18_TO_ROUTE_17_ROUTE_18_GATE_3_WP,
        "Route17Route18Gate", 10, dual_width= True
    )



    Route_19_Fuchsia_Gate_Links["ROUTE_19_FUCHSIA_GATE_TO_FUCHSIA_CITY_10_LINK"] = WarpLink(
        Route_19_Fuchsia_Gate_Warp_Points.ROUTE_19_FUCHSIA_GATE_TO_FUCHSIA_CITY_10_WP,
        Fuchsia_City_Warp_Points.FUCHSIA_CITY_TO_ROUTE_19_FUCHSIA_GATE_1_WP,
        "Route19FuchsiaGate", dual_width= True
    )

    Route_19_Fuchsia_Gate_Links["ROUTE_19_FUCHSIA_GATE_TO_ROUTE_19_1_LINK"] = WarpLink(
        Route_19_Fuchsia_Gate_Warp_Points.ROUTE_19_FUCHSIA_GATE_TO_ROUTE_19_1_WP,
        Route_19_Warp_Points.ROUTE_19_TO_ROUTE_19_FUCHSIA_GATE_3_WP,
        "Route19FuchsiaGate", 10, dual_width= True
    )


#######################################################################
#                    Kanto_Routes Group                               #
#######################################################################



    Route_2_Links["ROUTE_2_TO_ROUTE_2_NUGGET_HOUSE_1_LINK"] = WarpLink(
        Route_2_Warp_Points.ROUTE_2_TO_ROUTE_2_NUGGET_HOUSE_1_WP,
        Route_2_Nugget_House_Warp_Points.Route_2_Nugget_House_Exit_WP,
        "Route2"
    )

    Route_2_Links["ROUTE_2_TO_ROUTE_2_GATE_3_LINK"] = WarpLink(
        Route_2_Warp_Points.ROUTE_2_TO_ROUTE_2_GATE_3_WP,
        Route_2_Gate_Warp_Points.ROUTE_2_GATE_TO_ROUTE_2_2_WP,
        "Route2", 5
    )

    Route_2_Links["ROUTE_2_TO_ROUTE_2_GATE_1_LINK"] = WarpLink(
        Route_2_Warp_Points.ROUTE_2_TO_ROUTE_2_GATE_1_WP,
        Route_2_Gate_Warp_Points.ROUTE_2_GATE_TO_ROUTE_2_3_WP,
        "Route2", 10, dual_width= True
    )

    Route_2_Links["ROUTE_2_TO_DIGLETTS_CAVE_3_LINK"] = WarpLink(
        Route_2_Warp_Points.ROUTE_2_TO_DIGLETTS_CAVE_3_WP,
        Digletts_Cave_Warp_Points.DIGLETTS_CAVE_TO_ROUTE_2_5_WP,
        "Route2", 20
    )



    Route_3_Links["ROUTE_3_TO_MOUNT_MOON_1_LINK"] = WarpLink(
        Route_3_Warp_Points.ROUTE_3_TO_MOUNT_MOON_1_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_ROUTE_3_1_WP,
        "Route3"
    )



    Route_4_Links["ROUTE_4_TO_MOUNT_MOON_2_LINK"] = WarpLink(
        Route_4_Warp_Points.ROUTE_4_TO_MOUNT_MOON_2_WP,
        Mount_Moon_Warp_Points.MOUNT_MOON_TO_ROUTE_4_1_WP,
        "Route4"
    )



    Route_5_Cleanse_Tag_House_Links["ROUTE_5_CLEANSE_TAG_HOUSE_TO_ROUTE_5_4_LINK"] = WarpLink(
        Route_5_Cleanse_Tag_House_Warp_Points.ROUTE_5_CLEANSE_TAG_HOUSE_TO_ROUTE_5_4_WP,
        Route_5_Warp_Points.ROUTE_5_TO_ROUTE_5_CLEANSE_TAG_HOUSE_1_WP,
        "Route5CleanseTagHouse", dual_width= True
    )



    Route_5_Links["ROUTE_5_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_1_LINK"] = WarpLink(
        Route_5_Warp_Points.ROUTE_5_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_1_WP,
        Route_5_Underground_Path_Entrance_Warp_Points.ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_5_1_WP,
        "Route5", locked_by=[Unlock_Keys.MACHINE_PART]
    )

    Route_5_Links["ROUTE_5_TO_ROUTE_5_SAFFRON_GATE_1_LINK"] = WarpLink(
        Route_5_Warp_Points.ROUTE_5_TO_ROUTE_5_SAFFRON_GATE_1_WP,
        Route_5_Saffron_Gate_Warp_Points.ROUTE_5_SAFFRON_GATE_TO_ROUTE_5_2_WP,
        "Route5", 5, dual_width= True
    )

    Route_5_Links["ROUTE_5_TO_ROUTE_5_CLEANSE_TAG_HOUSE_1_LINK"] = WarpLink(
        Route_5_Warp_Points.ROUTE_5_TO_ROUTE_5_CLEANSE_TAG_HOUSE_1_WP,
        Route_5_Cleanse_Tag_House_Warp_Points.ROUTE_5_CLEANSE_TAG_HOUSE_TO_ROUTE_5_4_WP,
        "Route5", 15
    )



    Route_5_Underground_Path_Entrance_Links["ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_5_1_LINK"] = WarpLink(
        Route_5_Underground_Path_Entrance_Warp_Points.ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_5_1_WP,
        Route_5_Warp_Points.ROUTE_5_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_1_WP,
        "Route5UndergroundPathEntrance", dual_width= True
    )

    Route_5_Underground_Path_Entrance_Links["ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_1_LINK"] = WarpLink(
        Route_5_Underground_Path_Entrance_Warp_Points.ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_1_WP,
        Underground_Path_Warp_Points.UNDERGROUND_PATH_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_3_WP,
        "Route5UndergroundPathEntrance", 10
    )



    Route_6_Links["ROUTE_6_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_1_LINK"] = WarpLink(
        Route_6_Warp_Points.ROUTE_6_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_1_WP,
        Route_6_Underground_Path_Entrance_Warp_Points.ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_6_1_WP,
        "Route6", locked_by=[Unlock_Keys.MACHINE_PART]
    )

    Route_6_Links["ROUTE_6_TO_ROUTE_6_SAFFRON_GATE_3_LINK"] = WarpLink(
        Route_6_Warp_Points.ROUTE_6_TO_ROUTE_6_SAFFRON_GATE_3_WP,
        Route_6_Saffron_Gate_Warp_Points.ROUTE_6_SAFFRON_GATE_TO_ROUTE_6_2_WP,
        "Route6", 5
    )



    Route_6_Underground_Path_Entrance_Links["ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_6_1_LINK"] = WarpLink(
        Route_6_Underground_Path_Entrance_Warp_Points.ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_6_1_WP,
        Route_6_Warp_Points.ROUTE_6_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_1_WP,
        "Route6UndergroundPathEntrance", dual_width= True
    )

    Route_6_Underground_Path_Entrance_Links["ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_2_LINK"] = WarpLink(
        Route_6_Underground_Path_Entrance_Warp_Points.ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_2_WP,
        Underground_Path_Warp_Points.UNDERGROUND_PATH_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_3_WP,
        "Route6UndergroundPathEntrance", 10
    )



    Route_7_Links["ROUTE_7_TO_ROUTE_7_SAFFRON_GATE_1_LINK"] = WarpLink(
        Route_7_Warp_Points.ROUTE_7_TO_ROUTE_7_SAFFRON_GATE_1_WP,
        Route_7_Saffron_Gate_Warp_Points.ROUTE_7_SAFFRON_GATE_TO_ROUTE_7_1_WP,
        "Route7", dual_width= True
    )



    Route_8_Links["ROUTE_8_TO_ROUTE_8_SAFFRON_GATE_3_LINK"] = WarpLink(
        Route_8_Warp_Points.ROUTE_8_TO_ROUTE_8_SAFFRON_GATE_3_WP,
        Route_8_Saffron_Gate_Warp_Points.ROUTE_8_SAFFRON_GATE_TO_ROUTE_8_1_WP,
        "Route8", dual_width= True
    )



    Route_9_Links["ROUTE_9_TO_ROCK_TUNNEL_1F_1_LINK"] = WarpLink(
        Route_9_Warp_Points.ROUTE_9_TO_ROCK_TUNNEL_1F_1_WP,
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROUTE_9_1_WP,
        "Route9"
    )



    Route_10_North_Links["ROUTE_10_NORTH_TO_ROUTE_10_POKECENTER_1F_1_LINK"] = WarpLink(
        Route_10_North_Warp_Points.ROUTE_10_NORTH_TO_ROUTE_10_POKECENTER_1F_1_WP,
        Route_10_Pokecenter_1F_Warp_Points.ROUTE_10_POKECENTER_1F_TO_ROUTE_10_NORTH_1_WP,
        "Route10North"
    )

    Route_10_North_Links["ROUTE_10_NORTH_TO_POWER_PLANT_1_LINK"] = WarpLink(
        Route_10_North_Warp_Points.ROUTE_10_NORTH_TO_POWER_PLANT_1_WP,
        Power_Plant_Warp_Points.Power_Plant_Exit_WP,
        "Route10North", 5
    )



    Route_10_Pokecenter_1F_Links["ROUTE_10_POKECENTER_1F_TO_ROUTE_10_NORTH_1_LINK"] = WarpLink(
        Route_10_Pokecenter_1F_Warp_Points.ROUTE_10_POKECENTER_1F_TO_ROUTE_10_NORTH_1_WP,
        Route_10_North_Warp_Points.ROUTE_10_NORTH_TO_ROUTE_10_POKECENTER_1F_1_WP,
        "Route10Pokecenter1F", dual_width= True
    )

    Route_10_Pokecenter_1F_Links["ROUTE_10_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"] = WarpLink(
        Route_10_Pokecenter_1F_Warp_Points.ROUTE_10_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "Route10Pokecenter1F", 10
    )



    Route_10_South_Links["ROUTE_10_SOUTH_TO_ROCK_TUNNEL_1F_2_LINK"] = WarpLink(
        Route_10_South_Warp_Points.ROUTE_10_SOUTH_TO_ROCK_TUNNEL_1F_2_WP,
        Rock_Tunnel_1F_Warp_Points.ROCK_TUNNEL_1F_TO_ROUTE_10_SOUTH_1_WP,
        "Route10South"
    )



    Route_12_Links["ROUTE_12_TO_ROUTE_12_SUPER_ROD_HOUSE_1_LINK"] = WarpLink(
        Route_12_Warp_Points.ROUTE_12_TO_ROUTE_12_SUPER_ROD_HOUSE_1_WP,
        Route_12_Super_Rod_House_Warp_Points.ROUTE_12_SUPER_ROD_HOUSE_TO_ROUTE_12_1_WP,
        "Route12"
    )



    Route_12_Super_Rod_House_Links["ROUTE_12_SUPER_ROD_HOUSE_TO_ROUTE_12_1_LINK"] = WarpLink(
        Route_12_Super_Rod_House_Warp_Points.ROUTE_12_SUPER_ROD_HOUSE_TO_ROUTE_12_1_WP,
        Route_12_Warp_Points.ROUTE_12_TO_ROUTE_12_SUPER_ROD_HOUSE_1_WP,
        "Route12SuperRodHouse", dual_width= True
    )



    Route_15_Links["ROUTE_15_TO_ROUTE_15_FUCHSIA_GATE_3_LINK"] = WarpLink(
        Route_15_Warp_Points.ROUTE_15_TO_ROUTE_15_FUCHSIA_GATE_3_WP,
        Route_15_Fuchsia_Gate_Warp_Points.ROUTE_15_FUCHSIA_GATE_TO_ROUTE_15_1_WP,
        "Route15", dual_width= True
    )




    Route_16_Fuchsia_Speech_House_Links["ROUTE_16_FUCHSIA_SPEECH_HOUSE_TO_ROUTE_16_1_LINK"] = WarpLink(
        Route_16_Fuchsia_Speech_House_Warp_Points.ROUTE_16_FUCHSIA_SPEECH_HOUSE_TO_ROUTE_16_1_WP,
        Route_16_Warp_Points.ROUTE_16_TO_ROUTE_16_FUCHSIA_SPEECH_HOUSE_1_WP,
        "Route16FuchsiaSpeechHouse", dual_width= True
    )



    Route_16_Links["ROUTE_16_TO_ROUTE_16_FUCHSIA_SPEECH_HOUSE_1_LINK"] = WarpLink(
        Route_16_Warp_Points.ROUTE_16_TO_ROUTE_16_FUCHSIA_SPEECH_HOUSE_1_WP,
        Route_16_Fuchsia_Speech_House_Warp_Points.ROUTE_16_FUCHSIA_SPEECH_HOUSE_TO_ROUTE_16_1_WP,
        "Route16"
    )

    Route_16_Links["ROUTE_16_TO_ROUTE_16_GATE_3_LINK"] = WarpLink(
        Route_16_Warp_Points.ROUTE_16_TO_ROUTE_16_GATE_3_WP,
        Route_16_Gate_Warp_Points.ROUTE_16_GATE_TO_ROUTE_16_2_WP,
        "Route16", 5, dual_width= True
    )

    Route_16_Links["ROUTE_16_TO_ROUTE_16_GATE_1_LINK"] = WarpLink(
        Route_16_Warp_Points.ROUTE_16_TO_ROUTE_16_GATE_1_WP,
        Route_16_Gate_Warp_Points.ROUTE_16_GATE_TO_ROUTE_16_4_WP,
        "Route16", 15, dual_width= True
    )



    Route_17_Links["ROUTE_17_TO_ROUTE_17_ROUTE_18_GATE_1_LINK"] = WarpLink(
        Route_17_Warp_Points.ROUTE_17_TO_ROUTE_17_ROUTE_18_GATE_1_WP,
        Route_17_Route_18_Gate_Warp_Points.ROUTE_17_ROUTE_18_GATE_TO_ROUTE_17_1_WP,
        "Route17", dual_width= True
    )




    Route_18_Links["ROUTE_18_TO_ROUTE_17_ROUTE_18_GATE_3_LINK"] = WarpLink(
        Route_18_Warp_Points.ROUTE_18_TO_ROUTE_17_ROUTE_18_GATE_3_WP,
        Route_17_Route_18_Gate_Warp_Points.ROUTE_17_ROUTE_18_GATE_TO_ROUTE_18_1_WP,
        "Route18", dual_width= True
    )




    Route_19_Links["ROUTE_19_TO_ROUTE_19_FUCHSIA_GATE_3_LINK"] = WarpLink(
        Route_19_Warp_Points.ROUTE_19_TO_ROUTE_19_FUCHSIA_GATE_3_WP,
        Route_19_Fuchsia_Gate_Warp_Points.ROUTE_19_FUCHSIA_GATE_TO_ROUTE_19_1_WP,
        "Route19"
    )



    Route_20_Links["ROUTE_20_TO_SEAFOAM_GYM_1_LINK"] = WarpLink(
        Route_20_Warp_Points.ROUTE_20_TO_SEAFOAM_GYM_1_WP,
        Seafoam_Gym_Warp_Points.Seafoam_Gym_Exit_WP,
        "Route20"
    )



    Route_22_Links["ROUTE_22_TO_VICTORY_ROAD_GATE_1_LINK"] = WarpLink(
        Route_22_Warp_Points.ROUTE_22_TO_VICTORY_ROAD_GATE_1_WP, #todo victory road gate
        Celadon_City_Warp_Points.Celadon_City_Dept_Store_1F_Entrance_WP,
        "Route22"
    )



    Route_25_Links["ROUTE_25_TO_BILLS_HOUSE_1_LINK"] = WarpLink(
        Route_25_Warp_Points.ROUTE_25_TO_BILLS_HOUSE_1_WP,
        Bills_House_Warp_Points.Bills_House_Exit_WP,
        "Route25"
    )


#######################################################################
#                    Fast ship Group                                  #
#######################################################################

 #10-11 corridor, rest except 1 is hub

#We don't randomize ship entrance/exit
    #["FAST_SHIP_1F_TO_FAST_SHIP_1F_-1_LINK"]= WarpLink(
    #    Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_1F_-1_WP,
    #    <return warp>
    #    "FastShip1F"
    #)

    Fast_Ship_1F_Links["FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_1_LINK"] = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_1_WP,
        Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_2_WP,
        "FastShip1F", 5
    )

    Fast_Ship_1F_Links["FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_2_LINK"] = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_2_WP,
        Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_3_WP,
        "FastShip1F", 10
    )

    Fast_Ship_1F_Links["FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_3_LINK"] = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_3_WP,
        Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_4_WP,
        "FastShip1F", 15
    )

    Fast_Ship_1F_Links["FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_1_LINK"] = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_1_WP,
        Fast_Ship_Cabins_SW_SSW_NW_Warp_Points.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_5_WP,
        "FastShip1F", 20
    )

    Fast_Ship_1F_Links["FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_2_LINK"] = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_2_WP,
        Fast_Ship_Cabins_SW_SSW_NW_Warp_Points.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_6_WP,
        "FastShip1F", 25
    )

    Fast_Ship_1F_Links["FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_4_LINK"] = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_4_WP,
        Fast_Ship_Cabins_SW_SSW_NW_Warp_Points.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_7_WP,
        "FastShip1F", 30
    )

    Fast_Ship_1F_Links["FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_1_LINK"] = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_1_WP,
        Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_8_WP,
        "FastShip1F", 35
    )

    Fast_Ship_1F_Links["FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_3_LINK"] = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_3_WP,
        Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_9_WP,
        "FastShip1F", 40
    )

    Fast_Ship_1F_Links["FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5_LINK"] = WarpLink( #1011
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5_WP,
        Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_10_WP,
        "FastShip1F", 45
    )

    Fast_Ship_1F_Links["FAST_SHIP_1F_TO_FAST_SHIP_B1F_1_LINK"] = WarpLink( #1011
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_B1F_1_WP,
        Fast_Ship_B1F_Warp_Points.FAST_SHIP_B1F_TO_FAST_SHIP_1F_11_WP,
        "FastShip1F", 50
    )

    Fast_Ship_1F_Links["FAST_SHIP_1F_TO_FAST_SHIP_B1F_2_LINK"] = WarpLink(
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_B1F_2_WP,
        Fast_Ship_B1F_Warp_Points.FAST_SHIP_B1F_TO_FAST_SHIP_1F_12_WP,
        "FastShip1F", 55
    )



    Fast_Ship_B1F_Links["FAST_SHIP_B1F_TO_FAST_SHIP_1F_11_LINK"] = WarpLink(
        Fast_Ship_B1F_Warp_Points.FAST_SHIP_B1F_TO_FAST_SHIP_1F_11_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_B1F_1_WP,
        "FastShipB1F"
    )

    Fast_Ship_B1F_Links["FAST_SHIP_B1F_TO_FAST_SHIP_1F_12_LINK"] = WarpLink(
        Fast_Ship_B1F_Warp_Points.FAST_SHIP_B1F_TO_FAST_SHIP_1F_12_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_B1F_2_WP,
        "FastShipB1F", 5
    )



    Fast_Ship_Cabins_NNW_NNE_NE_Links["FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_2_LINK"] = WarpLink(
        Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_2_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_1_WP,
        "FastShipCabins_NNW_NNE_NE"
    )

    Fast_Ship_Cabins_NNW_NNE_NE_Links["FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_3_LINK"] = WarpLink(
        Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_3_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_2_WP,
        "FastShipCabins_NNW_NNE_NE", 5
    )

    Fast_Ship_Cabins_NNW_NNE_NE_Links["FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_4_LINK"] = WarpLink( #lazy sailor
        Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points.FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_4_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_3_WP,
        "FastShipCabins_NNW_NNE_NE", 10
    )



    Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links["FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_8_LINK"] = WarpLink(
        Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_8_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_1_WP,
        "FastShipCabins_SE_SSE_CaptainsCabin", dual_width= True
    )

    Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links["FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_9_LINK"] = WarpLink(
        Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_9_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_3_WP,
        "FastShipCabins_SE_SSE_CaptainsCabin", 10, dual_width= True
    )

    Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links["FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_10_LINK"] = WarpLink( # captain
        Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_10_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5_WP,
        "FastShipCabins_SE_SSE_CaptainsCabin", 20, dual_width= True
    )



    Fast_Ship_Cabins_SW_SSW_NW_Links["FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_5_LINK"] = WarpLink( #player cabin
        Fast_Ship_Cabins_SW_SSW_NW_Warp_Points.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_5_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_1_WP,
        "FastShipCabins_SW_SSW_NW"
    )

    Fast_Ship_Cabins_SW_SSW_NW_Links["FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_6_LINK"] = WarpLink(
        Fast_Ship_Cabins_SW_SSW_NW_Warp_Points.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_6_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_2_WP,
        "FastShipCabins_SW_SSW_NW", 5, dual_width= True
    )

    Fast_Ship_Cabins_SW_SSW_NW_Links["FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_7_LINK"] = WarpLink(
        Fast_Ship_Cabins_SW_SSW_NW_Warp_Points.FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_7_WP,
        Fast_Ship_1F_Warp_Points.FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_4_WP,
        "FastShipCabins_SW_SSW_NW", 15, dual_width= True
    )


    Route_28_Links["ROUTE_28_TO_ROUTE_28_STEEL_WING_HOUSE_1_LINK"] = WarpLink(
        Route_28_Warp_Points.ROUTE_28_TO_ROUTE_28_STEEL_WING_HOUSE_1_WP,
        Route_28_Steel_Wing_House_Warp_Points.ROUTE_28_STEEL_WING_HOUSE_TO_ROUTE_28_1_WP,
        "Route28"
    )
    Route_28_Links["ROUTE_28_TO_VICTORY_ROAD_GATE_7_LINK"] = WarpLink(
        Route_28_Warp_Points.ROUTE_28_TO_VICTORY_ROAD_GATE_7_WP,
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_ROUTE_28_2_WP,
        "Route28", 5
    )


    Route_28_Steel_Wing_House_Links["ROUTE_28_STEEL_WING_HOUSE_TO_ROUTE_28_1_LINK"] = WarpLink(
        Route_28_Steel_Wing_House_Warp_Points.ROUTE_28_STEEL_WING_HOUSE_TO_ROUTE_28_1_WP,
        Route_28_Warp_Points.ROUTE_28_TO_ROUTE_28_STEEL_WING_HOUSE_1_WP,
        "Route28SteelWingHouse", dual_width=True
    )


    Silver_Cave_Outside_Links["SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_POKECENTER_1F_1_LINK"] = WarpLink(
        Silver_Cave_Outside_Warp_Points.SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_POKECENTER_1F_1_WP,
        Silver_Cave_Pokecenter_1F_Warp_Points.SILVER_CAVE_POKECENTER_1F_TO_SILVER_CAVE_OUTSIDE_1_WP,
        "SilverCaveOutside"
    )
    Silver_Cave_Outside_Links["SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_ROOM_1_1_LINK"] = WarpLink(
        Silver_Cave_Outside_Warp_Points.SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_ROOM_1_1_WP,
        Silver_Cave_Room_1_Warp_Points.SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_OUTSIDE_2_WP,
        "SilverCaveOutside", 5
    )


    Silver_Cave_Pokecenter_1F_Links["SILVER_CAVE_POKECENTER_1F_TO_SILVER_CAVE_OUTSIDE_1_LINK"] = WarpLink(
        Silver_Cave_Pokecenter_1F_Warp_Points.SILVER_CAVE_POKECENTER_1F_TO_SILVER_CAVE_OUTSIDE_1_WP,
        Silver_Cave_Outside_Warp_Points.SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_POKECENTER_1F_1_WP,
        "SilverCavePokecenter1F", dual_width=True
    )
    Silver_Cave_Pokecenter_1F_Links["SILVER_CAVE_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"] = WarpLink(
        Silver_Cave_Pokecenter_1F_Warp_Points.SILVER_CAVE_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "SilverCavePokecenter1F", 10
    )


    Silver_Cave_Room_1_Links["SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_OUTSIDE_2_LINK"] = WarpLink(
        Silver_Cave_Room_1_Warp_Points.SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_OUTSIDE_2_WP,
        Silver_Cave_Outside_Warp_Points.SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_ROOM_1_1_WP,
        "SilverCaveRoom1"
    )
    Silver_Cave_Room_1_Links["SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_ROOM_2_1_LINK"] = WarpLink(
        Silver_Cave_Room_1_Warp_Points.SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_ROOM_2_1_WP,
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_1_2_WP,
        "SilverCaveRoom1", 5
    )


    Silver_Cave_Room_2_Links["SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_1_2_LINK"] = WarpLink(
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_1_2_WP,
        Silver_Cave_Room_1_Warp_Points.SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_ROOM_2_1_WP,
        "SilverCaveRoom2"
    )
    Silver_Cave_Room_2_Links["SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_3_1_LINK"] = WarpLink(
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_3_1_WP,
        Silver_Cave_Room_3_Warp_Points.SILVER_CAVE_ROOM_3_TO_SILVER_CAVE_ROOM_2_2_WP,
        "SilverCaveRoom2", 5
    )
    Silver_Cave_Room_2_Links["SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_1_LINK"] = WarpLink(
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_1_WP,
        Silver_Cave_Item_Rooms_Warp_Points.SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_3_WP,
        "SilverCaveRoom2", 10
    )
    Silver_Cave_Room_2_Links["SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_2_LINK"] = WarpLink(
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_2_WP,
        Silver_Cave_Item_Rooms_Warp_Points.SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_4_WP,
        "SilverCaveRoom2", 15
    )

    Silver_Cave_Room_3_Links["SILVER_CAVE_ROOM_3_TO_SILVER_CAVE_ROOM_2_2_LINK"] = WarpLink(
        Silver_Cave_Room_3_Warp_Points.SILVER_CAVE_ROOM_3_TO_SILVER_CAVE_ROOM_2_2_WP,
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_ROUTE_28_2_WP,
        "SilverCaveRoom3"
    )


    Silver_Cave_Item_Rooms_Links["SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_3_LINK"] = WarpLink(
        Silver_Cave_Item_Rooms_Warp_Points.SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_3_WP,
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_1_WP,
        "SilverCaveItemRooms"
    )
    Silver_Cave_Item_Rooms_Links["SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_4_LINK"] = WarpLink(
        Silver_Cave_Item_Rooms_Warp_Points.SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_4_WP,
        Silver_Cave_Room_2_Warp_Points.SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_2_WP,
        "SilverCaveItemRooms", 5
    )


    warpGroups = dict()
    warpGroups["Celadon_Cafe_Links"] = dict(Celadon_Cafe_Links)
    warpGroups["Celadon_Dept_Store_1F_Links"] = dict(Celadon_Dept_Store_1F_Links)
    warpGroups["Celadon_Dept_Store_2F_Links"] = dict(Celadon_Dept_Store_2F_Links)
    warpGroups["Celadon_Dept_Store_3F_Links"] = dict(Celadon_Dept_Store_3F_Links)
    warpGroups["Celadon_Dept_Store_4F_Links"] = dict(Celadon_Dept_Store_4F_Links)
    warpGroups["Celadon_Dept_Store_5F_Links"] = dict(Celadon_Dept_Store_5F_Links)
    warpGroups["Celadon_Dept_Store_6F_Links"] = dict(Celadon_Dept_Store_6F_Links)
    warpGroups["Celadon_Game_Corner_Links"] = dict(Celadon_Game_Corner_Links)
    warpGroups["Celadon_Game_Corner_Prize_Room_Links"] = dict(Celadon_Game_Corner_Prize_Room_Links)
    warpGroups["Celadon_Gym_Links"] = dict(Celadon_Gym_Links)
    warpGroups["Celadon_Mansion_1F_Links"] = dict(Celadon_Mansion_1F_Links)
    warpGroups["Celadon_Mansion_2F_Links"] = dict(Celadon_Mansion_2F_Links)
    warpGroups["Celadon_Mansion_3F_Links"] = dict(Celadon_Mansion_3F_Links)
    warpGroups["Celadon_Mansion_Roof_House_Links"] = dict(Celadon_Mansion_Roof_House_Links)
    warpGroups["Celadon_Mansion_Roof_Links"] = dict(Celadon_Mansion_Roof_Links)
    warpGroups["Celadon_Pokecenter_1F_Links"] = dict(Celadon_Pokecenter_1F_Links)
    warpGroups["Celadon_City_Links"] = dict(Celadon_City_Links)
    warpGroups["Bills_House_Links"] = dict(Bills_House_Links)
    warpGroups["Cerulean_Gym_Badge_Speech_House_Links"] = dict(Cerulean_Gym_Badge_Speech_House_Links)
    warpGroups["Cerulean_Gym_Links"] = dict(Cerulean_Gym_Links)
    warpGroups["Cerulean_Mart_Links"] = dict(Cerulean_Mart_Links)
    warpGroups["Cerulean_Pokecenter_1F_Links"] = dict(Cerulean_Pokecenter_1F_Links)
    warpGroups["Cerulean_Police_Station_Links"] = dict(Cerulean_Police_Station_Links)
    warpGroups["Cerulean_Trade_Speech_House_Links"] = dict(Cerulean_Trade_Speech_House_Links)
    warpGroups["Power_Plant_Links"] = dict(Power_Plant_Links)
    warpGroups["Cerulean_City_Links"] = dict(Cerulean_City_Links)
    warpGroups["Cinnabar_Pokecenter_1F_Links"] = dict(Cinnabar_Pokecenter_1F_Links)
    warpGroups["Seafoam_Gym_Links"] = dict(Seafoam_Gym_Links)
    warpGroups["Cinnabar_Island_Links"] = dict(Cinnabar_Island_Links)
    warpGroups["Bills_Brothers_House_Links"] = dict(Bills_Brothers_House_Links)
    warpGroups["Fuchsia_Gym_Links"] = dict(Fuchsia_Gym_Links)
    warpGroups["Fuchsia_Mart_Links"] = dict(Fuchsia_Mart_Links)
    warpGroups["Fuchsia_Pokecenter_1F_Links"] = dict(Fuchsia_Pokecenter_1F_Links)
    warpGroups["Safari_Zone_Main_Office_Links"] = dict(Safari_Zone_Main_Office_Links)
    warpGroups["Safari_Zone_Wardens_Home_Links"] = dict(Safari_Zone_Wardens_Home_Links)
    warpGroups["Fuchsia_City_Links"] = dict(Fuchsia_City_Links)
    warpGroups["Lavender_Mart_Links"] = dict(Lavender_Mart_Links)
    warpGroups["Lavender_Name_Rater_Links"] = dict(Lavender_Name_Rater_Links)
    warpGroups["Lavender_Pokecenter_1F_Links"] = dict(Lavender_Pokecenter_1F_Links)
    warpGroups["Lavender_Speech_House_Links"] = dict(Lavender_Speech_House_Links)
    warpGroups["Lav_Radio_Tower_1F_Links"] = dict(Lav_Radio_Tower_1F_Links)
    warpGroups["Mr_Fujis_House_Links"] = dict(Mr_Fujis_House_Links)
    warpGroups["Soul_House_Links"] = dict(Soul_House_Links)
    warpGroups["Lavender_Town_Links"] = dict(Lavender_Town_Links)
    warpGroups["Blues_House_Links"] = dict(Blues_House_Links)
    warpGroups["Oaks_Lab_Links"] = dict(Oaks_Lab_Links)
    warpGroups["Reds_House_1F_Links"] = dict(Reds_House_1F_Links)
    warpGroups["Reds_House_2F_Links"] = dict(Reds_House_2F_Links)
    warpGroups["Pallet_Town_Links"] = dict(Pallet_Town_Links)
    warpGroups["Pewter_Gym_Links"] = dict(Pewter_Gym_Links)
    warpGroups["Pewter_Mart_Links"] = dict(Pewter_Mart_Links)
    warpGroups["Pewter_Nidoran_Speech_House_Links"] = dict(Pewter_Nidoran_Speech_House_Links)
    warpGroups["Pewter_Snooze_Speech_House_Links"] = dict(Pewter_Snooze_Speech_House_Links)
    warpGroups["Pewter_Pokecenter_1F_Links"] = dict(Pewter_Pokecenter_1F_Links)
    warpGroups["Pewter_City_Links"] = dict(Pewter_City_Links)
    warpGroups["Copycats_House_1F_Links"] = dict(Copycats_House_1F_Links)
    warpGroups["Copycats_House_2F_Links"] = dict(Copycats_House_2F_Links)
    warpGroups["Fighting_Dojo_Links"] = dict(Fighting_Dojo_Links)
    warpGroups["Mr_Psychics_House_Links"] = dict(Mr_Psychics_House_Links)
    warpGroups["Saffron_Gym_Links"] = dict(Saffron_Gym_Links)
    warpGroups["Saffron_Magnet_Train_Station_Links"] = dict(Saffron_Magnet_Train_Station_Links)
    warpGroups["Saffron_Mart_Links"] = dict(Saffron_Mart_Links)
    warpGroups["Saffron_Pokecenter_1F_Links"] = dict(Saffron_Pokecenter_1F_Links)
    warpGroups["Silph_Co_1F_Links"] = dict(Silph_Co_1F_Links)
    warpGroups["Saffron_City_Links"] = dict(Saffron_City_Links)
    warpGroups["Pokemon_Fan_Club_Links"] = dict(Pokemon_Fan_Club_Links)
    warpGroups["Vermilion_Digletts_Cave_Speech_House_Links"] = dict(Vermilion_Digletts_Cave_Speech_House_Links)
    warpGroups["Vermilion_Fishing_Speech_House_Links"] = dict(Vermilion_Fishing_Speech_House_Links)
    warpGroups["Vermilion_Gym_Links"] = dict(Vermilion_Gym_Links)
    warpGroups["Vermilion_Magnet_Train_Speech_House_Links"] = dict(Vermilion_Magnet_Train_Speech_House_Links)
    warpGroups["Vermilion_Mart_Links"] = dict(Vermilion_Mart_Links)
    warpGroups["Vermilion_Pokecenter_1F_Links"] = dict(Vermilion_Pokecenter_1F_Links)
    warpGroups["Vermilion_Port_Links"] = dict(Vermilion_Port_Links)
    warpGroups["Vermilion_Port_Passage_Links"] = dict(Vermilion_Port_Passage_Links)
    warpGroups["Vermilion_City_Links"] = dict(Vermilion_City_Links)
    warpGroups["Route_2_Nugget_House_Links"] = dict(Route_2_Nugget_House_Links)
    warpGroups["Trainer_House_1F_Links"] = dict(Trainer_House_1F_Links)
    warpGroups["Trainer_House_B1F_Links"] = dict(Trainer_House_B1F_Links)
    warpGroups["Viridian_Gym_Links"] = dict(Viridian_Gym_Links)
    warpGroups["Viridian_Mart_Links"] = dict(Viridian_Mart_Links)
    warpGroups["Viridian_Nickname_Speech_House_Links"] = dict(Viridian_Nickname_Speech_House_Links)
    warpGroups["Viridian_Pokecenter_1F_Links"] = dict(Viridian_Pokecenter_1F_Links)
    warpGroups["Viridian_City_Links"] = dict(Viridian_City_Links)
    warpGroups["Digletts_Cave_Links"] = dict(Digletts_Cave_Links)
    warpGroups["Mount_Moon_Gift_Shop_Links"] = dict(Mount_Moon_Gift_Shop_Links)
    warpGroups["Mount_Moon_Links"] = dict(Mount_Moon_Links)
    warpGroups["Mount_Moon_Square_Links"] = dict(Mount_Moon_Square_Links)
    warpGroups["Rock_Tunnel_1F_Links"] = dict(Rock_Tunnel_1F_Links)
    warpGroups["Rock_Tunnel_B1F_Links"] = dict(Rock_Tunnel_B1F_Links)
    warpGroups["Underground_Path_Links"] = dict(Underground_Path_Links)
    warpGroups["Route_2_Gate_Links"] = dict(Route_2_Gate_Links)
    warpGroups["Route_5_Saffron_Gate_Links"] = dict(Route_5_Saffron_Gate_Links)
    warpGroups["Route_6_Saffron_Gate_Links"] = dict(Route_6_Saffron_Gate_Links)
    warpGroups["Route_7_Saffron_Gate_Links"] = dict(Route_7_Saffron_Gate_Links)
    warpGroups["Route_8_Saffron_Gate_Links"] = dict(Route_8_Saffron_Gate_Links)
    warpGroups["Route_15_Fuchsia_Gate_Links"] = dict(Route_15_Fuchsia_Gate_Links)
    warpGroups["Route_16_Gate_Links"] = dict(Route_16_Gate_Links)
    warpGroups["Route_17_Route_18_Gate_Links"] = dict(Route_17_Route_18_Gate_Links)
    warpGroups["Route_19_Fuchsia_Gate_Links"] = dict(Route_19_Fuchsia_Gate_Links)
    warpGroups["Route_2_Links"] = dict(Route_2_Links)
    warpGroups["Route_3_Links"] = dict(Route_3_Links)
    warpGroups["Route_4_Links"] = dict(Route_4_Links)
    warpGroups["Route_5_Cleanse_Tag_House_Links"] = dict(Route_5_Cleanse_Tag_House_Links)
    warpGroups["Route_5_Links"] = dict(Route_5_Links)
    warpGroups["Route_5_Underground_Path_Entrance_Links"] = dict(Route_5_Underground_Path_Entrance_Links)
    warpGroups["Route_6_Links"] = dict(Route_6_Links)
    warpGroups["Route_6_Underground_Path_Entrance_Links"] = dict(Route_6_Underground_Path_Entrance_Links)
    warpGroups["Route_7_Links"] = dict(Route_7_Links)
    warpGroups["Route_8_Links"] = dict(Route_8_Links)
    warpGroups["Route_9_Links"] = dict(Route_9_Links)
    warpGroups["Route_10_North_Links"] = dict(Route_10_North_Links)
    warpGroups["Route_10_Pokecenter_1F_Links"] = dict(Route_10_Pokecenter_1F_Links)
    warpGroups["Route_10_South_Links"] = dict(Route_10_South_Links)
    warpGroups["Route_12_Links"] = dict(Route_12_Links)
    warpGroups["Route_12_Super_Rod_House_Links"] = dict(Route_12_Super_Rod_House_Links)
    warpGroups["Route_15_Links"] = dict(Route_15_Links)
    warpGroups["Route_16_Fuchsia_Speech_House_Links"] = dict(Route_16_Fuchsia_Speech_House_Links)
    warpGroups["Route_16_Links"] = dict(Route_16_Links)
    warpGroups["Route_17_Links"] = dict(Route_17_Links)
    warpGroups["Route_18_Links"] = dict(Route_18_Links)
    warpGroups["Route_19_Links"] = dict(Route_19_Links)
    warpGroups["Route_20_Links"] = dict(Route_20_Links)
    warpGroups["Route_22_Links"] = dict(Route_22_Links)
    warpGroups["Route_25_Links"] = dict(Route_25_Links)
    warpGroups["Fast_Ship_1F_Links"] = dict(Fast_Ship_1F_Links)
    warpGroups["Fast_Ship_B1F_Links"] = dict(Fast_Ship_B1F_Links)
    warpGroups["Fast_Ship_Cabins_NNW_NNE_NE_Links"] = dict(Fast_Ship_Cabins_NNW_NNE_NE_Links)
    warpGroups["Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links"] = dict(Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Links)
    warpGroups["Fast_Ship_Cabins_SW_SSW_NW_Links"] = dict(Fast_Ship_Cabins_SW_SSW_NW_Links)
    warpGroups["Route_28_Links"] = dict(Route_28_Links)
    warpGroups["Route_28_Steel_Wing_House_Links"] = dict(Route_28_Steel_Wing_House_Links)
    warpGroups["Silver_Cave_Outside_Links"] = dict(Silver_Cave_Outside_Links)
    warpGroups["Silver_Cave_Pokecenter_1F_Links"] = dict(Silver_Cave_Pokecenter_1F_Links)
    warpGroups["Silver_Cave_Room_1_Links"] = dict(Silver_Cave_Room_1_Links)
    warpGroups["Silver_Cave_Room_2_Links"] = dict(Silver_Cave_Room_2_Links)
    warpGroups["Silver_Cave_Room_3_Links"] = dict(Silver_Cave_Room_3_Links)
    warpGroups["Silver_Cave_Item_Rooms_Links"] = dict(Silver_Cave_Item_Rooms_Links)



    return warpGroups

#######################################################################
#                    END OF GROUPS                                    #
#######################################################################
