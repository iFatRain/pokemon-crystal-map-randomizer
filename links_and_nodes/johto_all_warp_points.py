import itertools
from enum import Enum

from class_definitions import WarpLink, Unlock_Keys
from logic.MemoryAddressReader import buildMemoryLocationsFromSym
from map_data.Azalea_Group.AzaleaGym_Map import Azalea_Gym_Warp_Points
from map_data.Azalea_Group.AzaleaMart_Map import Azalea_Mart_Warp_Points
from map_data.Azalea_Group.AzaleaPokecenter_Map import Azalea_Pokecenter_Warp_Points
from map_data.Azalea_Group.AzaleaTown_Map import Azalea_Town_Warp_Points
from map_data.Azalea_Group.CharcoalKiln_Map import Charcoal_Kiln_Warp_Points
from map_data.Azalea_Group.KurtsHouse_Map import Kurts_House_Warp_Points
from map_data.Blackthorn_Group.BlackthornCity_Map import Blackthorn_City_Warp_Points
from map_data.Blackthorn_Group.BlackthornDragonSpeechHouse_Map import Blackthorn_Dragon_Speech_House_Warp_Points
from map_data.Blackthorn_Group.BlackthornEmysHouse_Map import Blackthorn_Emys_House_Warp_Points
from map_data.Blackthorn_Group.BlackthornGym_Map import Blackthorn_Gym_1F_Warp_Points
from map_data.Blackthorn_Group.BlackthornMart_Map import Blackthorn_Mart_Warp_Points
from map_data.Blackthorn_Group.BlackthornPokecenter_Map import Blackthorn_Pokecenter_Warp_Points
from map_data.Blackthorn_Group.MoveDeletersHouse_Map import Move_Deleters_House_Warp_Points
from map_data.Cherrygrove_Group.CherrygroveCity_Map import Cherrygrove_City_Warp_Points
from map_data.Cherrygrove_Group.CherrygroveEvolutionSpeechHouse_Map import \
    Cherrygrove_Evolution_Speech_House_Warp_Points
from map_data.Cherrygrove_Group.CherrygroveGymSpeechHouse_Map import Cherrygrove_Gym_Speech_House_Warp_Points
from map_data.Cherrygrove_Group.CherrygroveMart_Map import Cherrygrove_Mart_Warp_Points
from map_data.Cherrygrove_Group.CherrygrovePokecenter_Map import Cherrygrove_Pokecenter_Warp_Points
from map_data.Cherrygrove_Group.GuideGentsHouse_Map import Guide_Gents_House_Warp_Points
from map_data.Cherrygrove_Group.MrPokemonsHouse_Map import Mr_Pokemons_House_Warp_Points
from map_data.Cherrygrove_Group.Route30BerryHouse_Map import Route_30_Berry_House_Warp_Points
from map_data.Cianwood_Group.BattleTowerOutside_Map import Battle_Tower_Outside_Warp_Points
from map_data.Cianwood_Group.CianwoodCity_Map import Cianwood_City_Warp_Points
from map_data.Cianwood_Group.CianwoodGym_Map import Cianwood_Gym_Warp_Points
from map_data.Cianwood_Group.CianwoodLugiaSpeechHouse_Map import Cianwood_Lugia_Speech_House_Warp_Points
from map_data.Cianwood_Group.CianwoodPharmacy_Map import Cianwood_Pharmacy_Warp_Points
from map_data.Cianwood_Group.CianwoodPhotoStudio_Map import Cianwood_Photo_Studio_Warp_Points
from map_data.Cianwood_Group.CianwoodPokecenter_Map import Cianwood_Pokecenter_Warp_Points
from map_data.Cianwood_Group.ManiasHouse_Map import Manias_House_Warp_Points
from map_data.Cianwood_Group.PokeSeersHouse_Map import Poke_Seers_House_Warp_Points
from map_data.Cianwood_Group.Route40BattleTowerGate_Map import Route_40_Battle_Tower_Gate_Warp_Points
from map_data.Dungeons_Group.BurnedTower1F_Map import Burned_Tower_1F_Warp_Points
from map_data.Dungeons_Group.DarkCaveBlackthornEntrance_Map import Dark_Cave_Blackthorn_Entrance_Warp_Points
from map_data.Dungeons_Group.DarkCaveVioletEntrance_Map import Dark_Cave_Violet_Entrance_Warp_Points
from map_data.Dungeons_Group.DragonShrine_Map import Dragon_Shrine_Warp_Points
from map_data.Dungeons_Group.DragonsDen1F_Map import Dragons_Den_1F_Warp_Points
from map_data.Dungeons_Group.DragonsDenB1F_Map import Dragons_Den_B1F_Warp_Points
from map_data.Dungeons_Group.GoldenrodUndergroundWarehouse_Map import Goldenrod_Underground_Warehouse_Warp_Points
from map_data.Dungeons_Group.GoldenrodUnderground_Map import Goldenrod_Underground_Warp_Points
from map_data.Dungeons_Group.IcePath1F_Map import Ice_Path_1F_Warp_Points
from map_data.Dungeons_Group.IcePathB1F_Map import Ice_Path_B1F_Warp_Points
from map_data.Dungeons_Group.IcePathB2FBlackthornSide_Map import Ice_Path_B2F_Blackthorn_Side_Warp_Points
from map_data.Dungeons_Group.IcePathB2FMahoganySide_Map import Ice_Path_B2F_Mahogany_Side_Warp_Points
from map_data.Dungeons_Group.IcePathB3F_Map import Ice_Path_B3F_Warp_Points
from map_data.Dungeons_Group.IlexForest_Map import Ilex_Forest_Warp_Points
from map_data.Dungeons_Group.LakeOfRage_Subgroup.LakeOfRageHiddenPowerHouse_Map import \
    Lake_Of_Rage_Hidden_Power_House_Warp_Points
from map_data.Dungeons_Group.LakeOfRage_Subgroup.LakeOfRageMagikarpHouse_Map import \
    Lake_Of_Rage_Magikarp_House_Warp_Points
from map_data.Dungeons_Group.LakeOfRage_Subgroup.LakeOfRage_Map import Lake_Of_Rage_Warp_Points
from map_data.Dungeons_Group.MountMortar1FInside_Map import Mount_Mortar_1F_Inside_Warp_Points
from map_data.Dungeons_Group.MountMortar1FOutside_Map import Mount_Mortar_1F_Outside_Warp_Points
from map_data.Dungeons_Group.MountMortar2FInside_Map import Mount_Mortar_2F_Inside_Warp_Points
from map_data.Dungeons_Group.MountMortarB1F_Map import Mount_Mortar_B1F_Warp_Points
from map_data.Dungeons_Group.NationalPark_Map import National_Park_Warp_Points
from map_data.Dungeons_Group.Pokecenter2F_Map import Pokecenter_2F_Warp_Points
from map_data.Dungeons_Group.RuinsOfAlphAerodactylChamber_Map import Ruins_Of_Alph_Aerodactyl_Chamber_Warp_Points
from map_data.Dungeons_Group.RuinsOfAlphAerodactylItemRoom_Map import Ruins_Of_Alph_Aerodactyl_Item_Room_Warp_Points
from map_data.Dungeons_Group.RuinsOfAlphHoOhChamber_Map import Ruins_Of_Alph_Ho_Oh_Chamber_Warp_Points
from map_data.Dungeons_Group.RuinsOfAlphHoOhItemRoom_Map import Ruins_Of_Alph_Ho_Oh_Item_Room_Warp_Points
from map_data.Dungeons_Group.RuinsOfAlphInnerChamber_Map import Ruins_Of_Alph_Inner_Chamber_Warp_Points
from map_data.Dungeons_Group.RuinsOfAlphKabutoChamber_Map import Ruins_Of_Alph_Kabuto_Chamber_Warp_Points
from map_data.Dungeons_Group.RuinsOfAlphKabutoItemRoom_Map import Ruins_Of_Alph_Kabuto_Item_Room_Warp_Points
from map_data.Dungeons_Group.RuinsOfAlphOmanyteChamber_Map import Ruins_Of_Alph_Omanyte_Chamber_Warp_Points
from map_data.Dungeons_Group.RuinsOfAlphOmanyteItemRoom_Map import Ruins_Of_Alph_Omanyte_Item_Room_Warp_Points
from map_data.Dungeons_Group.RuinsOfAlphOutside_Map import Ruins_Of_Alph_Outside_Warp_Points
from map_data.Dungeons_Group.RuinsOfAlphResearchCenter_Map import Ruins_Of_Alph_Research_Center_Warp_Points
from map_data.Dungeons_Group.SlowpokeWellB1F_Map import Slowpoke_Well_B1F_Warp_Points
from map_data.Dungeons_Group.SlowpokeWellB2F_Map import Slowpoke_Well_B2F_Warp_Points
from map_data.Dungeons_Group.SproutTower1F_Map import Sprout_Tower_1F_Warp_Points
from map_data.Dungeons_Group.SproutTower2F_Map import Sprout_Tower_2F_Warp_Points
from map_data.Dungeons_Group.SproutTower3F_Map import Sprout_Tower_3F_Warp_Points
from map_data.Dungeons_Group.TinTower1F_Map import Tin_Tower_1F_Warp_Points
from map_data.Dungeons_Group.TinTower2F_Map import Tin_Tower_2F_Warp_Points
from map_data.Dungeons_Group.TinTower3F_Map import Tin_Tower_3F_Warp_Points
from map_data.Dungeons_Group.TinTower4F_Map import Tin_Tower_4F_Warp_Points
from map_data.Dungeons_Group.TinTower5F_Map import Tin_Tower_5F_Warp_Points
from map_data.Dungeons_Group.TinTower6F_Map import Tin_Tower_6F_Warp_Points
from map_data.Dungeons_Group.TinTower7F_Map import Tin_Tower_7F_Warp_Points
from map_data.Dungeons_Group.TinTower8F_Map import Tin_Tower_8F_Warp_Points
from map_data.Dungeons_Group.TinTower9F_Map import Tin_Tower_9F_Warp_Points
from map_data.Dungeons_Group.TinTowerRoof_Map import Tin_Tower_Roof_Warp_Points
from map_data.Dungeons_Group.TohjoFalls_Map import Tohjo_Falls_Warp_Points
from map_data.Dungeons_Group.UnionCave1F_Map import Union_Cave_1F_Warp_Points
from map_data.Dungeons_Group.UnionCaveB1F_Map import Union_Cave_B1F_Warp_Points
from map_data.Dungeons_Group.UnionCaveB2F_Map import Union_Cave_B2F_Warp_Points
from map_data.Dungeons_Group.VictoryRoad_Map import Victory_Road_Warp_Points
from map_data.Dungeons_Group.WhirlIslandB1F_Map import Whirl_Island_B1F_Warp_Points
from map_data.Dungeons_Group.WhirlIslandB2F_Map import Whirl_Island_B2F_Warp_Points
from map_data.Dungeons_Group.WhirlIslandCave_Map import Whirl_Island_Cave_Warp_Points
from map_data.Dungeons_Group.WhirlIslandLugiaChamber_Map import Whirl_Island_Lugia_Chamber_Warp_Points
from map_data.Dungeons_Group.WhirlIslandNE_Map import Whirl_Island_NE_Warp_Points
from map_data.Dungeons_Group.WhirlIslandNW_Map import Whirl_Island_NW_Warp_Points
from map_data.Dungeons_Group.WhirlIslandSE_Map import Whirl_Island_SE_Warp_Points
from map_data.Dungeons_Group.WhirlIslandSW_Map import Whirl_Island_SW_Warp_Points
from map_data.Ecruteak_Group.DanceTheatre_Map import Dance_Theatre_Warp_Points
from map_data.Ecruteak_Group.EcruteakCity_Map import Ecruteak_City_Warp_Points
from map_data.Ecruteak_Group.EcruteakGym_Map import Ecruteak_Gym_Warp_Points
from map_data.Ecruteak_Group.EcruteakItemFinderHouse_Map import Ecruteak_Itemfinder_House_Warp_Points
from map_data.Ecruteak_Group.EcruteakLugiaSpeechHouse_Map import Ecruteak_Lugia_Speech_House_Warp_Points
from map_data.Ecruteak_Group.EcruteakMart_Map import Ecruteak_Mart_Warp_Points
from map_data.Ecruteak_Group.EcruteakPokecenter_Map import Ecruteak_Pokecenter_Warp_Points
from map_data.Ecruteak_Group.EcruteakTinTowerEntrance_Map import Ecruteak_Tin_Tower_Entrance_Warp_Points
from map_data.Ecruteak_Group.WiseTriosRoom_Map import Wise_Trios_Room_Warp_Points
from map_data.Elite4AndChampion_Group.BrunosRoom_Map import Brunos_Room_Warp_Points
from map_data.Elite4AndChampion_Group.KarensRoom_Map import Karens_Room_Warp_Points
from map_data.Elite4AndChampion_Group.KogaRoom_Map import Kogas_Room_Warp_Points
from map_data.Elite4AndChampion_Group.LancesRoom import Lances_Room_Warp_Points
from map_data.Elite4AndChampion_Group.WillsRoom_Map import Wills_Room_Warp_Points
from map_data.Gates.IlexForestAzaleaGate_Map import Ilex_Forest_Azalea_Gate_Warp_Points
from map_data.Gates.Route29Route46Gate_Map import Route_29_Route_46_Gate_Warp_Points
from map_data.Gates.Route31VioletGate_Map import Route_31_Violet_Gate_Warp_Points
from map_data.Gates.Route32RuinsOfAlphGate_Map import Route_32_Ruins_Of_Alph_Gate_Warp_Points
from map_data.Gates.Route34IlexForestGate_Map import Route_34_Ilex_Forest_Gate_Warp_Points
from map_data.Gates.Route35GoldenrodGate_Map import Route_35_Goldenrod_Gate_Warp_Points
from map_data.Gates.Route35NationalParkGate_Map import Route_35_National_Park_Gate_Warp_Points
from map_data.Gates.Route36NationalParkGate_Map import Route_36_National_Park_Gate_Warp_Points
from map_data.Gates.Route36RuinsOfAlphGate_Map import Route_36_Ruins_Of_Alph_Gate_Warp_Points
from map_data.Gates.Route38EcruteakGate_Map import Route_38_Ecruteak_Gate_Warp_Points
from map_data.Gates.Route42EcruteakGate_Map import Route_42_Ecruteak_Gate_Warp_Points
from map_data.Gates.Route43Gate_Map import Route_43_Gate_Warp_Points
from map_data.Gates.Route43MahoganyGate_Map import Route_43_Mahogany_Gate_Warp_Points
from map_data.Gates.VictoryRoadGate_Map import Victory_Road_Gate_Warp_Points
from map_data.Goldenrod_Group.BillsFamilysHouse_Map import Bills_Familys_House_Warp_Points
from map_data.Goldenrod_Group.DayCare_Map import Day_Care_Warp_Points
from map_data.Goldenrod_Group.GoldenrodBikeShop_Map import Goldenrod_Bike_Shop_Warp_Points
from map_data.Goldenrod_Group.GoldenrodCity_Map import Goldenrod_City_Warp_Points
from map_data.Goldenrod_Group.GoldenrodDeptStore1F_Map import Goldenrod_Dept_Store_1F_Warp_Points
from map_data.Goldenrod_Group.GoldenrodDeptStore2F_Map import Goldenrod_Dept_Store_2F_Warp_Points
from map_data.Goldenrod_Group.GoldenrodDeptStore3F_Map import Goldenrod_Dept_Store_3F_Warp_Points
from map_data.Goldenrod_Group.GoldenrodDeptStore4F_Map import Goldenrod_Dept_Store_4F_Warp_Points
from map_data.Goldenrod_Group.GoldenrodDeptStore5F_Map import Goldenrod_Dept_Store_5F_Warp_Points
from map_data.Goldenrod_Group.GoldenrodDeptStore6F_Map import Goldenrod_Dept_Store_6F_Warp_Points
from map_data.Goldenrod_Group.GoldenrodDeptStoreB1F_Map import Goldenrod_Dept_Store_B1F_Warp_Points
from map_data.Goldenrod_Group.GoldenrodDeptStoreRoof_Map import Goldenrod_Dept_Store_Roof_Warp_Points
from map_data.Goldenrod_Group.GoldenrodFlowerShop_Map import Goldenrod_Flower_Shop_Warp_Points
from map_data.Goldenrod_Group.GoldenrodGameCorner_Map import Goldenrod_Game_Corner_Warp_Points
from map_data.Goldenrod_Group.GoldenrodGym_Map import Goldenrod_Gym_Warp_Points
from map_data.Goldenrod_Group.GoldenrodHappinessRater_Map import Goldenrod_Happiness_Rater_Warp_Points
from map_data.Goldenrod_Group.GoldenrodMagnetTrainStation_Map import Goldenrod_Magnet_Train_Station_Warp_Points
from map_data.Goldenrod_Group.GoldenrodNameRater_Map import Goldenrod_Name_Rater_Warp_Points
from map_data.Goldenrod_Group.GoldenrodPPSpeechHouse_Map import Goldenrod_PP_Speech_House_Warp_Points
from map_data.Goldenrod_Group.GoldenrodPokecenter_Map import Goldenrod_Pokecenter_Warp_Points
from map_data.Dungeons_Group.GoldenrodUndergroundSwitchRoomEntrance_Map import \
    Goldenrod_Underground_Switch_Room_Entrances_Warp_Points
from map_data.Goldenrod_Group.RadioTower1F_Map import Radio_Tower_1F_Warp_Points
from map_data.Indigo_Group.IndigoPlateauPokecenter1F_Map import Indigo_Plateau_Pokecenter_1F_Warp_Points
from map_data.Indigo_Group.Route23_Map import Route23_Warp_Points
from map_data.Kanto_Routes.Route22_Map import Route_22_Warp_Points
from map_data.Mahogany_Group.MahoganyGym_Map import Mahogany_Gym_Warp_Points
from map_data.Mahogany_Group.MahoganyMart_Map import Mahogany_Mart_Warp_Points
from map_data.Mahogany_Group.MahoganyPokecenter_Map import Mahogany_Pokecenter_Warp_Points
from map_data.Mahogany_Group.MahoganyRedGyaradosSpeechHouse_Map import Mahogany_Red_Gyarados_Speech_House_Warp_Points
from map_data.Mahogany_Group.MahoganyTown_Map import Mahogany_Town_Warp_Points
from map_data.NewBark_Group.DayOfWeekSiblingsHouse_Map import Day_Of_Week_Siblings_House_Warp_Points
from map_data.NewBark_Group.ElmsHouse_Map import Elms_House_Warp_Points
from map_data.NewBark_Group.NeighborsHouse_Map import Players_Neighbors_House_Warp_Points
from map_data.NewBark_Group.NewBarkTown_Map import New_Bark_Warp_Points
from map_data.NewBark_Group.Route26HealHouse_Map import Route_26_Heal_House_Warp_Points
from map_data.NewBark_Group.Route27SandstormHouse_Map import Route_27_Sandstorm_House_Warp_Points
from map_data.Olivine_Group.OlivineCafe_Map import Olivine_Cafe_Warp_Points
from map_data.Olivine_Group.OlivineCity_Map import Olivine_City_Warp_Points
from map_data.Olivine_Group.OlivineGoodRodHouse_Map import Olivine_Good_Rod_House_Warp_Points
from map_data.Olivine_Group.OlivineGym_Map import Olivine_Gym_Warp_Points
from map_data.Olivine_Group.OlivineLighthouse1F_Map import Olivine_Lighthouse_1F_Warp_Points
from map_data.Olivine_Group.OlivineLighthouse2F_Map import Olivine_Lighthouse_2F_Warp_Points
from map_data.Olivine_Group.OlivineLighthouse3F_Map import Olivine_Lighthouse_3F_Warp_Points
from map_data.Olivine_Group.OlivineLighthouse4F_Map import Olivine_Lighthouse_4F_Warp_Points
from map_data.Olivine_Group.OlivineLighthouse5F_Map import Olivine_Lighthouse_5F_Warp_Points
from map_data.Olivine_Group.OlivineLighthouse6F_Map import Olivine_Lighthouse_6F_Warp_Points
from map_data.Olivine_Group.OlivineMart_Map import Olivine_Mart_Warp_Points
from map_data.Olivine_Group.OlivinePokecenter_Map import Olivine_Pokecenter_Warp_Points
from map_data.Olivine_Group.OlivinePortPassage_Map import Olivine_Port_Passage_Warp_Points
from map_data.Olivine_Group.OlivinePunishmentSpeechHouse_Map import Olivine_Punishment_Speech_House_Warp_Points
from map_data.Olivine_Group.OlivineTimsHouse_Map import Olivine_Tims_House_Warp_Points
from map_data.Olivine_Group.Route39Barn_Map import Route_39_Barn_Warp_Points
from map_data.Olivine_Group.Route39Farmhouse_Map import Route_39_Farmhouse_Warp_Points
from map_data.Routes.Route26_Map import Route_26_Warp_Points
from map_data.Routes.Route27_Map import Route_27_Warp_Points
from map_data.Routes.Route29_Map import Route_29_Warp_Points
from map_data.Routes.Route30_Map import Route_30_Warp_Points
from map_data.Routes.Route31_Map import Route_31_Warp_Points
from map_data.Routes.Route32Pokecenter_Map import Route_32_Pokecenter_Warp_Points
from map_data.Routes.Route32_Map import Route_32_Warp_Points
from map_data.Routes.Route33_Map import Route_33_Warp_Points
from map_data.Routes.Route34_Map import Route_34_Warp_Points
from map_data.Routes.Route35_Map import Route_35_Warp_Points
from map_data.Routes.Route36_Map import Route_36_Warp_Points
from map_data.Routes.Route38_Map import Route_38_Warp_Points
from map_data.Routes.Route39_Map import Route_39_Warp_Points
from map_data.Routes.Route40_Map import Route_40_Warp_Points
from map_data.Routes.Route41_Map import Route_41_Warp_Points
from map_data.Routes.Route42_Map import Route_42_Warp_Points
from map_data.Routes.Route43_Map import Route_43_Warp_Points
from map_data.Routes.Route44_Map import Route_44_Warp_Points
from map_data.Routes.Route45_Map import Route_45_Warp_Points
from map_data.Routes.Route46_Map import Route_46_Warp_Points
from map_data.Violet_Group.EarlsPokemonAcademy_Map import Earls_Pokemon_Academy_Warp_Points
from map_data.Violet_Group.VioletCityMart_Map import Violet_Mart_Warp_Points
from map_data.Violet_Group.VioletCityPokecenter_Map import Violet_Pokecenter_Warp_Points
from map_data.Violet_Group.VioletCity_Map import Violet_City_Warp_Points
from map_data.Violet_Group.VioletGym_Map import Violet_Gym_Warp_Points
from map_data.Violet_Group.VioletKylesHouse_Map import Violet_Kyles_House_Warp_Points
from map_data.Violet_Group.VioletNicknameSpeechHouse_Map import Violet_Nickname_Speech_House_Warp_Points



#######################################################################
#                                                                     #
#                Organized Linking is Below This Point                #
#                                                                     #
#######################################################################

#######################################################################
#                    Azalea Group                                     #
#######################################################################
class Azalea_Gym_Links(Enum):

    AZALEA_GYM_TO_AZALEA_TOWN_LINK = WarpLink(
        Azalea_Gym_Warp_Points.AZALEA_GYM_TO_AZALEA_TOWN_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_AZALEA_GYM_WP,
        "AzaleaGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_2]
    )

class Azalea_Mart_Links(Enum):

    AZALEA_MART_TO_AZALEA_TOWN_LINK = WarpLink(
        Azalea_Mart_Warp_Points.AZALEA_MART_TO_AZALEA_TOWN_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_AZALEA_MART_WP,
        "AzaleaMart", dual_width=True
    )

class Azalea_Pokecenter_Links(Enum):

    AZALEA_POKECENTER_TO_AZALEA_TOWN_LINK = WarpLink(
        Azalea_Pokecenter_Warp_Points.AZALEA_POKECENTER_TO_AZALEA_TOWN_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_AZALEA_POKECENTER_1F_WP,
        "AzaleaPokecenter1F", dual_width=True
    )

    AZALEA_POKECENTER_1F_TO_AZALEA_POKECENTER_2F_LINK = WarpLink(
        Azalea_Pokecenter_Warp_Points.AZALEA_POKECENTER_TO_AZALEA_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "AzaleaPokecenter1F", 10
    )

class Azalea_Town_Links(Enum):

    AZALEA_TOWN_TO_AZALEA_POKECENTER_1F_LINK = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_AZALEA_POKECENTER_1F_WP,
        Azalea_Pokecenter_Warp_Points.AZALEA_POKECENTER_TO_AZALEA_TOWN_WP,
        "AzaleaTown"
    )

    AZALEA_TOWN_TO_CHARCOAL_KILN_LINK = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_CHARCOAL_KILN_WP,
        Charcoal_Kiln_Warp_Points.CHARCOAL_KILN_TO_AZALEA_TOWN_WP,
        "AzaleaTown" , 5
    )

    AZALEA_TOWN_TO_AZALEA_MART_LINK = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_AZALEA_MART_WP,
        Azalea_Mart_Warp_Points.AZALEA_MART_TO_AZALEA_TOWN_WP,
        "AzaleaTown" , 10
    )

    AZALEA_TOWN_TO_KURTS_LINK = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_KURTS_HOUSE_WP,
        Kurts_House_Warp_Points.KURTS_HOUSE_TO_AZALEA_TOWN_WP,
        "AzaleaTown" , 15
    )

    AZALEA_TOWN_TO_AZALEA_GYM_LINK = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_AZALEA_GYM_WP,
        Azalea_Gym_Warp_Points.AZALEA_GYM_TO_AZALEA_TOWN_WP,
        "AzaleaTown" , 20, locked_by=[Unlock_Keys.CAN_CLEAR_SLOWPOKE_WELL]
    )

    AZALEA_TOWN_TO_SLOWPOKE_WELL_B1F_LINK = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_SLOWPOKE_WELL_B1F_WP,
        Slowpoke_Well_B1F_Warp_Points.SLOWPOKE_WELL_B1F_TO_AZALEA_TOWN_6_WP,
        "AzaleaTown" , 25, locked_by=[Unlock_Keys.KURTS_HOUSE_FOUND]
    )


    AZALEA_TOWN_TO_ILEX_FOREST_AZALEA_GATE_LINK = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_ILEX_FOREST_AZALEA_GATE_WP,
        Ilex_Forest_Azalea_Gate_Warp_Points.ILEX_FOREST_AZALEA_GATE_TO_AZALEA_TOWN_WP,
        "AzaleaTown" , 30, dual_width=True
    )

class Charcoal_Kiln_Links(Enum):

    CHARCOAL_KILN_TO_AZALEA_TOWN_LINK = WarpLink(
        Charcoal_Kiln_Warp_Points.CHARCOAL_KILN_TO_AZALEA_TOWN_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_CHARCOAL_KILN_WP,
        "CharcoalKiln", dual_width=True
    )

class Kurts_House_Links(Enum):

    KURTS_HOUSE_TO_AZALEA_TOWN_LINK = WarpLink(
        Kurts_House_Warp_Points.KURTS_HOUSE_TO_AZALEA_TOWN_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_KURTS_HOUSE_WP,
        "KurtsHouse", dual_width=True, unlocks=[Unlock_Keys.KURTS_HOUSE_FOUND]
    )


#######################################################################
#                    Blackthorn Group                                 #
#######################################################################
class Blackthorn_City_Links(Enum):

    BLACKTHORN_CITY_TO_BLACKTHORN_GYM_1F_LINK = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_GYM_1F_WP,
        Blackthorn_Gym_1F_Warp_Points.BLACKTHORN_GYM_1F_TO_BLACKTHORN_CITY_WP,
        "BlackthornCity", locked_by=[Unlock_Keys.CAN_CLEAR_RADIO_TOWER_ROCKETS],
    )

    BLACKTHORN_CITY_TO_BLACKTHORN_DRAGON_SPEECH_HOUSE_LINK = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_DRAGON_SPEECH_HOUSE_WP,
        Blackthorn_Dragon_Speech_House_Warp_Points.BLACKTHORN_DRAGON_SPEECH_HOUSE_TO_BLACKTHORN_CITY_WP,
        "BlackthornCity" , 5
    )

    BLACKTHORN_CITY_TO_BLACKTHORN_EMYS_HOUSE_LINK = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_EMYS_HOUSE_WP,
        Blackthorn_Emys_House_Warp_Points.BLACKTHORN_EMYS_HOUSE_TO_BLACKTHORN_CITY_WP,
        "BlackthornCity" , 10
    )

    BLACKTHORN_CITY_TO_BLACKTHORN_MART_LINK = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_MART_WP,
        Blackthorn_Mart_Warp_Points.BLACKTHORN_MART_TO_BLACKTHORN_CITY_WP,
        "BlackthornCity" , 15
    )

    BLACKTHORN_CITY_TO_BLACKTHORN_POKECENTER_1F_LINK = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_POKECENTER_1F_WP,
        Blackthorn_Pokecenter_Warp_Points.BLACKTHORN_POKECENTER_1F_TO_BLACKTHORN_CITY_WP,
        "BlackthornCity" , 20
    )

    BLACKTHORN_CITY_TO_MOVE_DELETERS_HOUSE_LINK = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_MOVE_DELETERS_HOUSE_WP,
        Move_Deleters_House_Warp_Points.MOVE_DELETERS_HOUSE_TO_BLACKTHORN_CITY_WP,
        "BlackthornCity" , 25
    )

    BLACKTHORN_CITY_TO_ICE_PATH_1F_LINK = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_ICE_PATH_1F_WP,
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_BLACKTHORN_CITY_7_WP,
        "BlackthornCity" , 30
    )

    BLACKTHORN_CITY_TO_DRAGONS_DEN_1F_LINK = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_DRAGONS_DEN_1F_WP,
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_BLACKTHORN_CITY_8_WP,
        "BlackthornCity" , 35, locked_by=[Unlock_Keys.GYM_BATTLE_8]
    )

class Blackthorn_Dragon_Speech_House_Links(Enum):

    BLACKTHORN_DRAGON_SPEECH_HOUSE_TO_BLACKTHORN_CITY_LINK = WarpLink(
        Blackthorn_Dragon_Speech_House_Warp_Points.BLACKTHORN_DRAGON_SPEECH_HOUSE_TO_BLACKTHORN_CITY_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_DRAGON_SPEECH_HOUSE_WP,
        "BlackthornDragonSpeechHouse", dual_width=True
    )

class Blackthorn_Emys_House_Links(Enum):

    BLACKTHORN_EMYS_HOUSE_TO_BLACKTHORN_CITY_LINK = WarpLink(
        Blackthorn_Emys_House_Warp_Points.BLACKTHORN_EMYS_HOUSE_TO_BLACKTHORN_CITY_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_EMYS_HOUSE_WP,
        "BlackthornEmysHouse", dual_width=True
    )

class Blackthorn_Gym_Links(Enum):

    BLACKTHORN_GYM_1F_TO_BLACKTHORN_CITY_LINK = WarpLink(
        Blackthorn_Gym_1F_Warp_Points.BLACKTHORN_GYM_1F_TO_BLACKTHORN_CITY_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_GYM_1F_WP,
        "BlackthornGym1F", dual_width=True, unlocks=[Unlock_Keys.GYM_BATTLE_8],
        locked_by=[Unlock_Keys.CAN_USE_STRENGTH]
    )

class Blackthorn_Mart_Links(Enum):

    BLACKTHORN_MART_TO_BLACKTHORN_CITY_LINK = WarpLink(
        Blackthorn_Mart_Warp_Points.BLACKTHORN_MART_TO_BLACKTHORN_CITY_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_MART_WP,
        "BlackthornMart", dual_width=True
    )

class Blackthorn_Pokecenter_Links(Enum):

    BLACKTHORN_POKECENTER_1F_TO_BLACKTHORN_CITY_LINK = WarpLink(
        Blackthorn_Pokecenter_Warp_Points.BLACKTHORN_POKECENTER_1F_TO_BLACKTHORN_CITY_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_POKECENTER_1F_WP,
        "BlackthornPokecenter1F", dual_width=True
    )

    BLACKTHORN_POKECENTER_1F_TO_BLACKTHORN_POKECENTER_2F_LINK = WarpLink(
        Blackthorn_Pokecenter_Warp_Points.BLACKTHORN_POKECENTER_TO_BLACKTHORN_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "BlackthornPokecenter1F", 10
    )

class Move_Deleters_House_Links(Enum):

    MOVE_DELETERS_HOUSE_TO_BLACKTHORN_CITY_LINK = WarpLink(
        Move_Deleters_House_Warp_Points.MOVE_DELETERS_HOUSE_TO_BLACKTHORN_CITY_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_MOVE_DELETERS_HOUSE_WP,
        "MoveDeletersHouse", dual_width=True
    )

#######################################################################
#                    Cherrywood Group                                 #
#######################################################################
class Cherrygrove_City_Links(Enum):

    CHERRYGROVE_CITY_TO_CHERRYGROVE_MART_LINK = WarpLink(
        Cherrygrove_City_Warp_Points.CHERRYGROVE_CITY_TO_CHERRYGROVE_MART_WP,
        Cherrygrove_Mart_Warp_Points.CHERRYGROVE_MART_TO_CHERRYGROVE_CITY_WP,
        "CherrygroveCity"
    )

    CHERRYGROVE_CITY_TO_CHERRYGROVE_POKECENTER_1F_LINK = WarpLink(
        Cherrygrove_City_Warp_Points.CHERRYGROVE_CITY_TO_CHERRYGROVE_POKECENTER_1F_WP,
        Cherrygrove_Pokecenter_Warp_Points.CHERRYGROVE_POKECENTER_TO_CHERRYGROVE_CITY,
        "CherrygroveCity" , 5
    )

    CHERRYGROVE_CITY_TO_CHERRYGROVE_GYM_SPEECH_HOUSE_LINK = WarpLink(
        Cherrygrove_City_Warp_Points.CHERRYGROVE_CITY_TO_CHERRYGROVE_GYM_SPEECH_HOUSE_WP,
        Cherrygrove_Gym_Speech_House_Warp_Points.CHERRYGROVE_GYM_SPEECH_HOUSE_TO_CHERRYGROVE_CITY,
        "CherrygroveCity" , 10
    )

    CHERRYGROVE_CITY_TO_GUIDE_GENTS_HOUSE_LINK = WarpLink(
        Cherrygrove_City_Warp_Points.CHERRYGROVE_CITY_TO_GUIDE_GENTS_HOUSE_WP,
        Guide_Gents_House_Warp_Points.GUIDE_GENTS_HOUSE_TO_CHERRYGROVE_CITY_WP,
        "CherrygroveCity" , 15
    )

    CHERRYGROVE_CITY_TO_CHERRYGROVE_EVOLUTION_SPEECH_HOUSE_LINK = WarpLink(
        Cherrygrove_City_Warp_Points.CHERRYGROVE_CITY_TO_CHERRYGROVE_EVOLUTION_SPEECH_HOUSE_WP,
        Cherrygrove_Evolution_Speech_House_Warp_Points.CHERRYGROVE_EVOLUTION_SPEECH_HOUSE_TO_CHERRYGROVE_CITY_WP,
        "CherrygroveCity" , 20
)

class Cherrygrove_Pokecenter_Links(Enum):

    CHERRYGROVE_POKECENTER_TO_CHERRYGROVE_CITY_LINK = WarpLink(
        Cherrygrove_Pokecenter_Warp_Points.CHERRYGROVE_POKECENTER_TO_CHERRYGROVE_CITY,
        Cherrygrove_City_Warp_Points.CHERRYGROVE_CITY_TO_CHERRYGROVE_POKECENTER_1F_WP,
        "CherrygrovePokecenter1F",
        dual_width=True
    )

    CHERRYGROVE_POKECENTER_TO_CHERRYGROVE_POKECENTER_2F_LINK = WarpLink(
        Cherrygrove_Pokecenter_Warp_Points.CHERRYGROVE_POKECENTER_TO_CHERRYGROVE_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "CherrygrovePokecenter1F", 10
    )

class Cherrygrove_Evolution_Speech_House_Links(Enum):

    CHERRYGROVE_EVOLUTION_SPEECH_HOUSE_TO_CHERRYGROVE_CITY_LINK = WarpLink(
        Cherrygrove_Evolution_Speech_House_Warp_Points.CHERRYGROVE_EVOLUTION_SPEECH_HOUSE_TO_CHERRYGROVE_CITY_WP,
        Cherrygrove_City_Warp_Points.CHERRYGROVE_CITY_TO_CHERRYGROVE_EVOLUTION_SPEECH_HOUSE_WP,
        "CherrygroveEvolutionSpeechHouse",
        dual_width=True
    )

class Cherrygrove_Mart_Links(Enum):

    CHERRYGROVE_MART_TO_CHERRYGROVE_CITY_LINK = WarpLink(
        Cherrygrove_Mart_Warp_Points.CHERRYGROVE_MART_TO_CHERRYGROVE_CITY_WP,
        Cherrygrove_City_Warp_Points.CHERRYGROVE_CITY_TO_CHERRYGROVE_MART_WP,
        "CherrygroveMart",
        dual_width=True
    )

class Cherrygrove_Gym_Speech_House_Links(Enum):

    CHERRYGROVE_GYM_SPEECH_HOUSE_TO_CHERRYGROVE_CITY_LINK = WarpLink(
        Cherrygrove_Gym_Speech_House_Warp_Points.CHERRYGROVE_GYM_SPEECH_HOUSE_TO_CHERRYGROVE_CITY,
        Cherrygrove_City_Warp_Points.CHERRYGROVE_CITY_TO_CHERRYGROVE_GYM_SPEECH_HOUSE_WP,
        "CherrygroveGymSpeechHouse",
        dual_width=True
    )

class Guide_Gents_House_Links(Enum):

    GUIDE_GENTS_HOUSE_TO_CHERRYGROVE_CITY_LINK = WarpLink(
        Guide_Gents_House_Warp_Points.GUIDE_GENTS_HOUSE_TO_CHERRYGROVE_CITY_WP,
        Cherrygrove_City_Warp_Points.CHERRYGROVE_CITY_TO_GUIDE_GENTS_HOUSE_WP,
        "GuideGentsHouse",
        dual_width=True
    )

class Mr_Pokemons_House_Links(Enum):

    MR_POKEMONS_HOUSE_TO_ROUTE_30_LINK = WarpLink(
        Mr_Pokemons_House_Warp_Points.MR_POKEMONS_HOUSE_TO_ROUTE_30_WP,
        Route_30_Warp_Points.ROUTE_30_TO_MR_POKEMONS_HOUSE_WP,
        "MrPokemonsHouse",
        dual_width=True
    )

class Route_30_Berry_House_Links(Enum):

    ROUTE_30_BERRY_HOUSE_TO_ROUTE_30_LINK = WarpLink(
        Route_30_Berry_House_Warp_Points.ROUTE_30_BERRY_HOUSE_TO_ROUTE_30_WP,
        Route_30_Warp_Points.ROUTE_30_TO_ROUTE_30_BERRY_HOUSE_WP,
        "Route30BerryHouse",
        dual_width=True
    )

#######################################################################
#                    Cianwood Group                                   #
#######################################################################
class Cianwood_City_Links(Enum):

    CIANWOOD_CITY_TO_MANIAS_HOUSE_LINK = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_MANIAS_HOUSE_WP,
        Manias_House_Warp_Points.MANIAS_HOUSE_TO_CIANWOOD_CITY_WP,
        "CianwoodCity",unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )
    CIANWOOD_CITY_TO_CIANWOOD_GYM_LINK = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_GYM_WP,
        Cianwood_Gym_Warp_Points.CIANWOOD_GYM_TO_CIANWOOD_CITY_WP,
        "CianwoodCity" , 5,unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )
    CIANWOOD_CITY_TO_CIANWOOD_POKECENTER_1F_LINK = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_POKECENTER_1F_WP,
        Cianwood_Pokecenter_Warp_Points.CIANWOOD_POKECENTER_1F_TO_CIANWOOD_CITY_WP,
        "CianwoodCity" , 10,unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )
    CIANWOOD_CITY_TO_CIANWOOD_PHARMACY_LINK = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_PHARMACY_WP,
        Cianwood_Pharmacy_Warp_Points.CIANWOOD_PHARMACY_TO_CIANWOOD_CITY_WP,
        "CianwoodCity" , 15,unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )
    CIANWOOD_CITY_TO_CIANWOOD_PHOTO_STUDIO_LINK = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_PHOTO_STUDIO_WP,
        Cianwood_Photo_Studio_Warp_Points.CIANWOOD_PHOTO_STUDIO_TO_CIANWOOD_CITY_WP,
        "CianwoodCity" , 20,unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )
    CIANWOOD_CITY_TO_CIANWOOD_LUGIA_SPEECH_HOUSE_LINK = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_LUGIA_SPEECH_HOUSE_WP,
        Cianwood_Lugia_Speech_House_Warp_Points.CIANWOOD_LUGIA_SPEECH_HOUSE_TO_CIANWOOD_CITY_WP,
        "CianwoodCity" , 25,unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )
    CIANWOOD_CITY_TO_POKE_SEERS_HOUSE_LINK = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_POKE_SEERS_HOUSE_WP,
        Poke_Seers_House_Warp_Points.POKE_SEERS_HOUSE_TO_CIANWOOD_CITY_WP,
        "CianwoodCity" , 30,unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )

class Cianwood_Gym_Links(Enum):

    CIANWOOD_GYM_TO_CIANWOOD_CITY_LINK = WarpLink(
        Cianwood_Gym_Warp_Points.CIANWOOD_GYM_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_GYM_WP,
        "CianwoodGym", dual_width=True, unlocks=[Unlock_Keys.BADGE_5],
        locked_by=[Unlock_Keys.CAN_USE_STRENGTH]
    )

class Cianwood_Lugia_Speech_House_Links(Enum):

    CIANWOOD_LUGIA_SPEECH_HOUSE_TO_CIANWOOD_CITY_LINK = WarpLink(
        Cianwood_Lugia_Speech_House_Warp_Points.CIANWOOD_LUGIA_SPEECH_HOUSE_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_LUGIA_SPEECH_HOUSE_WP,
        "CianwoodLugiaSpeechHouse", dual_width=True
    )

class Cianwood_Pharmacy_Links(Enum):

    CIANWOOD_PHARMACY_TO_CIANWOOD_CITY_LINK = WarpLink(
        Cianwood_Pharmacy_Warp_Points.CIANWOOD_PHARMACY_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_PHARMACY_WP,
        "CianwoodPharmacy", dual_width=True, unlocks=[Unlock_Keys.CIANNWOOD_PHARMACY_FOUND]
    )

class Cianwood_Photo_Studio_Links(Enum): #Unused as a node because it breaks the game
    CIANWOOD_PHOTO_STUDIO_TO_CIANWOOD_CITY_LINK = WarpLink(
        Cianwood_Photo_Studio_Warp_Points.CIANWOOD_PHOTO_STUDIO_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_PHOTO_STUDIO_WP,
        "CianwoodPhotoStudio", dual_width=True
    )

class Cianwood_Pokecenter_Links(Enum):

    CIANWOOD_POKECENTER_1F_TO_CIANWOOD_CITY_LINK = WarpLink(
        Cianwood_Pokecenter_Warp_Points.CIANWOOD_POKECENTER_1F_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_POKECENTER_1F_WP,
        "CianwoodPokecenter1F", dual_width=True
    )

    CIANWOOD_POKECENTER_1F_TO_CIANWOOD_POKECENTER_2F_LINK = WarpLink(
        Cianwood_Pokecenter_Warp_Points.CIANWOOD_POKECENTER_TO_CIANWOOD_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "CianwoodPokecenter1F", 10
    )

class Manias_House_Links(Enum):

    MANIAS_HOUSE_TO_CIANWOOD_CITY = WarpLink(
        Manias_House_Warp_Points.MANIAS_HOUSE_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_MANIAS_HOUSE_WP,
        "ManiasHouse", dual_width=True
    )

class Poke_Seers_House_Links(Enum):

    POKE_SEERS_HOUSE_TO_CIANWOOD_CITY_LINK = WarpLink(
        Poke_Seers_House_Warp_Points.POKE_SEERS_HOUSE_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_POKE_SEERS_HOUSE_WP,
        "PokeSeersHouse", dual_width=True
    )


#######################################################################
#                    Dungeons Group                                   #
#######################################################################
class Mount_Mortar_1F_Outside_Links(Enum):
    MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_3_LINK = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_3_WP,
        Route_42_Warp_Points.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_LEFT_WP,
        "MountMortar1FOutside"
    )

    MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_4_LINK = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_4_WP,
        Route_42_Warp_Points.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_MIDDLE_WP,
        "MountMortar1FOutside",5
    )

    MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_5_LINK = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_5_WP,
        Route_42_Warp_Points.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_RIGHT_WP,
        "MountMortar1FOutside",10
    )

    MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_2F_INSIDE_1_LINK = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_2F_INSIDE_1_WP,
        Mount_Mortar_2F_Inside_Warp_Points.MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_4_WP,
        "MountMortar1FOutside",15
    )

    MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_1_LINK = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_1_WP,
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_5_WP,
        "MountMortar1FOutside",20
    )

    MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_2_LINK = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_2_WP,
    Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_6_WP,
        "MountMortar1FOutside",25
    )

    MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_B1F_2_LINK = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_B1F_2_WP,
        Mount_Mortar_B1F_Warp_Points.MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_OUTSIDE_7_WP,
        "MountMortar1FOutside",30
    )

    MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_3_LINK = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_3_WP,
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_8_WP,
        "MountMortar1FOutside",35
    )

    MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_4_LINK = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_4_WP,
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_9_WP,
        "MountMortar1FOutside",40
    )

class Mount_Mortar_B1F_Links(Enum):
    MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_INSIDE_5_LINK = WarpLink(
        Mount_Mortar_B1F_Warp_Points.MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_INSIDE_5_WP,
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_B1F_1_WP,
        "MountMortarB1F"
    )

    MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_OUTSIDE_7_LINK = WarpLink(
        Mount_Mortar_B1F_Warp_Points.MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_OUTSIDE_7_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_B1F_2_WP,
        "MountMortarB1F",5
    )

class Mount_Mortar_2F_Inside_Links(Enum):

    MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_4_LINK = WarpLink(
        Mount_Mortar_2F_Inside_Warp_Points.MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_4_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_2F_INSIDE_1_WP,
        "MountMortar2FInside"
    )

    MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_INSIDE_6_LINK = WarpLink(
        Mount_Mortar_2F_Inside_Warp_Points.MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_INSIDE_6_WP,
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_2F_INSIDE_2_WP,
        "MountMortar2FInside", 5
    )

class Mount_Mortar_1F_Inside_Links(Enum):
    MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_5_LINK = WarpLink(
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_5_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_1_WP,
        "MountMortar1FInside"
    )

    MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_6_LINK = WarpLink(
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_6_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_2_WP,
        "MountMortar1FInside",5
    )

    MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_8_LINK = WarpLink(
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_8_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_3_WP,
        "MountMortar1FInside",10
    )

    MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_9_LINK = WarpLink(
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_9_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_4_WP,
        "MountMortar1FInside",15
    )

    MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_B1F_1_LINK = WarpLink(
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_B1F_1_WP,
        Mount_Mortar_B1F_Warp_Points.MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_INSIDE_5_WP,
        "MountMortar1FInside",20
    )

    MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_2F_INSIDE_2_LINK = WarpLink(
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_2F_INSIDE_2_WP,
        Mount_Mortar_2F_Inside_Warp_Points.MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_INSIDE_6_WP,
        "MountMortar1FInside",25
    )


class Ice_Path_1F_Links(Enum):
    ICE_PATH_1F_TO_ROUTE_44_1_LINK = WarpLink(
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_ROUTE_44_1_WP,
        Route_44_Warp_Points.ROUTE_44_TO_ICE_PATH_1F_WP,
        "IcePath1F", unlocks=[Unlock_Keys.HM_WATERFALL]
    )

    ICE_PATH_1F_TO_BLACKTHORN_CITY_7_LINK = WarpLink(
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_BLACKTHORN_CITY_7_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_ICE_PATH_1F_WP,
        "IcePath1F", 5
    )

    ICE_PATH_1F_TO_ICE_PATH_B1F_1_LINK = WarpLink(
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_ICE_PATH_B1F_1_WP,
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_1F_3_WP,
        "IcePath1F", 10, unlocks=[Unlock_Keys.HM_WATERFALL]
    )

    ICE_PATH_1F_TO_ICE_PATH_B1F_7_LINK = WarpLink(
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_ICE_PATH_B1F_7_WP,
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_1F_4_WP,
        "IcePath1F", 15
    )


class Ice_Path_B1F_Links(Enum):
    ICE_PATH_B1F_TO_ICE_PATH_1F_3_LINK = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_1F_3_WP,
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_ICE_PATH_B1F_1_WP,
        "IcePathB1F"
    )

    ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_1_LINK = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_1_WP,
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_2_WP,
        "IcePathB1F", 5
    )

    ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_3_LINK = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_3_WP,
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_3_WP,
        "IcePathB1F", 10
    )

    ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_4_LINK = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_4_WP,
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_4_WP,
        "IcePathB1F", 15
    )

    ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_5_LINK = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_5_WP,
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_5_WP,
        "IcePathB1F", 20
    )

    ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_6_LINK = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_6_WP,
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_6_WP,
        "IcePathB1F", 25
    )

    ICE_PATH_B1F_TO_ICE_PATH_1F_4_LINK = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_1F_4_WP,
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_ICE_PATH_B1F_7_WP,
        "IcePathB1F",30
    )

    ICE_PATH_B1F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_1_LINK = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_1_WP,
        Ice_Path_B2F_Blackthorn_Side_Warp_Points.ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B1F_8_WP,
        "IcePathB1F",35
    )

class Ice_Path_B2F_Blackthorn_Side_Links(Enum):
    ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B1F_8_LINK = WarpLink(
        Ice_Path_B2F_Blackthorn_Side_Warp_Points.ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B1F_8_WP,
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_1_WP,
        "IcePathB2FBlackthornSide"
    )

    ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B3F_2_LINK = WarpLink(
        Ice_Path_B2F_Blackthorn_Side_Warp_Points.ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B3F_2_WP,
        Ice_Path_B3F_Warp_Points.ICE_PATH_B3F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_2_WP,
        "IcePathB2FBlackthornSide",5
    )

class Ice_Path_B3F_Links(Enum):
    ICE_PATH_B3F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_2_LINK = WarpLink(
        Ice_Path_B3F_Warp_Points.ICE_PATH_B3F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_2_WP,
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B3F_1_WP,
        "IcePathB3F"
    )

    ICE_PATH_B3F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_2_LINK = WarpLink(
        Ice_Path_B3F_Warp_Points.ICE_PATH_B3F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_2_WP,
        Ice_Path_B2F_Blackthorn_Side_Links.ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B3F_2_LINK,
        "IcePathB3F",5
    )

class Ice_Path_B2F_Mahogany_Side_Links(Enum):

    ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_2_LINK = WarpLink(
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_2_WP,
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_1_WP,
        "IcePathB2FMahoganySide"
    )

    ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B3F_1_LINK = WarpLink(
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B3F_1_WP,
        Ice_Path_B3F_Warp_Points.ICE_PATH_B3F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_2_WP,
        "IcePathB2FMahoganySide",5
    )



class Burned_Tower_1F_Links(Enum):
    BURNED_TOWER_1F_TO_ECRUTEAK_CITY_LINK = WarpLink(
        Burned_Tower_1F_Warp_Points.BURNED_TOWER_1F_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_BURNED_TOWER_1F_WP,
        "BurnedTower1F", dual_width=True, unlocks=[Unlock_Keys.ENTERED_BURNED_TOWER]
    )

    # BURNED_TOWER_1F_TO_BURNED_TOWER_B1F_LINK = WarpLink(
    #     Burned_Tower_1F_Warp_Points.BURNED_TOWER_1F_TO_BURNED_TOWER_B1F_WP,
    #
    #     0x001860B7 , 10
    # )


class Dark_Cave_Violet_Entrance_Links(Enum):
    DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_31_LINK = WarpLink(
        Dark_Cave_Violet_Entrance_Warp_Points.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_31_WP,
        Route_31_Warp_Points.ROUTE_31_TO_DARK_CAVE_VIOLET_ENTRANCE_WP,
        "DarkCaveVioletEntrance",
    )

    DARK_CAVE_VIOLET_ENTRANCE_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_LINK = WarpLink(
        Dark_Cave_Violet_Entrance_Warp_Points.DARK_CAVE_VIOLET_ENTRANCE_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_WP,
        Dark_Cave_Blackthorn_Entrance_Warp_Points.DARK_CAVE_BLACKTHORN_ENTRANCE_TO_DARK_CAVE_VIOLET_ENTRANCE_WP,
        "DarkCaveVioletEntrance", 5
    ) #todo add rocksmash as a key, and determine where unlocks for it exist

    DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_46_LINK = WarpLink(
        Dark_Cave_Violet_Entrance_Warp_Points.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_46_WP,
        Route_46_Warp_Points.ROUTE_46_TO_DARK_CAVE_VIOLET_ENTRANCE_WP,
        "DarkCaveVioletEntrance" , 10
    )

class Dark_Cave_Blackthorn_Entrance_Links(Enum):
    DARK_CAVE_BLACKTHORN_ENTRANCE_TO_ROUTE_45_LINK = WarpLink(
        Dark_Cave_Blackthorn_Entrance_Warp_Points.DARK_CAVE_BLACKTHORN_ENTRANCE_TO_ROUTE_45_WP,
        Route_45_Warp_Points.ROUTE_45_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_WP,
        "DarkCaveBlackthornEntrance"
    )

    DARK_CAVE_BLACKTHORN_ENTRANCE_TO_DARK_CAVE_VIOLET_ENTRANCE_LINK = WarpLink(
        Dark_Cave_Blackthorn_Entrance_Warp_Points.DARK_CAVE_BLACKTHORN_ENTRANCE_TO_DARK_CAVE_VIOLET_ENTRANCE_WP,
        Dark_Cave_Violet_Entrance_Warp_Points.DARK_CAVE_VIOLET_ENTRANCE_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_WP,
        "DarkCaveBlackthornEntrance",5
    )


class Ilex_Forest_Links(Enum):
    ILEX_FOREST_TO_ROUTE_34_ILEX_FOREST_GATE_LINK = WarpLink(
        Ilex_Forest_Warp_Points.ILEX_FOREST_TO_ROUTE_34_ILEX_FOREST_GATE_WP,
        Route_34_Ilex_Forest_Gate_Warp_Points.ROUTE_34_ILEX_FOREST_GATE_TO_ILEX_FOREST_WP,
        "IlexForest"
    )

    ILEX_FOREST_TO_ILEX_FOREST_AZALEA_GATE_LINK = WarpLink(
        Ilex_Forest_Warp_Points.ILEX_FOREST_TO_ILEX_FOREST_AZALEA_GATE_WP,
        Ilex_Forest_Azalea_Gate_Warp_Points.ILEX_FOREST_AZALEA_GATE_TO_ILEX_FOREST_WP,
        "IlexForest" , 5, dual_width=True, locked_by=[Unlock_Keys.CAN_CLEAR_SLOWPOKE_WELL],
     unlocks=[Unlock_Keys.HM_CUT]
    )

#TODO Add National_Park_Bug_Catching_Contest
class National_Park_Links(Enum):
    NATIONAL_PARK_TO_ROUTE_36_NATIONAL_PARK_GATE_LINK = WarpLink(
        National_Park_Warp_Points.NATIONAL_PARK_TO_ROUTE_36_NATIONAL_PARK_GATE_WP,
        Route_36_National_Park_Gate_Warp_Points.ROUTE_36_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_WP,
        "NationalPark", dual_width=True
    )

    NATIONAL_PARK_TO_ROUTE_35_NATIONAL_PARK_GATE_LINK = WarpLink(
        National_Park_Warp_Points.NATIONAL_PARK_TO_ROUTE_35_NATIONAL_PARK_GATE_WP,
        Route_35_National_Park_Gate_Warp_Points.ROUTE_35_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_WP,
        "NationalPark" , 10, dual_width=True
    )

class Ruins_Of_Alph_Outside_Links(Enum):
    RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_1_LINK = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_1_WP,
        Ruins_Of_Alph_Ho_Oh_Chamber_Warp_Points.RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_1_WP,
        "RuinsOfAlphOutside"
    )

    RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_KABUTO_CHAMBER_1_LINK = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_KABUTO_CHAMBER_1_WP,
        Ruins_Of_Alph_Kabuto_Chamber_Warp_Points.RUINS_OF_ALPH_KABUTO_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_2_WP,
        "RuinsOfAlphOutside",5
    )

    RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_OMANYTE_CHAMBER_1_LINK = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_OMANYTE_CHAMBER_1_WP,
        Ruins_Of_Alph_Omanyte_Chamber_Warp_Points.RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_3_WP,
        "RuinsOfAlphOutside",10
    )

    RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_AERODACTYL_CHAMBER_1_LINK = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_AERODACTYL_CHAMBER_1_WP,
        Ruins_Of_Alph_Aerodactyl_Chamber_Warp_Points.RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_4_WP,
        "RuinsOfAlphOutside", 15
    )

    RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_INNER_CHAMBER_1_LINK = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_INNER_CHAMBER_1_WP,
        Ruins_Of_Alph_Inner_Chamber_Warp_Points.RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_WP,
        "RuinsOfAlphOutside", 20
    )

    RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_RESEARCH_CENTER_1_LINK = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_RESEARCH_CENTER_1_WP,
        Ruins_Of_Alph_Research_Center_Warp_Points.RUINS_OF_ALPH_RESEARCH_CENTER_TO_RUINS_OF_ALPH_OUTSIDE_WP,
        "RuinsOfAlphOutside",25
    )

    RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_1_LINK = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_1_WP,
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_7_WP,
        "RuinsOfAlphOutside",30
    )

    RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_2_LINK = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_2_WP,
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_8_WP,
        "RuinsOfAlphOutside",35
    )

    RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_36_RUINS_OF_ALPH_GATE_3_LINK = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_36_RUINS_OF_ALPH_GATE_3_WP,
        Route_36_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_36_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_WP,
        "RuinsOfAlphOutside",40
    )

    RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_32_RUINS_OF_ALPH_GATE_1_LINK = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_32_RUINS_OF_ALPH_GATE_1_WP,
        Route_32_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_32_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_WP,
        "RuinsOfAlphOutside",45, dual_width=True
    )



class Ruins_Of_Alph_Research_Center_Links(Enum):
    RUINS_OF_ALPH_RESEARCH_CENTER_TO_RUINS_OF_ALPH_OUTSIDE_LINK = WarpLink(
        Ruins_Of_Alph_Research_Center_Warp_Points.RUINS_OF_ALPH_RESEARCH_CENTER_TO_RUINS_OF_ALPH_OUTSIDE_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_RESEARCH_CENTER_1_WP,
        "RuinsOfAlphResearchCenter", dual_width=True
    )

class Ruins_Of_Alph_Inner_Chamber_Links(Enum):
    RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_LINK = WarpLink(
        Ruins_Of_Alph_Inner_Chamber_Warp_Points.RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_INNER_CHAMBER_1_WP,
        "RuinsOfAlphInnerChamber"
    )

class Ruins_Of_Alph_Aerodactyl_Chamber_Links(Enum):
    RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_4_LINK = WarpLink(
        Ruins_Of_Alph_Aerodactyl_Chamber_Warp_Points.RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_4_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_AERODACTYL_CHAMBER_1_WP,
        "RuinsOfAlphAerodactylChamber",dual_width=True
    )

    RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_8_LINK = WarpLink(
        Ruins_Of_Alph_Aerodactyl_Chamber_Warp_Points.RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_8_WP,
        Ruins_Of_Alph_Inner_Chamber_Warp_Points.RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_WP, #This is not correct but we always overwrite
        "RuinsOfAlphAerodactylChamber", 10, dual_width=True
    )


class Ruins_Of_Alph_Aerodactyl_Item_Room_Links(Enum):
    RUINS_OF_ALPH_AERODACTYL_ITEM_ROOM_TO_RUINS_OF_ALPH_AERODACTYL_WORD_ROOM_1_LINK = WarpLink(
        Ruins_Of_Alph_Aerodactyl_Item_Room_Warp_Points.RUINS_OF_ALPH_AERODACTYL_ITEM_ROOM_TO_RUINS_OF_ALPH_AERODACTYL_WORD_ROOM_1_WP,
        Ruins_Of_Alph_Aerodactyl_Item_Room_Warp_Points.RUINS_OF_ALPH_AERODACTYL_ITEM_ROOM_TO_RUINS_OF_ALPH_AERODACTYL_WORD_ROOM_1_WP, #Incorrect but always overwrite
        "RuinsOfAlphAerodactylItemRoom", 10, dual_width=True
    )

class Ruins_Of_Alph_Ho_Oh_Chamber_Links(Enum):
    RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_1_LINK = WarpLink(
        Ruins_Of_Alph_Ho_Oh_Chamber_Warp_Points.RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_1_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_1_WP,
        "RuinsOfAlphHoOhChamber",dual_width=True
    )

    RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_2_LINK = WarpLink(
        Ruins_Of_Alph_Ho_Oh_Chamber_Warp_Points.RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_2_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_1_WP, #incorrect but overwritten
        "RuinsOfAlphHoOhChamber", 10, dual_width=True
    )


class Ruins_Of_Alph_Ho_Oh_Item_Room_Links(Enum):
    RUINS_OF_ALPH_HO_OH_ITEM_ROOM_TO_RUINS_OF_ALPH_HO_OH_WORD_ROOM_1_LINK = WarpLink(
        Ruins_Of_Alph_Ho_Oh_Item_Room_Warp_Points.RUINS_OF_ALPH_HO_OH_ITEM_ROOM_TO_RUINS_OF_ALPH_HO_OH_WORD_ROOM_1_WP,
        Ruins_Of_Alph_Ho_Oh_Item_Room_Warp_Points.RUINS_OF_ALPH_HO_OH_ITEM_ROOM_TO_RUINS_OF_ALPH_HO_OH_WORD_ROOM_1_WP,
        "RuinsOfAlphHoOhItemRoom",10, dual_width=True
    )

class Ruins_Of_Alph_Kabuto_Chamber_Links(Enum):
    RUINS_OF_ALPH_KABUTO_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_2_LINK = WarpLink(
        Ruins_Of_Alph_Kabuto_Chamber_Warp_Points.RUINS_OF_ALPH_KABUTO_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_2_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_KABUTO_CHAMBER_1_WP,
        "RuinsOfAlphKabutoChamber", dual_width=True
    )

    RUINS_OF_ALPH_KABUTO_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_4_LINK = WarpLink(
        Ruins_Of_Alph_Kabuto_Chamber_Warp_Points.RUINS_OF_ALPH_KABUTO_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_4_WP,
        Ruins_Of_Alph_Inner_Chamber_Warp_Points.RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_WP, #overwritten
        "RuinsOfAlphKabutoChamber", 10, dual_width=True
    )


class Ruins_Of_Alph_Kabuto_Item_Room_Links(Enum):
    RUINS_OF_ALPH_KABUTO_ITEM_ROOM_TO_RUINS_OF_ALPH_KABUTO_WORD_ROOM_1_LINK = WarpLink(
        Ruins_Of_Alph_Kabuto_Item_Room_Warp_Points.RUINS_OF_ALPH_KABUTO_ITEM_ROOM_TO_RUINS_OF_ALPH_KABUTO_WORD_ROOM_1_WP,
        Ruins_Of_Alph_Kabuto_Item_Room_Warp_Points.RUINS_OF_ALPH_KABUTO_ITEM_ROOM_TO_RUINS_OF_ALPH_KABUTO_WORD_ROOM_1_WP,
        "RuinsOfAlphKabutoItemRoom", 10, dual_width=True
    )


class Ruins_Of_Alph_Omanyte_Chamber_Links(Enum):
    RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_3_LINK = WarpLink(
        Ruins_Of_Alph_Omanyte_Chamber_Warp_Points.RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_3_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_OMANYTE_CHAMBER_1_WP,
        "RuinsOfAlphOmanyteChamber", dual_width=True
    )

    RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_6_LINK = WarpLink(
        Ruins_Of_Alph_Omanyte_Chamber_Warp_Points.RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_6_WP,
        Ruins_Of_Alph_Inner_Chamber_Warp_Points.RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_WP, #incorrect but overwrite
        "RuinsOfAlphOmanyteChamber", 10, dual_width=True
    )


class Ruins_Of_Alph_Omanyte_Item_Room_Links(Enum):
    RUINS_OF_ALPH_OMANYTE_ITEM_ROOM_TO_RUINS_OF_ALPH_OMANYTE_WORD_ROOM_1_LINK = WarpLink(
        Ruins_Of_Alph_Omanyte_Item_Room_Warp_Points.RUINS_OF_ALPH_OMANYTE_ITEM_ROOM_TO_RUINS_OF_ALPH_OMANYTE_WORD_ROOM_1_WP,
        Ruins_Of_Alph_Omanyte_Item_Room_Warp_Points.RUINS_OF_ALPH_OMANYTE_ITEM_ROOM_TO_RUINS_OF_ALPH_OMANYTE_WORD_ROOM_1_WP,
        "RuinsOfOmanyteItemRoom", 10, dual_width=True
    )


class Slowpoke_Well_B1F_Links(Enum):
    SLOWPOKE_WELL_B1F_TO_AZALEA_TOWN_LINK = WarpLink(
        Slowpoke_Well_B1F_Warp_Points.SLOWPOKE_WELL_B1F_TO_AZALEA_TOWN_6_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_SLOWPOKE_WELL_B1F_WP,
        "SlowpokeWellB1F", unlocks=[Unlock_Keys.SLOWPOKE_WELL_FOUND]
    )

    SLOWPOKE_WELL_B1F_TO_SLOWPOKE_WELL_B2F_LINK = WarpLink(
        Slowpoke_Well_B1F_Warp_Points.SLOWPOKE_WELL_B1F_TO_SLOWPOKE_WELL_B2F_1_WP,
        Slowpoke_Well_B2F_Warp_Points.SLOWPOKE_WELL_B2_F_TO_SLOWPOKE_WELL_B1F_2_WP,
        "SlowpokeWellB1F" , 5
    )

class Slowpoke_Well_B2F_Links(Enum):
    SLOWPOKE_WELL_B2F_TO_SLOWPOKE_WELL_B1F_LINK = WarpLink(
        Slowpoke_Well_B2F_Warp_Points.SLOWPOKE_WELL_B2_F_TO_SLOWPOKE_WELL_B1F_2_WP,
        Slowpoke_Well_B1F_Warp_Points.SLOWPOKE_WELL_B1F_TO_SLOWPOKE_WELL_B2F_1_WP,
        "SlowpokeWellB2F"
    )

class Dragons_Den_1F_Links(Enum):

    DRAGONS_DEN_1F_TO_BLACKTHORN_CITY_8_LINK = WarpLink(
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_BLACKTHORN_CITY_8_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_DRAGONS_DEN_1F_WP,
        "DragonsDen1F"
    )

    DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_4_LINK = WarpLink(
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_4_WP,
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_2_WP,
        "DragonsDen1F", 5
    )

    DRAGONS_DEN_1F_TO_DRAGONS_DEN_B1F_1_LINK = WarpLink(
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_DRAGONS_DEN_B1F_1_WP,
        Dragons_Den_B1F_Warp_Points.DRAGONS_DEN_B1F_TO_DRAGONS_DEN_1F_3_WP,
        "DragonsDen1F", 10
    )

    DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_2_LINK = WarpLink(
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_2_WP,
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_4_WP,
        "DragonsDen1F", 15
    )

class Dragons_Den_B1F_Links(Enum):
    DRAGONS_DEN_B1F_TO_DRAGONS_DEN_1F_3_LINK = WarpLink(
        Dragons_Den_B1F_Warp_Points.DRAGONS_DEN_B1F_TO_DRAGONS_DEN_1F_3_WP,
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_DRAGONS_DEN_B1F_1_WP,
        "DragonsDenB1F"
    )

    DRAGONS_DEN_B1F_TO_DRAGON_SHRINE_1_LINK = WarpLink(
        Dragons_Den_B1F_Warp_Points.DRAGONS_DEN_B1F_TO_DRAGON_SHRINE_1_WP,
        Dragon_Shrine_Warp_Points.DRAGON_SHRINE_TO_DRAGONS_DEN_B1F_2_WP,
        "DragonsDenB1F", 5
    )


class Dragon_Shrine_Links(Enum):
    DRAGON_SHRINE_TO_DRAGONS_DEN_B1F_2_LINK = WarpLink(
        Dragon_Shrine_Warp_Points.DRAGON_SHRINE_TO_DRAGONS_DEN_B1F_2_WP,
        Dragons_Den_B1F_Warp_Points.DRAGONS_DEN_B1F_TO_DRAGON_SHRINE_1_WP,
        "DragonShrine", dual_width=True, unlocks=[Unlock_Keys.BADGE_8]
    )

class Sprout_Tower_1F_Links(Enum):
    SPROUT_TOWER_1F_TO_VIOLET_CITY_LINK = WarpLink(
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_SPROUT_TOWER_1F_WP,
        "SproutTower1F", dual_width=True
    )
    SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FA_LINK = WarpLink(
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FA_WP,
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_3_WP,
        "SproutTower1F", 10
    )
    SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FB_LINK = WarpLink(
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FB_WP,
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_4_WP,
        "SproutTower1F", 15
    )
    SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FC_LINK = WarpLink(
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FC_WP,
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_5_WP,
        "SproutTower1F", 20
    )

class Sprout_Tower_2F_Links(Enum):
    SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_3_LINK = WarpLink(
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_3_WP,
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FA_WP,
        "SproutTower2F"
    )

    SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_4_LINK = WarpLink(
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_4_WP,
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FB_WP,
        "SproutTower2F",5
    )

    SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_5_LINK = WarpLink(
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_5_WP,
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FC_WP,
        "SproutTower2F",10
    )

    SPROUT_TOWER_2F_TO_SPROUT_TOWER_3F_1_LINK = WarpLink(
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_3F_1_WP,
        Sprout_Tower_3F_Warp_Points.SPROUT_TOWER_3F_TO_SPROUT_TOWER_2F_4_WP,
        "SproutTower2F",15
    )



class Sprout_Tower_3F_Links(Enum):
    SPROUT_TOWER_3F_TO_SPROUT_TOWER_2F_LINK = WarpLink(
        Sprout_Tower_3F_Warp_Points.SPROUT_TOWER_3F_TO_SPROUT_TOWER_2F_4_WP,
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_3F_1_WP,
        "SproutTower3F", unlocks=[Unlock_Keys.HM_FLASH]
    )

class Tin_Tower_1F_Links(Enum):
    TIN_TOWER_1F_TO_ECRUTEAK_CITY_LINK = WarpLink(
        Tin_Tower_1F_Warp_Points.TIN_TOWER_1F_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_TIN_TOWER_1F_WP,
        "TinTower1F", dual_width=True
    )


class Tin_Tower_2F_Links(Enum):
    TIN_TOWER_2F_TO_TIN_TOWER_3F_1_LINK = WarpLink(
        Tin_Tower_2F_Warp_Points.TIN_TOWER_2F_TO_TIN_TOWER_3F_1_WP,
        Tin_Tower_3F_Warp_Points.TIN_TOWER_3F_TO_TIN_TOWER_2F_1_WP,
        "TinTower2F"
    )

    TIN_TOWER_2F_TO_TIN_TOWER_1F_3_LINK = WarpLink(
        Tin_Tower_2F_Warp_Points.TIN_TOWER_2F_TO_TIN_TOWER_1F_3_WP,
        Tin_Tower_1F_Warp_Points.TIN_TOWER_1F_TO_TIN_TOWER_2F_WP,
        "TinTower2F",5
    )


class Tin_Tower_3F_Links(Enum):
    TIN_TOWER_3F_TO_TIN_TOWER_2F_1_LINK = WarpLink(
        Tin_Tower_3F_Warp_Points.TIN_TOWER_3F_TO_TIN_TOWER_2F_1_WP,
        Tin_Tower_2F_Warp_Points.TIN_TOWER_2F_TO_TIN_TOWER_3F_1_WP,
        "TinTower3F"
    )

    TIN_TOWER_3F_TO_TIN_TOWER_4F_2_LINK = WarpLink(
        Tin_Tower_3F_Warp_Points.TIN_TOWER_3F_TO_TIN_TOWER_4F_2_WP,
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_3F_2_WP,
        "TinTower3F",5
    )


class Tin_Tower_4F_Links(Enum):
    TIN_TOWER_4F_TO_TIN_TOWER_5F_2_LINK = WarpLink(
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_5F_2_WP,
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_4F_1_WP,
        "TinTower4F"
    )

    TIN_TOWER_4F_TO_TIN_TOWER_3F_2_LINK = WarpLink(
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_3F_2_WP,
        Tin_Tower_3F_Warp_Points.TIN_TOWER_3F_TO_TIN_TOWER_4F_2_WP,
        "TinTower4F",5
    )

    TIN_TOWER_4F_TO_TIN_TOWER_5F_3_LINK = WarpLink(
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_5F_3_WP,
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_4F_3_WP,
        "TinTower4F",10
    )

    TIN_TOWER_4F_TO_TIN_TOWER_5F_4_LINK = WarpLink(
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_5F_4_WP,
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_4F_4_WP,
        "TinTower4F",15
    )


class Tin_Tower_5F_Links(Enum):
    TIN_TOWER_5F_TO_TIN_TOWER_6F_2_LINK = WarpLink(  # middle bottom one way
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_6F_2_WP,
        Tin_Tower_6F_Warp_Points.TIN_TOWER_6F_TO_TIN_TOWER_5F_1_WP,
        "TinTower5F"
    )

    TIN_TOWER_5F_TO_TIN_TOWER_4F_1_LINK = WarpLink(  # top
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_4F_1_WP,
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_5F_2_WP,
        "TinTower5F",5
    )

    TIN_TOWER_5F_TO_TIN_TOWER_4F_3_LINK = WarpLink(  # deadend (item) (left)
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_4F_3_WP,
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_5F_3_WP,
        "TinTower5F",10
    )

    TIN_TOWER_5F_TO_TIN_TOWER_4F_4_LINK = WarpLink(  # deadend (item) (left)
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_4F_4_WP,
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_5F_4_WP,
        "TinTower5F",15
    )


class Tin_Tower_6F_Links(Enum):
    TIN_TOWER_6F_TO_TIN_TOWER_7F_1_LINK = WarpLink(
        Tin_Tower_6F_Warp_Points.TIN_TOWER_6F_TO_TIN_TOWER_7F_1_WP,
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_6F_1_WP,
        "TinTower6F"
    )

    TIN_TOWER_6F_TO_TIN_TOWER_5F_1_LINK = WarpLink(
        Tin_Tower_6F_Warp_Points.TIN_TOWER_6F_TO_TIN_TOWER_5F_1_WP,
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_6F_2_WP,
        "TinTower6F",5
    )


class Tin_Tower_7F_Links(Enum):  # 1-2-4 , 3-5

    TIN_TOWER_7F_TO_TIN_TOWER_6F_1_LINK = WarpLink(
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_6F_1_WP,
        Tin_Tower_6F_Warp_Points.TIN_TOWER_6F_TO_TIN_TOWER_7F_1_WP,
        "TinTower7F"
    )

    TIN_TOWER_7F_TO_TIN_TOWER_8F_1_LINK = WarpLink(
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_8F_1_WP,
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_7F_2_WP,
        "TinTower7F",5
    )

    TIN_TOWER_7F_TO_TIN_TOWER_7F_4_LINK = WarpLink(
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_7F_4_WP,
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_7F_3_WP,
        "TinTower7F",10
    )

    TIN_TOWER_7F_TO_TIN_TOWER_7F_3_LINK = WarpLink(
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_7F_3_WP,
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_7F_4_WP,
        "TinTower7F",15
    )

    TIN_TOWER_7F_TO_TIN_TOWER_9F_5_LINK = WarpLink(
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_9F_5_WP,
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_7F_5_WP,
        "TinTower7F",20
    )


class Tin_Tower_8F_Links(Enum):  # 1-2 (left), 3-4 (top) ,5x (bottom) ,6x (middle)

    TIN_TOWER_8F_TO_TIN_TOWER_7F_2_LINK = WarpLink(
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_7F_2_WP,
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_8F_1_WP,
        "TinTower8F"
    )

    TIN_TOWER_8F_TO_TIN_TOWER_9F_1_LINK = WarpLink(
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_1_WP,
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_2_WP,
        "TinTower8F",5
    )

    TIN_TOWER_8F_TO_TIN_TOWER_9F_2_LINK = WarpLink(
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_2_WP,
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_3_WP,
        "TinTower8F",10
    )

    TIN_TOWER_8F_TO_TIN_TOWER_9F_3_LINK = WarpLink(
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_3_WP,
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_4_WP,
        "TinTower8F",15
    )

    TIN_TOWER_8F_TO_TIN_TOWER_9F_6_LINK = WarpLink(
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_6_WP,
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_5_WP,
        "TinTower8F",20
    )

    TIN_TOWER_8F_TO_TIN_TOWER_9F_7_LINK = WarpLink(
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_7_WP,
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_6_WP,
        "TinTower8F",25
    )


class Tin_Tower_9F_Links(Enum):  # 5-6-7, 1-2(top) , 3-4(middle)

    TIN_TOWER_9F_TO_TIN_TOWER_8F_2_LINK = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_2_WP,
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_1_WP,
        "TinTower9F"
    )

    TIN_TOWER_9F_TO_TIN_TOWER_8F_3_LINK = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_3_WP,
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_2_WP,
        "TinTower9F",5
    )

    TIN_TOWER_9F_TO_TIN_TOWER_8F_4_LINK = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_4_WP,
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_3_WP,
        "TinTower9F",10
    )

    TIN_TOWER_9F_TO_TIN_TOWER_ROOF_1_LINK = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_ROOF_1_WP,
        Tin_Tower_Roof_Warp_Points.TIN_TOWER_ROOF_TO_TIN_TOWER_9F_WP,
        "TinTower9F",15
    )

    TIN_TOWER_9F_TO_TIN_TOWER_7F_5_LINK = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_7F_5_WP,
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_9F_5_WP,
        "TinTower9F",20
    )

    TIN_TOWER_9F_TO_TIN_TOWER_8F_5_LINK = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_5_WP,
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_6_WP,
        "TinTower9F",25
    )

    TIN_TOWER_9F_TO_TIN_TOWER_8F_6_LINK = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_6_WP,
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_7_WP,
        "TinTower9F",30
    )

class Union_Cave_1F_Links(Enum):
    UNION_CAVE_1F_TO_UNION_CAVE_B1FA_LINK = WarpLink(
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_UNION_CAVE_B1FA_WP,
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_UNION_CAVE_1F_1_WP,
        "UnionCave1F"
    )

    UNION_CAVE_1F_TO_UNION_CAVE_B1FB_LINK = WarpLink(
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_UNION_CAVE_B1FB_WP,
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_UNION_CAVE_1F_2_WP,
        "UnionCave1F", 5
    )


    UNION_CAVE_1F_TO_ROUTE_33_LINK = WarpLink(
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_ROUTE_33_WP,
        Route_33_Warp_Points.ROUTE_33_TO_UNION_CAVE_1F_WP,
        "UnionCave1F" , 10
    )

    UNION_CAVE_1F_TO_ROUTE_32_LINK = WarpLink(
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_ROUTE_32_WP,
        Route_32_Warp_Points.ROUTE_32_TO_UNION_CAVE_1F_WP,
        "UnionCave1F" , 15
    )

class Union_Cave_B1F_Links(Enum):
    UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_7_LINK = WarpLink(
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_7_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_1_WP,
        "UnionCaveB1F"
    )
    UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_8_LINK = WarpLink(
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_8_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_2_WP,
        "UnionCaveB1F", 5
    )

    UNION_CAVE_B1F_TO_UNION_CAVE_1F_1_LINK = WarpLink(
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_UNION_CAVE_1F_1_WP,
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_UNION_CAVE_B1FA_WP,
        "UnionCaveB1F", 10
    )

    UNION_CAVE_B1F_TO_UNION_CAVE_1F_2_LINK = WarpLink(
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_UNION_CAVE_1F_2_WP,
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_UNION_CAVE_B1FB_WP,
        "UnionCaveB1F", 15
    )

    UNION_CAVE_B1F_TO_UNION_CAVE_B2F_1_LINK = WarpLink(
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_UNION_CAVE_B2F_1_WP,
        Union_Cave_B2F_Warp_Points.UNION_CAVE_B2F_TO_UNION_CAVE_B1F_5_WP,
        "UnionCaveB1F", 20
    )


class Union_Cave_B2F_Links(Enum):
    UNION_CAVE_B2F_TO_UNION_CAVE_B1F_5_LINK = WarpLink(
        Union_Cave_B2F_Warp_Points.UNION_CAVE_B2F_TO_UNION_CAVE_B1F_5_WP,
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_UNION_CAVE_B2F_1_WP,
        "UnionCaveB2F"
    )

class Lake_Of_Rage_Links(Enum):
    LAKE_OF_RAGE_TO_LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_LINK = WarpLink(
        Lake_Of_Rage_Warp_Points.LAKE_OF_RAGE_TO_LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_WP,
        Lake_Of_Rage_Hidden_Power_House_Warp_Points.LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_TO_LAKE_OF_RAGE_WP,
        "LakeOfRage", unlocks=[Unlock_Keys.LAKE_OF_RAGE_FOUND]
    )

    LAKE_OF_RAGE_TO_LAKE_OF_RAGE_MAGIKARP_HOUSE_LINK = WarpLink(
        Lake_Of_Rage_Warp_Points.LAKE_OF_RAGE_TO_LAKE_OF_RAGE_MAGIKARP_HOUSE_WP,
        Lake_Of_Rage_Magikarp_House_Warp_Points.LAKE_OF_RAGE_MAGIKARP_HOUSE_TO_LAKE_OF_RAGE_WP,
        "LakeOfRage" , 5, unlocks=[Unlock_Keys.LAKE_OF_RAGE_FOUND]
    )


class Lake_Of_Rage_Hidden_Power_House_Links(Enum):
    LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_TO_LAKE_OF_RAGE_LINK = WarpLink(
        Lake_Of_Rage_Hidden_Power_House_Warp_Points.LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_TO_LAKE_OF_RAGE_WP,
        Lake_Of_Rage_Warp_Points.LAKE_OF_RAGE_TO_LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_WP,
        "LakeOfRageHiddenPowerHouse", dual_width=True
    )

class Lake_Of_Rage_Magikarp_House_Links(Enum):
    LAKE_OF_RAGE_MAGIKARP_HOUSE_TO_LAKE_OF_RAGE_LINK = WarpLink(
        Lake_Of_Rage_Magikarp_House_Warp_Points.LAKE_OF_RAGE_MAGIKARP_HOUSE_TO_LAKE_OF_RAGE_WP,
        Lake_Of_Rage_Warp_Points.LAKE_OF_RAGE_TO_LAKE_OF_RAGE_MAGIKARP_HOUSE_WP,
        "LakeOfRageMagikarpHouse", dual_width=True
    )


class Whirl_Island_NW_Links(Enum):
    WHIRL_ISLAND_N_W_TO_ROUTE_41_1_LINK = WarpLink(
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_ROUTE_41_1_WP,
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_NW_WP,
        "WhirlIslandNW"
    )

    WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_B1F_1_LINK = WarpLink(
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_B1F_1_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NW_2_WP,
        "WhirlIslandNW", 5
    )

    WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_SW_4_LINK = WarpLink(
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_SW_4_WP,
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_NW_3_WP,
        "WhirlIslandNW", 10
    )

    WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_CAVE_2_LINK = WarpLink(
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_CAVE_2_WP,
        Whirl_Island_Cave_Warp_Points.WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_NW_4_WP,
        "WhirlIslandNW", 15
    )


class Whirl_Island_NE_Links(Enum):
    WHIRL_ISLAND_N_E_TO_ROUTE_41_2_LINK = WarpLink(
        Whirl_Island_NE_Warp_Points.WHIRL_ISLAND_N_E_TO_ROUTE_41_2_WP,
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_NE_WP,
        "WhirlIslandNE"
    )

    WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_2_LINK = WarpLink(
        Whirl_Island_NE_Warp_Points.WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_2_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NW_2_WP,
        "WhirlIslandNE", 5
    )

    WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_3_LINK = WarpLink(
        Whirl_Island_NE_Warp_Points.WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_3_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_3_WP,
        "WhirlIslandNE", 10
    )

class Whirl_Island_SW_Links(Enum):
    WHIRL_ISLAND_S_W_TO_ROUTE_41_3_LINK = WarpLink(
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_ROUTE_41_3_WP,
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_SW_WP,
        "WhirlIslandSW"
    )

    WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_5_LINK = WarpLink(
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_5_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_2_WP,
        "WhirlIslandSW", 5
    )

    WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_4_LINK = WarpLink(
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_4_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_3_WP,
        "WhirlIslandSW", 10
    )

    WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_NW_3_LINK = WarpLink(
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_NW_3_WP,
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_SW_4_WP,
        "WhirlIslandSW", 15
    )

    WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B2F_4_LINK = WarpLink(
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B2F_4_WP,
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_SW_5_WP,
        "WhirlIslandSW", 20
    )

class Whirl_Island_SE_Links(Enum):
    WHIRL_ISLAND_S_E_TO_ROUTE_41_4_LINK = WarpLink(
        Whirl_Island_SE_Warp_Points.WHIRL_ISLAND_S_E_TO_ROUTE_41_4_WP,
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_SE_WP,
        "WhirlIslandSE"
    )

    WHIRL_ISLAND_S_E_TO_WHIRL_ISLAND_B1F_6_LINK = WarpLink(
        Whirl_Island_SE_Warp_Points.WHIRL_ISLAND_S_E_TO_WHIRL_ISLAND_B1F_6_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SE_2_WP,
        "WhirlIslandSE",5
    )

class Whirl_Island_Cave_Links(Enum):
    WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_B1F_9_LINK = WarpLink(
        Whirl_Island_Cave_Warp_Points.WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_B1F_9_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_CAVE_1_WP,
        "WhirlIslandCave"
    )

    WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_NW_4_LINK = WarpLink(
        Whirl_Island_Cave_Warp_Points.WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_NW_4_WP,
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_CAVE_2_WP,
        "WhirlIslandCave", 5
    )




class Whirl_Island_B1F_Links(Enum):
    WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NW_2_LINK = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NW_2_WP,
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_B1F_1_WP,
        "WhirlIslandB1F"
    )

    WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_2_LINK = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_2_WP,
        Whirl_Island_NE_Warp_Points.WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_2_WP,
        "WhirlIslandB1F", 5
    )

    WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_3_LINK = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_3_WP,
        Whirl_Island_NE_Warp_Points.WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_3_WP,
        "WhirlIslandB1F", 10
    )

    WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_3_LINK = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_3_WP,
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_4_WP,
        "WhirlIslandB1F", 15
    )

    WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_2_LINK = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_2_WP,
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_5_WP,
        "WhirlIslandB1F", 20
    )

    WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SE_2_LINK = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SE_2_WP,
        Whirl_Island_SE_Warp_Points.WHIRL_ISLAND_S_E_TO_WHIRL_ISLAND_B1F_6_WP,
        "WhirlIslandB1F", 25
    )

    WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_1_LINK = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_1_WP,
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_7_WP,
        "WhirlIslandB1F", 30
    )

    WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_2_LINK = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_2_WP,
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_8_WP,
        "WhirlIslandB1F", 35
    )

    WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_CAVE_1_LINK = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_CAVE_1_WP,
        Whirl_Island_Cave_Warp_Points.WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_B1F_9_WP,
        "WhirlIslandB1F", 40
    )


class Whirl_Island_B2F_Links(Enum):
    WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_7_LINK = WarpLink(
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_7_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_1_WP,
        "WhirlIslandB2F"
    )

    WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_8_LINK = WarpLink(
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_8_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_2_WP,
        "WhirlIslandB2F", 5
    )

    WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_LUGIA_CHAMBER_1_LINK = WarpLink(
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_LUGIA_CHAMBER_1_WP,
        Whirl_Island_Lugia_Chamber_Warp_Points.WHIRL_ISLAND_LUGIA_CHAMBER_TO_WHIRL_ISLAND_B2F_WP,
        "WhirlIslandB2F", 10
    )

    WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_SW_5_LINK = WarpLink(
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_SW_5_WP,
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B2F_4_WP,
        "WhirlIslandB2F", 15
    )



class Whirl_Island_Lugia_Chamber_Links(Enum):
    WHIRL_ISLAND_LUGIA_CHAMBER_TO_WHIRL_ISLAND_B2F_LINK = WarpLink(
        Whirl_Island_Lugia_Chamber_Warp_Points.WHIRL_ISLAND_LUGIA_CHAMBER_TO_WHIRL_ISLAND_B2F_WP,
        New_Bark_Warp_Points.NEW_BARK_TO_PLAYERS_NEIGHBORS_HOUSE_WP,
        "WhirlIslandLugiaChamber"
    )

class Tin_Tower_Roof_Links(Enum):
    TIN_TOWER_ROOF_TO_TIN_TOWER_9F_LINK = WarpLink(
        Tin_Tower_Roof_Warp_Points.TIN_TOWER_ROOF_TO_TIN_TOWER_9F_WP,
        New_Bark_Warp_Points.NEW_BARK_TO_ELMS_HOUSE_WP,
        "TinTowerRoof"
    )
#######################################################################
#                    Ecruteak Group                                   #
#######################################################################
class Dance_Theatre_Links(Enum):

    DANCE_THEATRE_TO_ECRUTEAK_CITY_LINK = WarpLink(
        Dance_Theatre_Warp_Points.DANCE_THEATRE_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_DANCE_THEATRE_WP,
        "DanceTheatre", dual_width=True, unlocks=[Unlock_Keys.HM_SURF]
    )

class Ecruteak_City_Links(Enum):

    ECRUTEAK_CITY_TO_ROUTE_42_ECRUTEAK_GATE_LINK = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ROUTE_42_ECRUTEAK_GATE_WP,
        Route_42_Ecruteak_Gate_Warp_Points.ROUTE_42_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity", dual_width=True
    )

    ECRUTEAK_CITY_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_LINK = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_WP,
        Ecruteak_Tin_Tower_Entrance_Warp_Points.ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 10
    )

    ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_LINK = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_WP,
        Wise_Trios_Room_Warp_Points.WISE_TRIOS_ROOM_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 15, dual_width=True
    )

    ECRUTEAK_CITY_TO_ECRUTEAK_POKECENTER_1F_LINK = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_POKECENTER_1F,
        Ecruteak_Pokecenter_Warp_Points.ECRUTEAK_POKECENTER_1F_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 25
    )


    ECRUTEAK_CITY_TO_ECRUTEAK_LUGIA_SPEECH_HOUSE_LINK = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_LUGIA_SPEECH_HOUSE_WP,
        Ecruteak_Lugia_Speech_House_Warp_Points.ECRUTEAK_LUGIA_SPEECH_HOUSE_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 30
    )

    ECRUTEAK_CITY_TO_DANCE_THEATRE_LINK = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_DANCE_THEATRE_WP,
        Dance_Theatre_Warp_Points.DANCE_THEATRE_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 35
    )

    ECRUTEAK_CITY_TO_ECRUTEAK_MART_LINK = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_MART_WP,
        Ecruteak_Mart_Warp_Points.ECRUTEAK_MART_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 40
    )

    ECRUTEAK_CITY_TO_ECRUTEAK_GYM_LINK = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_GYM_WP,
        Ecruteak_Gym_Warp_Points.ECRUTEAK_GYM_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 45
    )

    ECRUTEAK_CITY_TO_ECRUTEAK_ITEMFINDER_HOUSE_LINK = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_ITEMFINDER_HOUSE_WP,
        Ecruteak_Itemfinder_House_Warp_Points.ECRUTEAK_ITEMFINDER_HOUSE_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 50
    )

    ECRUTEAK_CITY_TO_TIN_TOWER_1F_LINK = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_TIN_TOWER_1F_WP,
        Tin_Tower_1F_Warp_Points.TIN_TOWER_1F_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 55
    )

    ECRUTEAK_CITY_TO_BURNED_TOWER_1F_LINK = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_BURNED_TOWER_1F_WP,
        Burned_Tower_1F_Warp_Points.BURNED_TOWER_1F_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 60
    )

    ECRUTEAK_CITY_TO_ROUTE_38_ECRUTEAK_GATE_LINK = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ROUTE_38_ECRUTEAK_GATE_WP,
        Route_38_Ecruteak_Gate_Warp_Points.ROUTE_38_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 65, dual_width=True
    )

class Ecruteak_Gym_Links(Enum):

    ECRUTEAK_GYM_TO_ECRUTEAK_CITY_LINK = WarpLink(
        Ecruteak_Gym_Warp_Points.ECRUTEAK_GYM_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_GYM_WP,
        "EcruteakGym", dual_width=True, locked_by=[Unlock_Keys.ENTERED_BURNED_TOWER],
        unlocks=[Unlock_Keys.BADGE_4]
    )

class Ecruteak_Item_Finder_House_Links(Enum):

    ECRUTEAK_ITEMFINDER_HOUSE_TO_ECRUTEAK_CITY_LINK = WarpLink(
        Ecruteak_Itemfinder_House_Warp_Points.ECRUTEAK_ITEMFINDER_HOUSE_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_ITEMFINDER_HOUSE_WP,
        "EcruteakItemfinderHouse", dual_width=True
    )

class Ecruteak_Lugia_Speech_House_Links(Enum):

    ECRUTEAK_LUGIA_SPEECH_HOUSE_TO_ECRUTEAK_CITY_LINK = WarpLink(
        Ecruteak_Lugia_Speech_House_Warp_Points.ECRUTEAK_LUGIA_SPEECH_HOUSE_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_LUGIA_SPEECH_HOUSE_WP,
        "EcruteakLugiaSpeechHouse", dual_width=True
    )

class Ecruteak_Mart_Links(Enum):

    ECRUTEAK_MART_TO_ECRUTEAK_CITY_LINK = WarpLink(
        Ecruteak_Mart_Warp_Points.ECRUTEAK_MART_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_MART_WP,
        "EcruteakMart", dual_width=True
    )

class Ecruteak_Pokecenter_Links(Enum):

    ECRUTEAK_POKECENTER_1F_TO_ECRUTEAK_CITY_LINK = WarpLink(
        Ecruteak_Pokecenter_Warp_Points.ECRUTEAK_POKECENTER_1F_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_POKECENTER_1F,
        "EcruteakPokecenter1F", dual_width=True
    )

    ECRUTEAK_POKECENTER_1F_TO_ECRUTEAK_POKECENTER_2F_LINK = WarpLink(
        Ecruteak_Pokecenter_Warp_Points.ECRUTEAK_POKECENTER_TO_ECRUTEAK_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "EcruteakPokecenter1F", 10
    )

class Ecruteak_Tin_Tower_Entrance_Links(Enum):


    ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_CITY_LINK = WarpLink(
        Ecruteak_Tin_Tower_Entrance_Warp_Points.ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_WP,
        "EcruteakTinTowerEntrance", dual_width=True
    )
    # ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_TIN_TOWER_ENTRANCEA_LINK
    # ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_TIN_TOWER_ENTRANCEB_LINK

    ECRUTEAK_TIN_TOWER_ENTRANCE_TO_WISE_TRIOS_ROOM_LINK = WarpLink(
        Ecruteak_Tin_Tower_Entrance_Warp_Points.ECRUTEAK_TIN_TOWER_ENTRANCE_TO_WISE_TRIOS_ROOM_WP,
        Wise_Trios_Room_Warp_Points.WISE_TRIOS_ROOM_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_WP,
        "EcruteakTinTowerEntrance" , 20
    )

class Wise_Trios_Room_Links(Enum):

    WISE_TRIOS_ROOM_TO_ECRUTEAK_CITY_LINK = WarpLink(
        Wise_Trios_Room_Warp_Points.WISE_TRIOS_ROOM_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_WP,
        "WiseTriosRoom", dual_width=True
    )

    WISE_TRIOS_ROOM_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_LINK = WarpLink(
        Wise_Trios_Room_Warp_Points.WISE_TRIOS_ROOM_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_WP,
        Ecruteak_Tin_Tower_Entrance_Warp_Points.ECRUTEAK_TIN_TOWER_ENTRANCE_TO_WISE_TRIOS_ROOM_WP,
        "WiseTriosRoom" , 10
    )


#######################################################################
#                    Gates Group                                      #
#######################################################################

class Ilex_Forest_Azalea_Gate_Links(Enum):

    ILEX_FOREST_AZALEA_GATE_TO_ILEX_FOREST_LINK = WarpLink(
        Ilex_Forest_Azalea_Gate_Warp_Points.ILEX_FOREST_AZALEA_GATE_TO_ILEX_FOREST_WP,
        Ilex_Forest_Warp_Points.ILEX_FOREST_TO_ILEX_FOREST_AZALEA_GATE_WP,
        "IlexForestAzaleaGate",
        dual_width=True
    )

    ILEX_FOREST_AZALEA_GATE_TO_AZALEA_TOWN = WarpLink(
        Ilex_Forest_Azalea_Gate_Warp_Points.ILEX_FOREST_AZALEA_GATE_TO_AZALEA_TOWN_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_ILEX_FOREST_AZALEA_GATE_WP,
        "IlexForestAzaleaGate" , 10,
        dual_width=True
    )

class Route_29_Route_46_Gate_Links(Enum):

    ROUTE_29_ROUTE_46_GATE_TO_ROUTE_46_LINK = WarpLink(
        Route_29_Route_46_Gate_Warp_Points.ROUTE_29_ROUTE_46_GATE_TO_ROUTE_46_WP,
        Route_46_Warp_Points.ROUTE_46_TO_ROUTE_29_ROUTE_46_GATE_WP,
        "Route29Route46Gate",
        dual_width=True
    )

    ROUTE_29_ROUTE_46_GATE_TO_ROUTE_29_LINK = WarpLink(
        Route_29_Route_46_Gate_Warp_Points.ROUTE_29_ROUTE_46_GATE_TO_ROUTE_29_WP,
        Route_29_Warp_Points.ROUTE_29_TO_ROUTE_46_GATE_WP,
        "Route29Route46Gate" , 10,
        dual_width=True
    )

class Route_31_Violet_Gate_Links(Enum):

    ROUTE_31_VIOLET_GATE_TO_VIOLET_CITY_LINK = WarpLink(
        Route_31_Violet_Gate_Warp_Points.ROUTE_31_VIOLET_GATE_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_ROUTE_31_VIOLET_GATE_WP,
        "Route31VioletGate",
        dual_width=True
    )

    ROUTE_31_VIOLET_GATE_TO_ROUTE_31_LINK = WarpLink(
        Route_31_Violet_Gate_Warp_Points.ROUTE_31_VIOLET_GATE_TO_ROUTE_31_WP,
        Route_31_Warp_Points.ROUTE_31_TO_ROUTE_31_VIOLET_GATE_WP,
        "Route31VioletGate" , 10,
        dual_width=True
    )

class Route_32_Ruins_Of_Alph_Gate_Links(Enum):

    ROUTE_32_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_LINK = WarpLink(
        Route_32_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_32_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_32_RUINS_OF_ALPH_GATE_1_WP,
        "Route32RuinsOfAlphGate",
        dual_width=True
    )

    ROUTE_32_RUINS_OF_ALPH_GATE_TO_ROUTE_32_LINK = WarpLink(
        Route_32_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_32_RUINS_OF_ALPH_GATE_TO_ROUTE_32_WP,
        Route_32_Warp_Points.ROUTE_32_TO_ROUTE_32_RUINS_OF_ALPH_GATE_WP,
        "Route32RuinsOfAlphGate", 10,
        dual_width=True
    )

class Route_34_Ilex_Forest_Gate_Links(Enum):
    ROUTE_34_ILEX_FOREST_GATE_TO_ROUTE_34_LINK = WarpLink(
        Route_34_Ilex_Forest_Gate_Warp_Points.ROUTE_34_ILEX_FOREST_GATE_TO_ROUTE_34_WP,
        Route_34_Warp_Points.ROUTE_34_TO_ROUTE_34_ILEX_FOREST_GATE_WP,
        "Route34IlexForestGate", dual_width=True
    )
    ROUTE_34_ILEX_FOREST_GATE_TO_ILEX_FOREST_LINK = WarpLink(
        Route_34_Ilex_Forest_Gate_Warp_Points.ROUTE_34_ILEX_FOREST_GATE_TO_ILEX_FOREST_WP,
        Ilex_Forest_Warp_Points.ILEX_FOREST_TO_ROUTE_34_ILEX_FOREST_GATE_WP,
        "Route34IlexForestGate" , 10, dual_width=True
    )

class Route_35_Goldenrod_Gate_Links(Enum):
    ROUTE_35_GOLDENROD_GATE_TO_ROUTE_35__LINK = WarpLink(
        Route_35_Goldenrod_Gate_Warp_Points.ROUTE_35_GOLDENROD_GATE_TO_ROUTE_35_WP,
        Route_35_Warp_Points.ROUTE_35_TO_ROUTE_35_GOLDENROD_GATE_WP,
        "Route35GoldenrodGate", dual_width=True
    )

    ROUTE_35_GOLDENROD_GATE_TO_GOLDENROD_CITY_LINK = WarpLink(
        Route_35_Goldenrod_Gate_Warp_Points.ROUTE_35_GOLDENROD_GATE_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_ROUTE_35_GOLDENROD_GATE_WP,
        "Route35GoldenrodGate" , 10, dual_width=True
    )

class Route_35_National_Park_Gate_Links(Enum):
    ROUTE_35_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_LINK = WarpLink(
        Route_35_National_Park_Gate_Warp_Points.ROUTE_35_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_WP,
        National_Park_Warp_Points.NATIONAL_PARK_TO_ROUTE_35_NATIONAL_PARK_GATE_WP,
        "Route35NationalParkGate", dual_width=True
    )
    ROUTE_35_NATIONAL_PARK_GATE_TO_ROUTE_35_LINK = WarpLink(
        Route_35_National_Park_Gate_Warp_Points.ROUTE_35_NATIONAL_PARK_GATE_TO_ROUTE_35_WP,
        Route_35_Warp_Points.ROUTE_35_TO_NATIONAL_PARK_GATE_WP,
        "Route35NationalParkGate" , 10, dual_width=True
    )

class Route_36_National_Park_Gate_Links(Enum):
    ROUTE_36_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_LINK = WarpLink(
        Route_36_National_Park_Gate_Warp_Points.ROUTE_36_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_WP,
        National_Park_Warp_Points.NATIONAL_PARK_TO_ROUTE_36_NATIONAL_PARK_GATE_WP,
        "Route36NationalParkGate", dual_width=True
    )
    ROUTE_36_NATIONAL_PARK_GATE_TO_ROUTE_36_LINK = WarpLink(
        Route_36_National_Park_Gate_Warp_Points.ROUTE_36_NATIONAL_PARK_GATE_TO_ROUTE_36_WP,
        Route_36_Warp_Points.ROUTE_36_TO_ROUTE_36_NATIONAL_PARK_GATE_WP,
        "Route36NationalParkGate" , 10, dual_width=True
    )

class Route_36_Ruins_Of_Alph_Gate_Links(Enum):

    ROUTE_36_RUINS_OF_ALPH_GATE_TO_ROUTE_36_LINK = WarpLink(
        Route_36_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_36_RUINS_OF_ALPH_GATE_TO_ROUTE_36_WP,
        Route_36_Warp_Points.ROUTE_36_TO_ROUTE_36_RUINS_OF_ALPH_GATE_WP,
        "Route36RuinsOfAlphGate",
        dual_width=True
    )

    ROUTE_36_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_LINK = WarpLink(
        Route_36_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_36_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_32_RUINS_OF_ALPH_GATE_1_WP,
        "Route36RuinsOfAlphGate" , 10,
        dual_width=True
    )



class Route_38_Ecruteak_Gate_Links(Enum):
    ROUTE_38_ECRUTEAK_GATE_TO_ROUTE_38_LINK = WarpLink(
        Route_38_Ecruteak_Gate_Warp_Points.ROUTE_38_ECRUTEAK_GATE_TO_ROUTE_38_WP,
        Route_38_Warp_Points.ROUTE_38_TO_ROUTE_38_ECRUTEAK_GATE_WP,
        "Route38EcruteakGate", dual_width=True
    )
    ROUTE_38_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_LINK = WarpLink(
        Route_38_Ecruteak_Gate_Warp_Points.ROUTE_38_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ROUTE_38_ECRUTEAK_GATE_WP,
        "Route38EcruteakGate" , 10, dual_width=True
    )

class Route_42_Ecruteak_Gate_Links(Enum):

    ROUTE_42_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_LINK = WarpLink(
        Route_42_Ecruteak_Gate_Warp_Points.ROUTE_42_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ROUTE_42_ECRUTEAK_GATE_WP,
        "Route42EcruteakGate", dual_width=True
    )

    ROUTE_42_ECRUTEAK_GATE_TO_ROUTE_42_LINK = WarpLink(
        Route_42_Ecruteak_Gate_Warp_Points.ROUTE_42_ECRUTEAK_GATE_TO_ROUTE_42_WP,
        Route_42_Warp_Points.ROUTE_42_TO_ROUTE_42_ECRUTEAK_GATE_WP,
        "Route42EcruteakGate", 10, dual_width=True
    )


class Route_43_Gate_Links(Enum):
    ROUTE_43_GATE_TO_ROUTE_43_TOP_LINK = WarpLink(
        Route_43_Gate_Warp_Points.ROUTE_43_GATE_TO_ROUTE_43_TOP_WP,
        Route_43_Warp_Points.ROUTE_43_TO_ROUTE_43_GATE_TOP_WP,
        "Route43Gate", dual_width=True
    )
    ROUTE_43_GATE_TO_ROUTE_43_BOTTOM_LINK = WarpLink(
        Route_43_Gate_Warp_Points.ROUTE_43_GATE_TO_ROUTE_43_BOTTOM_WP,
        Route_43_Warp_Points.ROUTE_43_TO_ROUTE_43_GATE_BOTTOM_WP,
        "Route43Gate" , 10, dual_width=True
    )

class Route_43_Mahogany_Gate_Links(Enum):
    ROUTE_43_MAHOGANY_GATE_TO_ROUTE_43_LINK = WarpLink(
        Route_43_Mahogany_Gate_Warp_Points.ROUTE_43_MAHOGANY_GATE_TO_ROUTE_43_WP,
        Route_43_Warp_Points.ROUTE_43_TO_ROUTE_43_MAHOGANY_GATE_WP,
        "Route43MahoganyGate", dual_width=True
    )
    ROUTE_43_MAHOGANY_GATE_TO_MAHOGANY_TOWN_LINK = WarpLink(
        Route_43_Mahogany_Gate_Warp_Points.ROUTE_43_MAHOGANY_GATE_TO_MAHOGANY_TOWN_WP,
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_ROUTE_43_MAHOGANY_GATE_WP,
        "Route43MahoganyGate" , 10, dual_width=True
    )

#######################################################################
#                    Goldenrod Group                                  #
#######################################################################
class Goldenrod_City_Links(Enum):
    GOLDENROD_CITY_TO_GOLDENROD_GYM_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_GYM_WP,
        Goldenrod_Gym_Warp_Points.GOLDENROD_GYM_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity"
    )

    GOLDENROD_CITY_TO_GOLDENROD_BIKE_SHOP_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_BIKE_SHOP_WP,
        Goldenrod_Bike_Shop_Warp_Points.GOLDENROD_BIKE_SHOP_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 5
    )

    GOLDENROD_CITY_TO_GOLDENROD_HAPPINESS_RATER_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_HAPPINESS_RATER_WP,
        Goldenrod_Happiness_Rater_Warp_Points.GOLDENROD_HAPPINESS_RATER_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 10
    )

    GOLDENROD_CITY_TO_BILLS_FAMILYS_HOUSE_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_BILLS_FAMILYS_HOUSE_WP,
        Bills_Familys_House_Warp_Points.BILLS_FAMILYS_HOUSE_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 15
    )

    GOLDENROD_CITY_TO_GOLDENROD_MAGNET_TRAIN_STATION_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_MAGNET_TRAIN_STATION_WP,
        Goldenrod_Magnet_Train_Station_Warp_Points.GOLDENROD_MAGNET_TRAIN_STATION_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 20
    )

    GOLDENROD_CITY_TO_GOLDENROD_FLOWER_SHOP_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_FLOWER_SHOP_WP,
        Goldenrod_Flower_Shop_Warp_Points.GOLDENROD_FLOWER_SHOP_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 25
    )

    GOLDENROD_CITY_TO_GOLDENROD_PP_SPEECH_HOUSE_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_PP_SPEECH_HOUSE_WP,
        Goldenrod_PP_Speech_House_Warp_Points.GOLDENROD_PP_SPEECH_HOUSE_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 30
    )

    GOLDENROD_CITY_TO_GOLDENROD_NAME_RATER_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_NAME_RATER_WP,
        Goldenrod_Name_Rater_Warp_Points.GOLDENROD_NAME_RATER_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 35
    )

    GOLDENROD_CITY_TO_GOLDENROD_DEPT_STORE_1F_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_DEPT_STORE_1F_WP,
        Goldenrod_Dept_Store_1F_Warp_Points.GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_CITY_9_WP,
        "GoldenrodCity" , 40
    )

    GOLDENROD_CITY_TO_GOLDENROD_GAME_CORNER_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_GAME_CORNER_WP,
        Goldenrod_Game_Corner_Warp_Points.GOLDENROD_GAME_CORNER_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 45
    )

    GOLDENROD_CITY_TO_RADIO_TOWER_1F_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_RADIO_TOWER_1F_WP,
        Radio_Tower_1F_Warp_Points.RADIO_TOWER_1F_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 50
    )

    GOLDENROD_CITY_TO_ROUTE_35_GOLDENROD_GATE_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_ROUTE_35_GOLDENROD_GATE_WP,
        Route_35_Goldenrod_Gate_Warp_Points.ROUTE_35_GOLDENROD_GATE_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 55
    )

    GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_NORTH_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_NORTH_WP,
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_NORTH_WP,
        "GoldenrodCity" , 60
    )

    GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_SOUTH_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_SOUTH_WP,
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_SOUTH_WP,
        "GoldenrodCity" , 65
    )

    GOLDENROD_CITY_TO_GOLDENROD_POKECENTER_1F_LINK = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_POKECENTER_1F_WP,
        Goldenrod_Pokecenter_Warp_Points.GOLDENROD_POKECENTER_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 70
    )

class Bills_Familys_House_Links(Enum):
    BILLS_FAMILYS_HOUSE_TO_GOLDENROD_CITY_LINK = WarpLink(
        Bills_Familys_House_Warp_Points.BILLS_FAMILYS_HOUSE_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_BILLS_FAMILYS_HOUSE_WP,
        "BillsFamilysHouse", dual_width=True
    )

class Day_Care_Links(Enum):
    DAY_CARE_TO_ROUTE_34_FRONT_LINK = WarpLink(
        Day_Care_Warp_Points.DAY_CARE_TO_ROUTE_34_FRONT_WP,
        Route_34_Warp_Points.ROUTE_34_TO_DAY_CARE_FRONT_WP,
        "DayCare", dual_width=True
    )
    # DAY_CARE_TO_ROUTE_34_SIDE

class Goldenrod_Bike_Shop_Links(Enum):
    GOLDENROD_BIKE_SHOP_TO_GOLDENROD_CITY_LINK = WarpLink(
        Goldenrod_Bike_Shop_Warp_Points.GOLDENROD_BIKE_SHOP_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_BIKE_SHOP_WP,
        "GoldenrodBikeShop", dual_width=True
    )

class Goldenrod_Dept_Store_B1F_Links(Enum):
    GOLDENROD_DEPT_STORE_B1F_TO_UNDERGROUND_WAREHOUSE_LINK = WarpLink(
        Goldenrod_Dept_Store_B1F_Warp_Points.GOLDENROD_DEPT_STORE_B1F_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_3_WP,
        Goldenrod_Underground_Warehouse_Warp_Points.GOLDENROD_UNDERGROUND_WAREHOUSE_TO_GOLDENROD_DEPT_STORE_B1F_WP,
        "GoldenrodDeptStoreB1F", locked_by=[Unlock_Keys.KEY_CARD]
    )

class Goldenrod_Dept_Store_1F_Links(Enum):
    GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_CITY_LINK = WarpLink(
        Goldenrod_Dept_Store_1F_Warp_Points.GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_CITY_9_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_DEPT_STORE_1F_WP,
        "GoldenrodDeptStore1F", dual_width=True
    )

    GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_DEPT_STORE_2F_2_LINK = WarpLink(
        Goldenrod_Dept_Store_1F_Warp_Points.GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_DEPT_STORE_2F_2_WP,
        Goldenrod_Dept_Store_2F_Warp_Points.GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_1F_3_WP,
        "GoldenrodDeptStore1F", 10
    )

class Goldenrod_Dept_Store_2F_Links(Enum):
    GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_3F_1_LINK = WarpLink(
        Goldenrod_Dept_Store_2F_Warp_Points.GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_3F_1_WP,
        Goldenrod_Dept_Store_3F_Warp_Points.GOLDENROD_DEPT_STORE_3F_TO_GOLDENROD_DEPT_STORE_2F_1_WP,
        "GoldenrodDeptStore2F"
    )

    GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_1F_3_LINK = WarpLink(
        Goldenrod_Dept_Store_2F_Warp_Points.GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_1F_3_WP,
        Goldenrod_Dept_Store_1F_Warp_Points.GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_DEPT_STORE_2F_2_WP,
        "GoldenrodDeptStore2F", 5
    )


class Goldenrod_Dept_Store_3F_Links(Enum):
    GOLDENROD_DEPT_STORE_3F_TO_GOLDENROD_DEPT_STORE_2F_1_LINK = WarpLink(
        Goldenrod_Dept_Store_3F_Warp_Points.GOLDENROD_DEPT_STORE_3F_TO_GOLDENROD_DEPT_STORE_2F_1_WP,
        Goldenrod_Dept_Store_2F_Warp_Points.GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_3F_1_WP,
        "GoldenrodDeptStore3F"
    )

    GOLDENROD_DEPT_STORE_3F_TO_GOLDENROD_DEPT_STORE_4F_2_LINK = WarpLink(
        Goldenrod_Dept_Store_3F_Warp_Points.GOLDENROD_DEPT_STORE_3F_TO_GOLDENROD_DEPT_STORE_4F_2_WP,
        Goldenrod_Dept_Store_4F_Warp_Points.GOLDENROD_DEPT_STORE_4F_TO_GOLDENROD_DEPT_STORE_3F_2_WP,
        "GoldenrodDeptStore3F", 5
    )

class Goldenrod_Dept_Store_4F_Links(Enum):
    GOLDENROD_DEPT_STORE_4F_TO_GOLDENROD_DEPT_STORE_5F_1_LINK = WarpLink(
        Goldenrod_Dept_Store_4F_Warp_Points.GOLDENROD_DEPT_STORE_4F_TO_GOLDENROD_DEPT_STORE_5F_1_WP,
        Goldenrod_Dept_Store_5F_Warp_Points.GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_4F_1_WP,
        "GoldenrodDeptStore4F"
    )

    GOLDENROD_DEPT_STORE_4F_TO_GOLDENROD_DEPT_STORE_3F_2_LINK = WarpLink(
        Goldenrod_Dept_Store_4F_Warp_Points.GOLDENROD_DEPT_STORE_4F_TO_GOLDENROD_DEPT_STORE_3F_2_WP,
        Goldenrod_Dept_Store_3F_Warp_Points.GOLDENROD_DEPT_STORE_3F_TO_GOLDENROD_DEPT_STORE_4F_2_WP,
        "GoldenrodDeptStore4F",5
    )

class Goldenrod_Dept_Store_5F_Links(Enum):
    GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_4F_1_LINK = WarpLink(
        Goldenrod_Dept_Store_5F_Warp_Points.GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_4F_1_WP,
        Goldenrod_Dept_Store_4F_Warp_Points.GOLDENROD_DEPT_STORE_4F_TO_GOLDENROD_DEPT_STORE_5F_1_WP,
        "GoldenrodDeptStore5F"
    )
    GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_6F_1_LINK = WarpLink(
        Goldenrod_Dept_Store_5F_Warp_Points.GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_6F_1_WP,
        Goldenrod_Dept_Store_6F_Warp_Points.GOLDENROD_DEPT_STORE_6F_TO_GOLDENROD_DEPT_STORE_5F_2_WP,
        "GoldenrodDeptStore5F", 5
    )

class Goldenrod_Dept_Store_6F_Links(Enum):
    GOLDENROD_DEPT_STORE_6F_TO_GOLDENROD_DEPT_STORE_5F_2_LINK = WarpLink(
        Goldenrod_Dept_Store_6F_Warp_Points.GOLDENROD_DEPT_STORE_6F_TO_GOLDENROD_DEPT_STORE_5F_2_WP,
        Goldenrod_Dept_Store_5F_Warp_Points.GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_6F_1_WP,
        "GoldenrodDeptStore6F"
    )
    GOLDENROD_DEPT_STORE_6F_TO_GOLDENROD_DEPT_STORE_ROOF_1_LINK = WarpLink(
        Goldenrod_Dept_Store_6F_Warp_Points.GOLDENROD_DEPT_STORE_6F_TO_GOLDENROD_DEPT_STORE_ROOF_1_WP,
        Goldenrod_Dept_Store_Roof_Warp_Points.GOLDENROD_DEPT_STORE_ROOF_TO_GOLDENROD_DEPT_STORE_6F_3_WP,
        "GoldenrodDeptStore6F", 10
    )

class Goldenrod_Dept_Store_Roof_Links(Enum):
    GOLDENROD_DEPT_STORE_ROOF_TO_GOLDENROD_DEPT_STORE_6F_3_LINK = WarpLink(
        Goldenrod_Dept_Store_Roof_Warp_Points.GOLDENROD_DEPT_STORE_ROOF_TO_GOLDENROD_DEPT_STORE_6F_3_WP,
        Goldenrod_Dept_Store_6F_Warp_Points.GOLDENROD_DEPT_STORE_6F_TO_GOLDENROD_DEPT_STORE_ROOF_1_WP,
        "GoldenrodDeptStoreRoof"
    )


class Goldenrod_Flower_Shop_Links(Enum):
    GOLDENROD_FLOWER_SHOP_TO_GOLDENROD_CITY_LINK = WarpLink(
        Goldenrod_Flower_Shop_Warp_Points.GOLDENROD_FLOWER_SHOP_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_FLOWER_SHOP_WP,
        "GoldenrodFlowerShop", dual_width=True
    )

class Goldenrod_Game_Corner_Links(Enum):
    GOLDENROD_GAME_CORNER_TO_GOLDENROD_CITY_LINK = WarpLink(
        Goldenrod_Game_Corner_Warp_Points.GOLDENROD_GAME_CORNER_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_GAME_CORNER_WP,
        "GoldenrodGameCorner", dual_width=True
    )

class Goldenrod_Gym_Links(Enum):
    GOLDENROD_GYM_TO_GOLDENROD_CITY_LINK = WarpLink(
        Goldenrod_Gym_Warp_Points.GOLDENROD_GYM_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_GYM_WP,
        "GoldenrodGym", dual_width=True, unlocks=[Unlock_Keys.BADGE_3]
    )

class Goldenrod_Happiness_Rater_Links(Enum):
    GOLDENROD_HAPPINESS_RATER_TO_GOLDENROD_CITY_LINK = WarpLink(
        Goldenrod_Happiness_Rater_Warp_Points.GOLDENROD_HAPPINESS_RATER_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_HAPPINESS_RATER_WP,
        "GoldenrodHappinessRater", dual_width=True
    )

class Goldenrod_Magnet_Train_Station_Links(Enum):
    GOLDENROD_MAGNET_TRAIN_STATION_TO_GOLDENROD_CITY_LINK = WarpLink(
        Goldenrod_Magnet_Train_Station_Warp_Points.GOLDENROD_MAGNET_TRAIN_STATION_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_MAGNET_TRAIN_STATION_WP,
        "GoldenrodMagnetTrainStation", dual_width=True
    )

class Goldenrod_Name_Rater_Links(Enum):
    GOLDENROD_NAME_RATER_TO_GOLDENROD_CITY_LINK = WarpLink(
        Goldenrod_Name_Rater_Warp_Points.GOLDENROD_NAME_RATER_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_NAME_RATER_WP,
        "GoldenrodNameRater", dual_width=True
    )

class Goldenrod_Pokecenter_Links(Enum):
    GOLDENROD_POKECENTER_TO_GOLDENROD_CITY_LINK = WarpLink(
        Goldenrod_Pokecenter_Warp_Points.GOLDENROD_POKECENTER_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_POKECENTER_1F_WP,
        "GoldenrodPokecenter1F", dual_width=True
    )

    GOLDENROD_POKECENTER_1F_TO_GOLDENROD_POKECENTER_2F_LINK = WarpLink(
        Goldenrod_Pokecenter_Warp_Points.GOLDENROD_POKECENTER_TO_GOLDENROD_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "GoldenrodPokecenter1F", 15
    )

class Goldenrod_PP_Speech_House_Links(Enum):
    GOLDENROD_PP_SPEECH_HOUSE_TO_GOLDENROD_CITY_LINK = WarpLink(
        Goldenrod_PP_Speech_House_Warp_Points.GOLDENROD_PP_SPEECH_HOUSE_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_PP_SPEECH_HOUSE_WP,
        "GoldenrodPPSpeechHouse", dual_width=True
    )

class Goldenrod_Underground_Warehouse_Links(Enum):
    GOLDENROD_UNDERGROUND_WAREHOUSE_TO_GOLDENROD_DEPT_STORE_B1F_LINK = WarpLink(
        Goldenrod_Underground_Warehouse_Warp_Points.GOLDENROD_UNDERGROUND_WAREHOUSE_TO_GOLDENROD_DEPT_STORE_B1F_WP,
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH_WP, #This is the wrong link but doesn't matter
        "GoldenrodUndergroundWarehouse", 10, unlocks=[Unlock_Keys.KEY_CARD]
    )


class Goldenrod_Underground_Switch_Room_Entrance_Links(Enum):

    #This is the entry stair in the actual switch room
    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_LINK = WarpLink(
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_WP,
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH_WP,
        "GoldenrodUndergroundSwitchRoomEntrances",
    )

    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_SOUTH_LINK = WarpLink(
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_SOUTH_WP,
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_WP,
        "GoldenrodUndergroundSwitchRoomEntrances", 15
    )

    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_SOUTH_LINK = WarpLink(
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_SOUTH_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_SOUTH_WP,
        "GoldenrodUndergroundSwitchRoomEntrances", 20, dual_width=True
    )

    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_NORTH_LINK = WarpLink(
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_NORTH_WP,
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_NORTH_WP,
        "GoldenrodUndergroundSwitchRoomEntrances", 30
    )

    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_NORTH_LINK = WarpLink(
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_NORTH_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_NORTH_WP,
        "GoldenrodUndergroundSwitchRoomEntrances" , 35, dual_width=True
    )

class Goldenrod_Underground_Links(Enum):

    GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_NORTH_LINK = WarpLink(
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_NORTH_WP,
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_NORTH_WP,
        "GoldenrodUnderground"
    )

    GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH_LINK = WarpLink(
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH_WP,
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_SOUTH_WP,
        "GoldenrodUnderground", 5

    )
    GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_KEY_DOOR_LINK = WarpLink(
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_KEY_DOOR_WP,
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_STAIR_WP,
        "GoldenrodUnderground", 10

    )
    GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_STAIR_LINK = WarpLink(
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_STAIR_WP,
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_KEY_DOOR_WP,
        "GoldenrodUnderground", 15, dual_width=True
    )

    GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_LINK = WarpLink(
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_WP,
        Goldenrod_Underground_Switch_Room_Entrance_Links.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_LINK,
        "GoldenrodUnderground", 25
    )




#Todo check if keycard early allows you to clear radio tower, or if you need the 7 badge trigger
class Radio_Tower_1F_Links(Enum):
    RADIO_TOWER_1F_TO_GOLDENROD_CITY_LINK = WarpLink(
        Radio_Tower_1F_Warp_Points.RADIO_TOWER_1F_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_RADIO_TOWER_1F_WP,
        "RadioTower1F", dual_width=True, unlocks=[Unlock_Keys.CAN_CLEAR_RADIO_TOWER_ROCKETS, Unlock_Keys.RADIO_CARD],
        locked_by=[Unlock_Keys.KEY_CARD]
    )
    # RADIO_TOWER_1F_TO_RADIO_TOWER_2F_LINK


#######################################################################
#                    Indigo Group                                     #
#######################################################################

class Kogas_Room_Links(Enum):
    KOGAS_ROOM_TO_WILLS_ROOM_LINK = WarpLink(
        Kogas_Room_Warp_Points.KOGAS_ROOM_TO_WILLS_ROOM_WP,
        Wills_Room_Warp_Points.WILLS_ROOM_TO_KOGAS_ROOM_WP,
        "KogasRoom", dual_width=True, unlocks=[Unlock_Keys.E4_KOGA])

    KOGAS_ROOM_TO_BRUNOS_ROOM_LINK = WarpLink(
        Kogas_Room_Warp_Points.KOGAS_ROOM_TO_BRUNOS_ROOM_WP,
        Brunos_Room_Warp_Points.BRUNOS_ROOM_TO_KOGAS_ROOM_WP,
        "KogasRoom", 10, dual_width=True, unlocks=[Unlock_Keys.E4_KOGA]
    )

class Wills_Room_Links(Enum):
    WILLS_ROOM_TO_INDIGO_PLATEAU_POKECENTER_1F_LINK = WarpLink(
        Wills_Room_Warp_Points.WILLS_ROOM_TO_INDIGO_PLATEAU_POKECENTER_1F_WP,
        Indigo_Plateau_Pokecenter_1F_Warp_Points.INDIGO_PLATEAU_POKECENTER_1F_TO_WILLS_ROOM_1_WP,    #CHANGE THIS IN THE FUTURE (THIS ISNT THE ACTUAL LINK)
        "WillsRoom", unlocks=[Unlock_Keys.E4_WILL]
    )

    WILLS_ROOM_TO_KOGAS_ROOM_LINK = WarpLink(
        Wills_Room_Warp_Points.WILLS_ROOM_TO_KOGAS_ROOM_WP,
        Kogas_Room_Warp_Points.KOGAS_ROOM_TO_WILLS_ROOM_WP,
        "WillsRoom", 5, dual_width=True, unlocks=[Unlock_Keys.E4_WILL]
    )

class Karens_Room_Links(Enum):
    KARENS_ROOM_TO_BRUNOS_ROOM_LINK = WarpLink(
        Karens_Room_Warp_Points.KARENS_ROOM_TO_BRUNOS_ROOM_WP,
        Brunos_Room_Warp_Points.BRUNOS_ROOM_TO_KARENS_ROOM_WP,
        "KarensRoom", dual_width=True, unlocks=[Unlock_Keys.E4_KAREN]
    )

    KARENS_ROOM_TO_LANCES_ROOM_LINK = WarpLink(
        Karens_Room_Warp_Points.KARENS_ROOM_TO_LANCES_ROOM_WP,
        Lances_Room_Warp_Points.LANCES_ROOM_TO_KARENS_ROOM_WP,
        "KarensRoom", 10, dual_width=True, unlocks=[Unlock_Keys.E4_KAREN]
    )

class Brunos_Room_Links(Enum):
    BRUNOS_ROOM_TO_KOGAS_ROOM_LINK = WarpLink(
        Brunos_Room_Warp_Points.BRUNOS_ROOM_TO_KOGAS_ROOM_WP,
        Kogas_Room_Warp_Points.KOGAS_ROOM_TO_BRUNOS_ROOM_WP,
        "BrunosRoom", dual_width=True, unlocks=[Unlock_Keys.E4_BRUNO]
    )

    BRUNOS_ROOM_TO_KARENS_ROOM_LINK = WarpLink(
        Brunos_Room_Warp_Points.BRUNOS_ROOM_TO_KARENS_ROOM_WP,
        Karens_Room_Warp_Points.KARENS_ROOM_TO_BRUNOS_ROOM_WP,
        "BrunosRoom", 10, dual_width=True, unlocks=[Unlock_Keys.E4_BRUNO]
    )

class Lances_Room_Links(Enum):
    LANCES_ROOM_TO_KARENS_ROOM_LINK = WarpLink(
        Lances_Room_Warp_Points.LANCES_ROOM_TO_KARENS_ROOM_WP,
        Karens_Room_Warp_Points.KARENS_ROOM_TO_LANCES_ROOM_WP,
        "LancesRoom", dual_width=True, unlocks=[Unlock_Keys.CHAMPION_LANCE]
    )


#######################################################################
#                    Mahogany Group                                   #
#######################################################################
class Mahogany_Town_Links(Enum):
    MAHOGANY_TOWN_TO_MAHOGANY_MART_1F_LINK = WarpLink(
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_MART_1F_WP,
        Mahogany_Mart_Warp_Points.MAHOGANY_MART_1F_TO_MAHOGANY_TOWN_WP,
        "MahoganyTown"
    )
    MAHOGANY_TOWN_TO_MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_LINK = WarpLink(
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_WP,
        Mahogany_Red_Gyarados_Speech_House_Warp_Points.MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_TO_MAHOGANY_TOWN_WP,
        "MahoganyTown" , 5
    )
    MAHOGANY_TOWN_TO_MAHOGANY_GYM_LINK = WarpLink(
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_GYM_WP,
        Mahogany_Gym_Warp_Points.MAHOGANY_GYM_TO_MAHOGANY_TOWN_WP,
        "MahoganyTown" , 10, locked_by=[Unlock_Keys.CAN_CLEAR_MAHOGANY_ROCKETS]
    )
    MAHOGANY_TOWN_TO_MAHOGANY_POKECENTER_1F_LINK = WarpLink(
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_POKECENTER_1F_WP,
        Mahogany_Pokecenter_Warp_Points.MAHOGANY_POKECENTER_1F_TO_MAHOGANY_TOWN_WP,
        "MahoganyTown" , 15
    )
    MAHOGANY_TOWN_TO_ROUTE_43_MAHOGANY_GATE_LINK = WarpLink(
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_ROUTE_43_MAHOGANY_GATE_WP,
        Route_43_Mahogany_Gate_Warp_Points.ROUTE_43_MAHOGANY_GATE_TO_MAHOGANY_TOWN_WP,
        "MahoganyTown" , 20
    )

class Mahogany_Gym_Links(Enum):
    MAHOGANY_GYM_TO_MAHOGANY_TOWN_LINK = WarpLink(
        Mahogany_Gym_Warp_Points.MAHOGANY_GYM_TO_MAHOGANY_TOWN_WP,
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_GYM_WP,
        "MahoganyGym", dual_width=True, unlocks=[Unlock_Keys.BADGE_7]
    )

class Mahogany_Mart_Links(Enum):
    MAHOGANY_MART_1F_TO_MAHOGANY_TOWN_LINK = WarpLink(
        Mahogany_Mart_Warp_Points.MAHOGANY_MART_1F_TO_MAHOGANY_TOWN_WP,
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_MART_1F_WP,
        "MahoganyMart1F", dual_width=True, unlocks=[Unlock_Keys.CAN_CLEAR_MAHOGANY_ROCKETS, Unlock_Keys.HM_WHIRLPOOL],
        locked_by=[Unlock_Keys.CAN_SURF, Unlock_Keys.LAKE_OF_RAGE_FOUND]
    )

    # MAHOGANY_MART_1F_TO_TEAM_ROCKET_BASE_B1F_LINK = WarpLink(
    #     Mahogany_Mart_Warp_Points.MAHOGANY_MART_1F_TO_TEAM_ROCKET_BASE_B1F_WP,
    #     Team_Rocket_Base_B1F_Warp_Points.,
    #     0x0006C600,10
    # )

class Mahogany_Pokecenter_Links(Enum):
    MAHOGANY_POKECENTER_1F_TO_MAHOGANY_TOWN_LINK = WarpLink(
        Mahogany_Pokecenter_Warp_Points.MAHOGANY_POKECENTER_1F_TO_MAHOGANY_TOWN_WP,
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_POKECENTER_1F_WP,
        "MahoganyPokecenter1F", dual_width=True
    )

    MAHOGANY_POKECENTER_1F_TO_MAHOGANY_POKECENTER_2F_LINK = WarpLink(
        Mahogany_Pokecenter_Warp_Points.MAHOGANY_POKECENTER_TO_MAHOGANY_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "MahoganyPokecenter1F", 10
    )

class Mahogany_Red_Gyarados_Speech_House_Links(Enum):
    MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_TO_MAHOGANY_TOWN = WarpLink(
        Mahogany_Red_Gyarados_Speech_House_Warp_Points.MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_TO_MAHOGANY_TOWN_WP,
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_WP,
        "MahoganyRedGyaradosSpeechHouse", dual_width=True
    )


#######################################################################
#                    New Bark Group                                   #
#######################################################################

class New_Bark_Links(Enum):
    #lugia coords are 01 03 49
    # 0018C546 is lugia coords, 0C 11 coordinates to 13, 8 for some reason
    #set above to 0F to be on shoreline
    # 01 0F 0C
    #set 0007 723C to 3E instaed of 41 to make ho oh always present

    #lugia presence, set 0018C510 to 12 instead of 15
    NEW_BARK_TO_PLAYERS_NEIGHBORS_HOUSE_LINK = WarpLink(
        New_Bark_Warp_Points.NEW_BARK_TO_PLAYERS_NEIGHBORS_HOUSE_WP,
        Players_Neighbors_House_Warp_Points.PLAYERS_NEIGHBORS_HOUSE_TO_NEW_BARK_WP,
         "NewBarkTown" , 10)

    NEW_BARK_TO_ELMS_HOUSE_LINK = WarpLink(
        New_Bark_Warp_Points.NEW_BARK_TO_ELMS_HOUSE_WP,
        Elms_House_Warp_Points.ELMS_HOUSE_TO_NEW_BARK_WP,
        "NewBarkTown" , 15)

    # Don't Randomize Elms Lab :P You need that starter pokemon
    # NEW_BARK_TO_ELMS_LAB_LINK = WarpLink(
    #     New_Bark_Warp_Points.NEW_BARK_TO_ELMS_LAB_WP,
    #     Elms_Lab_Warp_Points.ELMS_LAB_TO_NEW_BARK_WP,
    #     0x001A8352)

class Players_Neighbors_House_Links(Enum):

    PLAYERS_NEIGHBORS_HOUSE_TO_NEW_BARK_LINK = WarpLink(
        Players_Neighbors_House_Warp_Points.PLAYERS_NEIGHBORS_HOUSE_TO_NEW_BARK_WP,
        New_Bark_Warp_Points.NEW_BARK_TO_PLAYERS_NEIGHBORS_HOUSE_WP,
        "PlayersNeighborsHouse",
        dual_width=True)

class Elms_House_Links(Enum):

    ELMS_HOUSE_TO_NEW_BARK_LINK = WarpLink(
        Elms_House_Warp_Points.ELMS_HOUSE_TO_NEW_BARK_WP,
        New_Bark_Warp_Points.NEW_BARK_TO_ELMS_HOUSE_WP,
        "ElmsHouse",
        dual_width=True)

#######################################################################
#                    Olivine Group                                    #
#######################################################################
class Olivine_City_Links(Enum):



    OLIVINE_CITY_TO_OLIVINE_POKECENTER_LINK = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_POKECENTER_1F_WP,
        Olivine_Pokecenter_Warp_Points.OLIVINE_POKECENTER_TO_OLIVINE_CITY_WP,
        "OlivineCity")

    OLIVINE_CITY_TO_OLIVINE_GYM_LINK = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_GYM_WP,
        Olivine_Gym_Warp_Points.OLIVINE_GYM_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 5)

    OLIVINE_CITY_TO_OLIVINE_TIMS_HOUSE_LINK = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_TIMS_HOUSE_WP,
        Olivine_Tims_House_Warp_Points.OLIVINE_TIMS_HOUSE_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 10)

    OLIVINE_CITY_TO_OLIVINE_SPEECH_HOUSE_LINK = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_PUNISHMENT_SPEECH_HOUSE_WP,
        Olivine_Punishment_Speech_House_Warp_Points.OLIVINE_PUNISHMENT_SPEECH_HOUSE_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 20)

    OLIVINE_CITY_TO_OLIVINE_GOOD_ROD_HOUSE_LINK = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_GOOD_ROD_HOUSE_WP,
        Olivine_Good_Rod_House_Warp_Points.OLIVINE_GOOD_ROD_HOUSE_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 25)

    OLIVINE_CITY_TO_OLIVINE_CAFE_LINK = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_CAFE_WP,
        Olivine_Cafe_Warp_Points.OLIVINE_CAFE_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 30)

    OLIVINE_CITY_TO_OLIVINE_MART_LINK = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_MART_WP,
        Olivine_Mart_Warp_Points.OLIVINE_MART_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 35)

    OLIVINE_CITY_TO_OLIVINE_LIGHTHOUSE_1F_LINK = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_LIGHTHOUSE_1F_WP,
        Olivine_Lighthouse_1F_Warp_Points.OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 40)

    OLIVINE_CITY_TO_OLIVINE_PORT_PASSAGE_LINK = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_PORT_PASSAGE_WP,
        Olivine_Port_Passage_Warp_Points.OLIVINE_PORT_PASSAGE_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 45,
        dual_width=True)

class Olivine_Cafe_Links(Enum):

    OLIVINE_CAFE_TO_OLIVINE_CITY_LINK = WarpLink(
        Olivine_Cafe_Warp_Points.OLIVINE_CAFE_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_CAFE_WP,
        "OlivineCafe",
        dual_width=True,
        unlocks=[Unlock_Keys.HM_STRENGTH])

class Olivine_Good_Rod_House_Links(Enum):

    OLIVINE_GOOD_ROD_HOUSE_TO_OLIVINE_CITY_LINK = WarpLink(
        Olivine_Good_Rod_House_Warp_Points.OLIVINE_GOOD_ROD_HOUSE_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_GOOD_ROD_HOUSE_WP,
        "OlivineGoodRodHouse",
        dual_width=True)

class Olivine_Gym_Links(Enum):

    OLIVINE_GYM_TO_OLIVINE_CITY_LINK = WarpLink(
        Olivine_Gym_Warp_Points.OLIVINE_GYM_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_GYM_WP,
        "OlivineGym",
        dual_width=True, locked_by=[Unlock_Keys.OLIVINE_MEDICINE],
        unlocks=[Unlock_Keys.BADGE_6])

class Olivine_Lighthouse_1F_Links(Enum):

    OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_CITY_LINK = WarpLink(
        Olivine_Lighthouse_1F_Warp_Points.OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_LIGHTHOUSE_1F_WP,
        "OlivineLighthouse1F",
        dual_width=True)

    OLIVINE_LIGHTHOUSE_1F_TO_2F_STAIR_LINK = WarpLink(
        Olivine_Lighthouse_1F_Warp_Points.OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_LIGHTHOUSE_2FA_WP,
        Olivine_Lighthouse_2F_Warp_Points.OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_1FA_WP,
        "OlivineLighthouse1F" , 10)

class Olivine_Lighthouse_2F_Links(Enum):

    OLIVINE_LIGHTHOUSE_2F_TO_1F_STAIR_LINK = WarpLink(
        Olivine_Lighthouse_2F_Warp_Points.OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_1FA_WP,
        Olivine_Lighthouse_1F_Warp_Points.OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_LIGHTHOUSE_2FA_WP,
        "OlivineLighthouse2F")

    OLIVINE_LIGHTHOUSE_2F_TO_3F_STAIR_LINK = WarpLink(
        Olivine_Lighthouse_2F_Warp_Points.OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_3FA_WP,
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_2FA_WP,
        "OlivineLighthouse2F" , 5)

    OLIVINE_LIGHTHOUSE_2F_TO_1F_PITFALL_LINK = WarpLink(
        Olivine_Lighthouse_2F_Warp_Points.OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_1FB_WP,
        Olivine_Lighthouse_1F_Warp_Points.OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_LIGHTHOUSE_2FB_WP,
        "OlivineLighthouse2F" , 10,
        dual_width=True)

class Olivine_Lighthouse_3F_Links(Enum):

    OLIVINE_LIGHTHOUSE_3F_TO_4F_RIGHT_STAIR_LINK = WarpLink(
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FA_WP,
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FA_WP,
        "OlivineLighthouse3F")

    OLIVINE_LIGHTHOUSE_3F_TO_2F_STAIR_LINK = WarpLink(
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_2FA_WP,
        Olivine_Lighthouse_2F_Warp_Points.OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_3FA_WP,
        "OlivineLighthouse3F" , 5)

    OLIVINE_LIGHTHOUSE_3F_TO_4F_MIDDLE_STAIR_LINK = WarpLink(
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FB_WP,
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FB_WP,
        "OlivineLighthouse3F" , 10)

    OLIVINE_LIGHTHOUSE_3F_TO_2F_PITFALL_LINK = WarpLink(
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_2FB_WP,
        Olivine_Lighthouse_2F_Warp_Points.OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_3FB_WP,
        "OlivineLighthouse3F" , 15,
        dual_width=True)

class Olivine_Lighthouse_4F_Links(Enum):

    OLIVINE_LIGHTHOUSE_4F_TO_3F_STAIR_1_LINK = WarpLink(
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FA_WP,
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FA_WP,
        "OlivineLighthouse4F")

    OLIVINE_LIGHTHOUSE_4F_TO_5F_STAIR_1_LINK = WarpLink(
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FA_WP,
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FA_WP,
        "OlivineLighthouse4F" , 5)

    OLIVINE_LIGHTHOUSE_4F_TO_5F_STAIR_2_LINK = WarpLink(
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FB_WP,
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FB_WP,
        "OlivineLighthouse4F" , 10)

    OLIVINE_LIGHTHOUSE_4F_TO_3F_STAIR_2_LINK = WarpLink(
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FB_WP,
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FB_WP,
        "OlivineLighthouse4F" , 15)

    OLIVINE_LIGHTHOUSE_4F_TO_3F_PITFALL_1_LINK = WarpLink(
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FC_WP,
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FC_WP,
        "OlivineLighthouse4F" , 20,
        dual_width=True)

    OLIVINE_LIGHTHOUSE_4F_TO_3F_PITFALL_2_LINK = WarpLink(
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FD_WP,
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FD_WP,
        "OlivineLighthouse4F" , 30,
        dual_width=True)

class Olivine_Lighthouse_5F_Links(Enum):

    OLIVINE_LIGHTHOUSE_5F_TO_6F_STAIR_LINK = WarpLink(
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_6FA_WP,
        Olivine_Lighthouse_6F_Warp_Points.OLIVINE_LIGHTHOUSE_6F_TO_OLIVINE_LIGHTHOUSE_5FA_WP,
        "OlivineLighthouse5F")


    OLIVINE_LIGHTHOUSE_5F_TO_4F_OUTER_STAIR_LINK = WarpLink(
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FA_WP,
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FA_WP,
        "OlivineLighthouse5F" , 5)

    OLIVINE_LIGHTHOUSE_5F_TO_4F_INNER_STAIR_LINK = WarpLink(
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FB_WP,
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FB_WP,
        "OlivineLighthouse5F" , 10)

    OLIVINE_LIGHTHOUSE_5F_TO_4F_PITFALL_LINK = WarpLink(
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FC_WP,
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FC_WP,
        "OlivineLighthouse5F" , 15,
        dual_width=True)

class Olivine_Lighthouse_6F_Links(Enum):

    OLIVINE_LIGHTHOUSE_6F_TO_5F_STAIR_LINK = WarpLink(
        Olivine_Lighthouse_6F_Warp_Points.OLIVINE_LIGHTHOUSE_6F_TO_OLIVINE_LIGHTHOUSE_5FA_WP,
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_6FA_WP,
        "OlivineLighthouse6F", unlocks=[Unlock_Keys.TOP_OF_LIGHTHOUSE_FOUND]
    )

    OLIVINE_LIGHTHOUSE_6F_TO_5F_PITFALL_LINK = WarpLink(
        Olivine_Lighthouse_6F_Warp_Points.OLIVINE_LIGHTHOUSE_6F_TO_OLIVINE_LIGHTHOUSE_5FB_WP,
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_6FB_WP,
        "OlivineLighthouse6F" , 5,dual_width=True, unlocks=[Unlock_Keys.TOP_OF_LIGHTHOUSE_FOUND]
    )

class Olivine_Mart_Links(Enum):

    OLIVINE_MART_TO_OLIVINE_CITY_LINK = WarpLink(
        Olivine_Mart_Warp_Points.OLIVINE_MART_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_MART_WP,
        "OlivineMart",
        dual_width=True)

class Olivine_Pokecenter_Links(Enum):

    OLIVINE_POKECENTER_TO_OLIVINE_CITY_LINK = WarpLink(
        Olivine_Pokecenter_Warp_Points.OLIVINE_POKECENTER_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_POKECENTER_1F_WP,
        "OlivinePokecenter1F",
        dual_width=True)

    OLIVINE_POKECENTER_1F_TO_OLIVINE_POKECENTER_2F_LINK = WarpLink(
        Olivine_Pokecenter_Warp_Points.OLIVINE_POKECENTER_TO_OLIVINE_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "OlivinePokecenter1F", 10
    )

class Olivine_Port_Passage_Links(Enum):

    OLIVINE_PORT_PASSAGE_TO_OLIVINE_CITY_LINK = WarpLink(
        Olivine_Port_Passage_Warp_Points.OLIVINE_PORT_PASSAGE_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_PORT_PASSAGE_WP,
        "OlivinePortPassage",
        dual_width=True)

#     ADD OTHER LINKS WHEN THEIR WARP POINTS EXIST

class Olivine_Punishment_Speech_House_Links(Enum):

    OLIVINE_PUNISHMENT_SPEECH_HOUSE_TO_OLIVINE_CITY_LINK = WarpLink(
        Olivine_Punishment_Speech_House_Warp_Points.OLIVINE_PUNISHMENT_SPEECH_HOUSE_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_PUNISHMENT_SPEECH_HOUSE_WP,
        "OlivinePunishmentSpeechHouse",
        dual_width=True)

class Olivine_Tims_House_Links(Enum):

    OLIVINE_TIMS_HOUSE_TO_OLIVINE_CITY_LINK = WarpLink(
        Olivine_Tims_House_Warp_Points.OLIVINE_TIMS_HOUSE_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_TIMS_HOUSE_WP,
        "OlivineTimsHouse",
        dual_width=True)

#######################################################################
#                    Routes Group                                     #
#######################################################################

class Indigo_Plateau_Pokecenter_1F_Links(Enum):

    INDIGO_PLATEAU_POKECENTER_1F_TO_ROUTE_23_1_LINK = WarpLink(
        Indigo_Plateau_Pokecenter_1F_Warp_Points.INDIGO_PLATEAU_POKECENTER_1F_TO_ROUTE_23_1_WP,
        Route23_Warp_Points.ROUTE23_TO_INDIGO_PLATEAU_POKECENTER_1F_1_WP,
        "IndigoPlateauPokecenter1F", dual_width=True)

    INDIGO_PLATEAU_POKECENTER_1F_TO_POKECENTER_2F_1_LINK = WarpLink(
        Indigo_Plateau_Pokecenter_1F_Warp_Points.INDIGO_PLATEAU_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "IndigoPlateauPokecenter1F", 10
    )

    INDIGO_PLATEAU_POKECENTER_1F_TO_WILLS_ROOM_1_LINK = WarpLink(
        Indigo_Plateau_Pokecenter_1F_Warp_Points.INDIGO_PLATEAU_POKECENTER_1F_TO_WILLS_ROOM_1_WP,
        Wills_Room_Warp_Points.WILLS_ROOM_TO_INDIGO_PLATEAU_POKECENTER_1F_WP,
        "IndigoPlateauPokecenter1F", 15
    )


class Route23_Links(Enum):

    ROUTE23_TO_INDIGO_PLATEAU_POKECENTER_1F_1_LINK = WarpLink(
        Route23_Warp_Points.ROUTE23_TO_INDIGO_PLATEAU_POKECENTER_1F_1_WP,
        Indigo_Plateau_Pokecenter_1F_Warp_Points.INDIGO_PLATEAU_POKECENTER_1F_TO_ROUTE_23_1_WP,
        "Route23", dual_width=True)

    ROUTE23_TO_VICTORY_ROAD_10_LINK = WarpLink(
        Route23_Warp_Points.ROUTE23_TO_VICTORY_ROAD_10_WP,
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_ROUTE_23_3_WP,
        "Route23", 10, dual_width=True)
class Day_Of_Week_Siblings_House_Links(Enum):
    DAY_OF_WEEK_SIBLINGS_HOUSE_TO_ROUTE_26_3_LINK = WarpLink(
        Day_Of_Week_Siblings_House_Warp_Points.DAY_OF_WEEK_SIBLINGS_HOUSE_TO_ROUTE_26_3_WP,
        Route_26_Warp_Points.ROUTE_26_TO_DAY_OF_WEEK_SIBLINGS_HOUSE_1_WP,
        "DayOfWeekSiblingsHouse", dual_width=True)


class Route_26_Heal_House_Links(Enum):
    ROUTE_26_HEAL_HOUSE_TO_ROUTE_26_2_LINK = WarpLink(
        Route_26_Heal_House_Warp_Points.ROUTE_26_HEAL_HOUSE_TO_ROUTE_26_2_WP,
        Route_26_Warp_Points.ROUTE_26_TO_ROUTE_26_HEAL_HOUSE_1_WP,
        "Route26HealHouse", dual_width=True)


class Route_27_Sandstorm_House_Links(Enum):
    ROUTE_27_SANDSTORM_HOUSE_TO_ROUTE_27_1_LINK = WarpLink(
        Route_27_Sandstorm_House_Warp_Points.ROUTE27_SANDSTORM_HOUSE_TO_ROUTE_27_1_WP,
        Route_27_Warp_Points.ROUTE_27_TO_ROUTE_27_SANDSTORM_HOUSE_1_WP,
        "Route27SandstormHouse", dual_width=True)

class Route_26_Links(Enum):

    ROUTE_26_TO_VICTORY_ROAD_GATE_3_LINK = WarpLink(
        Route_26_Warp_Points.ROUTE_26_TO_VICTORY_ROAD_GATE_3_WP,
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_ROUTE_26_1_WP,
        "Route26")

    ROUTE_26_TO_ROUTE_26_HEAL_HOUSE_1_LINK = WarpLink(
        Route_26_Warp_Points.ROUTE_26_TO_ROUTE_26_HEAL_HOUSE_1_WP,
        Route_26_Heal_House_Warp_Points.ROUTE_26_HEAL_HOUSE_TO_ROUTE_26_2_WP,
        "Route26", 5)

    ROUTE_26_TO_DAY_OF_WEEK_SIBLINGS_HOUSE_1_LINK = WarpLink(
        Route_26_Warp_Points.ROUTE_26_TO_DAY_OF_WEEK_SIBLINGS_HOUSE_1_WP,
        Day_Of_Week_Siblings_House_Warp_Points.DAY_OF_WEEK_SIBLINGS_HOUSE_TO_ROUTE_26_3_WP,
        "Route26", 10)


class Route_27_Links(Enum):

    ROUTE_27_TO_ROUTE_27_SANDSTORM_HOUSE_1_LINK = WarpLink(
        Route_27_Warp_Points.ROUTE_27_TO_ROUTE_27_SANDSTORM_HOUSE_1_WP,
        Route_27_Sandstorm_House_Warp_Points.ROUTE27_SANDSTORM_HOUSE_TO_ROUTE_27_1_WP,
        "Route27")

    ROUTE_27_TO_TOHJO_FALLS_1_LINK = WarpLink(
        Route_27_Warp_Points.ROUTE_27_TO_TOHJO_FALLS_1_WP,
        Tohjo_Falls_Warp_Points.TOHJO_FALLS_TO_ROUTE_27_2_WP,
        "Route27", 5)

    ROUTE_27_TO_TOHJO_FALLS_2_LINK = WarpLink(
        Route_27_Warp_Points.ROUTE_27_TO_TOHJO_FALLS_2_WP,
        Tohjo_Falls_Warp_Points.TOHJO_FALLS_TO_ROUTE_27_3_WP,
        "Route27", 10)


class Route_41_Links(Enum):

    ROUTE_41_TO_WHIRL_ISLAND_NW_LINK = WarpLink(
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_NW_WP,
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_ROUTE_41_1_WP,
        "Route41")

    ROUTE_41_TO_WHIRL_ISLAND_NE_LINK = WarpLink(
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_NE_WP,
        Whirl_Island_NE_Warp_Points.WHIRL_ISLAND_N_E_TO_ROUTE_41_2_WP,
        "Route41", 5)

    ROUTE_41_TO_WHIRL_ISLAND_SW_LINK = WarpLink(
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_SW_WP,
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_ROUTE_41_3_WP,
        "Route41", 10)

    ROUTE_41_TO_WHIRL_ISLAND_SE_LINK = WarpLink(
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_SE_WP,
        Whirl_Island_SE_Warp_Points.WHIRL_ISLAND_S_E_TO_ROUTE_41_4_WP,
        "Route41", 15)
class Route_29_Links(Enum):

    ROUTE_29_TO_ROUTE_46_GATE_LINK = WarpLink(
        Route_29_Warp_Points.ROUTE_29_TO_ROUTE_46_GATE_WP,
        Route_29_Route_46_Gate_Warp_Points.ROUTE_29_ROUTE_46_GATE_TO_ROUTE_29_WP,
        "Route29"
    )

class Route_30_Links(Enum):

    ROUTE_30_TO_ROUTE_30_BERRY_HOUSE_LINK = WarpLink(
        Route_30_Warp_Points.ROUTE_30_TO_ROUTE_30_BERRY_HOUSE_WP,
        Route_30_Berry_House_Warp_Points.ROUTE_30_BERRY_HOUSE_TO_ROUTE_30_WP,
        "Route30"
    )

    ROUTE_30_TO_MR_POKEMONS_HOUSE_LINK = WarpLink(
        Route_30_Warp_Points.ROUTE_30_TO_MR_POKEMONS_HOUSE_WP,
        Mr_Pokemons_House_Warp_Points.MR_POKEMONS_HOUSE_TO_ROUTE_30_WP,
        "Route30" , 5
    )

class Route_31_Links(Enum):

    ROUTE_31_TO_ROUTE_31_VIOLET_GATE_LINK = WarpLink(
        Route_31_Warp_Points.ROUTE_31_TO_ROUTE_31_VIOLET_GATE_WP,
        Route_31_Violet_Gate_Warp_Points.ROUTE_31_VIOLET_GATE_TO_ROUTE_31_WP,
        "Route31", dual_width=True
    )

    ROUTE_31_TO_DARK_CAVE_VIOLET_ENTRANCE_LINK = WarpLink(
        Route_31_Warp_Points.ROUTE_31_TO_DARK_CAVE_VIOLET_ENTRANCE_WP,
        Dark_Cave_Violet_Entrance_Warp_Points.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_31_WP,
        "Route31" , 10
    )

class Route_32_Links(Enum):

    ROUTE_32_TO_ROUTE_32_POKECENTER_LINK = WarpLink(
        Route_32_Warp_Points.ROUTE_32_TO_ROUTE_32_POKECENTER_WP,
        Route_32_Pokecenter_Warp_Points.ROUTE_32_POKECENTER_TO_ROUTE_32_WP,
        "Route32"
    )

    ROUTE_32_TO_ROUTE_32_RUINS_OF_ALPH_GATE_LINK = WarpLink(
        Route_32_Warp_Points.ROUTE_32_TO_ROUTE_32_RUINS_OF_ALPH_GATE_WP,
        Route_32_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_32_RUINS_OF_ALPH_GATE_TO_ROUTE_32_WP,
        "Route32", 5, dual_width=True
    )

    ROUTE_32_TO_UNION_CAVE_LINK = WarpLink(
        Route_32_Warp_Points.ROUTE_32_TO_UNION_CAVE_1F_WP,
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_ROUTE_32_WP,
        "Route32" , 15
    )

class Route_32_Pokecenter_Links(Enum):
    ROUTE_32_POKECENTER_TO_ROUTE_32_LINK = WarpLink(
        Route_32_Pokecenter_Warp_Points.ROUTE_32_POKECENTER_TO_ROUTE_32_WP,
        Route_32_Warp_Points.ROUTE_32_TO_ROUTE_32_POKECENTER_WP,
        "Route32Pokecenter1F", dual_width=True
    )

    ROUTE_32_POKECENTER_1F_TO_ROUTE_32_POKECENTER_2F_LINK = WarpLink(
        Route_32_Pokecenter_Warp_Points.ROUTE_32_POKECENTER_TO_ROUTE_32_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "Route32Pokecenter1F", 10
    )

class Route_33_Links(Enum):
    ROUTE_33_TO_UNION_CAVE_1F_LINK = WarpLink(
        Route_33_Warp_Points.ROUTE_33_TO_UNION_CAVE_1F_WP,
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_ROUTE_33_WP,
        "Route33"
    )

class Route_34_Links(Enum):
    ROUTE_34_TO_ROUTE_34_ILEX_FOREST_GATE_LINK = WarpLink(
        Route_34_Warp_Points.ROUTE_34_TO_ROUTE_34_ILEX_FOREST_GATE_WP,
        Route_34_Ilex_Forest_Gate_Warp_Points.ROUTE_34_ILEX_FOREST_GATE_TO_ROUTE_34_WP,
        "Route34", dual_width=True
    )

    ROUTE_34_TO_DAY_CARE_FRONT_LINK = WarpLink(
        Route_34_Warp_Points.ROUTE_34_TO_DAY_CARE_FRONT_WP,
        Day_Care_Warp_Points.DAY_CARE_TO_ROUTE_34_FRONT_WP,
        "Route34" , 10, dual_width=True
    )
    # ROUTE_34_TO_DAY_CARE_SIDE_LINK = WarpLink(
    #
    #     0x00078A81 , 20,
    # )

class Route_35_Links(Enum):
    ROUTE_35_TO_ROUTE_35_GOLDENROD_GATE_LINK = WarpLink(
        Route_35_Warp_Points.ROUTE_35_TO_ROUTE_35_GOLDENROD_GATE_WP,
        Route_35_Goldenrod_Gate_Warp_Points.ROUTE_35_GOLDENROD_GATE_TO_ROUTE_35_WP,
        "Route35", dual_width=True
    )

    ROUTE_35_TO_NATIONAL_PARK_GATE_LINK = WarpLink(
        Route_35_Warp_Points.ROUTE_35_TO_NATIONAL_PARK_GATE_WP,
        Route_35_National_Park_Gate_Warp_Points.ROUTE_35_NATIONAL_PARK_GATE_TO_ROUTE_35_WP,
        "Route35" , 10
    )

class Route_36_Links(Enum):

    ROUTE_36_TO_ROUTE_36_NATIONAL_PARK_GATE_LINK = WarpLink(
        Route_36_Warp_Points.ROUTE_36_TO_ROUTE_36_NATIONAL_PARK_GATE_WP,
        Route_36_National_Park_Gate_Warp_Points.ROUTE_36_NATIONAL_PARK_GATE_TO_ROUTE_36_WP,
        "Route36",
        dual_width=True
    )

    ROUTE_36_TO_ROUTE_36_RUINS_OF_ALPH_GATE_LINK = WarpLink(
        Route_36_Warp_Points.ROUTE_36_TO_ROUTE_36_RUINS_OF_ALPH_GATE_WP,
        Route_36_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_36_RUINS_OF_ALPH_GATE_TO_ROUTE_36_WP,
        "Route36" , 10,
        dual_width=True
    )

class Route_38_Links(Enum):
    ROUTE_38_TO_ROUTE_38_ECRUTEAK_GATE_LINK = WarpLink(
        Route_38_Warp_Points.ROUTE_38_TO_ROUTE_38_ECRUTEAK_GATE_WP,
        Route_38_Ecruteak_Gate_Warp_Points.ROUTE_38_ECRUTEAK_GATE_TO_ROUTE_38_WP,
        "Route38", dual_width=True
    )

class Route_39_Links(Enum):
    ROUTE_39_TO_ROUTE_39_BARN_LINK = WarpLink(
        Route_39_Warp_Points.ROUTE_39_TO_ROUTE_39_BARN_WP,
        Route_39_Barn_Warp_Points.ROUTE_39_BARN_TO_ROUTE_39_1_WP,
        "Route39"
    )
    ROUTE_39_TO_ROUTE_39_FARMHOUSE_LINK = WarpLink(
        Route_39_Warp_Points.ROUTE_39_TO_ROUTE_39_FARMHOUSE_WP,
        Route_39_Farmhouse_Warp_Points.ROUTE39_FARMHOUSE_TO_ROUTE_39_2_WP,
        "Route39", 5
    )

class Route_39_Barn_Links(Enum):
    ROUTE_39_BARN_TO_ROUTE_39_LINK = WarpLink(
        Route_39_Barn_Warp_Points.ROUTE_39_BARN_TO_ROUTE_39_1_WP,
        Route_39_Warp_Points.ROUTE_39_TO_ROUTE_39_BARN_WP,
        "Route39Barn", dual_width=True
    )

class Route_39_Farmhouse_Links(Enum):
    ROUTE_39_FARMHOUSE_TO_ROUTE_39_LINK = WarpLink(
        Route_39_Farmhouse_Warp_Points.ROUTE39_FARMHOUSE_TO_ROUTE_39_2_WP,
        Route_39_Warp_Points.ROUTE_39_TO_ROUTE_39_FARMHOUSE_WP,
        "Route39Farmhouse", dual_width=True
    )

class Route_40_Links(Enum):
    ROUTE_40_TO_ROUTE_40_BATTLE_TOWER_GATE_1_LINK = WarpLink(
        Route_40_Warp_Points.ROUTE_40_TO_ROUTE_40_BATTLE_TOWER_GATE_1_WP,
        Route_40_Battle_Tower_Gate_Warp_Points.ROUTE_40_BATTLE_TOWER_GATE_TO_ROUTE_40_1_WP,
        "Route40"
    )
class Route_40_Battle_Tower_Gate_Links(Enum):
    ROUTE_40_BATTLE_TOWER_GATE_TO_ROUTE_40_1_LINK = WarpLink(
        Route_40_Battle_Tower_Gate_Warp_Points.ROUTE_40_BATTLE_TOWER_GATE_TO_ROUTE_40_1_WP,
        Route_40_Warp_Points.ROUTE_40_TO_ROUTE_40_BATTLE_TOWER_GATE_1_WP,
        "Route40BattleTowerGate", dual_width=True
    )

    ROUTE_40_BATTLE_TOWER_GATE_TO_BATTLE_TOWER_OUTSIDE_1_LINK = WarpLink(
        Route_40_Battle_Tower_Gate_Warp_Points.ROUTE_40_BATTLE_TOWER_GATE_TO_BATTLE_TOWER_OUTSIDE_1_WP,
        Battle_Tower_Outside_Warp_Points.BATTLE_TOWER_OUTSIDE_TO_ROUTE_40_BATTLE_TOWER_GATE_3_WP,
        "Route40BattleTowerGate", 10,dual_width=True
    )


class Battle_Tower_Outside_Links(Enum):
    BATTLE_TOWER_OUTSIDE_TO_ROUTE_40_BATTLE_TOWER_GATE_3_LINK = WarpLink(
        Battle_Tower_Outside_Warp_Points.BATTLE_TOWER_OUTSIDE_TO_ROUTE_40_BATTLE_TOWER_GATE_3_WP,
        Route_40_Battle_Tower_Gate_Warp_Points.ROUTE_40_BATTLE_TOWER_GATE_TO_BATTLE_TOWER_OUTSIDE_1_WP,
        "BattleTowerOutside",dual_width=True
    )

    BATTLE_TOWER_OUTSIDE_TO_BATTLE_TOWER_1F_1_LINK = WarpLink(
        Battle_Tower_Outside_Warp_Points.BATTLE_TOWER_OUTSIDE_TO_BATTLE_TOWER_1F_1_WP,
        Battle_Tower_Outside_Warp_Points.BATTLE_TOWER_OUTSIDE_TO_BATTLE_TOWER_1F_1_WP, # wrong but overwritten always
        "BattleTowerOutside", 10, dual_width=True
    )

# class Route_41_Links(Enum):
#TODO WHIRLS ISLANDS

class Route_42_Links(Enum):
    ROUTE_42_TO_ROUTE_42_ECRUTEAK_GATE_LINK = WarpLink(
        Route_42_Warp_Points.ROUTE_42_TO_ROUTE_42_ECRUTEAK_GATE_WP,
        Route_42_Ecruteak_Gate_Warp_Points.ROUTE_42_ECRUTEAK_GATE_TO_ROUTE_42_WP,
        "Route42", dual_width=True
    )

    ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_LEFT_LINK = WarpLink(
        Route_42_Warp_Points.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_LEFT_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_3_WP,
        "Route42", 10
    )

    ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_MIDDLE_LINK = WarpLink(
        Route_42_Warp_Points.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_MIDDLE_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_4_WP,
        "Route42", 15
    )

    ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_RIGHT_LINK = WarpLink(
        Route_42_Warp_Points.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_RIGHT_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_5_WP,
        "Route42", 20
    )

class Route_43_Links(Enum):
    ROUTE_43_TO_ROUTE_43_MAHOGANY_GATE_LINK = WarpLink(
        Route_43_Warp_Points.ROUTE_43_TO_ROUTE_43_MAHOGANY_GATE_WP,
        Route_43_Mahogany_Gate_Warp_Points.ROUTE_43_MAHOGANY_GATE_TO_ROUTE_43_WP,
        "Route43", dual_width=True
    )

    ROUTE_43_TO_ROUTE_43_GATE_BOTTOM_LINK = WarpLink(
        Route_43_Warp_Points.ROUTE_43_TO_ROUTE_43_GATE_BOTTOM_WP,
        Route_43_Gate_Warp_Points.ROUTE_43_GATE_TO_ROUTE_43_TOP_WP,
        "Route43",10
    )

    ROUTE_43_TO_ROUTE_43_GATE_TOP_LINK = WarpLink(
        Route_43_Warp_Points.ROUTE_43_TO_ROUTE_43_GATE_TOP_WP,
        Route_43_Gate_Warp_Points.ROUTE_43_GATE_TO_ROUTE_43_BOTTOM_WP,
        "Route43" ,15,dual_width=True
    )

class Route_44_Links(Enum):
    ROUTE_44_TO_ICE_PATH_1F_LINK = WarpLink(
        Route_44_Warp_Points.ROUTE_44_TO_ICE_PATH_1F_WP,
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_ROUTE_44_1_WP,
        "Route44"
    )

class Route_45_Links(Enum):
    ROUTE_45_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_LINK = WarpLink(
        Route_45_Warp_Points.ROUTE_45_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_WP,
        Dark_Cave_Blackthorn_Entrance_Warp_Points.DARK_CAVE_BLACKTHORN_ENTRANCE_TO_ROUTE_45_WP,
        "Route45"
    )

class Route_46_Links(Enum):
    ROUTE_46_TO_ROUTE_29_ROUTE_46_GATE_LINK = WarpLink(
        Route_46_Warp_Points.ROUTE_46_TO_ROUTE_29_ROUTE_46_GATE_WP,
        Route_29_Route_46_Gate_Warp_Points.ROUTE_29_ROUTE_46_GATE_TO_ROUTE_46_WP,
        "Route46", dual_width=True
    )

    ROUTE_46_TO_DARK_CAVE_VIOLET_ENTRANCE_LINK = WarpLink(
        Route_46_Warp_Points.ROUTE_46_TO_DARK_CAVE_VIOLET_ENTRANCE_WP,
        Dark_Cave_Violet_Entrance_Warp_Points.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_46_WP,
        "Route46" , 10
    )


#######################################################################
#                    Violet Group                                     #
#######################################################################
class Violet_City_Links(Enum):

    VIOLET_CITY_TO_VIOLET_MART_LINK = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_MART_WP,
        Violet_Mart_Warp_Points.VIOLET_MART_TO_VIOLET_CITY_WP,
        "VioletCity"
    )

    VIOLET_CITY_TO_VIOLET_GYM_LINK = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_GYM_WP,
        Violet_Gym_Warp_Points.VIOLET_GYM_TO_VIOLET_CITY_WP,
        "VioletCity" , 5
    )

    VIOLET_CITY_TO_EARLS_POKEMON_ACADEMY_LINK = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_EARLS_POKEMON_ACADEMY_WP,
        Earls_Pokemon_Academy_Warp_Points.EARLS_POKEMON_ACADEMY_TO_VIOLET_CITY_WP,
        "VioletCity" , 10
    )

    VIOLET_CITY_TO_GUIDE_NICKNAME_SPEECH_HOUSE_LINK = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_NICKNAME_SPEECH_HOUSE_WP,
        Violet_Nickname_Speech_House_Warp_Points.VIOLET_NICKNAME_SPEECH_HOUSE_TO_VIOLET_CITY_WP,
        "VioletCity" , 15
    )

    VIOLET_CITY_TO_VIOLET_POKECENTER_1F_LINK = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_POKECENTER_1F_WP,
        Violet_Pokecenter_Warp_Points.VIOLET_POKECENTER_TO_VIOLET_CITY_WP,
        "VioletCity" , 20
    )

    VIOLET_CITY_TO_VIOLET_KYLES_HOUSE_LINK = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_KYLES_HOUSE_WP,
        Violet_Kyles_House_Warp_Points.VIOLET_KYLES_HOUSE_TO_VIOLET_CITY_WP,
        "VioletCity" , 25
    )

    VIOLET_CITY_TO_SPROUT_TOWER_1F_LINK = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_SPROUT_TOWER_1F_WP,
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_VIOLET_CITY_WP,
        "VioletCity" , 30
    )

    VIOLET_CITY_ROUTE_31_VIOLET_GATE_LINK = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_ROUTE_31_VIOLET_GATE_WP,
        Route_31_Violet_Gate_Warp_Points.ROUTE_31_VIOLET_GATE_TO_VIOLET_CITY_WP,
        "VioletCity" , 35,
        dual_width=True
    )

class Earls_Pokemon_Academy_Links(Enum):

    EARLS_POKEMON_ACADEMY_TO_VIOLET_CITY_LINK = WarpLink(
        Earls_Pokemon_Academy_Warp_Points.EARLS_POKEMON_ACADEMY_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_EARLS_POKEMON_ACADEMY_WP,
        "EarlsPokemonAcademy",
        dual_width=True
    )

class Violet_City_Mart_Links(Enum):

    VIOLET_MART_TO_VIOLET_CITY_LINK = WarpLink(
        Violet_Mart_Warp_Points.VIOLET_MART_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_MART_WP,
        "VioletMart",
        dual_width=True
    )

class Violet_City_Pokecenter_Links(Enum):

    VIOLET_POKECENTER_TO_VIOLET_CITY_LINK = WarpLink(
        Violet_Pokecenter_Warp_Points.VIOLET_POKECENTER_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_POKECENTER_1F_WP,
        "VioletPokecenter1F",
        dual_width=True
    )

    VIOLET_POKECENTER_1F_TO_VIOLET_POKECENTER_2F_LINK = WarpLink(
        Violet_Pokecenter_Warp_Points.VIOLET_POKECENTER_TO_VIOLET_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "VioletPokecenter1F", 10
    )

class Violet_City_Gym_Links(Enum):

    VIOLET_GYM_TO_VIOLET_CITY_LINK = WarpLink(
        Violet_Gym_Warp_Points.VIOLET_GYM_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_GYM_WP,
        "VioletGym",
        dual_width=True, unlocks=[Unlock_Keys.BADGE_1]
    )

class Violet_City_Kyles_House_Links(Enum):

    VIOLET_KYLES_HOUSE_TO_VIOLET_CITY_LINK = WarpLink(
        Violet_Kyles_House_Warp_Points.VIOLET_KYLES_HOUSE_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_KYLES_HOUSE_WP,
        "VioletKylesHouse",
        dual_width=True
    )

class Violet_Nickname_Speech_House_Links(Enum):

    VIOLET_NICKNAME_SPEECH_HOUSE_TO_VIOLET_CITY_LINK = WarpLink(
        Violet_Nickname_Speech_House_Warp_Points.VIOLET_NICKNAME_SPEECH_HOUSE_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_NICKNAME_SPEECH_HOUSE_WP,
        "VioletNicknameSpeechHouse",
        dual_width=True
    )


class Route_28_Warp_Points:
    pass


class Victory_Road_Gate_Links(Enum):

    VICTORY_ROAD_GATE_TO_ROUTE_22_1_LINK = WarpLink(
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_ROUTE_22_1_WP,
        Route_22_Warp_Points.ROUTE_22_TO_VICTORY_ROAD_GATE_1_WP,
        "VictoryRoadGate", dual_width=True)

    VICTORY_ROAD_GATE_TO_ROUTE_26_1_LINK = WarpLink(
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_ROUTE_26_1_WP,
        Route_26_Warp_Points.ROUTE_26_TO_VICTORY_ROAD_GATE_3_WP,
        "VictoryRoadGate", 10, dual_width=True, unlocks=[Unlock_Keys.VICTORY_ROAD_GATE_ACCESS])

    VICTORY_ROAD_GATE_TO_VICTORY_ROAD_1_LINK = WarpLink(
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_VICTORY_ROAD_1_WP,
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_GATE_5_WP,
        "VictoryRoadGate", 20, dual_width=True)

    # VICTORY_ROAD_GATE_TO_ROUTE_28_2_LINK = WarpLink(
    #     Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_ROUTE_28_2_WP,
    #     Route_28_Warp_Points.ROUTE_28_TO_VICTORY_ROAD_GATE_7_WP, #todo - might have to import route 28 (will probably keep route 28 vanilla though)
    #     "VictoryRoadGate", 30, dual_width=True)

class Victory_Road_Links(Enum):

    VICTORY_ROAD_TO_VICTORY_ROAD_GATE_5_LINK = WarpLink(
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_GATE_5_WP,
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_VICTORY_ROAD_1_WP,
        "VictoryRoad")
    #Leaving the interior vanilla
    # VICTORY_ROAD_TO_VICTORY_ROAD_3_LINK = WarpLink(
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_3_WP,
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_2_WP,
    #     "VictoryRoad", 5)
    #
    # VICTORY_ROAD_TO_VICTORY_ROAD_2_LINK = WarpLink(
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_2_WP,
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_3_WP,
    #     "VictoryRoad", 10)
    #
    # VICTORY_ROAD_TO_VICTORY_ROAD_5_LINK = WarpLink(
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_5_WP,
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_4_WP,
    #     "VictoryRoad", 15)
    #
    # VICTORY_ROAD_TO_VICTORY_ROAD_4_LINK = WarpLink(
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_4_WP,
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_5_WP,
    #     "VictoryRoad", 20)
    #
    # VICTORY_ROAD_TO_VICTORY_ROAD_7_LINK = WarpLink(
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_7_WP,
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_6_WP,
    #     "VictoryRoad", 25)
    #
    # VICTORY_ROAD_TO_VICTORY_ROAD_6_LINK = WarpLink(
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_6_WP,
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_7_WP,
    #     "VictoryRoad", 30)
    #
    # VICTORY_ROAD_TO_VICTORY_ROAD_9_LINK = WarpLink(
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_9_WP,
    #     Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_8_WP,
    #     "VictoryRoad", 35)

    VICTORY_ROAD_TO_ROUTE_23_3_LINK = WarpLink(
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_ROUTE_23_3_WP,
        Route23_Warp_Points.ROUTE23_TO_VICTORY_ROAD_10_WP,
        "VictoryRoad", 45)
class Tohjo_Falls_Links(Enum):

    TOHJO_FALLS_TO_ROUTE_27_2_LINK = WarpLink(
        Tohjo_Falls_Warp_Points.TOHJO_FALLS_TO_ROUTE_27_2_WP,
        Route_27_Warp_Points.ROUTE_27_TO_TOHJO_FALLS_1_WP,
        "TohjoFalls")

    TOHJO_FALLS_TO_ROUTE_27_3_LINK = WarpLink(
        Tohjo_Falls_Warp_Points.TOHJO_FALLS_TO_ROUTE_27_3_WP,
        Route_27_Warp_Points.ROUTE_27_TO_TOHJO_FALLS_2_WP,
        "TohjoFalls", 5)

#######################################################################
#                    END OF GROUPS                                    #
#######################################################################