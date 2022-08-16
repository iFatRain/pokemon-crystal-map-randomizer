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
from map_data.Dungeons_Group.NationalParkBugContest_Map import National_Park_Bug_Contest_Warp_Points
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
from map_data.Silver_Group.SilverCaveRoom3_Map import Silver_Cave_Room_3_Warp_Points
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
def buildJohtoWarpLinks():


    Azalea_Gym_Links = dict()
    Azalea_Mart_Links = dict()
    Azalea_Pokecenter_Links = dict()
    Azalea_Town_Links = dict()
    Charcoal_Kiln_Links = dict()
    Kurts_House_Links = dict()
    Blackthorn_City_Links = dict()
    Blackthorn_Dragon_Speech_House_Links = dict()
    Blackthorn_Emys_House_Links = dict()
    Blackthorn_Gym_Links = dict()
    Blackthorn_Mart_Links = dict()
    Blackthorn_Pokecenter_Links = dict()
    Move_Deleters_House_Links = dict()
    Cherrygrove_City_Links = dict()
    Cherrygrove_Pokecenter_Links = dict()
    Cherrygrove_Evolution_Speech_House_Links = dict()
    Cherrygrove_Mart_Links = dict()
    Cherrygrove_Gym_Speech_House_Links = dict()
    Guide_Gents_House_Links = dict()
    Mr_Pokemons_House_Links = dict()
    Route_30_Berry_House_Links = dict()
    Cianwood_City_Links = dict()
    Cianwood_Gym_Links = dict()
    Cianwood_Lugia_Speech_House_Links = dict()
    Cianwood_Pharmacy_Links = dict()
    Cianwood_Pokecenter_Links = dict()
    Manias_House_Links = dict()
    Poke_Seers_House_Links = dict()
    Mount_Mortar_1F_Outside_Links = dict()
    Mount_Mortar_B1F_Links = dict()
    Mount_Mortar_2F_Inside_Links = dict()
    Mount_Mortar_1F_Inside_Links = dict()
    Ice_Path_1F_Links = dict()
    Ice_Path_B1F_Links = dict()
    Ice_Path_B2F_Blackthorn_Side_Links = dict()
    Ice_Path_B3F_Links = dict()
    Ice_Path_B2F_Mahogany_Side_Links = dict()
    Burned_Tower_1F_Links = dict()
    Dark_Cave_Violet_Entrance_Links = dict()
    Dark_Cave_Blackthorn_Entrance_Links = dict()
    Ilex_Forest_Links = dict()
    National_Park_Bug_Contest_Links = dict()
    National_Park_Links = dict()
    Ruins_Of_Alph_Outside_Links = dict()
    Ruins_Of_Alph_Research_Center_Links = dict()
    Ruins_Of_Alph_Inner_Chamber_Links = dict()
    Ruins_Of_Alph_Aerodactyl_Chamber_Links = dict()
    Ruins_Of_Alph_Aerodactyl_Item_Room_Links = dict()
    Ruins_Of_Alph_Ho_Oh_Chamber_Links = dict()
    Ruins_Of_Alph_Ho_Oh_Item_Room_Links = dict()
    Ruins_Of_Alph_Kabuto_Chamber_Links = dict()
    Ruins_Of_Alph_Kabuto_Item_Room_Links = dict()
    Ruins_Of_Alph_Omanyte_Chamber_Links = dict()
    Ruins_Of_Alph_Omanyte_Item_Room_Links = dict()
    Slowpoke_Well_B1F_Links = dict()
    Slowpoke_Well_B2F_Links = dict()
    Dragons_Den_1F_Links = dict()
    Dragons_Den_B1F_Links = dict()
    Dragon_Shrine_Links = dict()
    Sprout_Tower_1F_Links = dict()
    Sprout_Tower_2F_Links = dict()
    Sprout_Tower_3F_Links = dict()
    Tin_Tower_1F_Links = dict()
    Tin_Tower_2F_Links = dict()
    Tin_Tower_3F_Links = dict()
    Tin_Tower_4F_Links = dict()
    Tin_Tower_5F_Links = dict()
    Tin_Tower_6F_Links = dict()
    Tin_Tower_7F_Links = dict()  # 1-2-4 , 3-5
    Tin_Tower_8F_Links = dict()  # 1-2 (left), 3-4 (top) ,5x (bottom) ,6x (middle)
    Tin_Tower_9F_Links = dict()  # 5-6-7, 1-2(top) , 3-4(middle)
    Union_Cave_1F_Links = dict()
    Union_Cave_B1F_Links = dict()
    Union_Cave_B2F_Links = dict()
    Lake_Of_Rage_Links = dict()
    Lake_Of_Rage_Hidden_Power_House_Links = dict()
    Lake_Of_Rage_Magikarp_House_Links = dict()
    Whirl_Island_NW_Links = dict()
    Whirl_Island_NE_Links = dict()
    Whirl_Island_SW_Links = dict()
    Whirl_Island_SE_Links = dict()
    Whirl_Island_Cave_Links = dict()
    Whirl_Island_B1F_Links = dict()
    Whirl_Island_B2F_Links = dict()
    Whirl_Island_Lugia_Chamber_Links = dict()
    Tin_Tower_Roof_Links = dict()
    Dance_Theatre_Links = dict()
    Ecruteak_City_Links = dict()
    Ecruteak_Gym_Links = dict()
    Ecruteak_Item_Finder_House_Links = dict()
    Ecruteak_Lugia_Speech_House_Links = dict()
    Ecruteak_Mart_Links = dict()
    Ecruteak_Pokecenter_Links = dict()
    Ecruteak_Tin_Tower_Entrance_Links = dict()
    Wise_Trios_Room_Links = dict()  # Wise Trio's room unused, bug when early tower in warp rando
    Ilex_Forest_Azalea_Gate_Links = dict()
    Route_29_Route_46_Gate_Links = dict()
    Route_31_Violet_Gate_Links = dict()
    Route_32_Ruins_Of_Alph_Gate_Links = dict()
    Route_34_Ilex_Forest_Gate_Links = dict()
    Route_35_Goldenrod_Gate_Links = dict()
    Route_35_National_Park_Gate_Links = dict()
    Route_36_National_Park_Gate_Links = dict()
    Route_36_Ruins_Of_Alph_Gate_Links = dict()
    Route_38_Ecruteak_Gate_Links = dict()
    Route_42_Ecruteak_Gate_Links = dict()
    Route_43_Gate_Links = dict()
    Route_43_Mahogany_Gate_Links = dict()
    Goldenrod_City_Links = dict()
    Bills_Familys_House_Links = dict()
    Day_Care_Links = dict()
    Goldenrod_Bike_Shop_Links = dict()
    Goldenrod_Dept_Store_B1F_Links = dict()
    Goldenrod_Dept_Store_1F_Links = dict()
    Goldenrod_Dept_Store_2F_Links = dict()
    Goldenrod_Dept_Store_3F_Links = dict()
    Goldenrod_Dept_Store_4F_Links = dict()
    Goldenrod_Dept_Store_5F_Links = dict()
    Goldenrod_Dept_Store_6F_Links = dict()
    Goldenrod_Dept_Store_Roof_Links = dict()
    Goldenrod_Flower_Shop_Links = dict()
    Goldenrod_Game_Corner_Links = dict()
    Goldenrod_Gym_Links = dict()
    Goldenrod_Happiness_Rater_Links = dict()
    Goldenrod_Magnet_Train_Station_Links = dict()
    Goldenrod_Name_Rater_Links = dict()
    Goldenrod_Pokecenter_Links = dict()
    Goldenrod_PP_Speech_House_Links = dict()
    Goldenrod_Underground_Warehouse_Links = dict()
    Goldenrod_Underground_Switch_Room_Entrance_Links = dict()
    Goldenrod_Underground_Links = dict()
    Radio_Tower_1F_Links = dict()
    Kogas_Room_Links = dict()
    Wills_Room_Links = dict()
    Karens_Room_Links = dict()
    Brunos_Room_Links = dict()
    Lances_Room_Links = dict()
    Mahogany_Town_Links = dict()
    Mahogany_Gym_Links = dict()
    Mahogany_Mart_Links = dict()
    Mahogany_Pokecenter_Links = dict()
    Mahogany_Red_Gyarados_Speech_House_Links = dict()
    New_Bark_Links = dict()
    Players_Neighbors_House_Links = dict()
    Elms_House_Links = dict()
    Olivine_City_Links = dict()
    Olivine_Cafe_Links = dict()
    Olivine_Good_Rod_House_Links = dict()
    Olivine_Gym_Links = dict()
    Olivine_Lighthouse_1F_Links = dict()
    Olivine_Lighthouse_2F_Links = dict()
    Olivine_Lighthouse_3F_Links = dict()
    Olivine_Lighthouse_4F_Links = dict()
    Olivine_Lighthouse_5F_Links = dict()
    Olivine_Lighthouse_6F_Links = dict()
    Olivine_Mart_Links = dict()
    Olivine_Pokecenter_Links = dict()
    Olivine_Port_Passage_Links = dict()
    Olivine_Punishment_Speech_House_Links = dict()
    Olivine_Tims_House_Links = dict()
    Indigo_Plateau_Pokecenter_1F_Links = dict()
    Route23_Links = dict()
    Day_Of_Week_Siblings_House_Links = dict()
    Route_26_Heal_House_Links = dict()
    Route_27_Sandstorm_House_Links = dict()
    Route_26_Links = dict()
    Route_27_Links = dict()
    Route_41_Links = dict()
    Route_29_Links = dict()
    Route_30_Links = dict()
    Route_31_Links = dict()
    Route_32_Links = dict()
    Route_32_Pokecenter_Links = dict()
    Route_33_Links = dict()
    Route_34_Links = dict()
    Route_35_Links = dict()
    Route_36_Links = dict()
    Route_38_Links = dict()
    Route_39_Links = dict()
    Route_39_Barn_Links = dict()
    Route_39_Farmhouse_Links = dict()
    Route_40_Links = dict()
    Route_40_Battle_Tower_Gate_Links = dict()
    Battle_Tower_Outside_Links = dict()
    Route_42_Links = dict()
    Route_43_Links = dict()
    Route_44_Links = dict()
    Route_45_Links = dict()
    Route_46_Links = dict()
    Violet_City_Links = dict()
    Earls_Pokemon_Academy_Links = dict()
    Violet_City_Mart_Links = dict()
    Violet_City_Pokecenter_Links = dict()
    Violet_City_Gym_Links = dict()
    Violet_City_Kyles_House_Links = dict()
    Violet_Nickname_Speech_House_Links = dict()
    Victory_Road_Gate_Links = dict()
    Victory_Road_Links = dict()
    Tohjo_Falls_Links = dict()
    

    Azalea_Gym_Links["AZALEA_GYM_TO_AZALEA_TOWN_LINK"] = WarpLink(
        Azalea_Gym_Warp_Points.AZALEA_GYM_TO_AZALEA_TOWN_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_AZALEA_GYM_WP,
        "AzaleaGym", dual_width= True, unlocks=[Unlock_Keys.BADGE_2]
    )


    Azalea_Mart_Links["AZALEA_MART_TO_AZALEA_TOWN_LINK"] = WarpLink(
        Azalea_Mart_Warp_Points.AZALEA_MART_TO_AZALEA_TOWN_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_AZALEA_MART_WP,
        "AzaleaMart", dual_width=True
    )

    

    Azalea_Pokecenter_Links["AZALEA_POKECENTER_TO_AZALEA_TOWN_LINK"] = WarpLink(
        Azalea_Pokecenter_Warp_Points.AZALEA_POKECENTER_TO_AZALEA_TOWN_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_AZALEA_POKECENTER_1F_WP,
        "AzaleaPokecenter1F", dual_width=True
    )
    Azalea_Pokecenter_Links["AZALEA_POKECENTER_1F_TO_AZALEA_POKECENTER_2F_LINK"] = WarpLink(
        Azalea_Pokecenter_Warp_Points.AZALEA_POKECENTER_TO_AZALEA_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "AzaleaPokecenter1F", 10
    )

    

    Azalea_Town_Links["AZALEA_TOWN_TO_AZALEA_POKECENTER_1F_LINK"] = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_AZALEA_POKECENTER_1F_WP,
        Azalea_Pokecenter_Warp_Points.AZALEA_POKECENTER_TO_AZALEA_TOWN_WP,
        "AzaleaTown"
    )

    Azalea_Town_Links["AZALEA_TOWN_TO_CHARCOAL_KILN_LINK"] = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_CHARCOAL_KILN_WP,
        Charcoal_Kiln_Warp_Points.CHARCOAL_KILN_TO_AZALEA_TOWN_WP,
        "AzaleaTown" , 5
    )

    Azalea_Town_Links["AZALEA_TOWN_TO_AZALEA_MART_LINK"] = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_AZALEA_MART_WP,
        Azalea_Mart_Warp_Points.AZALEA_MART_TO_AZALEA_TOWN_WP,
        "AzaleaTown" , 10
    )

    Azalea_Town_Links["AZALEA_TOWN_TO_KURTS_LINK"] = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_KURTS_HOUSE_WP,
        Kurts_House_Warp_Points.KURTS_HOUSE_TO_AZALEA_TOWN_WP,
        "AzaleaTown" , 15
    )

    Azalea_Town_Links["AZALEA_TOWN_TO_AZALEA_GYM_LINK"] = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_AZALEA_GYM_WP,
        Azalea_Gym_Warp_Points.AZALEA_GYM_TO_AZALEA_TOWN_WP,
        "AzaleaTown" , 20, locked_by=[Unlock_Keys.CAN_CLEAR_SLOWPOKE_WELL]
    )

    Azalea_Town_Links["AZALEA_TOWN_TO_SLOWPOKE_WELL_B1F_LINK"] = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_SLOWPOKE_WELL_B1F_WP,
        Slowpoke_Well_B1F_Warp_Points.SLOWPOKE_WELL_B1F_TO_AZALEA_TOWN_6_WP,
        "AzaleaTown" , 25, locked_by=[Unlock_Keys.KURTS_HOUSE_FOUND]
    )


    Azalea_Town_Links["AZALEA_TOWN_TO_ILEX_FOREST_AZALEA_GATE_LINK"] = WarpLink(
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_ILEX_FOREST_AZALEA_GATE_WP,
        Ilex_Forest_Azalea_Gate_Warp_Points.ILEX_FOREST_AZALEA_GATE_TO_AZALEA_TOWN_WP,
        "AzaleaTown" , 30, dual_width=True
    )

    

    Charcoal_Kiln_Links["CHARCOAL_KILN_TO_AZALEA_TOWN_LINK"] = WarpLink(
        Charcoal_Kiln_Warp_Points.CHARCOAL_KILN_TO_AZALEA_TOWN_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_CHARCOAL_KILN_WP,
        "CharcoalKiln", dual_width=True
    )

    

    Kurts_House_Links["KURTS_HOUSE_TO_AZALEA_TOWN_LINK"] = WarpLink(
        Kurts_House_Warp_Points.KURTS_HOUSE_TO_AZALEA_TOWN_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_KURTS_HOUSE_WP,
        "KurtsHouse", dual_width=True, unlocks=[Unlock_Keys.KURTS_HOUSE_FOUND]
    )


#######################################################################
#                    Blackthorn Group                                 #
#######################################################################
    

    Blackthorn_City_Links["BLACKTHORN_CITY_TO_BLACKTHORN_GYM_1F_LINK"] = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_GYM_1F_WP,
        Blackthorn_Gym_1F_Warp_Points.BLACKTHORN_GYM_1F_TO_BLACKTHORN_CITY_WP,
        "BlackthornCity", locked_by=[Unlock_Keys.CAN_CLEAR_RADIO_TOWER_ROCKETS],
    )

    Blackthorn_City_Links["BLACKTHORN_CITY_TO_BLACKTHORN_DRAGON_SPEECH_HOUSE_LINK"] = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_DRAGON_SPEECH_HOUSE_WP,
        Blackthorn_Dragon_Speech_House_Warp_Points.BLACKTHORN_DRAGON_SPEECH_HOUSE_TO_BLACKTHORN_CITY_WP,
        "BlackthornCity" , 5
    )

    Blackthorn_City_Links["BLACKTHORN_CITY_TO_BLACKTHORN_EMYS_HOUSE_LINK"] = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_EMYS_HOUSE_WP,
        Blackthorn_Emys_House_Warp_Points.BLACKTHORN_EMYS_HOUSE_TO_BLACKTHORN_CITY_WP,
        "BlackthornCity" , 10
    )

    Blackthorn_City_Links["BLACKTHORN_CITY_TO_BLACKTHORN_MART_LINK"] = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_MART_WP,
        Blackthorn_Mart_Warp_Points.BLACKTHORN_MART_TO_BLACKTHORN_CITY_WP,
        "BlackthornCity" , 15
    )

    Blackthorn_City_Links["BLACKTHORN_CITY_TO_BLACKTHORN_POKECENTER_1F_LINK"] = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_POKECENTER_1F_WP,
        Blackthorn_Pokecenter_Warp_Points.BLACKTHORN_POKECENTER_1F_TO_BLACKTHORN_CITY_WP,
        "BlackthornCity" , 20
    )

    Blackthorn_City_Links["BLACKTHORN_CITY_TO_MOVE_DELETERS_HOUSE_LINK"] = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_MOVE_DELETERS_HOUSE_WP,
        Move_Deleters_House_Warp_Points.MOVE_DELETERS_HOUSE_TO_BLACKTHORN_CITY_WP,
        "BlackthornCity" , 25
    )

    Blackthorn_City_Links["BLACKTHORN_CITY_TO_ICE_PATH_1F_LINK"] = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_ICE_PATH_1F_WP,
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_BLACKTHORN_CITY_7_WP,
        "BlackthornCity" , 30
    )

    Blackthorn_City_Links["BLACKTHORN_CITY_TO_DRAGONS_DEN_1F_LINK"] = WarpLink(
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_DRAGONS_DEN_1F_WP,
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_BLACKTHORN_CITY_8_WP,
        "BlackthornCity" , 35, locked_by=[Unlock_Keys.GYM_BATTLE_8, Unlock_Keys.CAN_SURF]
    )

    

    Blackthorn_Dragon_Speech_House_Links["BLACKTHORN_DRAGON_SPEECH_HOUSE_TO_BLACKTHORN_CITY_LINK"] = WarpLink(
        Blackthorn_Dragon_Speech_House_Warp_Points.BLACKTHORN_DRAGON_SPEECH_HOUSE_TO_BLACKTHORN_CITY_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_DRAGON_SPEECH_HOUSE_WP,
        "BlackthornDragonSpeechHouse", dual_width=True
    )

    

    Blackthorn_Emys_House_Links["BLACKTHORN_EMYS_HOUSE_TO_BLACKTHORN_CITY_LINK"] = WarpLink(
        Blackthorn_Emys_House_Warp_Points.BLACKTHORN_EMYS_HOUSE_TO_BLACKTHORN_CITY_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_EMYS_HOUSE_WP,
        "BlackthornEmysHouse", dual_width=True
    )

    

    Blackthorn_Gym_Links["BLACKTHORN_GYM_1F_TO_BLACKTHORN_CITY_LINK"] = WarpLink(
        Blackthorn_Gym_1F_Warp_Points.BLACKTHORN_GYM_1F_TO_BLACKTHORN_CITY_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_GYM_1F_WP,
        "BlackthornGym1F", dual_width=True, unlocks=[Unlock_Keys.GYM_BATTLE_8],
        locked_by=[Unlock_Keys.CAN_USE_STRENGTH]
    )

    

    Blackthorn_Mart_Links["BLACKTHORN_MART_TO_BLACKTHORN_CITY_LINK"] = WarpLink(
        Blackthorn_Mart_Warp_Points.BLACKTHORN_MART_TO_BLACKTHORN_CITY_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_MART_WP,
        "BlackthornMart", dual_width=True
    )

    

    Blackthorn_Pokecenter_Links["BLACKTHORN_POKECENTER_1F_TO_BLACKTHORN_CITY_LINK"] = WarpLink(
        Blackthorn_Pokecenter_Warp_Points.BLACKTHORN_POKECENTER_1F_TO_BLACKTHORN_CITY_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_BLACKTHORN_POKECENTER_1F_WP,
        "BlackthornPokecenter1F", dual_width=True
    )

    Blackthorn_Pokecenter_Links["BLACKTHORN_POKECENTER_1F_TO_BLACKTHORN_POKECENTER_2F_LINK"] = WarpLink(
        Blackthorn_Pokecenter_Warp_Points.BLACKTHORN_POKECENTER_TO_BLACKTHORN_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "BlackthornPokecenter1F", 10
    )

    

    Move_Deleters_House_Links["MOVE_DELETERS_HOUSE_TO_BLACKTHORN_CITY_LINK"] = WarpLink(
        Move_Deleters_House_Warp_Points.MOVE_DELETERS_HOUSE_TO_BLACKTHORN_CITY_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_MOVE_DELETERS_HOUSE_WP,
        "MoveDeletersHouse", dual_width=True
    )

#######################################################################
#                    Cherrywood Group                                 #
#######################################################################
    

    Cherrygrove_City_Links["CHERRYGROVE_CITY_TO_CHERRYGROVE_MART_LINK"] = WarpLink(
        Cherrygrove_City_Warp_Points.Cherrygrove_City_Mart_Entrance_WP,
        Cherrygrove_Mart_Warp_Points.Cherrygrove_City_Mart_Exit_WP,
        "CherrygroveCity"
    )

    Cherrygrove_City_Links["CHERRYGROVE_CITY_TO_CHERRYGROVE_POKECENTER_1F_LINK"] = WarpLink(
        Cherrygrove_City_Warp_Points.Cherrygrove_City_Pokecenter_Entrance_WP,
        Cherrygrove_Pokecenter_Warp_Points.Cherrygrove_Pokecenter_Exit_WP,
        "CherrygroveCity" , 5
    )

    Cherrygrove_City_Links["CHERRYGROVE_CITY_TO_CHERRYGROVE_GYM_SPEECH_HOUSE_LINK"] = WarpLink(
        Cherrygrove_City_Warp_Points.Cherrygrove_City_West_House_Entrance_WP,
        Cherrygrove_Gym_Speech_House_Warp_Points.Cherrygrove_City_West_House_Exit_WP,
        "CherrygroveCity" , 10
    )

    Cherrygrove_City_Links["CHERRYGROVE_CITY_TO_GUIDE_GENTS_HOUSE_LINK"] = WarpLink(
        Cherrygrove_City_Warp_Points.Cherrygrove_City_Guide_Gents_House_Entrance_WP,
        Guide_Gents_House_Warp_Points.Cherrygrove_City_Guide_Gents_House_Exit_WP,
        "CherrygroveCity" , 15
    )

    Cherrygrove_City_Links["CHERRYGROVE_CITY_TO_CHERRYGROVE_EVOLUTION_SPEECH_HOUSE_LINK"] = WarpLink(
        Cherrygrove_City_Warp_Points.Cherrygrove_City_East_House_Entrance_WP,
        Cherrygrove_Evolution_Speech_House_Warp_Points.Cherrygrove_City_East_House_Exit_WP,
        "CherrygroveCity" , 20
)

    

    Cherrygrove_Pokecenter_Links["CHERRYGROVE_POKECENTER_TO_CHERRYGROVE_CITY_LINK"] = WarpLink(
        Cherrygrove_Pokecenter_Warp_Points.Cherrygrove_Pokecenter_Exit_WP,
        Cherrygrove_City_Warp_Points.Cherrygrove_City_Pokecenter_Entrance_WP,
        "CherrygrovePokecenter1F",
        dual_width=True
    )

    Cherrygrove_Pokecenter_Links["CHERRYGROVE_POKECENTER_TO_CHERRYGROVE_POKECENTER_2F_LINK"] = WarpLink(
        Cherrygrove_Pokecenter_Warp_Points.Cherrygrove_Pokecenter_Stairs_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "CherrygrovePokecenter1F", 10
    )

    

    Cherrygrove_Evolution_Speech_House_Links["CHERRYGROVE_EVOLUTION_SPEECH_HOUSE_TO_CHERRYGROVE_CITY_LINK"] = WarpLink(
        Cherrygrove_Evolution_Speech_House_Warp_Points.Cherrygrove_City_East_House_Exit_WP,
        Cherrygrove_City_Warp_Points.Cherrygrove_City_East_House_Entrance_WP,
        "CherrygroveEvolutionSpeechHouse",
        dual_width=True
    )

    

    Cherrygrove_Mart_Links["CHERRYGROVE_MART_TO_CHERRYGROVE_CITY_LINK"] = WarpLink(
        Cherrygrove_Mart_Warp_Points.Cherrygrove_City_Mart_Exit_WP,
        Cherrygrove_City_Warp_Points.Cherrygrove_City_Mart_Entrance_WP,
        "CherrygroveMart",
        dual_width=True
    )

    

    Cherrygrove_Gym_Speech_House_Links["CHERRYGROVE_GYM_SPEECH_HOUSE_TO_CHERRYGROVE_CITY_LINK"] = WarpLink(
        Cherrygrove_Gym_Speech_House_Warp_Points.Cherrygrove_City_West_House_Exit_WP,
        Cherrygrove_City_Warp_Points.Cherrygrove_City_West_House_Entrance_WP,
        "CherrygroveGymSpeechHouse",
        dual_width=True
    )

    

    Guide_Gents_House_Links["GUIDE_GENTS_HOUSE_TO_CHERRYGROVE_CITY_LINK"] = WarpLink(
        Guide_Gents_House_Warp_Points.Cherrygrove_City_Guide_Gents_House_Exit_WP,
        Cherrygrove_City_Warp_Points.Cherrygrove_City_Guide_Gents_House_Entrance_WP,
        "GuideGentsHouse",
        dual_width=True
    )

    

    Mr_Pokemons_House_Links["MR_POKEMONS_HOUSE_TO_ROUTE_30_LINK"] = WarpLink(
        Mr_Pokemons_House_Warp_Points.MR_POKEMONS_HOUSE_EXIT_WP,
        Route_30_Warp_Points.MR_POKEMONS_HOUSE_ENTRANCE_WP,
        "MrPokemonsHouse",
        dual_width=True
    )

    

    Route_30_Berry_House_Links["ROUTE_30_BERRY_HOUSE_TO_ROUTE_30_LINK"] = WarpLink(
        Route_30_Berry_House_Warp_Points.ROUTE_30_BERRY_HOUSE_EXIT_WP,
        Route_30_Warp_Points.ROUTE_30_BERRY_HOUSE_ENTRANCE_WP,
        "Route30BerryHouse",
        dual_width=True
    )

#######################################################################
#                    Cianwood Group                                   #
#######################################################################
    

    Cianwood_City_Links["CIANWOOD_CITY_TO_MANIAS_HOUSE_LINK"] = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_MANIAS_HOUSE_WP,
        Manias_House_Warp_Points.MANIAS_HOUSE_TO_CIANWOOD_CITY_WP,
        "CianwoodCity",unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )
    Cianwood_City_Links["CIANWOOD_CITY_TO_CIANWOOD_GYM_LINK"] = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_GYM_WP,
        Cianwood_Gym_Warp_Points.CIANWOOD_GYM_TO_CIANWOOD_CITY_WP,
        "CianwoodCity" , 5,unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )
    Cianwood_City_Links["CIANWOOD_CITY_TO_CIANWOOD_POKECENTER_1F_LINK"] = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_POKECENTER_1F_WP,
        Cianwood_Pokecenter_Warp_Points.CIANWOOD_POKECENTER_1F_TO_CIANWOOD_CITY_WP,
        "CianwoodCity" , 10,unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )
    Cianwood_City_Links["CIANWOOD_CITY_TO_CIANWOOD_PHARMACY_LINK"] = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_PHARMACY_WP,
        Cianwood_Pharmacy_Warp_Points.CIANWOOD_PHARMACY_TO_CIANWOOD_CITY_WP,
        "CianwoodCity" , 15,unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )
    Cianwood_City_Links["CIANWOOD_CITY_TO_CIANWOOD_PHOTO_STUDIO_LINK"] = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_PHOTO_STUDIO_WP,
        Cianwood_Photo_Studio_Warp_Points.CIANWOOD_PHOTO_STUDIO_TO_CIANWOOD_CITY_WP,
        "CianwoodCity" , 20,unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )
    Cianwood_City_Links["CIANWOOD_CITY_TO_CIANWOOD_LUGIA_SPEECH_HOUSE_LINK"] = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_LUGIA_SPEECH_HOUSE_WP,
        Cianwood_Lugia_Speech_House_Warp_Points.CIANWOOD_LUGIA_SPEECH_HOUSE_TO_CIANWOOD_CITY_WP,
        "CianwoodCity" , 25,unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )
    Cianwood_City_Links["CIANWOOD_CITY_TO_POKE_SEERS_HOUSE_LINK"] = WarpLink(
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_POKE_SEERS_HOUSE_WP,
        Poke_Seers_House_Warp_Points.POKE_SEERS_HOUSE_TO_CIANWOOD_CITY_WP,
        "CianwoodCity" , 30,unlocks=[Unlock_Keys.FOUND_CIANWOOD]
    )

    

    Cianwood_Gym_Links["CIANWOOD_GYM_TO_CIANWOOD_CITY_LINK"] = WarpLink(
        Cianwood_Gym_Warp_Points.CIANWOOD_GYM_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_GYM_WP,
        "CianwoodGym", dual_width=True, unlocks=[Unlock_Keys.BADGE_5],
        locked_by=[Unlock_Keys.CAN_USE_STRENGTH]
    )

    

    Cianwood_Lugia_Speech_House_Links["CIANWOOD_LUGIA_SPEECH_HOUSE_TO_CIANWOOD_CITY_LINK"] = WarpLink(
        Cianwood_Lugia_Speech_House_Warp_Points.CIANWOOD_LUGIA_SPEECH_HOUSE_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_LUGIA_SPEECH_HOUSE_WP,
        "CianwoodLugiaSpeechHouse", dual_width=True
    )

    

    Cianwood_Pharmacy_Links["CIANWOOD_PHARMACY_TO_CIANWOOD_CITY_LINK"] = WarpLink(
        Cianwood_Pharmacy_Warp_Points.CIANWOOD_PHARMACY_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_PHARMACY_WP,
        "CianwoodPharmacy", dual_width=True, unlocks=[Unlock_Keys.CIANNWOOD_PHARMACY_FOUND]
    )

    # 
    # Cianwood_Photo_Studio_Links["CIANWOOD_PHOTO_STUDIO_TO_CIANWOOD_CITY_LINK"] = WarpLink(
    #     Cianwood_Photo_Studio_Warp_Points.CIANWOOD_PHOTO_STUDIO_TO_CIANWOOD_CITY_WP,
    #     Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_PHOTO_STUDIO_WP,
    #     "CianwoodPhotoStudio", dual_width=True
    # )

    

    Cianwood_Pokecenter_Links["Cianwood_Pokecenter_LinksCIANWOOD_POKECENTER_1F_TO_CIANWOOD_CITY_LINK"] = WarpLink(
        Cianwood_Pokecenter_Warp_Points.CIANWOOD_POKECENTER_1F_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_CIANWOOD_POKECENTER_1F_WP,
        "CianwoodPokecenter1F", dual_width=True
    )

    Cianwood_Pokecenter_Links["CIANWOOD_POKECENTER_1F_TO_CIANWOOD_POKECENTER_2F_LINK"] = WarpLink(
        Cianwood_Pokecenter_Warp_Points.CIANWOOD_POKECENTER_TO_CIANWOOD_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "CianwoodPokecenter1F", 10
    )

    

    Manias_House_Links["MANIAS_HOUSE_TO_CIANWOOD_CITY"] = WarpLink(
        Manias_House_Warp_Points.MANIAS_HOUSE_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_MANIAS_HOUSE_WP,
        "ManiasHouse", dual_width=True
    )

    

    Poke_Seers_House_Links["POKE_SEERS_HOUSE_TO_CIANWOOD_CITY_LINK"] = WarpLink(
        Poke_Seers_House_Warp_Points.POKE_SEERS_HOUSE_TO_CIANWOOD_CITY_WP,
        Cianwood_City_Warp_Points.CIANWOOD_CITY_TO_POKE_SEERS_HOUSE_WP,
        "PokeSeersHouse", dual_width=True
    )


#######################################################################
#                    Dungeons Group                                   #
#######################################################################
    
    Mount_Mortar_1F_Outside_Links["MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_3_LINK"] = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_3_WP,
        Route_42_Warp_Points.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_LEFT_WP,
        "MountMortar1FOutside"
    )

    Mount_Mortar_1F_Outside_Links["MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_4_LINK"] = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_4_WP,
        Route_42_Warp_Points.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_MIDDLE_WP,
        "MountMortar1FOutside",5
    )

    Mount_Mortar_1F_Outside_Links["MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_5_LINK"] = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_5_WP,
        Route_42_Warp_Points.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_RIGHT_WP,
        "MountMortar1FOutside",10
    )

    Mount_Mortar_1F_Outside_Links["MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_2F_INSIDE_1_LINK"] = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_2F_INSIDE_1_WP,
        Mount_Mortar_2F_Inside_Warp_Points.MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_4_WP,
        "MountMortar1FOutside",15
    )

    Mount_Mortar_1F_Outside_Links["MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_1_LINK"] = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_1_WP,
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_5_WP,
        "MountMortar1FOutside",20
    )

    Mount_Mortar_1F_Outside_Links["MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_2_LINK"] = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_2_WP,
    Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_6_WP,
        "MountMortar1FOutside",25
    )

    Mount_Mortar_1F_Outside_Links["MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_B1F_2_LINK"] = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_B1F_2_WP,
        Mount_Mortar_B1F_Warp_Points.MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_OUTSIDE_7_WP,
        "MountMortar1FOutside",30
    )

    Mount_Mortar_1F_Outside_Links["MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_3_LINK"] = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_3_WP,
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_8_WP,
        "MountMortar1FOutside",35
    )

    Mount_Mortar_1F_Outside_Links["MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_4_LINK"] = WarpLink(
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_4_WP,
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_9_WP,
        "MountMortar1FOutside",40
    )

    
    Mount_Mortar_B1F_Links["MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_INSIDE_5_LINK"] = WarpLink(
        Mount_Mortar_B1F_Warp_Points.MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_INSIDE_5_WP,
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_B1F_1_WP,
        "MountMortarB1F"
    )

    Mount_Mortar_B1F_Links["MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_OUTSIDE_7_LINK"] = WarpLink(
        Mount_Mortar_B1F_Warp_Points.MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_OUTSIDE_7_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_B1F_2_WP,
        "MountMortarB1F",5
    )

    

    Mount_Mortar_2F_Inside_Links["MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_4_LINK"] = WarpLink(
        Mount_Mortar_2F_Inside_Warp_Points.MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_4_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_2F_INSIDE_1_WP,
        "MountMortar2FInside"
    )

    Mount_Mortar_2F_Inside_Links["MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_INSIDE_6_LINK"] = WarpLink(
        Mount_Mortar_2F_Inside_Warp_Points.MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_INSIDE_6_WP,
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_2F_INSIDE_2_WP,
        "MountMortar2FInside", 5
    )

    
    Mount_Mortar_1F_Inside_Links["MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_5_LINK"] = WarpLink(
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_5_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_1_WP,
        "MountMortar1FInside"
    )

    Mount_Mortar_1F_Inside_Links["MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_6_LINK"] = WarpLink(
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_6_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_2_WP,
        "MountMortar1FInside",5
    )

    Mount_Mortar_1F_Inside_Links["MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_8_LINK"] = WarpLink(
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_8_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_3_WP,
        "MountMortar1FInside",10
    )

    Mount_Mortar_1F_Inside_Links["MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_9_LINK"] = WarpLink(
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_9_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_4_WP,
        "MountMortar1FInside",15
    )

    Mount_Mortar_1F_Inside_Links["MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_B1F_1_LINK"] = WarpLink(
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_B1F_1_WP,
        Mount_Mortar_B1F_Warp_Points.MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_INSIDE_5_WP,
        "MountMortar1FInside",20
    )

    Mount_Mortar_1F_Inside_Links["MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_2F_INSIDE_2_LINK"] = WarpLink(
        Mount_Mortar_1F_Inside_Warp_Points.MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_2F_INSIDE_2_WP,
        Mount_Mortar_2F_Inside_Warp_Points.MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_INSIDE_6_WP,
        "MountMortar1FInside",25
    )


    
    Ice_Path_1F_Links["ICE_PATH_1F_TO_ROUTE_44_1_LINK"] = WarpLink(
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_ROUTE_44_1_WP,
        Route_44_Warp_Points.ROUTE_44_TO_ICE_PATH_1F_WP,
        "IcePath1F", unlocks=[Unlock_Keys.HM_WATERFALL]
    )

    Ice_Path_1F_Links["ICE_PATH_1F_TO_BLACKTHORN_CITY_7_LINK"] = WarpLink(
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_BLACKTHORN_CITY_7_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_ICE_PATH_1F_WP,
        "IcePath1F", 5
    )

    Ice_Path_1F_Links["ICE_PATH_1F_TO_ICE_PATH_B1F_1_LINK"] = WarpLink(
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_ICE_PATH_B1F_1_WP,
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_1F_3_WP,
        "IcePath1F", 10, unlocks=[Unlock_Keys.HM_WATERFALL]
    )

    Ice_Path_1F_Links["ICE_PATH_1F_TO_ICE_PATH_B1F_7_LINK"] = WarpLink(
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_ICE_PATH_B1F_7_WP,
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_1F_4_WP,
        "IcePath1F", 15
    )


    
    Ice_Path_B1F_Links["ICE_PATH_B1F_TO_ICE_PATH_1F_3_LINK"] = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_1F_3_WP,
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_ICE_PATH_B1F_1_WP,
        "IcePathB1F"
    )

    Ice_Path_B1F_Links["ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_1_LINK"] = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_1_WP,
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_2_WP,
        "IcePathB1F", 5
    )

    Ice_Path_B1F_Links["ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_3_LINK"] = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_3_WP,
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_3_WP,
        "IcePathB1F", 10
    )

    Ice_Path_B1F_Links["ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_4_LINK"] = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_4_WP,
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_4_WP,
        "IcePathB1F", 15
    )

    Ice_Path_B1F_Links["ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_5_LINK"] = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_5_WP,
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_5_WP,
        "IcePathB1F", 20
    )

    Ice_Path_B1F_Links["ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_6_LINK"] = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_6_WP,
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_6_WP,
        "IcePathB1F", 25
    )

    Ice_Path_B1F_Links["ICE_PATH_B1F_TO_ICE_PATH_1F_4_LINK"] = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_1F_4_WP,
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_ICE_PATH_B1F_7_WP,
        "IcePathB1F",30
    )

    Ice_Path_B1F_Links["ICE_PATH_B1F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_1_LINK"] = WarpLink(
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_1_WP,
        Ice_Path_B2F_Blackthorn_Side_Warp_Points.ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B1F_8_WP,
        "IcePathB1F",35
    )

    
    Ice_Path_B2F_Blackthorn_Side_Links["ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B1F_8_LINK"] = WarpLink(
        Ice_Path_B2F_Blackthorn_Side_Warp_Points.ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B1F_8_WP,
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_1_WP,
        "IcePathB2FBlackthornSide"
    )

    Ice_Path_B2F_Blackthorn_Side_Links["ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B3F_2_LINK"] = WarpLink(
        Ice_Path_B2F_Blackthorn_Side_Warp_Points.ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B3F_2_WP,
        Ice_Path_B3F_Warp_Points.ICE_PATH_B3F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_2_WP,
        "IcePathB2FBlackthornSide",5
    )

    
    Ice_Path_B3F_Links["ICE_PATH_B3F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_2_LINK"] = WarpLink(
        Ice_Path_B3F_Warp_Points.ICE_PATH_B3F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_2_WP,
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B3F_1_WP,
        "IcePathB3F"
    )

    Ice_Path_B3F_Links["ICE_PATH_B3F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_2_LINK"] = WarpLink(
        Ice_Path_B3F_Warp_Points.ICE_PATH_B3F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_2_WP,
        Ice_Path_B2F_Blackthorn_Side_Warp_Points.ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B3F_2_WP,
        "IcePathB3F",5
    )

    

    Ice_Path_B2F_Mahogany_Side_Links["ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_2_LINK"] = WarpLink(
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_2_WP,
        Ice_Path_B1F_Warp_Points.ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_1_WP,
        "IcePathB2FMahoganySide"
    )

    Ice_Path_B2F_Mahogany_Side_Links["ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B3F_1_LINK"] = WarpLink(
        Ice_Path_B2F_Mahogany_Side_Warp_Points.ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B3F_1_WP,
        Ice_Path_B3F_Warp_Points.ICE_PATH_B3F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_2_WP,
        "IcePathB2FMahoganySide",5
    )



    
    Burned_Tower_1F_Links["BURNED_TOWER_1F_TO_ECRUTEAK_CITY_LINK"] = WarpLink(
        Burned_Tower_1F_Warp_Points.BURNED_TOWER_1F_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_BURNED_TOWER_1F_WP,
        "BurnedTower1F", dual_width=True, unlocks=[Unlock_Keys.ENTERED_BURNED_TOWER]
    )

    # BURNED_TOWER_1F_TO_BURNED_TOWER_B1F_LINK"] = WarpLink(
    #     Burned_Tower_1F_Warp_Points.BURNED_TOWER_1F_TO_BURNED_TOWER_B1F_WP,
    #
    #     0x001860B7 , 10
    # )


    
    Dark_Cave_Violet_Entrance_Links["DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_31_LINK"] = WarpLink(
        Dark_Cave_Violet_Entrance_Warp_Points.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_31_WP,
        Route_31_Warp_Points.ROUTE_31_TO_DARK_CAVE_VIOLET_ENTRANCE_WP,
        "DarkCaveVioletEntrance",
    )

    Dark_Cave_Violet_Entrance_Links["DARK_CAVE_VIOLET_ENTRANCE_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_LINK"] = WarpLink(
        Dark_Cave_Violet_Entrance_Warp_Points.DARK_CAVE_VIOLET_ENTRANCE_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_WP,
        Dark_Cave_Blackthorn_Entrance_Warp_Points.DARK_CAVE_BLACKTHORN_ENTRANCE_TO_DARK_CAVE_VIOLET_ENTRANCE_WP,
        "DarkCaveVioletEntrance", 5
    ) #todo add rocksmash as a key, and determine where unlocks for it exist

    Dark_Cave_Violet_Entrance_Links["DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_46_LINK"] = WarpLink(
        Dark_Cave_Violet_Entrance_Warp_Points.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_46_WP,
        Route_46_Warp_Points.ROUTE_46_TO_DARK_CAVE_VIOLET_ENTRANCE_WP,
        "DarkCaveVioletEntrance" , 10
    )

    
    Dark_Cave_Blackthorn_Entrance_Links["DARK_CAVE_BLACKTHORN_ENTRANCE_TO_ROUTE_45_LINK"] = WarpLink(
        Dark_Cave_Blackthorn_Entrance_Warp_Points.DARK_CAVE_BLACKTHORN_ENTRANCE_TO_ROUTE_45_WP,
        Route_45_Warp_Points.ROUTE_45_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_WP,
        "DarkCaveBlackthornEntrance"
    )

    Dark_Cave_Blackthorn_Entrance_Links["DARK_CAVE_BLACKTHORN_ENTRANCE_TO_DARK_CAVE_VIOLET_ENTRANCE_LINK"] = WarpLink(
        Dark_Cave_Blackthorn_Entrance_Warp_Points.DARK_CAVE_BLACKTHORN_ENTRANCE_TO_DARK_CAVE_VIOLET_ENTRANCE_WP,
        Dark_Cave_Violet_Entrance_Warp_Points.DARK_CAVE_VIOLET_ENTRANCE_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_WP,
        "DarkCaveBlackthornEntrance",5
    )


    
    Ilex_Forest_Links["ILEX_FOREST_TO_ROUTE_34_ILEX_FOREST_GATE_LINK"] = WarpLink(
        Ilex_Forest_Warp_Points.ILEX_FOREST_TO_ROUTE_34_ILEX_FOREST_GATE_WP,
        Route_34_Ilex_Forest_Gate_Warp_Points.ROUTE_34_ILEX_FOREST_GATE_TO_ILEX_FOREST_WP,
        "IlexForest"
    )

    Ilex_Forest_Links["ILEX_FOREST_TO_ILEX_FOREST_AZALEA_GATE_LINK"] = WarpLink(
        Ilex_Forest_Warp_Points.ILEX_FOREST_TO_ILEX_FOREST_AZALEA_GATE_WP,
        Ilex_Forest_Azalea_Gate_Warp_Points.ILEX_FOREST_AZALEA_GATE_TO_ILEX_FOREST_WP,
        "IlexForest" , 5, dual_width=True, locked_by=[Unlock_Keys.CAN_CLEAR_SLOWPOKE_WELL],
     unlocks=[Unlock_Keys.HM_CUT]
    )

# This     is unused and unneeded at present. Vanilla Bug Contest,
# Can only be entered/exited from Rt36/Nat Gate
#     
#     National_Park_Bug_Contest_Links["NATIONAL_PARK_TO_ROUTE_36_NATIONAL_PARK_GATE_LINK"] = WarpLink(
#         National_Park_Bug_Contest_Warp_Points.NATIONAL_PARK_BUG_CONTEST_TO_ROUTE_36_NATIONAL_PARK_GATE_1_WP,
#         Route_36_National_Park_Gate_Warp_Points.ROUTE_36_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_WP,
#         "NationalParkBugContest", dual_width=True
#     )
#
#     National_Park_Bug_Contest_Links["NATIONAL_PARK_TO_ROUTE_35_NATIONAL_PARK_GATE_LINK"] = WarpLink(
#         National_Park_Bug_Contest_Warp_Points.NATIONAL_PARK_BUG_CONTEST_TO_ROUTE_35_NATIONAL_PARK_GATE_1_WP,
#         Route_35_National_Park_Gate_Warp_Points.ROUTE_35_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_WP,
#         "NationalParkBugContest", 10, dual_width=True
#     )


    
    National_Park_Links["NATIONAL_PARK_TO_ROUTE_36_NATIONAL_PARK_GATE_LINK"] = WarpLink(
        National_Park_Warp_Points.NATIONAL_PARK_TO_ROUTE_36_NATIONAL_PARK_GATE_WP,
        Route_36_National_Park_Gate_Warp_Points.ROUTE_36_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_WP,
        "NationalPark", dual_width=True
    )

    National_Park_Links["NATIONAL_PARK_TO_ROUTE_35_NATIONAL_PARK_GATE_LINK"] = WarpLink(
        National_Park_Warp_Points.NATIONAL_PARK_TO_ROUTE_35_NATIONAL_PARK_GATE_WP,
        Route_35_National_Park_Gate_Warp_Points.ROUTE_35_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_WP,
        "NationalPark" , 10, dual_width=True
    )

    
    Ruins_Of_Alph_Outside_Links["RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_1_WP,
        Ruins_Of_Alph_Ho_Oh_Chamber_Warp_Points.RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_1_WP,
        "RuinsOfAlphOutside"
    )

    Ruins_Of_Alph_Outside_Links["RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_KABUTO_CHAMBER_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_KABUTO_CHAMBER_1_WP,
        Ruins_Of_Alph_Kabuto_Chamber_Warp_Points.RUINS_OF_ALPH_KABUTO_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_2_WP,
        "RuinsOfAlphOutside",5
    )

    Ruins_Of_Alph_Outside_Links["RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_OMANYTE_CHAMBER_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_OMANYTE_CHAMBER_1_WP,
        Ruins_Of_Alph_Omanyte_Chamber_Warp_Points.RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_3_WP,
        "RuinsOfAlphOutside",10
    )

    Ruins_Of_Alph_Outside_Links["RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_AERODACTYL_CHAMBER_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_AERODACTYL_CHAMBER_1_WP,
        Ruins_Of_Alph_Aerodactyl_Chamber_Warp_Points.RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_4_WP,
        "RuinsOfAlphOutside", 15
    )

    Ruins_Of_Alph_Outside_Links["RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_INNER_CHAMBER_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_INNER_CHAMBER_1_WP,
        Ruins_Of_Alph_Inner_Chamber_Warp_Points.RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_WP,
        "RuinsOfAlphOutside", 20
    )

    Ruins_Of_Alph_Outside_Links["RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_RESEARCH_CENTER_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_RESEARCH_CENTER_1_WP,
        Ruins_Of_Alph_Research_Center_Warp_Points.RUINS_OF_ALPH_RESEARCH_CENTER_TO_RUINS_OF_ALPH_OUTSIDE_WP,
        "RuinsOfAlphOutside",25
    )

    Ruins_Of_Alph_Outside_Links["RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_1_WP,
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_7_WP,
        "RuinsOfAlphOutside",30
    )

    Ruins_Of_Alph_Outside_Links["RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_2_LINK"] = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_2_WP,
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_8_WP,
        "RuinsOfAlphOutside",35
    )

    Ruins_Of_Alph_Outside_Links["RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_36_RUINS_OF_ALPH_GATE_3_LINK"] = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_36_RUINS_OF_ALPH_GATE_3_WP,
        Route_36_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_36_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_WP,
        "RuinsOfAlphOutside",40
    )

    Ruins_Of_Alph_Outside_Links["RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_32_RUINS_OF_ALPH_GATE_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_32_RUINS_OF_ALPH_GATE_1_WP,
        Route_32_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_32_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_WP,
        "RuinsOfAlphOutside",45, dual_width=True
    )



    
    Ruins_Of_Alph_Research_Center_Links["RUINS_OF_ALPH_RESEARCH_CENTER_TO_RUINS_OF_ALPH_OUTSIDE_LINK"] = WarpLink(
        Ruins_Of_Alph_Research_Center_Warp_Points.RUINS_OF_ALPH_RESEARCH_CENTER_TO_RUINS_OF_ALPH_OUTSIDE_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_RESEARCH_CENTER_1_WP,
        "RuinsOfAlphResearchCenter", dual_width=True
    )

    
    Ruins_Of_Alph_Inner_Chamber_Links["RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_LINK"] = WarpLink(
        Ruins_Of_Alph_Inner_Chamber_Warp_Points.RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_INNER_CHAMBER_1_WP,
        "RuinsOfAlphInnerChamber"
    )

    
    Ruins_Of_Alph_Aerodactyl_Chamber_Links["RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_4_LINK"] = WarpLink(
        Ruins_Of_Alph_Aerodactyl_Chamber_Warp_Points.RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_4_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_AERODACTYL_CHAMBER_1_WP,
        "RuinsOfAlphAerodactylChamber",dual_width=True
    )

    Ruins_Of_Alph_Aerodactyl_Chamber_Links["RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_8_LINK"] = WarpLink(
        Ruins_Of_Alph_Aerodactyl_Chamber_Warp_Points.RUINS_OF_ALPH_AERODACTYL_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_8_WP,
        Ruins_Of_Alph_Inner_Chamber_Warp_Points.RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_WP, #This is not correct but we always overwrite
        "RuinsOfAlphAerodactylChamber", 10, dual_width=True
    )


    
    Ruins_Of_Alph_Aerodactyl_Item_Room_Links["RUINS_OF_ALPH_AERODACTYL_ITEM_ROOM_TO_RUINS_OF_ALPH_AERODACTYL_WORD_ROOM_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Aerodactyl_Item_Room_Warp_Points.RUINS_OF_ALPH_AERODACTYL_ITEM_ROOM_TO_RUINS_OF_ALPH_AERODACTYL_WORD_ROOM_1_WP,
        Ruins_Of_Alph_Aerodactyl_Item_Room_Warp_Points.RUINS_OF_ALPH_AERODACTYL_ITEM_ROOM_TO_RUINS_OF_ALPH_AERODACTYL_WORD_ROOM_1_WP, #Incorrect but always overwrite
        "RuinsOfAlphAerodactylItemRoom", 10, dual_width=True
    )

    
    Ruins_Of_Alph_Ho_Oh_Chamber_Links["RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Ho_Oh_Chamber_Warp_Points.RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_1_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_1_WP,
        "RuinsOfAlphHoOhChamber",dual_width=True
    )

    Ruins_Of_Alph_Ho_Oh_Chamber_Links["RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_2_LINK"] = WarpLink(
        Ruins_Of_Alph_Ho_Oh_Chamber_Warp_Points.RUINS_OF_ALPH_HO_OH_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_2_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_HO_OH_CHAMBER_1_WP, #incorrect but overwritten
        "RuinsOfAlphHoOhChamber", 10, dual_width=True
    )


    
    Ruins_Of_Alph_Ho_Oh_Item_Room_Links["RUINS_OF_ALPH_HO_OH_ITEM_ROOM_TO_RUINS_OF_ALPH_HO_OH_WORD_ROOM_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Ho_Oh_Item_Room_Warp_Points.RUINS_OF_ALPH_HO_OH_ITEM_ROOM_TO_RUINS_OF_ALPH_HO_OH_WORD_ROOM_1_WP,
        Ruins_Of_Alph_Ho_Oh_Item_Room_Warp_Points.RUINS_OF_ALPH_HO_OH_ITEM_ROOM_TO_RUINS_OF_ALPH_HO_OH_WORD_ROOM_1_WP,
        "RuinsOfAlphHoOhItemRoom",10, dual_width=True
    )

    
    Ruins_Of_Alph_Kabuto_Chamber_Links["RUINS_OF_ALPH_KABUTO_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_2_LINK"] = WarpLink(
        Ruins_Of_Alph_Kabuto_Chamber_Warp_Points.RUINS_OF_ALPH_KABUTO_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_2_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_KABUTO_CHAMBER_1_WP,
        "RuinsOfAlphKabutoChamber", dual_width=True
    )

    Ruins_Of_Alph_Kabuto_Chamber_Links["RUINS_OF_ALPH_KABUTO_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_4_LINK"] = WarpLink(
        Ruins_Of_Alph_Kabuto_Chamber_Warp_Points.RUINS_OF_ALPH_KABUTO_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_4_WP,
        Ruins_Of_Alph_Inner_Chamber_Warp_Points.RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_WP, #overwritten
        "RuinsOfAlphKabutoChamber", 10, dual_width=True
    )


    
    Ruins_Of_Alph_Kabuto_Item_Room_Links["RUINS_OF_ALPH_KABUTO_ITEM_ROOM_TO_RUINS_OF_ALPH_KABUTO_WORD_ROOM_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Kabuto_Item_Room_Warp_Points.RUINS_OF_ALPH_KABUTO_ITEM_ROOM_TO_RUINS_OF_ALPH_KABUTO_WORD_ROOM_1_WP,
        Ruins_Of_Alph_Kabuto_Item_Room_Warp_Points.RUINS_OF_ALPH_KABUTO_ITEM_ROOM_TO_RUINS_OF_ALPH_KABUTO_WORD_ROOM_1_WP,
        "RuinsOfAlphKabutoItemRoom", 10, dual_width=True
    )


    
    Ruins_Of_Alph_Omanyte_Chamber_Links["RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_3_LINK"] = WarpLink(
        Ruins_Of_Alph_Omanyte_Chamber_Warp_Points.RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_3_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_OMANYTE_CHAMBER_1_WP,
        "RuinsOfAlphOmanyteChamber", dual_width=True
    )

    Ruins_Of_Alph_Omanyte_Chamber_Links["RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_6_LINK"] = WarpLink(
        Ruins_Of_Alph_Omanyte_Chamber_Warp_Points.RUINS_OF_ALPH_OMANYTE_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_6_WP,
        Ruins_Of_Alph_Inner_Chamber_Warp_Points.RUINS_OF_ALPH_INNER_CHAMBER_TO_RUINS_OF_ALPH_OUTSIDE_5_WP, #incorrect but overwrite
        "RuinsOfAlphOmanyteChamber", 10, dual_width=True
    )


    
    Ruins_Of_Alph_Omanyte_Item_Room_Links["RUINS_OF_ALPH_OMANYTE_ITEM_ROOM_TO_RUINS_OF_ALPH_OMANYTE_WORD_ROOM_1_LINK"] = WarpLink(
        Ruins_Of_Alph_Omanyte_Item_Room_Warp_Points.RUINS_OF_ALPH_OMANYTE_ITEM_ROOM_TO_RUINS_OF_ALPH_OMANYTE_WORD_ROOM_1_WP,
        Ruins_Of_Alph_Omanyte_Item_Room_Warp_Points.RUINS_OF_ALPH_OMANYTE_ITEM_ROOM_TO_RUINS_OF_ALPH_OMANYTE_WORD_ROOM_1_WP,
        "RuinsOfAlphOmanyteItemRoom", 10, dual_width=True
    )


    
    Slowpoke_Well_B1F_Links["SLOWPOKE_WELL_B1F_TO_AZALEA_TOWN_LINK"] = WarpLink(
        Slowpoke_Well_B1F_Warp_Points.SLOWPOKE_WELL_B1F_TO_AZALEA_TOWN_6_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_SLOWPOKE_WELL_B1F_WP,
        "SlowpokeWellB1F", unlocks=[Unlock_Keys.SLOWPOKE_WELL_FOUND]
    )

    Slowpoke_Well_B1F_Links["SLOWPOKE_WELL_B1F_TO_SLOWPOKE_WELL_B2F_LINK"] = WarpLink(
        Slowpoke_Well_B1F_Warp_Points.SLOWPOKE_WELL_B1F_TO_SLOWPOKE_WELL_B2F_1_WP,
        Slowpoke_Well_B2F_Warp_Points.SLOWPOKE_WELL_B2_F_TO_SLOWPOKE_WELL_B1F_2_WP,
        "SlowpokeWellB1F" , 5
    )

    
    Slowpoke_Well_B2F_Links["SLOWPOKE_WELL_B2F_TO_SLOWPOKE_WELL_B1F_LINK"] = WarpLink(
        Slowpoke_Well_B2F_Warp_Points.SLOWPOKE_WELL_B2_F_TO_SLOWPOKE_WELL_B1F_2_WP,
        Slowpoke_Well_B1F_Warp_Points.SLOWPOKE_WELL_B1F_TO_SLOWPOKE_WELL_B2F_1_WP,
        "SlowpokeWellB2F"
    )

    

    Dragons_Den_1F_Links["DRAGONS_DEN_1F_TO_BLACKTHORN_CITY_8_LINK"] = WarpLink(
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_BLACKTHORN_CITY_8_WP,
        Blackthorn_City_Warp_Points.BLACKTHORN_CITY_TO_DRAGONS_DEN_1F_WP,
        "DragonsDen1F"
    )

    Dragons_Den_1F_Links["DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_4_LINK"] = WarpLink(
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_4_WP,
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_2_WP,
        "DragonsDen1F", 5
    )

    Dragons_Den_1F_Links["DRAGONS_DEN_1F_TO_DRAGONS_DEN_B1F_1_LINK"] = WarpLink(
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_DRAGONS_DEN_B1F_1_WP,
        Dragons_Den_B1F_Warp_Points.DRAGONS_DEN_B1F_TO_DRAGONS_DEN_1F_3_WP,
        "DragonsDen1F", 10
    )

    Dragons_Den_1F_Links["DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_2_LINK"] = WarpLink(
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_2_WP,
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_4_WP,
        "DragonsDen1F", 15
    )

    
    Dragons_Den_B1F_Links["DRAGONS_DEN_B1F_TO_DRAGONS_DEN_1F_3_LINK"] = WarpLink(
        Dragons_Den_B1F_Warp_Points.DRAGONS_DEN_B1F_TO_DRAGONS_DEN_1F_3_WP,
        Dragons_Den_1F_Warp_Points.DRAGONS_DEN_1F_TO_DRAGONS_DEN_B1F_1_WP,
        "DragonsDenB1F"
    )

    Dragons_Den_B1F_Links["DRAGONS_DEN_B1F_TO_DRAGON_SHRINE_1_LINK"] = WarpLink(
        Dragons_Den_B1F_Warp_Points.DRAGONS_DEN_B1F_TO_DRAGON_SHRINE_1_WP,
        Dragon_Shrine_Warp_Points.DRAGON_SHRINE_TO_DRAGONS_DEN_B1F_2_WP,
        "DragonsDenB1F", 5
    )


    
    Dragon_Shrine_Links["DRAGON_SHRINE_TO_DRAGONS_DEN_B1F_2_LINK"] = WarpLink(
        Dragon_Shrine_Warp_Points.DRAGON_SHRINE_TO_DRAGONS_DEN_B1F_2_WP,
        Dragons_Den_B1F_Warp_Points.DRAGONS_DEN_B1F_TO_DRAGON_SHRINE_1_WP,
        "DragonShrine", dual_width=True, unlocks=[Unlock_Keys.BADGE_8]
    )

    
    Sprout_Tower_1F_Links["SPROUT_TOWER_1F_TO_VIOLET_CITY_LINK"] = WarpLink(
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_SPROUT_TOWER_1F_WP,
        "SproutTower1F", dual_width=True
    )
    Sprout_Tower_1F_Links["SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FA_LINK"] = WarpLink(
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FA_WP,
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_3_WP,
        "SproutTower1F", 10
    )
    Sprout_Tower_1F_Links["SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FB_LINK"] = WarpLink(
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FB_WP,
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_4_WP,
        "SproutTower1F", 15
    )
    Sprout_Tower_1F_Links["SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FC_LINK"] = WarpLink(
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FC_WP,
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_5_WP,
        "SproutTower1F", 20
    )

    
    Sprout_Tower_2F_Links["SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_3_LINK"] = WarpLink(
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_3_WP,
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FA_WP,
        "SproutTower2F"
    )

    Sprout_Tower_2F_Links["SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_4_LINK"] = WarpLink(
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_4_WP,
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FB_WP,
        "SproutTower2F",5
    )

    Sprout_Tower_2F_Links["SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_5_LINK"] = WarpLink(
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_5_WP,
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FC_WP,
        "SproutTower2F",10
    )

    Sprout_Tower_2F_Links["SPROUT_TOWER_2F_TO_SPROUT_TOWER_3F_1_LINK"] = WarpLink(
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_3F_1_WP,
        Sprout_Tower_3F_Warp_Points.SPROUT_TOWER_3F_TO_SPROUT_TOWER_2F_4_WP,
        "SproutTower2F",15
    )



    
    Sprout_Tower_3F_Links["SPROUT_TOWER_3F_TO_SPROUT_TOWER_2F_LINK"] = WarpLink(
        Sprout_Tower_3F_Warp_Points.SPROUT_TOWER_3F_TO_SPROUT_TOWER_2F_4_WP,
        Sprout_Tower_2F_Warp_Points.SPROUT_TOWER_2F_TO_SPROUT_TOWER_3F_1_WP,
        "SproutTower3F", unlocks=[Unlock_Keys.HM_FLASH]
    )

    
    Tin_Tower_1F_Links["TIN_TOWER_1F_TO_ECRUTEAK_CITY_LINK"] = WarpLink(
        Tin_Tower_1F_Warp_Points.TIN_TOWER_1F_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_TIN_TOWER_1F_WP,
        "TinTower1F", dual_width=True
    )


    
    Tin_Tower_2F_Links["TIN_TOWER_2F_TO_TIN_TOWER_3F_1_LINK"] = WarpLink(
        Tin_Tower_2F_Warp_Points.TIN_TOWER_2F_TO_TIN_TOWER_3F_1_WP,
        Tin_Tower_3F_Warp_Points.TIN_TOWER_3F_TO_TIN_TOWER_2F_1_WP,
        "TinTower2F"
    )

    Tin_Tower_2F_Links["TIN_TOWER_2F_TO_TIN_TOWER_1F_3_LINK"] = WarpLink(
        Tin_Tower_2F_Warp_Points.TIN_TOWER_2F_TO_TIN_TOWER_1F_3_WP,
        Tin_Tower_1F_Warp_Points.TIN_TOWER_1F_TO_TIN_TOWER_2F_WP,
        "TinTower2F",5
    )


    
    Tin_Tower_3F_Links["TIN_TOWER_3F_TO_TIN_TOWER_2F_1_LINK"] = WarpLink(
        Tin_Tower_3F_Warp_Points.TIN_TOWER_3F_TO_TIN_TOWER_2F_1_WP,
        Tin_Tower_2F_Warp_Points.TIN_TOWER_2F_TO_TIN_TOWER_3F_1_WP,
        "TinTower3F"
    )

    Tin_Tower_3F_Links["TIN_TOWER_3F_TO_TIN_TOWER_4F_2_LINK"] = WarpLink(
        Tin_Tower_3F_Warp_Points.TIN_TOWER_3F_TO_TIN_TOWER_4F_2_WP,
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_3F_2_WP,
        "TinTower3F",5
    )


    
    Tin_Tower_4F_Links["TIN_TOWER_4F_TO_TIN_TOWER_5F_2_LINK"] = WarpLink(
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_5F_2_WP,
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_4F_1_WP,
        "TinTower4F"
    )

    Tin_Tower_4F_Links["TIN_TOWER_4F_TO_TIN_TOWER_3F_2_LINK"] = WarpLink(
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_3F_2_WP,
        Tin_Tower_3F_Warp_Points.TIN_TOWER_3F_TO_TIN_TOWER_4F_2_WP,
        "TinTower4F",5
    )

    Tin_Tower_4F_Links["TIN_TOWER_4F_TO_TIN_TOWER_5F_3_LINK"] = WarpLink(
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_5F_3_WP,
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_4F_3_WP,
        "TinTower4F",10
    )

    Tin_Tower_4F_Links["TIN_TOWER_4F_TO_TIN_TOWER_5F_4_LINK"] = WarpLink(
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_5F_4_WP,
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_4F_4_WP,
        "TinTower4F",15
    )


    
    Tin_Tower_5F_Links["TIN_TOWER_5F_TO_TIN_TOWER_6F_2_LINK"] = WarpLink(  # middle bottom one way
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_6F_2_WP,
        Tin_Tower_6F_Warp_Points.TIN_TOWER_6F_TO_TIN_TOWER_5F_1_WP,
        "TinTower5F"
    )

    Tin_Tower_5F_Links["TIN_TOWER_5F_TO_TIN_TOWER_4F_1_LINK"] = WarpLink(  # top
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_4F_1_WP,
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_5F_2_WP,
        "TinTower5F",5
    )

    Tin_Tower_5F_Links["TIN_TOWER_5F_TO_TIN_TOWER_4F_3_LINK"] = WarpLink(  # deadend (item) (left)
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_4F_3_WP,
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_5F_3_WP,
        "TinTower5F",10
    )

    Tin_Tower_5F_Links["TIN_TOWER_5F_TO_TIN_TOWER_4F_4_LINK"] = WarpLink(  # deadend (item) (left)
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_4F_4_WP,
        Tin_Tower_4F_Warp_Points.TIN_TOWER_4F_TO_TIN_TOWER_5F_4_WP,
        "TinTower5F",15
    )


    
    Tin_Tower_6F_Links["TIN_TOWER_6F_TO_TIN_TOWER_7F_1_LINK"] = WarpLink(
        Tin_Tower_6F_Warp_Points.TIN_TOWER_6F_TO_TIN_TOWER_7F_1_WP,
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_6F_1_WP,
        "TinTower6F"
    )

    Tin_Tower_6F_Links["TIN_TOWER_6F_TO_TIN_TOWER_5F_1_LINK"] = WarpLink(
        Tin_Tower_6F_Warp_Points.TIN_TOWER_6F_TO_TIN_TOWER_5F_1_WP,
        Tin_Tower_5F_Warp_Points.TIN_TOWER_5F_TO_TIN_TOWER_6F_2_WP,
        "TinTower6F",5
    )


    

    Tin_Tower_7F_Links["TIN_TOWER_7F_TO_TIN_TOWER_6F_1_LINK"] = WarpLink(
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_6F_1_WP,
        Tin_Tower_6F_Warp_Points.TIN_TOWER_6F_TO_TIN_TOWER_7F_1_WP,
        "TinTower7F"
    )

    Tin_Tower_7F_Links["TIN_TOWER_7F_TO_TIN_TOWER_8F_1_LINK"] = WarpLink(
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_8F_1_WP,
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_7F_2_WP,
        "TinTower7F",5
    )

    Tin_Tower_7F_Links["TIN_TOWER_7F_TO_TIN_TOWER_7F_4_LINK"] = WarpLink(
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_7F_4_WP,
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_7F_3_WP,
        "TinTower7F",10
    )

    Tin_Tower_7F_Links["TIN_TOWER_7F_TO_TIN_TOWER_7F_3_LINK"] = WarpLink(
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_7F_3_WP,
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_7F_4_WP,
        "TinTower7F",15
    )

    Tin_Tower_7F_Links["TIN_TOWER_7F_TO_TIN_TOWER_9F_5_LINK"] = WarpLink(
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_9F_5_WP,
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_7F_5_WP,
        "TinTower7F",20
    )


    

    Tin_Tower_8F_Links["TIN_TOWER_8F_TO_TIN_TOWER_7F_2_LINK"] = WarpLink(
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_7F_2_WP,
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_8F_1_WP,
        "TinTower8F"
    )

    Tin_Tower_8F_Links["TIN_TOWER_8F_TO_TIN_TOWER_9F_1_LINK"] = WarpLink(
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_1_WP,
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_2_WP,
        "TinTower8F",5
    )

    Tin_Tower_8F_Links["TIN_TOWER_8F_TO_TIN_TOWER_9F_2_LINK"] = WarpLink(
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_2_WP,
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_3_WP,
        "TinTower8F",10
    )

    Tin_Tower_8F_Links["TIN_TOWER_8F_TO_TIN_TOWER_9F_3_LINK"] = WarpLink(
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_3_WP,
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_4_WP,
        "TinTower8F",15
    )

    Tin_Tower_8F_Links["TIN_TOWER_8F_TO_TIN_TOWER_9F_6_LINK"] = WarpLink(
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_6_WP,
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_5_WP,
        "TinTower8F",20
    )

    Tin_Tower_8F_Links["TIN_TOWER_8F_TO_TIN_TOWER_9F_7_LINK"] = WarpLink(
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_7_WP,
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_6_WP,
        "TinTower8F",25
    )


    

    Tin_Tower_9F_Links["TIN_TOWER_9F_TO_TIN_TOWER_8F_2_LINK"] = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_2_WP,
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_1_WP,
        "TinTower9F"
    )

    Tin_Tower_9F_Links["TIN_TOWER_9F_TO_TIN_TOWER_8F_3_LINK"] = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_3_WP,
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_2_WP,
        "TinTower9F",5
    )

    Tin_Tower_9F_Links["TIN_TOWER_9F_TO_TIN_TOWER_8F_4_LINK"] = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_4_WP,
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_3_WP,
        "TinTower9F",10
    )

    Tin_Tower_9F_Links["TIN_TOWER_9F_TO_TIN_TOWER_ROOF_1_LINK"] = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_ROOF_1_WP,
        Tin_Tower_Roof_Warp_Points.TIN_TOWER_ROOF_TO_TIN_TOWER_9F_WP,
        "TinTower9F",15
    )

    Tin_Tower_9F_Links["TIN_TOWER_9F_TO_TIN_TOWER_7F_5_LINK"] = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_7F_5_WP,
        Tin_Tower_7F_Warp_Points.TIN_TOWER_7F_TO_TIN_TOWER_9F_5_WP,
        "TinTower9F",20
    )

    Tin_Tower_9F_Links["TIN_TOWER_9F_TO_TIN_TOWER_8F_5_LINK"] = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_5_WP,
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_6_WP,
        "TinTower9F",25
    )

    Tin_Tower_9F_Links["TIN_TOWER_9F_TO_TIN_TOWER_8F_6_LINK"] = WarpLink(
        Tin_Tower_9F_Warp_Points.TIN_TOWER_9F_TO_TIN_TOWER_8F_6_WP,
        Tin_Tower_8F_Warp_Points.TIN_TOWER_8F_TO_TIN_TOWER_9F_7_WP,
        "TinTower9F",30
    )

    
    Union_Cave_1F_Links["UNION_CAVE_1F_TO_UNION_CAVE_B1FA_LINK"] = WarpLink(
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_UNION_CAVE_B1FA_WP,
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_UNION_CAVE_1F_1_WP,
        "UnionCave1F"
    )

    Union_Cave_1F_Links["UNION_CAVE_1F_TO_UNION_CAVE_B1FB_LINK"] = WarpLink(
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_UNION_CAVE_B1FB_WP,
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_UNION_CAVE_1F_2_WP,
        "UnionCave1F", 5
    )


    Union_Cave_1F_Links["UNION_CAVE_1F_TO_ROUTE_33_LINK"] = WarpLink(
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_ROUTE_33_WP,
        Route_33_Warp_Points.ROUTE_33_TO_UNION_CAVE_1F_WP,
        "UnionCave1F" , 10
    )

    Union_Cave_1F_Links["UNION_CAVE_1F_TO_ROUTE_32_LINK"] = WarpLink(
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_ROUTE_32_WP,
        Route_32_Warp_Points.ROUTE_32_TO_UNION_CAVE_1F_WP,
        "UnionCave1F" , 15
    )

    
    Union_Cave_B1F_Links["UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_7_LINK"] = WarpLink(
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_7_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_1_WP,
        "UnionCaveB1F"
    )
    Union_Cave_B1F_Links["UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_8_LINK"] = WarpLink(
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_8_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_UNION_CAVE_B1F_2_WP,
        "UnionCaveB1F", 5
    )

    Union_Cave_B1F_Links["UNION_CAVE_B1F_TO_UNION_CAVE_1F_1_LINK"] = WarpLink(
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_UNION_CAVE_1F_1_WP,
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_UNION_CAVE_B1FA_WP,
        "UnionCaveB1F", 10
    )

    Union_Cave_B1F_Links["UNION_CAVE_B1F_TO_UNION_CAVE_1F_2_LINK"] = WarpLink(
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_UNION_CAVE_1F_2_WP,
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_UNION_CAVE_B1FB_WP,
        "UnionCaveB1F", 15
    )

    Union_Cave_B1F_Links["UNION_CAVE_B1F_TO_UNION_CAVE_B2F_1_LINK"] = WarpLink(
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_UNION_CAVE_B2F_1_WP,
        Union_Cave_B2F_Warp_Points.UNION_CAVE_B2F_TO_UNION_CAVE_B1F_5_WP,
        "UnionCaveB1F", 20
    )


    
    Union_Cave_B2F_Links["UNION_CAVE_B2F_TO_UNION_CAVE_B1F_5_LINK"] = WarpLink(
        Union_Cave_B2F_Warp_Points.UNION_CAVE_B2F_TO_UNION_CAVE_B1F_5_WP,
        Union_Cave_B1F_Warp_Points.UNION_CAVE_B1F_TO_UNION_CAVE_B2F_1_WP,
        "UnionCaveB2F"
    )

    
    Lake_Of_Rage_Links["LAKE_OF_RAGE_TO_LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_LINK"] = WarpLink(
        Lake_Of_Rage_Warp_Points.LAKE_OF_RAGE_TO_LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_WP,
        Lake_Of_Rage_Hidden_Power_House_Warp_Points.LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_TO_LAKE_OF_RAGE_WP,
        "LakeOfRage", unlocks=[Unlock_Keys.LAKE_OF_RAGE_FOUND]
    )

    Lake_Of_Rage_Links["LAKE_OF_RAGE_TO_LAKE_OF_RAGE_MAGIKARP_HOUSE_LINK"] = WarpLink(
        Lake_Of_Rage_Warp_Points.LAKE_OF_RAGE_TO_LAKE_OF_RAGE_MAGIKARP_HOUSE_WP,
        Lake_Of_Rage_Magikarp_House_Warp_Points.LAKE_OF_RAGE_MAGIKARP_HOUSE_TO_LAKE_OF_RAGE_WP,
        "LakeOfRage" , 5, unlocks=[Unlock_Keys.LAKE_OF_RAGE_FOUND]
    )


    
    Lake_Of_Rage_Hidden_Power_House_Links["LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_TO_LAKE_OF_RAGE_LINK"] = WarpLink(
        Lake_Of_Rage_Hidden_Power_House_Warp_Points.LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_TO_LAKE_OF_RAGE_WP,
        Lake_Of_Rage_Warp_Points.LAKE_OF_RAGE_TO_LAKE_OF_RAGE_HIDDEN_POWER_HOUSE_WP,
        "LakeOfRageHiddenPowerHouse", dual_width=True
    )

    
    Lake_Of_Rage_Magikarp_House_Links["LAKE_OF_RAGE_MAGIKARP_HOUSE_TO_LAKE_OF_RAGE_LINK"] = WarpLink(
        Lake_Of_Rage_Magikarp_House_Warp_Points.LAKE_OF_RAGE_MAGIKARP_HOUSE_TO_LAKE_OF_RAGE_WP,
        Lake_Of_Rage_Warp_Points.LAKE_OF_RAGE_TO_LAKE_OF_RAGE_MAGIKARP_HOUSE_WP,
        "LakeOfRageMagikarpHouse", dual_width=True
    )


    
    Whirl_Island_NW_Links["WHIRL_ISLAND_N_W_TO_ROUTE_41_1_LINK"] = WarpLink(
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_ROUTE_41_1_WP,
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_NW_WP,
        "WhirlIslandNW"
    )

    Whirl_Island_NW_Links["WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_B1F_1_LINK"] = WarpLink(
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_B1F_1_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NW_2_WP,
        "WhirlIslandNW", 5
    )

    Whirl_Island_NW_Links["WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_SW_4_LINK"] = WarpLink(
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_SW_4_WP,
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_NW_3_WP,
        "WhirlIslandNW", 10
    )

    Whirl_Island_NW_Links["WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_CAVE_2_LINK"] = WarpLink(
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_CAVE_2_WP,
        Whirl_Island_Cave_Warp_Points.WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_NW_4_WP,
        "WhirlIslandNW", 15
    )


    
    Whirl_Island_NE_Links["WHIRL_ISLAND_N_E_TO_ROUTE_41_2_LINK"] = WarpLink(
        Whirl_Island_NE_Warp_Points.WHIRL_ISLAND_N_E_TO_ROUTE_41_2_WP,
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_NE_WP,
        "WhirlIslandNE"
    )

    Whirl_Island_NE_Links["WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_2_LINK"] = WarpLink(
        Whirl_Island_NE_Warp_Points.WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_2_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NW_2_WP,
        "WhirlIslandNE", 5
    )

    Whirl_Island_NE_Links["WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_3_LINK"] = WarpLink(
        Whirl_Island_NE_Warp_Points.WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_3_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_3_WP,
        "WhirlIslandNE", 10
    )

    
    Whirl_Island_SW_Links["WHIRL_ISLAND_S_W_TO_ROUTE_41_3_LINK"] = WarpLink(
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_ROUTE_41_3_WP,
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_SW_WP,
        "WhirlIslandSW"
    )

    Whirl_Island_SW_Links["WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_5_LINK"] = WarpLink(
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_5_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_2_WP,
        "WhirlIslandSW", 5
    )

    Whirl_Island_SW_Links["WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_4_LINK"] = WarpLink(
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_4_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_3_WP,
        "WhirlIslandSW", 10
    )

    Whirl_Island_SW_Links["WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_NW_3_LINK"] = WarpLink(
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_NW_3_WP,
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_SW_4_WP,
        "WhirlIslandSW", 15
    )

    Whirl_Island_SW_Links["WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B2F_4_LINK"] = WarpLink(
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B2F_4_WP,
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_SW_5_WP,
        "WhirlIslandSW", 20
    )

    
    Whirl_Island_SE_Links["WHIRL_ISLAND_S_E_TO_ROUTE_41_4_LINK"] = WarpLink(
        Whirl_Island_SE_Warp_Points.WHIRL_ISLAND_S_E_TO_ROUTE_41_4_WP,
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_SE_WP,
        "WhirlIslandSE"
    )

    Whirl_Island_SE_Links["WHIRL_ISLAND_S_E_TO_WHIRL_ISLAND_B1F_6_LINK"] = WarpLink(
        Whirl_Island_SE_Warp_Points.WHIRL_ISLAND_S_E_TO_WHIRL_ISLAND_B1F_6_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SE_2_WP,
        "WhirlIslandSE",5
    )

    
    Whirl_Island_Cave_Links["WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_B1F_9_LINK"] = WarpLink(
        Whirl_Island_Cave_Warp_Points.WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_B1F_9_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_CAVE_1_WP,
        "WhirlIslandCave"
    )

    Whirl_Island_Cave_Links["WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_NW_4_LINK"] = WarpLink(
        Whirl_Island_Cave_Warp_Points.WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_NW_4_WP,
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_CAVE_2_WP,
        "WhirlIslandCave", 5
    )




    
    Whirl_Island_B1F_Links["WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NW_2_LINK"] = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NW_2_WP,
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_B1F_1_WP,
        "WhirlIslandB1F"
    )

    Whirl_Island_B1F_Links["WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_2_LINK"] = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_2_WP,
        Whirl_Island_NE_Warp_Points.WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_2_WP,
        "WhirlIslandB1F", 5
    )

    Whirl_Island_B1F_Links["WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_3_LINK"] = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_3_WP,
        Whirl_Island_NE_Warp_Points.WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_3_WP,
        "WhirlIslandB1F", 10
    )

    Whirl_Island_B1F_Links["WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_3_LINK"] = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_3_WP,
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_4_WP,
        "WhirlIslandB1F", 15
    )

    Whirl_Island_B1F_Links["WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_2_LINK"] = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_2_WP,
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_5_WP,
        "WhirlIslandB1F", 20
    )

    Whirl_Island_B1F_Links["WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SE_2_LINK"] = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SE_2_WP,
        Whirl_Island_SE_Warp_Points.WHIRL_ISLAND_S_E_TO_WHIRL_ISLAND_B1F_6_WP,
        "WhirlIslandB1F", 25
    )

    Whirl_Island_B1F_Links["WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_1_LINK"] = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_1_WP,
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_7_WP,
        "WhirlIslandB1F", 30
    )

    Whirl_Island_B1F_Links["WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_2_LINK"] = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_2_WP,
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_8_WP,
        "WhirlIslandB1F", 35
    )

    Whirl_Island_B1F_Links["WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_CAVE_1_LINK"] = WarpLink(
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_CAVE_1_WP,
        Whirl_Island_Cave_Warp_Points.WHIRL_ISLAND_CAVE_TO_WHIRL_ISLAND_B1F_9_WP,
        "WhirlIslandB1F", 40
    )


    
    Whirl_Island_B2F_Links["WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_7_LINK"] = WarpLink(
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_7_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_1_WP,
        "WhirlIslandB2F"
    )

    Whirl_Island_B2F_Links["WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_8_LINK"] = WarpLink(
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_B1F_8_WP,
        Whirl_Island_B1F_Warp_Points.WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_2_WP,
        "WhirlIslandB2F", 5
    )

    Whirl_Island_B2F_Links["WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_LUGIA_CHAMBER_1_LINK"] = WarpLink(
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_LUGIA_CHAMBER_1_WP,
        Whirl_Island_Lugia_Chamber_Warp_Points.WHIRL_ISLAND_LUGIA_CHAMBER_TO_WHIRL_ISLAND_B2F_WP,
        "WhirlIslandB2F", 10
    )

    Whirl_Island_B2F_Links["WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_SW_5_LINK"] = WarpLink(
        Whirl_Island_B2F_Warp_Points.WHIRL_ISLAND_B2F_TO_WHIRL_ISLAND_SW_5_WP,
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B2F_4_WP,
        "WhirlIslandB2F", 15
    )



    
    Whirl_Island_Lugia_Chamber_Links["WHIRL_ISLAND_LUGIA_CHAMBER_TO_WHIRL_ISLAND_B2F_LINK"] = WarpLink(
        Whirl_Island_Lugia_Chamber_Warp_Points.WHIRL_ISLAND_LUGIA_CHAMBER_TO_WHIRL_ISLAND_B2F_WP,
        New_Bark_Warp_Points.NEW_BARK_TO_PLAYERS_NEIGHBORS_HOUSE_WP,
        "WhirlIslandLugiaChamber"
    )

    
    Tin_Tower_Roof_Links["TIN_TOWER_ROOF_TO_TIN_TOWER_9F_LINK"] = WarpLink(
        Tin_Tower_Roof_Warp_Points.TIN_TOWER_ROOF_TO_TIN_TOWER_9F_WP,
        New_Bark_Warp_Points.NEW_BARK_TO_ELMS_HOUSE_WP,
        "TinTowerRoof"
    )
#######################################################################
#                    Ecruteak Group                                   #
#######################################################################
    

    Dance_Theatre_Links["DANCE_THEATRE_TO_ECRUTEAK_CITY_LINK"] = WarpLink(
        Dance_Theatre_Warp_Points.DANCE_THEATRE_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_DANCE_THEATRE_WP,
        "DanceTheatre", dual_width=True, unlocks=[Unlock_Keys.HM_SURF]
    )

    

    Ecruteak_City_Links["ECRUTEAK_CITY_TO_ROUTE_42_ECRUTEAK_GATE_LINK"] = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ROUTE_42_ECRUTEAK_GATE_WP,
        Route_42_Ecruteak_Gate_Warp_Points.ROUTE_42_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity", dual_width=True
    )

    Ecruteak_City_Links["ECRUTEAK_CITY_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_LINK"] = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_WP,
        Ecruteak_Tin_Tower_Entrance_Warp_Points.ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 10
    )

    Ecruteak_City_Links["ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_LINK"] = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_WP,
        Wise_Trios_Room_Warp_Points.WISE_TRIOS_ROOM_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 15, dual_width=True
    )

    Ecruteak_City_Links["ECRUTEAK_CITY_TO_ECRUTEAK_POKECENTER_1F_LINK"] = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_POKECENTER_1F,
        Ecruteak_Pokecenter_Warp_Points.ECRUTEAK_POKECENTER_1F_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 25
    )


    Ecruteak_City_Links["ECRUTEAK_CITY_TO_ECRUTEAK_LUGIA_SPEECH_HOUSE_LINK"] = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_LUGIA_SPEECH_HOUSE_WP,
        Ecruteak_Lugia_Speech_House_Warp_Points.ECRUTEAK_LUGIA_SPEECH_HOUSE_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 30
    )

    Ecruteak_City_Links["ECRUTEAK_CITY_TO_DANCE_THEATRE_LINK"] = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_DANCE_THEATRE_WP,
        Dance_Theatre_Warp_Points.DANCE_THEATRE_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 35
    )

    Ecruteak_City_Links["ECRUTEAK_CITY_TO_ECRUTEAK_MART_LINK"] = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_MART_WP,
        Ecruteak_Mart_Warp_Points.ECRUTEAK_MART_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 40
    )

    Ecruteak_City_Links["ECRUTEAK_CITY_TO_ECRUTEAK_GYM_LINK"] = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_GYM_WP,
        Ecruteak_Gym_Warp_Points.ECRUTEAK_GYM_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 45
    )

    Ecruteak_City_Links["ECRUTEAK_CITY_TO_ECRUTEAK_ITEMFINDER_HOUSE_LINK"] = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_ITEMFINDER_HOUSE_WP,
        Ecruteak_Itemfinder_House_Warp_Points.ECRUTEAK_ITEMFINDER_HOUSE_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 50
    )

    Ecruteak_City_Links["ECRUTEAK_CITY_TO_TIN_TOWER_1F_LINK"] = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_TIN_TOWER_1F_WP,
        Tin_Tower_1F_Warp_Points.TIN_TOWER_1F_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 55
    )

    Ecruteak_City_Links["ECRUTEAK_CITY_TO_BURNED_TOWER_1F_LINK"] = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_BURNED_TOWER_1F_WP,
        Burned_Tower_1F_Warp_Points.BURNED_TOWER_1F_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 60
    )

    Ecruteak_City_Links["ECRUTEAK_CITY_TO_ROUTE_38_ECRUTEAK_GATE_LINK"] = WarpLink(
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ROUTE_38_ECRUTEAK_GATE_WP,
        Route_38_Ecruteak_Gate_Warp_Points.ROUTE_38_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_WP,
        "EcruteakCity" , 65, dual_width=True
    )

    

    Ecruteak_Gym_Links["ECRUTEAK_GYM_TO_ECRUTEAK_CITY_LINK"] = WarpLink(
        Ecruteak_Gym_Warp_Points.ECRUTEAK_GYM_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_GYM_WP,
        "EcruteakGym", dual_width=True, locked_by=[Unlock_Keys.ENTERED_BURNED_TOWER],
        unlocks=[Unlock_Keys.BADGE_4]
    )

    

    Ecruteak_Item_Finder_House_Links["ECRUTEAK_ITEMFINDER_HOUSE_TO_ECRUTEAK_CITY_LINK"] = WarpLink(
        Ecruteak_Itemfinder_House_Warp_Points.ECRUTEAK_ITEMFINDER_HOUSE_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_ITEMFINDER_HOUSE_WP,
        "EcruteakItemfinderHouse", dual_width=True
    )

    

    Ecruteak_Lugia_Speech_House_Links["ECRUTEAK_LUGIA_SPEECH_HOUSE_TO_ECRUTEAK_CITY_LINK"] = WarpLink(
        Ecruteak_Lugia_Speech_House_Warp_Points.ECRUTEAK_LUGIA_SPEECH_HOUSE_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_LUGIA_SPEECH_HOUSE_WP,
        "EcruteakLugiaSpeechHouse", dual_width=True
    )

    

    Ecruteak_Mart_Links["ECRUTEAK_MART_TO_ECRUTEAK_CITY_LINK"] = WarpLink(
        Ecruteak_Mart_Warp_Points.ECRUTEAK_MART_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_MART_WP,
        "EcruteakMart", dual_width=True
    )

    

    Ecruteak_Pokecenter_Links["ECRUTEAK_POKECENTER_1F_TO_ECRUTEAK_CITY_LINK"] = WarpLink(
        Ecruteak_Pokecenter_Warp_Points.ECRUTEAK_POKECENTER_1F_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_POKECENTER_1F,
        "EcruteakPokecenter1F", dual_width=True
    )

    Ecruteak_Pokecenter_Links["ECRUTEAK_POKECENTER_1F_TO_ECRUTEAK_POKECENTER_2F_LINK"] = WarpLink(
        Ecruteak_Pokecenter_Warp_Points.ECRUTEAK_POKECENTER_TO_ECRUTEAK_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "EcruteakPokecenter1F", 10
    )

    


    Ecruteak_Tin_Tower_Entrance_Links["ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_CITY_LINK"] = WarpLink(
        Ecruteak_Tin_Tower_Entrance_Warp_Points.ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_WP,
        "EcruteakTinTowerEntrance", dual_width=True
    )
    # ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_TIN_TOWER_ENTRANCEA_LINK
    # ECRUTEAK_TIN_TOWER_ENTRANCE_TO_ECRUTEAK_TIN_TOWER_ENTRANCEB_LINK

    Ecruteak_Tin_Tower_Entrance_Links["ECRUTEAK_TIN_TOWER_ENTRANCE_TO_WISE_TRIOS_ROOM_LINK"] = WarpLink(
        Ecruteak_Tin_Tower_Entrance_Warp_Points.ECRUTEAK_TIN_TOWER_ENTRANCE_TO_WISE_TRIOS_ROOM_WP,
        Wise_Trios_Room_Warp_Points.WISE_TRIOS_ROOM_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_WP,
        "EcruteakTinTowerEntrance" , 20
    )

    

    Wise_Trios_Room_Links["WISE_TRIOS_ROOM_TO_ECRUTEAK_CITY_LINK"] = WarpLink(
        Wise_Trios_Room_Warp_Points.WISE_TRIOS_ROOM_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_WP,
        "WiseTriosRoom", dual_width=True
    )

    Wise_Trios_Room_Links["WISE_TRIOS_ROOM_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_LINK"] = WarpLink(
        Wise_Trios_Room_Warp_Points.WISE_TRIOS_ROOM_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_WP,
        Ecruteak_Tin_Tower_Entrance_Warp_Points.ECRUTEAK_TIN_TOWER_ENTRANCE_TO_WISE_TRIOS_ROOM_WP,
        "WiseTriosRoom" , 10
    )


#######################################################################
#                    Gates Group                                      #
#######################################################################

    

    Ilex_Forest_Azalea_Gate_Links["ILEX_FOREST_AZALEA_GATE_TO_ILEX_FOREST_LINK"] = WarpLink(
        Ilex_Forest_Azalea_Gate_Warp_Points.ILEX_FOREST_AZALEA_GATE_TO_ILEX_FOREST_WP,
        Ilex_Forest_Warp_Points.ILEX_FOREST_TO_ILEX_FOREST_AZALEA_GATE_WP,
        "IlexForestAzaleaGate",
        dual_width=True
    )

    Ilex_Forest_Azalea_Gate_Links["ILEX_FOREST_AZALEA_GATE_TO_AZALEA_TOWN"] = WarpLink(
        Ilex_Forest_Azalea_Gate_Warp_Points.ILEX_FOREST_AZALEA_GATE_TO_AZALEA_TOWN_WP,
        Azalea_Town_Warp_Points.AZALEA_TOWN_TO_ILEX_FOREST_AZALEA_GATE_WP,
        "IlexForestAzaleaGate" , 10,
        dual_width=True
    )

    

    Route_29_Route_46_Gate_Links["ROUTE_29_ROUTE_46_GATE_TO_ROUTE_46_LINK"] = WarpLink(
        Route_29_Route_46_Gate_Warp_Points.ROUTE_29_AND_46_GATE_EXIT_TO_ROUTE_46_WP,
        Route_46_Warp_Points.ROUTE_46_TO_ROUTE_29_ROUTE_46_GATE_WP,
        "Route29Route46Gate",
        dual_width=True
    )

    Route_29_Route_46_Gate_Links["ROUTE_29_ROUTE_46_GATE_TO_ROUTE_29_LINK"] = WarpLink(
        Route_29_Route_46_Gate_Warp_Points.ROUTE_29_AND_46_GATE_EXIT_TO_ROUTE_29_WP,
        Route_29_Warp_Points.ROUTE_29_TO_ROUTE_46_GATE_ENTRANCE_WP,
        "Route29Route46Gate" , 10,
        dual_width=True
    )

    

    Route_31_Violet_Gate_Links["ROUTE_31_VIOLET_GATE_TO_VIOLET_CITY_LINK"] = WarpLink(
        Route_31_Violet_Gate_Warp_Points.ROUTE_31_VIOLET_GATE_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_ROUTE_31_VIOLET_GATE_WP,
        "Route31VioletGate",
        dual_width=True
    )

    Route_31_Violet_Gate_Links["ROUTE_31_VIOLET_GATE_TO_ROUTE_31_LINK"] = WarpLink(
        Route_31_Violet_Gate_Warp_Points.ROUTE_31_VIOLET_GATE_TO_ROUTE_31_WP,
        Route_31_Warp_Points.ROUTE_31_TO_ROUTE_31_VIOLET_GATE_WP,
        "Route31VioletGate" , 10,
        dual_width=True
    )

    

    Route_32_Ruins_Of_Alph_Gate_Links["ROUTE_32_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_LINK"] = WarpLink(
        Route_32_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_32_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_32_RUINS_OF_ALPH_GATE_1_WP,
        "Route32RuinsOfAlphGate",
        dual_width=True
    )

    Route_32_Ruins_Of_Alph_Gate_Links["ROUTE_32_RUINS_OF_ALPH_GATE_TO_ROUTE_32_LINK"] = WarpLink(
        Route_32_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_32_RUINS_OF_ALPH_GATE_TO_ROUTE_32_WP,
        Route_32_Warp_Points.ROUTE_32_TO_ROUTE_32_RUINS_OF_ALPH_GATE_WP,
        "Route32RuinsOfAlphGate", 10,
        dual_width=True
    )

    
    Route_34_Ilex_Forest_Gate_Links["ROUTE_34_ILEX_FOREST_GATE_TO_ROUTE_34_LINK"] = WarpLink(
        Route_34_Ilex_Forest_Gate_Warp_Points.ROUTE_34_ILEX_FOREST_GATE_TO_ROUTE_34_WP,
        Route_34_Warp_Points.ROUTE_34_TO_ROUTE_34_ILEX_FOREST_GATE_WP,
        "Route34IlexForestGate", dual_width=True
    )
    Route_34_Ilex_Forest_Gate_Links["ROUTE_34_ILEX_FOREST_GATE_TO_ILEX_FOREST_LINK"] = WarpLink(
        Route_34_Ilex_Forest_Gate_Warp_Points.ROUTE_34_ILEX_FOREST_GATE_TO_ILEX_FOREST_WP,
        Ilex_Forest_Warp_Points.ILEX_FOREST_TO_ROUTE_34_ILEX_FOREST_GATE_WP,
        "Route34IlexForestGate" , 10, dual_width=True
    )

    
    Route_35_Goldenrod_Gate_Links["ROUTE_35_GOLDENROD_GATE_TO_ROUTE_35__LINK"] = WarpLink(
        Route_35_Goldenrod_Gate_Warp_Points.ROUTE_35_GOLDENROD_GATE_TO_ROUTE_35_WP,
        Route_35_Warp_Points.ROUTE_35_TO_ROUTE_35_GOLDENROD_GATE_WP,
        "Route35GoldenrodGate", dual_width=True
    )

    Route_35_Goldenrod_Gate_Links["ROUTE_35_GOLDENROD_GATE_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Route_35_Goldenrod_Gate_Warp_Points.ROUTE_35_GOLDENROD_GATE_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_ROUTE_35_GOLDENROD_GATE_WP,
        "Route35GoldenrodGate" , 10, dual_width=True
    )

    
    Route_35_National_Park_Gate_Links["ROUTE_35_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_LINK"] = WarpLink(
        Route_35_National_Park_Gate_Warp_Points.ROUTE_35_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_WP,
        National_Park_Warp_Points.NATIONAL_PARK_TO_ROUTE_35_NATIONAL_PARK_GATE_WP,
        "Route35NationalParkGate", dual_width=True
    )
    Route_35_National_Park_Gate_Links["ROUTE_35_NATIONAL_PARK_GATE_TO_ROUTE_35_LINK"] = WarpLink(
        Route_35_National_Park_Gate_Warp_Points.ROUTE_35_NATIONAL_PARK_GATE_TO_ROUTE_35_WP,
        Route_35_Warp_Points.ROUTE_35_TO_NATIONAL_PARK_GATE_WP,
        "Route35NationalParkGate" , 10, dual_width=True
    )

    
    Route_36_National_Park_Gate_Links["ROUTE_36_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_LINK"] = WarpLink(
        Route_36_National_Park_Gate_Warp_Points.ROUTE_36_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_WP,
        National_Park_Warp_Points.NATIONAL_PARK_TO_ROUTE_36_NATIONAL_PARK_GATE_WP,
        "Route36NationalParkGate", dual_width=True
    )
    Route_36_National_Park_Gate_Links["ROUTE_36_NATIONAL_PARK_GATE_TO_ROUTE_36_LINK"] = WarpLink(
        Route_36_National_Park_Gate_Warp_Points.ROUTE_36_NATIONAL_PARK_GATE_TO_ROUTE_36_WP,
        Route_36_Warp_Points.ROUTE_36_TO_ROUTE_36_NATIONAL_PARK_GATE_WP,
        "Route36NationalParkGate" , 10, dual_width=True
    )

    

    Route_36_Ruins_Of_Alph_Gate_Links["ROUTE_36_RUINS_OF_ALPH_GATE_TO_ROUTE_36_LINK"] = WarpLink(
        Route_36_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_36_RUINS_OF_ALPH_GATE_TO_ROUTE_36_WP,
        Route_36_Warp_Points.ROUTE_36_TO_ROUTE_36_RUINS_OF_ALPH_GATE_WP,
        "Route36RuinsOfAlphGate",
        dual_width=True
    )

    Route_36_Ruins_Of_Alph_Gate_Links["ROUTE_36_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_LINK"] = WarpLink(
        Route_36_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_36_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_WP,
        Ruins_Of_Alph_Outside_Warp_Points.RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_32_RUINS_OF_ALPH_GATE_1_WP,
        "Route36RuinsOfAlphGate" , 10,
        dual_width=True
    )



    
    Route_38_Ecruteak_Gate_Links["ROUTE_38_ECRUTEAK_GATE_TO_ROUTE_38_LINK"] = WarpLink(
        Route_38_Ecruteak_Gate_Warp_Points.ROUTE_38_ECRUTEAK_GATE_TO_ROUTE_38_WP,
        Route_38_Warp_Points.ROUTE_38_TO_ROUTE_38_ECRUTEAK_GATE_WP,
        "Route38EcruteakGate", dual_width=True
    )
    Route_38_Ecruteak_Gate_Links["ROUTE_38_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_LINK"] = WarpLink(
        Route_38_Ecruteak_Gate_Warp_Points.ROUTE_38_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ROUTE_38_ECRUTEAK_GATE_WP,
        "Route38EcruteakGate" , 10, dual_width=True
    )

    

    Route_42_Ecruteak_Gate_Links["ROUTE_42_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_LINK"] = WarpLink(
        Route_42_Ecruteak_Gate_Warp_Points.ROUTE_42_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_WP,
        Ecruteak_City_Warp_Points.ECRUTEAK_CITY_TO_ROUTE_42_ECRUTEAK_GATE_WP,
        "Route42EcruteakGate", dual_width=True
    )

    Route_42_Ecruteak_Gate_Links["ROUTE_42_ECRUTEAK_GATE_TO_ROUTE_42_LINK"] = WarpLink(
        Route_42_Ecruteak_Gate_Warp_Points.ROUTE_42_ECRUTEAK_GATE_TO_ROUTE_42_WP,
        Route_42_Warp_Points.ROUTE_42_TO_ROUTE_42_ECRUTEAK_GATE_WP,
        "Route42EcruteakGate", 10, dual_width=True
    )


    
    Route_43_Gate_Links["ROUTE_43_GATE_TO_ROUTE_43_TOP_LINK"] = WarpLink(
        Route_43_Gate_Warp_Points.ROUTE_43_GATE_TO_ROUTE_43_TOP_WP,
        Route_43_Warp_Points.ROUTE_43_TO_ROUTE_43_GATE_TOP_WP,
        "Route43Gate", dual_width=True
    )
    Route_43_Gate_Links["ROUTE_43_GATE_TO_ROUTE_43_BOTTOM_LINK"] = WarpLink(
        Route_43_Gate_Warp_Points.ROUTE_43_GATE_TO_ROUTE_43_BOTTOM_WP,
        Route_43_Warp_Points.ROUTE_43_TO_ROUTE_43_GATE_BOTTOM_WP,
        "Route43Gate" , 10, dual_width=True
    )

    
    Route_43_Mahogany_Gate_Links["ROUTE_43_MAHOGANY_GATE_TO_ROUTE_43_LINK"] = WarpLink(
        Route_43_Mahogany_Gate_Warp_Points.ROUTE_43_MAHOGANY_GATE_TO_ROUTE_43_WP,
        Route_43_Warp_Points.ROUTE_43_TO_ROUTE_43_MAHOGANY_GATE_WP,
        "Route43MahoganyGate", dual_width=True
    )
    Route_43_Mahogany_Gate_Links["ROUTE_43_MAHOGANY_GATE_TO_MAHOGANY_TOWN_LINK"] = WarpLink(
        Route_43_Mahogany_Gate_Warp_Points.ROUTE_43_MAHOGANY_GATE_TO_MAHOGANY_TOWN_WP,
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_ROUTE_43_MAHOGANY_GATE_WP,
        "Route43MahoganyGate" , 10, dual_width=True
    )

#######################################################################
#                    Goldenrod Group                                  #
#######################################################################
    
    Goldenrod_City_Links["GOLDENROD_CITY_TO_GOLDENROD_GYM_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_GYM_WP,
        Goldenrod_Gym_Warp_Points.GOLDENROD_GYM_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity"
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_GOLDENROD_BIKE_SHOP_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_BIKE_SHOP_WP,
        Goldenrod_Bike_Shop_Warp_Points.GOLDENROD_BIKE_SHOP_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 5
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_GOLDENROD_HAPPINESS_RATER_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_HAPPINESS_RATER_WP,
        Goldenrod_Happiness_Rater_Warp_Points.GOLDENROD_HAPPINESS_RATER_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 10
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_BILLS_FAMILYS_HOUSE_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_BILLS_FAMILYS_HOUSE_WP,
        Bills_Familys_House_Warp_Points.BILLS_FAMILYS_HOUSE_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 15
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_GOLDENROD_MAGNET_TRAIN_STATION_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_MAGNET_TRAIN_STATION_WP,
        Goldenrod_Magnet_Train_Station_Warp_Points.GOLDENROD_MAGNET_TRAIN_STATION_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 20
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_GOLDENROD_FLOWER_SHOP_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_FLOWER_SHOP_WP,
        Goldenrod_Flower_Shop_Warp_Points.GOLDENROD_FLOWER_SHOP_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 25
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_GOLDENROD_PP_SPEECH_HOUSE_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_PP_SPEECH_HOUSE_WP,
        Goldenrod_PP_Speech_House_Warp_Points.GOLDENROD_PP_SPEECH_HOUSE_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 30
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_GOLDENROD_NAME_RATER_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_NAME_RATER_WP,
        Goldenrod_Name_Rater_Warp_Points.GOLDENROD_NAME_RATER_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 35
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_GOLDENROD_DEPT_STORE_1F_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_DEPT_STORE_1F_WP,
        Goldenrod_Dept_Store_1F_Warp_Points.GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_CITY_9_WP,
        "GoldenrodCity" , 40
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_GOLDENROD_GAME_CORNER_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_GAME_CORNER_WP,
        Goldenrod_Game_Corner_Warp_Points.GOLDENROD_GAME_CORNER_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 45
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_RADIO_TOWER_1F_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_RADIO_TOWER_1F_WP,
        Radio_Tower_1F_Warp_Points.RADIO_TOWER_1F_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 50
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_ROUTE_35_GOLDENROD_GATE_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_ROUTE_35_GOLDENROD_GATE_WP,
        Route_35_Goldenrod_Gate_Warp_Points.ROUTE_35_GOLDENROD_GATE_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 55
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_NORTH_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_NORTH_WP,
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_NORTH_WP,
        "GoldenrodCity" , 60
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_SOUTH_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_SOUTH_WP,
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_SOUTH_WP,
        "GoldenrodCity" , 65
    )

    Goldenrod_City_Links["GOLDENROD_CITY_TO_GOLDENROD_POKECENTER_1F_LINK"] = WarpLink(
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_POKECENTER_1F_WP,
        Goldenrod_Pokecenter_Warp_Points.GOLDENROD_POKECENTER_TO_GOLDENROD_CITY_WP,
        "GoldenrodCity" , 70
    )

    
    Bills_Familys_House_Links["BILLS_FAMILYS_HOUSE_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Bills_Familys_House_Warp_Points.BILLS_FAMILYS_HOUSE_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_BILLS_FAMILYS_HOUSE_WP,
        "BillsFamilysHouse", dual_width=True
    )

    
    Day_Care_Links["DAY_CARE_TO_ROUTE_34_FRONT_LINK"] = WarpLink(
        Day_Care_Warp_Points.DAY_CARE_TO_ROUTE_34_FRONT_WP,
        Route_34_Warp_Points.ROUTE_34_TO_DAY_CARE_FRONT_WP,
        "DayCare", dual_width=True
    )
    # DAY_CARE_TO_ROUTE_34_SIDE

    
    Goldenrod_Bike_Shop_Links["GOLDENROD_BIKE_SHOP_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Goldenrod_Bike_Shop_Warp_Points.GOLDENROD_BIKE_SHOP_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_BIKE_SHOP_WP,
        "GoldenrodBikeShop", dual_width=True
    )

    
    Goldenrod_Dept_Store_B1F_Links["GOLDENROD_DEPT_STORE_B1F_TO_UNDERGROUND_WAREHOUSE_LINK"] = WarpLink(
        Goldenrod_Dept_Store_B1F_Warp_Points.GOLDENROD_DEPT_STORE_B1F_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_3_WP,
        Goldenrod_Underground_Warehouse_Warp_Points.GOLDENROD_UNDERGROUND_WAREHOUSE_TO_GOLDENROD_DEPT_STORE_B1F_WP,
        "GoldenrodDeptStoreB1F", locked_by=[Unlock_Keys.KEY_CARD]
    )

    
    Goldenrod_Dept_Store_1F_Links["GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Goldenrod_Dept_Store_1F_Warp_Points.GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_CITY_9_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_DEPT_STORE_1F_WP,
        "GoldenrodDeptStore1F", dual_width=True
    )

    Goldenrod_Dept_Store_1F_Links["GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_DEPT_STORE_2F_2_LINK"] = WarpLink(
        Goldenrod_Dept_Store_1F_Warp_Points.GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_DEPT_STORE_2F_2_WP,
        Goldenrod_Dept_Store_2F_Warp_Points.GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_1F_3_WP,
        "GoldenrodDeptStore1F", 10
    )

    
    Goldenrod_Dept_Store_2F_Links["GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_3F_1_LINK"] = WarpLink(
        Goldenrod_Dept_Store_2F_Warp_Points.GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_3F_1_WP,
        Goldenrod_Dept_Store_3F_Warp_Points.GOLDENROD_DEPT_STORE_3F_TO_GOLDENROD_DEPT_STORE_2F_1_WP,
        "GoldenrodDeptStore2F"
    )

    Goldenrod_Dept_Store_2F_Links["GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_1F_3_LINK"] = WarpLink(
        Goldenrod_Dept_Store_2F_Warp_Points.GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_1F_3_WP,
        Goldenrod_Dept_Store_1F_Warp_Points.GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_DEPT_STORE_2F_2_WP,
        "GoldenrodDeptStore2F", 5
    )


    
    Goldenrod_Dept_Store_3F_Links["GOLDENROD_DEPT_STORE_3F_TO_GOLDENROD_DEPT_STORE_2F_1_LINK"] = WarpLink(
        Goldenrod_Dept_Store_3F_Warp_Points.GOLDENROD_DEPT_STORE_3F_TO_GOLDENROD_DEPT_STORE_2F_1_WP,
        Goldenrod_Dept_Store_2F_Warp_Points.GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_3F_1_WP,
        "GoldenrodDeptStore3F"
    )

    Goldenrod_Dept_Store_3F_Links["GOLDENROD_DEPT_STORE_3F_TO_GOLDENROD_DEPT_STORE_4F_2_LINK"] = WarpLink(
        Goldenrod_Dept_Store_3F_Warp_Points.GOLDENROD_DEPT_STORE_3F_TO_GOLDENROD_DEPT_STORE_4F_2_WP,
        Goldenrod_Dept_Store_4F_Warp_Points.GOLDENROD_DEPT_STORE_4F_TO_GOLDENROD_DEPT_STORE_3F_2_WP,
        "GoldenrodDeptStore3F", 5
    )

    
    Goldenrod_Dept_Store_4F_Links["GOLDENROD_DEPT_STORE_4F_TO_GOLDENROD_DEPT_STORE_5F_1_LINK"] = WarpLink(
        Goldenrod_Dept_Store_4F_Warp_Points.GOLDENROD_DEPT_STORE_4F_TO_GOLDENROD_DEPT_STORE_5F_1_WP,
        Goldenrod_Dept_Store_5F_Warp_Points.GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_4F_1_WP,
        "GoldenrodDeptStore4F"
    )

    Goldenrod_Dept_Store_4F_Links["GOLDENROD_DEPT_STORE_4F_TO_GOLDENROD_DEPT_STORE_3F_2_LINK"] = WarpLink(
        Goldenrod_Dept_Store_4F_Warp_Points.GOLDENROD_DEPT_STORE_4F_TO_GOLDENROD_DEPT_STORE_3F_2_WP,
        Goldenrod_Dept_Store_3F_Warp_Points.GOLDENROD_DEPT_STORE_3F_TO_GOLDENROD_DEPT_STORE_4F_2_WP,
        "GoldenrodDeptStore4F",5
    )

    
    Goldenrod_Dept_Store_5F_Links["GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_4F_1_LINK"] = WarpLink(
        Goldenrod_Dept_Store_5F_Warp_Points.GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_4F_1_WP,
        Goldenrod_Dept_Store_4F_Warp_Points.GOLDENROD_DEPT_STORE_4F_TO_GOLDENROD_DEPT_STORE_5F_1_WP,
        "GoldenrodDeptStore5F"
    )
    Goldenrod_Dept_Store_5F_Links["GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_6F_1_LINK"] = WarpLink(
        Goldenrod_Dept_Store_5F_Warp_Points.GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_6F_1_WP,
        Goldenrod_Dept_Store_6F_Warp_Points.GOLDENROD_DEPT_STORE_6F_TO_GOLDENROD_DEPT_STORE_5F_2_WP,
        "GoldenrodDeptStore5F", 5
    )

    
    Goldenrod_Dept_Store_6F_Links["GOLDENROD_DEPT_STORE_6F_TO_GOLDENROD_DEPT_STORE_5F_2_LINK"] = WarpLink(
        Goldenrod_Dept_Store_6F_Warp_Points.GOLDENROD_DEPT_STORE_6F_TO_GOLDENROD_DEPT_STORE_5F_2_WP,
        Goldenrod_Dept_Store_5F_Warp_Points.GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_6F_1_WP,
        "GoldenrodDeptStore6F"
    )
    Goldenrod_Dept_Store_6F_Links["GOLDENROD_DEPT_STORE_6F_TO_GOLDENROD_DEPT_STORE_ROOF_1_LINK"] = WarpLink(
        Goldenrod_Dept_Store_6F_Warp_Points.GOLDENROD_DEPT_STORE_6F_TO_GOLDENROD_DEPT_STORE_ROOF_1_WP,
        Goldenrod_Dept_Store_Roof_Warp_Points.GOLDENROD_DEPT_STORE_ROOF_TO_GOLDENROD_DEPT_STORE_6F_3_WP,
        "GoldenrodDeptStore6F", 10
    )

    
    Goldenrod_Dept_Store_Roof_Links["GOLDENROD_DEPT_STORE_ROOF_TO_GOLDENROD_DEPT_STORE_6F_3_LINK"] = WarpLink(
        Goldenrod_Dept_Store_Roof_Warp_Points.GOLDENROD_DEPT_STORE_ROOF_TO_GOLDENROD_DEPT_STORE_6F_3_WP,
        Goldenrod_Dept_Store_6F_Warp_Points.GOLDENROD_DEPT_STORE_6F_TO_GOLDENROD_DEPT_STORE_ROOF_1_WP,
        "GoldenrodDeptStoreRoof"
    )


    
    Goldenrod_Flower_Shop_Links["GOLDENROD_FLOWER_SHOP_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Goldenrod_Flower_Shop_Warp_Points.GOLDENROD_FLOWER_SHOP_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_FLOWER_SHOP_WP,
        "GoldenrodFlowerShop", dual_width=True
    )

    
    Goldenrod_Game_Corner_Links["GOLDENROD_GAME_CORNER_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Goldenrod_Game_Corner_Warp_Points.GOLDENROD_GAME_CORNER_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_GAME_CORNER_WP,
        "GoldenrodGameCorner", dual_width=True
    )

    
    Goldenrod_Gym_Links["GOLDENROD_GYM_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Goldenrod_Gym_Warp_Points.GOLDENROD_GYM_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_GYM_WP,
        "GoldenrodGym", dual_width=True, unlocks=[Unlock_Keys.BADGE_3]
    )

    
    Goldenrod_Happiness_Rater_Links["GOLDENROD_HAPPINESS_RATER_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Goldenrod_Happiness_Rater_Warp_Points.GOLDENROD_HAPPINESS_RATER_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_HAPPINESS_RATER_WP,
        "GoldenrodHappinessRater", dual_width=True
    )

    
    Goldenrod_Magnet_Train_Station_Links["GOLDENROD_MAGNET_TRAIN_STATION_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Goldenrod_Magnet_Train_Station_Warp_Points.GOLDENROD_MAGNET_TRAIN_STATION_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_MAGNET_TRAIN_STATION_WP,
        "GoldenrodMagnetTrainStation", dual_width=True
    )

    
    Goldenrod_Name_Rater_Links["GOLDENROD_NAME_RATER_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Goldenrod_Name_Rater_Warp_Points.GOLDENROD_NAME_RATER_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_NAME_RATER_WP,
        "GoldenrodNameRater", dual_width=True
    )

    
    Goldenrod_Pokecenter_Links["GOLDENROD_POKECENTER_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Goldenrod_Pokecenter_Warp_Points.GOLDENROD_POKECENTER_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_POKECENTER_1F_WP,
        "GoldenrodPokecenter1F", dual_width=True
    )

    Goldenrod_Pokecenter_Links["GOLDENROD_POKECENTER_1F_TO_GOLDENROD_POKECENTER_2F_LINK"] = WarpLink(
        Goldenrod_Pokecenter_Warp_Points.GOLDENROD_POKECENTER_TO_GOLDENROD_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "GoldenrodPokecenter1F", 15
    )

    
    Goldenrod_PP_Speech_House_Links["GOLDENROD_PP_SPEECH_HOUSE_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Goldenrod_PP_Speech_House_Warp_Points.GOLDENROD_PP_SPEECH_HOUSE_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_PP_SPEECH_HOUSE_WP,
        "GoldenrodPPSpeechHouse", dual_width=True
    )

    
    Goldenrod_Underground_Warehouse_Links["GOLDENROD_UNDERGROUND_WAREHOUSE_TO_GOLDENROD_DEPT_STORE_B1F_LINK"] = WarpLink(
        Goldenrod_Underground_Warehouse_Warp_Points.GOLDENROD_UNDERGROUND_WAREHOUSE_TO_GOLDENROD_DEPT_STORE_B1F_WP,
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH_WP, #This is the wrong link but doesn't matter
        "GoldenrodUndergroundWarehouse", 10, unlocks=[Unlock_Keys.KEY_CARD]
    )


    

    #This is the entry stair in the actual switch room
    Goldenrod_Underground_Switch_Room_Entrance_Links["GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_LINK"] = WarpLink(
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_WP,
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH_WP,
        "GoldenrodUndergroundSwitchRoomEntrances",
    )

    Goldenrod_Underground_Switch_Room_Entrance_Links["GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_SOUTH_LINK"] = WarpLink(
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_SOUTH_WP,
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_WP,
        "GoldenrodUndergroundSwitchRoomEntrances", 15
    )

    Goldenrod_Underground_Switch_Room_Entrance_Links["GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_SOUTH_LINK"] = WarpLink(
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_SOUTH_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_SOUTH_WP,
        "GoldenrodUndergroundSwitchRoomEntrances", 20, dual_width=True
    )

    Goldenrod_Underground_Switch_Room_Entrance_Links["GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_NORTH_LINK"] = WarpLink(
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_NORTH_WP,
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_NORTH_WP,
        "GoldenrodUndergroundSwitchRoomEntrances", 30
    )

    Goldenrod_Underground_Switch_Room_Entrance_Links["GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_NORTH_LINK"] = WarpLink(
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_CITY_NORTH_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_NORTH_WP,
        "GoldenrodUndergroundSwitchRoomEntrances" , 35, dual_width=True
    )

    

    Goldenrod_Underground_Links["GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_NORTH_LINK"] = WarpLink(
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_NORTH_WP,
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_NORTH_WP,
        "GoldenrodUnderground"
    )

    Goldenrod_Underground_Links["GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH_LINK"] = WarpLink(
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_SOUTH_WP,
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_SOUTH_WP,
        "GoldenrodUnderground", 5

    )
    Goldenrod_Underground_Links["GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_KEY_DOOR_LINK"] = WarpLink(
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_KEY_DOOR_WP,
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_STAIR_WP,
        "GoldenrodUnderground", 10

    )
    Goldenrod_Underground_Links["GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_STAIR_LINK"] = WarpLink(
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_STAIR_WP,
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_KEY_DOOR_WP,
        "GoldenrodUnderground", 15, dual_width=True
    )

    Goldenrod_Underground_Links["GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_LINK"] = WarpLink(
        Goldenrod_Underground_Warp_Points.GOLDENROD_UNDERGROUND_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_WP,
        Goldenrod_Underground_Switch_Room_Entrances_Warp_Points.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES_TO_GOLDENROD_UNDERGROUND_WP,
        "GoldenrodUnderground", 25
    )




#Todo check if keycard early allows you to clear radio tower, or if you need the 7 badge trigger
    #You need the 7 badge, otherwise you get Object Event
    
    Radio_Tower_1F_Links["RADIO_TOWER_1F_TO_GOLDENROD_CITY_LINK"] = WarpLink(
        Radio_Tower_1F_Warp_Points.RADIO_TOWER_1F_TO_GOLDENROD_CITY_WP,
        Goldenrod_City_Warp_Points.GOLDENROD_CITY_TO_RADIO_TOWER_1F_WP,
        "RadioTower1F", dual_width=True, unlocks=[Unlock_Keys.CAN_CLEAR_RADIO_TOWER_ROCKETS, Unlock_Keys.RADIO_CARD],
        locked_by=[Unlock_Keys.KEY_CARD]
    )
    # RADIO_TOWER_1F_TO_RADIO_TOWER_2F_LINK


#######################################################################
#                    Indigo Group                                     #
#######################################################################

    
    Kogas_Room_Links["KOGAS_ROOM_TO_WILLS_ROOM_LINK"] = WarpLink(
        Kogas_Room_Warp_Points.KOGAS_ROOM_TO_WILLS_ROOM_WP,
        Wills_Room_Warp_Points.WILLS_ROOM_TO_KOGAS_ROOM_WP,
        "KogasRoom", dual_width=True, unlocks=[Unlock_Keys.E4_KOGA])

    Kogas_Room_Links["KOGAS_ROOM_TO_BRUNOS_ROOM_LINK"] = WarpLink(
        Kogas_Room_Warp_Points.KOGAS_ROOM_TO_BRUNOS_ROOM_WP,
        Brunos_Room_Warp_Points.BRUNOS_ROOM_TO_KOGAS_ROOM_WP,
        "KogasRoom", 10, dual_width=True, unlocks=[Unlock_Keys.E4_KOGA]
    )

    
    Wills_Room_Links["WILLS_ROOM_TO_INDIGO_PLATEAU_POKECENTER_1F_LINK"] = WarpLink(
        Wills_Room_Warp_Points.WILLS_ROOM_TO_INDIGO_PLATEAU_POKECENTER_1F_WP,
        Indigo_Plateau_Pokecenter_1F_Warp_Points.INDIGO_PLATEAU_POKECENTER_1F_TO_WILLS_ROOM_1_WP,    #CHANGE THIS IN THE FUTURE (THIS ISNT THE ACTUAL LINK)
        "WillsRoom", unlocks=[Unlock_Keys.E4_WILL]
    )

    Wills_Room_Links["WILLS_ROOM_TO_KOGAS_ROOM_LINK"] = WarpLink(
        Wills_Room_Warp_Points.WILLS_ROOM_TO_KOGAS_ROOM_WP,
        Kogas_Room_Warp_Points.KOGAS_ROOM_TO_WILLS_ROOM_WP,
        "WillsRoom", 5, dual_width=True, unlocks=[Unlock_Keys.E4_WILL]
    )

    
    Karens_Room_Links["KARENS_ROOM_TO_BRUNOS_ROOM_LINK"] = WarpLink(
        Karens_Room_Warp_Points.KARENS_ROOM_TO_BRUNOS_ROOM_WP,
        Brunos_Room_Warp_Points.BRUNOS_ROOM_TO_KARENS_ROOM_WP,
        "KarensRoom", dual_width=True, unlocks=[Unlock_Keys.E4_KAREN]
    )

    Karens_Room_Links["KARENS_ROOM_TO_LANCES_ROOM_LINK"] = WarpLink(
        Karens_Room_Warp_Points.KARENS_ROOM_TO_LANCES_ROOM_WP,
        Lances_Room_Warp_Points.LANCES_ROOM_TO_KARENS_ROOM_WP,
        "KarensRoom", 10, dual_width=True, unlocks=[Unlock_Keys.E4_KAREN]
    )

    
    Brunos_Room_Links["BRUNOS_ROOM_TO_KOGAS_ROOM_LINK"] = WarpLink(
        Brunos_Room_Warp_Points.BRUNOS_ROOM_TO_KOGAS_ROOM_WP,
        Kogas_Room_Warp_Points.KOGAS_ROOM_TO_BRUNOS_ROOM_WP,
        "BrunosRoom", dual_width=True, unlocks=[Unlock_Keys.E4_BRUNO]
    )

    Brunos_Room_Links["BRUNOS_ROOM_TO_KARENS_ROOM_LINK"] = WarpLink(
        Brunos_Room_Warp_Points.BRUNOS_ROOM_TO_KARENS_ROOM_WP,
        Karens_Room_Warp_Points.KARENS_ROOM_TO_BRUNOS_ROOM_WP,
        "BrunosRoom", 10, dual_width=True, unlocks=[Unlock_Keys.E4_BRUNO]
    )

    
    Lances_Room_Links["LANCES_ROOM_TO_KARENS_ROOM_LINK"] = WarpLink(
        Lances_Room_Warp_Points.LANCES_ROOM_TO_KARENS_ROOM_WP,
        Karens_Room_Warp_Points.KARENS_ROOM_TO_LANCES_ROOM_WP,
        "LancesRoom", dual_width=True, unlocks=[Unlock_Keys.CHAMPION_LANCE]
    )


#######################################################################
#                    Mahogany Group                                   #
#######################################################################
    
    Mahogany_Town_Links["MAHOGANY_TOWN_TO_MAHOGANY_MART_1F_LINK"] = WarpLink(
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_MART_1F_WP,
        Mahogany_Mart_Warp_Points.MAHOGANY_MART_1F_TO_MAHOGANY_TOWN_WP,
        "MahoganyTown"
    )
    Mahogany_Town_Links["MAHOGANY_TOWN_TO_MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_LINK"] = WarpLink(
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_WP,
        Mahogany_Red_Gyarados_Speech_House_Warp_Points.MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_TO_MAHOGANY_TOWN_WP,
        "MahoganyTown" , 5
    )
    Mahogany_Town_Links["MAHOGANY_TOWN_TO_MAHOGANY_GYM_LINK"] = WarpLink(
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_GYM_WP,
        Mahogany_Gym_Warp_Points.MAHOGANY_GYM_TO_MAHOGANY_TOWN_WP,
        "MahoganyTown" , 10, locked_by=[Unlock_Keys.CAN_CLEAR_MAHOGANY_ROCKETS]
    )
    Mahogany_Town_Links["MAHOGANY_TOWN_TO_MAHOGANY_POKECENTER_1F_LINK"] = WarpLink(
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_POKECENTER_1F_WP,
        Mahogany_Pokecenter_Warp_Points.MAHOGANY_POKECENTER_1F_TO_MAHOGANY_TOWN_WP,
        "MahoganyTown" , 15
    )
    Mahogany_Town_Links["MAHOGANY_TOWN_TO_ROUTE_43_MAHOGANY_GATE_LINK"] = WarpLink(
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_ROUTE_43_MAHOGANY_GATE_WP,
        Route_43_Mahogany_Gate_Warp_Points.ROUTE_43_MAHOGANY_GATE_TO_MAHOGANY_TOWN_WP,
        "MahoganyTown" , 20
    )

    
    Mahogany_Gym_Links["MAHOGANY_GYM_TO_MAHOGANY_TOWN_LINK"] = WarpLink(
        Mahogany_Gym_Warp_Points.MAHOGANY_GYM_TO_MAHOGANY_TOWN_WP,
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_GYM_WP,
        "MahoganyGym", dual_width=True, unlocks=[Unlock_Keys.BADGE_7]
    )

    
    Mahogany_Mart_Links["MAHOGANY_MART_1F_TO_MAHOGANY_TOWN_LINK"] = WarpLink(
        Mahogany_Mart_Warp_Points.MAHOGANY_MART_1F_TO_MAHOGANY_TOWN_WP,
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_MART_1F_WP,
        "MahoganyMart1F", dual_width=True, unlocks=[Unlock_Keys.CAN_CLEAR_MAHOGANY_ROCKETS, Unlock_Keys.HM_WHIRLPOOL],
        locked_by=[Unlock_Keys.CAN_SURF, Unlock_Keys.LAKE_OF_RAGE_FOUND]
    )

    # MAHOGANY_MART_1F_TO_TEAM_ROCKET_BASE_B1F_LINK"] = WarpLink(
    #     Mahogany_Mart_Warp_Points.MAHOGANY_MART_1F_TO_TEAM_ROCKET_BASE_B1F_WP,
    #     Team_Rocket_Base_B1F_Warp_Points.,
    #     0x0006C600,10
    # )

    
    Mahogany_Pokecenter_Links["MAHOGANY_POKECENTER_1F_TO_MAHOGANY_TOWN_LINK"] = WarpLink(
        Mahogany_Pokecenter_Warp_Points.MAHOGANY_POKECENTER_1F_TO_MAHOGANY_TOWN_WP,
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_POKECENTER_1F_WP,
        "MahoganyPokecenter1F", dual_width=True
    )

    Mahogany_Pokecenter_Links["MAHOGANY_POKECENTER_1F_TO_MAHOGANY_POKECENTER_2F_LINK"] = WarpLink(
        Mahogany_Pokecenter_Warp_Points.MAHOGANY_POKECENTER_TO_MAHOGANY_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "MahoganyPokecenter1F", 10
    )

    
    Mahogany_Red_Gyarados_Speech_House_Links["MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_TO_MAHOGANY_TOWN"] = WarpLink(
        Mahogany_Red_Gyarados_Speech_House_Warp_Points.MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_TO_MAHOGANY_TOWN_WP,
        Mahogany_Town_Warp_Points.MAHOGANY_TOWN_TO_MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_WP,
        "MahoganyRedGyaradosSpeechHouse", dual_width=True
    )


#######################################################################
#                    New Bark Group                                   #
#######################################################################

    # 
    #lugia coords are 01 03 49
    # 0018C546 is lugia coords, 0C 11 coordinates to 13, 8 for some reason
    #set above to 0F to be on shoreline
    # 01 0F 0C
    #set 0007 723C to 3E instaed of 41 to make ho oh always present

    #lugia presence, set 0018C510 to 12 instead of 15
    # NEW_BARK_TO_PLAYERS_NEIGHBORS_HOUSE_LINK"] = WarpLink(
    #     New_Bark_Warp_Points.NEW_BARK_TO_PLAYERS_NEIGHBORS_HOUSE_WP,
    #     Players_Neighbors_House_Warp_Points.PLAYERS_NEIGHBORS_HOUSE_TO_NEW_BARK_WP,
    #      "NewBarkTown" , 10)
    #
    # NEW_BARK_TO_ELMS_HOUSE_LINK"] = WarpLink(
    #     New_Bark_Warp_Points.NEW_BARK_TO_ELMS_HOUSE_WP,
    #     Elms_House_Warp_Points.ELMS_HOUSE_TO_NEW_BARK_WP,
    #     "NewBarkTown" , 15)

    # Don't Randomize Elms Lab :P You need that starter pokemon
    # NEW_BARK_TO_ELMS_LAB_LINK"] = WarpLink(
    #     New_Bark_Warp_Points.NEW_BARK_TO_ELMS_LAB_WP,
    #     Elms_Lab_Warp_Points.ELMS_LAB_TO_NEW_BARK_WP,
    #     0x001A8352)

    

    Players_Neighbors_House_Links["PLAYERS_NEIGHBORS_HOUSE_TO_NEW_BARK_LINK"] = WarpLink(
        Players_Neighbors_House_Warp_Points.PLAYERS_NEIGHBORS_HOUSE_TO_NEW_BARK_WP,
        New_Bark_Warp_Points.NEW_BARK_TO_PLAYERS_NEIGHBORS_HOUSE_WP,
        "PlayersNeighborsHouse",
        dual_width=True)

    

    Elms_House_Links["ELMS_HOUSE_TO_NEW_BARK_LINK"] = WarpLink(
        Elms_House_Warp_Points.ELMS_HOUSE_TO_NEW_BARK_WP,
        New_Bark_Warp_Points.NEW_BARK_TO_ELMS_HOUSE_WP,
        "ElmsHouse",
        dual_width=True)

#######################################################################
#                    Olivine Group                                    #
#######################################################################
    



    Olivine_City_Links["OLIVINE_CITY_TO_OLIVINE_POKECENTER_LINK"] = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_POKECENTER_1F_WP,
        Olivine_Pokecenter_Warp_Points.OLIVINE_POKECENTER_TO_OLIVINE_CITY_WP,
        "OlivineCity")

    Olivine_City_Links["OLIVINE_CITY_TO_OLIVINE_GYM_LINK"] = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_GYM_WP,
        Olivine_Gym_Warp_Points.OLIVINE_GYM_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 5)

    Olivine_City_Links["OLIVINE_CITY_TO_OLIVINE_TIMS_HOUSE_LINK"] = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_TIMS_HOUSE_WP,
        Olivine_Tims_House_Warp_Points.OLIVINE_TIMS_HOUSE_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 10)

    Olivine_City_Links["OLIVINE_CITY_TO_OLIVINE_SPEECH_HOUSE_LINK"] = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_PUNISHMENT_SPEECH_HOUSE_WP,
        Olivine_Punishment_Speech_House_Warp_Points.OLIVINE_PUNISHMENT_SPEECH_HOUSE_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 20)

    Olivine_City_Links["OLIVINE_CITY_TO_OLIVINE_GOOD_ROD_HOUSE_LINK"] = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_GOOD_ROD_HOUSE_WP,
        Olivine_Good_Rod_House_Warp_Points.OLIVINE_GOOD_ROD_HOUSE_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 25)

    Olivine_City_Links["OLIVINE_CITY_TO_OLIVINE_CAFE_LINK"] = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_CAFE_WP,
        Olivine_Cafe_Warp_Points.OLIVINE_CAFE_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 30)

    Olivine_City_Links["OLIVINE_CITY_TO_OLIVINE_MART_LINK"] = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_MART_WP,
        Olivine_Mart_Warp_Points.OLIVINE_MART_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 35)

    Olivine_City_Links["OLIVINE_CITY_TO_OLIVINE_LIGHTHOUSE_1F_LINK"] = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_LIGHTHOUSE_1F_WP,
        Olivine_Lighthouse_1F_Warp_Points.OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 40)

    Olivine_City_Links["OLIVINE_CITY_TO_OLIVINE_PORT_PASSAGE_LINK"] = WarpLink(
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_PORT_PASSAGE_WP,
        Olivine_Port_Passage_Warp_Points.OLIVINE_PORT_PASSAGE_TO_OLIVINE_CITY_WP,
        "OlivineCity" , 45,
        dual_width=True)

    

    Olivine_Cafe_Links["OLIVINE_CAFE_TO_OLIVINE_CITY_LINK"] = WarpLink(
        Olivine_Cafe_Warp_Points.OLIVINE_CAFE_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_CAFE_WP,
        "OlivineCafe",
        dual_width=True,
        unlocks=[Unlock_Keys.HM_STRENGTH])

    

    Olivine_Good_Rod_House_Links["OLIVINE_GOOD_ROD_HOUSE_TO_OLIVINE_CITY_LINK"] = WarpLink(
        Olivine_Good_Rod_House_Warp_Points.OLIVINE_GOOD_ROD_HOUSE_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_GOOD_ROD_HOUSE_WP,
        "OlivineGoodRodHouse",
        dual_width=True)

    

    Olivine_Gym_Links["OLIVINE_GYM_TO_OLIVINE_CITY_LINK"] = WarpLink(
        Olivine_Gym_Warp_Points.OLIVINE_GYM_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_GYM_WP,
        "OlivineGym",
        dual_width=True, locked_by=[Unlock_Keys.OLIVINE_MEDICINE],
        unlocks=[Unlock_Keys.BADGE_6])

    

    Olivine_Lighthouse_1F_Links["OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_CITY_LINK"] = WarpLink(
        Olivine_Lighthouse_1F_Warp_Points.OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_LIGHTHOUSE_1F_WP,
        "OlivineLighthouse1F",
        dual_width=True)

    Olivine_Lighthouse_1F_Links["OLIVINE_LIGHTHOUSE_1F_TO_2F_STAIR_LINK"] = WarpLink(
        Olivine_Lighthouse_1F_Warp_Points.OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_LIGHTHOUSE_2FA_WP,
        Olivine_Lighthouse_2F_Warp_Points.OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_1FA_WP,
        "OlivineLighthouse1F" , 10)

    

    Olivine_Lighthouse_2F_Links["OLIVINE_LIGHTHOUSE_2F_TO_1F_STAIR_LINK"] = WarpLink(
        Olivine_Lighthouse_2F_Warp_Points.OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_1FA_WP,
        Olivine_Lighthouse_1F_Warp_Points.OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_LIGHTHOUSE_2FA_WP,
        "OlivineLighthouse2F")

    Olivine_Lighthouse_2F_Links["OLIVINE_LIGHTHOUSE_2F_TO_3F_STAIR_LINK"] = WarpLink(
        Olivine_Lighthouse_2F_Warp_Points.OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_3FA_WP,
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_2FA_WP,
        "OlivineLighthouse2F" , 5)

    Olivine_Lighthouse_2F_Links["OLIVINE_LIGHTHOUSE_2F_TO_1F_PITFALL_LINK"] = WarpLink(
        Olivine_Lighthouse_2F_Warp_Points.OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_1FB_WP,
        Olivine_Lighthouse_1F_Warp_Points.OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_LIGHTHOUSE_2FB_WP,
        "OlivineLighthouse2F" , 10,
        dual_width=True)

    

    Olivine_Lighthouse_3F_Links["OLIVINE_LIGHTHOUSE_3F_TO_4F_RIGHT_STAIR_LINK"] = WarpLink(
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FA_WP,
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FA_WP,
        "OlivineLighthouse3F")

    Olivine_Lighthouse_3F_Links["OLIVINE_LIGHTHOUSE_3F_TO_2F_STAIR_LINK"] = WarpLink(
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_2FA_WP,
        Olivine_Lighthouse_2F_Warp_Points.OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_3FA_WP,
        "OlivineLighthouse3F" , 5)

    Olivine_Lighthouse_3F_Links["OLIVINE_LIGHTHOUSE_3F_TO_4F_MIDDLE_STAIR_LINK"] = WarpLink(
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FB_WP,
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FB_WP,
        "OlivineLighthouse3F" , 10)

    Olivine_Lighthouse_3F_Links["OLIVINE_LIGHTHOUSE_3F_TO_2F_PITFALL_LINK"] = WarpLink(
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_2FB_WP,
        Olivine_Lighthouse_2F_Warp_Points.OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_3FB_WP,
        "OlivineLighthouse3F" , 15,
        dual_width=True)

    

    Olivine_Lighthouse_4F_Links["OLIVINE_LIGHTHOUSE_4F_TO_3F_STAIR_1_LINK"] = WarpLink(
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FA_WP,
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FA_WP,
        "OlivineLighthouse4F")

    Olivine_Lighthouse_4F_Links["OLIVINE_LIGHTHOUSE_4F_TO_5F_STAIR_1_LINK"] = WarpLink(
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FA_WP,
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FA_WP,
        "OlivineLighthouse4F" , 5)

    Olivine_Lighthouse_4F_Links["OLIVINE_LIGHTHOUSE_4F_TO_5F_STAIR_2_LINK"] = WarpLink(
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FB_WP,
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FB_WP,
        "OlivineLighthouse4F" , 10)

    Olivine_Lighthouse_4F_Links["OLIVINE_LIGHTHOUSE_4F_TO_3F_STAIR_2_LINK"] = WarpLink(
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FB_WP,
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FB_WP,
        "OlivineLighthouse4F" , 15)

    Olivine_Lighthouse_4F_Links["OLIVINE_LIGHTHOUSE_4F_TO_3F_PITFALL_1_LINK"] = WarpLink(
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FC_WP,
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FC_WP,
        "OlivineLighthouse4F" , 20,
        dual_width=True)

    Olivine_Lighthouse_4F_Links["OLIVINE_LIGHTHOUSE_4F_TO_3F_PITFALL_2_LINK"] = WarpLink(
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FD_WP,
        Olivine_Lighthouse_3F_Warp_Points.OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FD_WP,
        "OlivineLighthouse4F" , 30,
        dual_width=True)

    

    Olivine_Lighthouse_5F_Links["OLIVINE_LIGHTHOUSE_5F_TO_6F_STAIR_LINK"] = WarpLink(
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_6FA_WP,
        Olivine_Lighthouse_6F_Warp_Points.OLIVINE_LIGHTHOUSE_6F_TO_OLIVINE_LIGHTHOUSE_5FA_WP,
        "OlivineLighthouse5F")


    Olivine_Lighthouse_5F_Links["OLIVINE_LIGHTHOUSE_5F_TO_4F_OUTER_STAIR_LINK"] = WarpLink(
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FA_WP,
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FA_WP,
        "OlivineLighthouse5F" , 5)

    Olivine_Lighthouse_5F_Links["OLIVINE_LIGHTHOUSE_5F_TO_4F_INNER_STAIR_LINK"] = WarpLink(
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FB_WP,
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FB_WP,
        "OlivineLighthouse5F" , 10)

    Olivine_Lighthouse_5F_Links["OLIVINE_LIGHTHOUSE_5F_TO_4F_PITFALL_LINK"] = WarpLink(
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FC_WP,
        Olivine_Lighthouse_4F_Warp_Points.OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FC_WP,
        "OlivineLighthouse5F" , 15,
        dual_width=True)

    

    Olivine_Lighthouse_6F_Links["OLIVINE_LIGHTHOUSE_6F_TO_5F_STAIR_LINK"] = WarpLink(
        Olivine_Lighthouse_6F_Warp_Points.OLIVINE_LIGHTHOUSE_6F_TO_OLIVINE_LIGHTHOUSE_5FA_WP,
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_6FA_WP,
        "OlivineLighthouse6F", unlocks=[Unlock_Keys.TOP_OF_LIGHTHOUSE_FOUND]
    )

    Olivine_Lighthouse_6F_Links["OLIVINE_LIGHTHOUSE_6F_TO_5F_PITFALL_LINK"] = WarpLink(
        Olivine_Lighthouse_6F_Warp_Points.OLIVINE_LIGHTHOUSE_6F_TO_OLIVINE_LIGHTHOUSE_5FB_WP,
        Olivine_Lighthouse_5F_Warp_Points.OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_6FB_WP,
        "OlivineLighthouse6F" , 5,dual_width=True, unlocks=[Unlock_Keys.TOP_OF_LIGHTHOUSE_FOUND]
    )

    

    Olivine_Mart_Links["OLIVINE_MART_TO_OLIVINE_CITY_LINK"] = WarpLink(
        Olivine_Mart_Warp_Points.OLIVINE_MART_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_MART_WP,
        "OlivineMart",
        dual_width=True)

    

    Olivine_Pokecenter_Links["OLIVINE_POKECENTER_TO_OLIVINE_CITY_LINK"] = WarpLink(
        Olivine_Pokecenter_Warp_Points.OLIVINE_POKECENTER_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_POKECENTER_1F_WP,
        "OlivinePokecenter1F",
        dual_width=True)

    Olivine_Pokecenter_Links["OLIVINE_POKECENTER_1F_TO_OLIVINE_POKECENTER_2F_LINK"] = WarpLink(
        Olivine_Pokecenter_Warp_Points.OLIVINE_POKECENTER_TO_OLIVINE_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "OlivinePokecenter1F", 10
    )

    #Currently left Vanilla can become togglable in the future
    # 
    #
    # Olivine_Port_Passage_Links["OLIVINE_PORT_PASSAGE_TO_OLIVINE_CITY_LINK"] = WarpLink(
    #     Olivine_Port_Passage_Warp_Points.OLIVINE_PORT_PASSAGE_TO_OLIVINE_CITY_WP,
    #     Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_PORT_PASSAGE_WP,
    #     "OlivinePortPassage",
    #     dual_width=True)

#     ADD OTHER LINKS WHEN THEIR WARP POINTS EXIST

    

    Olivine_Punishment_Speech_House_Links["OLIVINE_PUNISHMENT_SPEECH_HOUSE_TO_OLIVINE_CITY_LINK"] = WarpLink(
        Olivine_Punishment_Speech_House_Warp_Points.OLIVINE_PUNISHMENT_SPEECH_HOUSE_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_PUNISHMENT_SPEECH_HOUSE_WP,
        "OlivinePunishmentSpeechHouse",
        dual_width=True)

    

    Olivine_Tims_House_Links["OLIVINE_TIMS_HOUSE_TO_OLIVINE_CITY_LINK"] = WarpLink(
        Olivine_Tims_House_Warp_Points.OLIVINE_TIMS_HOUSE_TO_OLIVINE_CITY_WP,
        Olivine_City_Warp_Points.OLIVINE_CITY_TO_OLIVINE_TIMS_HOUSE_WP,
        "OlivineTimsHouse",
        dual_width=True)

#######################################################################
#                    Routes Group                                     #
#######################################################################

    

    Indigo_Plateau_Pokecenter_1F_Links["INDIGO_PLATEAU_POKECENTER_1F_TO_ROUTE_23_1_LINK"] = WarpLink(
        Indigo_Plateau_Pokecenter_1F_Warp_Points.INDIGO_PLATEAU_POKECENTER_1F_TO_ROUTE_23_1_WP,
        Route23_Warp_Points.ROUTE23_TO_INDIGO_PLATEAU_POKECENTER_1F_1_WP,
        "IndigoPlateauPokecenter1F", dual_width=True)

    Indigo_Plateau_Pokecenter_1F_Links["INDIGO_PLATEAU_POKECENTER_1F_TO_POKECENTER_2F_1_LINK"] = WarpLink(
        Indigo_Plateau_Pokecenter_1F_Warp_Points.INDIGO_PLATEAU_POKECENTER_1F_TO_POKECENTER_2F_1_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "IndigoPlateauPokecenter1F", 10
    )

    Indigo_Plateau_Pokecenter_1F_Links["INDIGO_PLATEAU_POKECENTER_1F_TO_WILLS_ROOM_1_LINK"] = WarpLink(
        Indigo_Plateau_Pokecenter_1F_Warp_Points.INDIGO_PLATEAU_POKECENTER_1F_TO_WILLS_ROOM_1_WP,
        Wills_Room_Warp_Points.WILLS_ROOM_TO_INDIGO_PLATEAU_POKECENTER_1F_WP,
        "IndigoPlateauPokecenter1F", 15
    )


    

    Route23_Links["ROUTE23_TO_INDIGO_PLATEAU_POKECENTER_1F_1_LINK"] = WarpLink(
        Route23_Warp_Points.ROUTE23_TO_INDIGO_PLATEAU_POKECENTER_1F_1_WP,
        Indigo_Plateau_Pokecenter_1F_Warp_Points.INDIGO_PLATEAU_POKECENTER_1F_TO_ROUTE_23_1_WP,
        "Route23", dual_width=True)

    Route23_Links["ROUTE23_TO_VICTORY_ROAD_10_LINK"] = WarpLink(
        Route23_Warp_Points.ROUTE23_TO_VICTORY_ROAD_10_WP,
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_ROUTE_23_3_WP,
        "Route23", 10, dual_width=True)

    
    Day_Of_Week_Siblings_House_Links["DAY_OF_WEEK_SIBLINGS_HOUSE_TO_ROUTE_26_3_LINK"] = WarpLink(
        Day_Of_Week_Siblings_House_Warp_Points.DAY_OF_WEEK_SIBLINGS_HOUSE_TO_ROUTE_26_3_WP,
        Route_26_Warp_Points.ROUTE_26_TO_DAY_OF_WEEK_SIBLINGS_HOUSE_1_WP,
        "DayOfWeekSiblingsHouse", dual_width=True)


    
    Route_26_Heal_House_Links["ROUTE_26_HEAL_HOUSE_TO_ROUTE_26_2_LINK"] = WarpLink(
        Route_26_Heal_House_Warp_Points.ROUTE_26_HEAL_HOUSE_TO_ROUTE_26_2_WP,
        Route_26_Warp_Points.ROUTE_26_TO_ROUTE_26_HEAL_HOUSE_1_WP,
        "Route26HealHouse", dual_width=True)


    
    Route_27_Sandstorm_House_Links["ROUTE_27_SANDSTORM_HOUSE_TO_ROUTE_27_1_LINK"] = WarpLink(
        Route_27_Sandstorm_House_Warp_Points.ROUTE27_SANDSTORM_HOUSE_TO_ROUTE_27_1_WP,
        Route_27_Warp_Points.ROUTE_27_TO_ROUTE_27_SANDSTORM_HOUSE_1_WP,
        "Route27SandstormHouse", dual_width=True)

    

    Route_26_Links["ROUTE_26_TO_VICTORY_ROAD_GATE_3_LINK"] = WarpLink(
        Route_26_Warp_Points.ROUTE_26_TO_VICTORY_ROAD_GATE_3_WP,
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_ROUTE_26_1_WP,
        "Route26")

    Route_26_Links["ROUTE_26_TO_ROUTE_26_HEAL_HOUSE_1_LINK"] = WarpLink(
        Route_26_Warp_Points.ROUTE_26_TO_ROUTE_26_HEAL_HOUSE_1_WP,
        Route_26_Heal_House_Warp_Points.ROUTE_26_HEAL_HOUSE_TO_ROUTE_26_2_WP,
        "Route26", 5)

    Route_26_Links["ROUTE_26_TO_DAY_OF_WEEK_SIBLINGS_HOUSE_1_LINK"] = WarpLink(
        Route_26_Warp_Points.ROUTE_26_TO_DAY_OF_WEEK_SIBLINGS_HOUSE_1_WP,
        Day_Of_Week_Siblings_House_Warp_Points.DAY_OF_WEEK_SIBLINGS_HOUSE_TO_ROUTE_26_3_WP,
        "Route26", 10)


    

    Route_27_Links["ROUTE_27_TO_ROUTE_27_SANDSTORM_HOUSE_1_LINK"] = WarpLink(
        Route_27_Warp_Points.ROUTE_27_TO_ROUTE_27_SANDSTORM_HOUSE_1_WP,
        Route_27_Sandstorm_House_Warp_Points.ROUTE27_SANDSTORM_HOUSE_TO_ROUTE_27_1_WP,
        "Route27")

    Route_27_Links["ROUTE_27_TO_TOHJO_FALLS_1_LINK"] = WarpLink(
        Route_27_Warp_Points.ROUTE_27_TO_TOHJO_FALLS_1_WP,
        Tohjo_Falls_Warp_Points.TOHJO_FALLS_TO_ROUTE_27_2_WP,
        "Route27", 5)

    Route_27_Links["ROUTE_27_TO_TOHJO_FALLS_2_LINK"] = WarpLink(
        Route_27_Warp_Points.ROUTE_27_TO_TOHJO_FALLS_2_WP,
        Tohjo_Falls_Warp_Points.TOHJO_FALLS_TO_ROUTE_27_3_WP,
        "Route27", 10)


    

    Route_41_Links["ROUTE_41_TO_WHIRL_ISLAND_NW_LINK"] = WarpLink(
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_NW_WP,
        Whirl_Island_NW_Warp_Points.WHIRL_ISLAND_N_W_TO_ROUTE_41_1_WP,
        "Route41")

    Route_41_Links["ROUTE_41_TO_WHIRL_ISLAND_NE_LINK"] = WarpLink(
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_NE_WP,
        Whirl_Island_NE_Warp_Points.WHIRL_ISLAND_N_E_TO_ROUTE_41_2_WP,
        "Route41", 5)

    Route_41_Links["ROUTE_41_TO_WHIRL_ISLAND_SW_LINK"] = WarpLink(
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_SW_WP,
        Whirl_Island_SW_Warp_Points.WHIRL_ISLAND_S_W_TO_ROUTE_41_3_WP,
        "Route41", 10)

    Route_41_Links["ROUTE_41_TO_WHIRL_ISLAND_SE_LINK"] = WarpLink(
        Route_41_Warp_Points.ROUTE_41_TO_WHIRL_ISLAND_SE_WP,
        Whirl_Island_SE_Warp_Points.WHIRL_ISLAND_S_E_TO_ROUTE_41_4_WP,
        "Route41", 15)
    

    Route_29_Links["ROUTE_29_TO_ROUTE_46_GATE_LINK"] = WarpLink(
        Route_29_Warp_Points.ROUTE_29_TO_ROUTE_46_GATE_ENTRANCE_WP,
        Route_29_Route_46_Gate_Warp_Points.ROUTE_29_AND_46_GATE_EXIT_TO_ROUTE_29_WP,
        "Route29"
    )

    

    Route_30_Links["ROUTE_30_TO_ROUTE_30_BERRY_HOUSE_LINK"] = WarpLink(
        Route_30_Warp_Points.ROUTE_30_BERRY_HOUSE_ENTRANCE_WP,
        Route_30_Berry_House_Warp_Points.ROUTE_30_BERRY_HOUSE_EXIT_WP,
        "Route30"
    )

    Route_30_Links["ROUTE_30_TO_MR_POKEMONS_HOUSE_LINK"] = WarpLink(
        Route_30_Warp_Points.MR_POKEMONS_HOUSE_ENTRANCE_WP,
        Mr_Pokemons_House_Warp_Points.MR_POKEMONS_HOUSE_EXIT_WP,
        "Route30" , 5
    )

    

    Route_31_Links["ROUTE_31_TO_ROUTE_31_VIOLET_GATE_LINK"] = WarpLink(
        Route_31_Warp_Points.ROUTE_31_TO_ROUTE_31_VIOLET_GATE_WP,
        Route_31_Violet_Gate_Warp_Points.ROUTE_31_VIOLET_GATE_TO_ROUTE_31_WP,
        "Route31", dual_width=True
    )

    Route_31_Links["ROUTE_31_TO_DARK_CAVE_VIOLET_ENTRANCE_LINK"] = WarpLink(
        Route_31_Warp_Points.ROUTE_31_TO_DARK_CAVE_VIOLET_ENTRANCE_WP,
        Dark_Cave_Violet_Entrance_Warp_Points.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_31_WP,
        "Route31" , 10
    )

    

    Route_32_Links["ROUTE_32_TO_ROUTE_32_POKECENTER_LINK"] = WarpLink(
        Route_32_Warp_Points.ROUTE_32_TO_ROUTE_32_POKECENTER_WP,
        Route_32_Pokecenter_Warp_Points.ROUTE_32_POKECENTER_TO_ROUTE_32_WP,
        "Route32"
    )

    Route_32_Links["ROUTE_32_TO_ROUTE_32_RUINS_OF_ALPH_GATE_LINK"] = WarpLink(
        Route_32_Warp_Points.ROUTE_32_TO_ROUTE_32_RUINS_OF_ALPH_GATE_WP,
        Route_32_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_32_RUINS_OF_ALPH_GATE_TO_ROUTE_32_WP,
        "Route32", 5, dual_width=True
    )

    Route_32_Links["ROUTE_32_TO_UNION_CAVE_LINK"] = WarpLink(
        Route_32_Warp_Points.ROUTE_32_TO_UNION_CAVE_1F_WP,
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_ROUTE_32_WP,
        "Route32" , 15
    )

    
    Route_32_Pokecenter_Links["ROUTE_32_POKECENTER_TO_ROUTE_32_LINK"] = WarpLink(
        Route_32_Pokecenter_Warp_Points.ROUTE_32_POKECENTER_TO_ROUTE_32_WP,
        Route_32_Warp_Points.ROUTE_32_TO_ROUTE_32_POKECENTER_WP,
        "Route32Pokecenter1F", dual_width=True
    )

    Route_32_Pokecenter_Links["ROUTE_32_POKECENTER_1F_TO_ROUTE_32_POKECENTER_2F_LINK"] = WarpLink(
        Route_32_Pokecenter_Warp_Points.ROUTE_32_POKECENTER_TO_ROUTE_32_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "Route32Pokecenter1F", 10
    )

    
    Route_33_Links["ROUTE_33_TO_UNION_CAVE_1F_LINK"] = WarpLink(
        Route_33_Warp_Points.ROUTE_33_TO_UNION_CAVE_1F_WP,
        Union_Cave_1F_Warp_Points.UNION_CAVE_1F_TO_ROUTE_33_WP,
        "Route33"
    )

    
    Route_34_Links["ROUTE_34_TO_ROUTE_34_ILEX_FOREST_GATE_LINK"] = WarpLink(
        Route_34_Warp_Points.ROUTE_34_TO_ROUTE_34_ILEX_FOREST_GATE_WP,
        Route_34_Ilex_Forest_Gate_Warp_Points.ROUTE_34_ILEX_FOREST_GATE_TO_ROUTE_34_WP,
        "Route34", dual_width=True
    )

    Route_34_Links["ROUTE_34_TO_DAY_CARE_FRONT_LINK"] = WarpLink(
        Route_34_Warp_Points.ROUTE_34_TO_DAY_CARE_FRONT_WP,
        Day_Care_Warp_Points.DAY_CARE_TO_ROUTE_34_FRONT_WP,
        "Route34" , 10, dual_width=True
    )
    # ROUTE_34_TO_DAY_CARE_SIDE_LINK"] = WarpLink(
    #
    #     0x00078A81 , 20,
    # )

    
    Route_35_Links["ROUTE_35_TO_ROUTE_35_GOLDENROD_GATE_LINK"] = WarpLink(
        Route_35_Warp_Points.ROUTE_35_TO_ROUTE_35_GOLDENROD_GATE_WP,
        Route_35_Goldenrod_Gate_Warp_Points.ROUTE_35_GOLDENROD_GATE_TO_ROUTE_35_WP,
        "Route35", dual_width=True
    )

    Route_35_Links["ROUTE_35_TO_NATIONAL_PARK_GATE_LINK"] = WarpLink(
        Route_35_Warp_Points.ROUTE_35_TO_NATIONAL_PARK_GATE_WP,
        Route_35_National_Park_Gate_Warp_Points.ROUTE_35_NATIONAL_PARK_GATE_TO_ROUTE_35_WP,
        "Route35" , 10
    )

    

    Route_36_Links["ROUTE_36_TO_ROUTE_36_NATIONAL_PARK_GATE_LINK"] = WarpLink(
        Route_36_Warp_Points.ROUTE_36_TO_ROUTE_36_NATIONAL_PARK_GATE_WP,
        Route_36_National_Park_Gate_Warp_Points.ROUTE_36_NATIONAL_PARK_GATE_TO_ROUTE_36_WP,
        "Route36",
        dual_width=True
    )

    Route_36_Links["ROUTE_36_TO_ROUTE_36_RUINS_OF_ALPH_GATE_LINK"] = WarpLink(
        Route_36_Warp_Points.ROUTE_36_TO_ROUTE_36_RUINS_OF_ALPH_GATE_WP,
        Route_36_Ruins_Of_Alph_Gate_Warp_Points.ROUTE_36_RUINS_OF_ALPH_GATE_TO_ROUTE_36_WP,
        "Route36" , 10,
        dual_width=True
    )

    
    Route_38_Links["ROUTE_38_TO_ROUTE_38_ECRUTEAK_GATE_LINK"] = WarpLink(
        Route_38_Warp_Points.ROUTE_38_TO_ROUTE_38_ECRUTEAK_GATE_WP,
        Route_38_Ecruteak_Gate_Warp_Points.ROUTE_38_ECRUTEAK_GATE_TO_ROUTE_38_WP,
        "Route38", dual_width=True
    )

    
    Route_39_Links["ROUTE_39_TO_ROUTE_39_BARN_LINK"] = WarpLink(
        Route_39_Warp_Points.ROUTE_39_TO_ROUTE_39_BARN_WP,
        Route_39_Barn_Warp_Points.ROUTE_39_BARN_TO_ROUTE_39_1_WP,
        "Route39"
    )
    Route_39_Links["ROUTE_39_TO_ROUTE_39_FARMHOUSE_LINK"] = WarpLink(
        Route_39_Warp_Points.ROUTE_39_TO_ROUTE_39_FARMHOUSE_WP,
        Route_39_Farmhouse_Warp_Points.ROUTE39_FARMHOUSE_TO_ROUTE_39_2_WP,
        "Route39", 5
    )

    
    Route_39_Barn_Links["ROUTE_39_BARN_TO_ROUTE_39_LINK"] = WarpLink(
        Route_39_Barn_Warp_Points.ROUTE_39_BARN_TO_ROUTE_39_1_WP,
        Route_39_Warp_Points.ROUTE_39_TO_ROUTE_39_BARN_WP,
        "Route39Barn", dual_width=True
    )

    
    Route_39_Farmhouse_Links["ROUTE_39_FARMHOUSE_TO_ROUTE_39_LINK"] = WarpLink(
        Route_39_Farmhouse_Warp_Points.ROUTE39_FARMHOUSE_TO_ROUTE_39_2_WP,
        Route_39_Warp_Points.ROUTE_39_TO_ROUTE_39_FARMHOUSE_WP,
        "Route39Farmhouse", dual_width=True
    )

    
    Route_40_Links["ROUTE_40_TO_ROUTE_40_BATTLE_TOWER_GATE_1_LINK"] = WarpLink(
        Route_40_Warp_Points.ROUTE_40_TO_ROUTE_40_BATTLE_TOWER_GATE_1_WP,
        Route_40_Battle_Tower_Gate_Warp_Points.ROUTE_40_BATTLE_TOWER_GATE_TO_ROUTE_40_1_WP,
        "Route40"
    )
    
    Route_40_Battle_Tower_Gate_Links["ROUTE_40_BATTLE_TOWER_GATE_TO_ROUTE_40_1_LINK"] = WarpLink(
        Route_40_Battle_Tower_Gate_Warp_Points.ROUTE_40_BATTLE_TOWER_GATE_TO_ROUTE_40_1_WP,
        Route_40_Warp_Points.ROUTE_40_TO_ROUTE_40_BATTLE_TOWER_GATE_1_WP,
        "Route40BattleTowerGate", dual_width=True
    )

    Route_40_Battle_Tower_Gate_Links["ROUTE_40_BATTLE_TOWER_GATE_TO_BATTLE_TOWER_OUTSIDE_1_LINK"] = WarpLink(
        Route_40_Battle_Tower_Gate_Warp_Points.ROUTE_40_BATTLE_TOWER_GATE_TO_BATTLE_TOWER_OUTSIDE_1_WP,
        Battle_Tower_Outside_Warp_Points.BATTLE_TOWER_OUTSIDE_TO_ROUTE_40_BATTLE_TOWER_GATE_3_WP,
        "Route40BattleTowerGate", 10,dual_width=True
    )


    
    Battle_Tower_Outside_Links["BATTLE_TOWER_OUTSIDE_TO_ROUTE_40_BATTLE_TOWER_GATE_3_LINK"] = WarpLink(
        Battle_Tower_Outside_Warp_Points.BATTLE_TOWER_OUTSIDE_TO_ROUTE_40_BATTLE_TOWER_GATE_3_WP,
        Route_40_Battle_Tower_Gate_Warp_Points.ROUTE_40_BATTLE_TOWER_GATE_TO_BATTLE_TOWER_OUTSIDE_1_WP,
        "BattleTowerOutside",dual_width=True
    )

    Battle_Tower_Outside_Links["BATTLE_TOWER_OUTSIDE_TO_BATTLE_TOWER_1F_1_LINK"] = WarpLink(
        Battle_Tower_Outside_Warp_Points.BATTLE_TOWER_OUTSIDE_TO_BATTLE_TOWER_1F_1_WP,
        Battle_Tower_Outside_Warp_Points.BATTLE_TOWER_OUTSIDE_TO_BATTLE_TOWER_1F_1_WP, # wrong but overwritten always
        "BattleTowerOutside", 10, dual_width=True
    )


    
    Route_42_Links["ROUTE_42_TO_ROUTE_42_ECRUTEAK_GATE_LINK"] = WarpLink(
        Route_42_Warp_Points.ROUTE_42_TO_ROUTE_42_ECRUTEAK_GATE_WP,
        Route_42_Ecruteak_Gate_Warp_Points.ROUTE_42_ECRUTEAK_GATE_TO_ROUTE_42_WP,
        "Route42", dual_width=True
    )

    Route_42_Links["ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_LEFT_LINK"] = WarpLink(
        Route_42_Warp_Points.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_LEFT_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_3_WP,
        "Route42", 10
    )

    Route_42_Links["ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_MIDDLE_LINK"] = WarpLink(
        Route_42_Warp_Points.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_MIDDLE_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_4_WP,
        "Route42", 15
    )

    Route_42_Links["ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_RIGHT_LINK"] = WarpLink(
        Route_42_Warp_Points.ROUTE_42_TO_MOUNT_MORTAR_1F_OUTSIDE_RIGHT_WP,
        Mount_Mortar_1F_Outside_Warp_Points.MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_5_WP,
        "Route42", 20
    )

    
    Route_43_Links["ROUTE_43_TO_ROUTE_43_MAHOGANY_GATE_LINK"] = WarpLink(
        Route_43_Warp_Points.ROUTE_43_TO_ROUTE_43_MAHOGANY_GATE_WP,
        Route_43_Mahogany_Gate_Warp_Points.ROUTE_43_MAHOGANY_GATE_TO_ROUTE_43_WP,
        "Route43", dual_width=True
    )

    Route_43_Links["ROUTE_43_TO_ROUTE_43_GATE_BOTTOM_LINK"] = WarpLink(
        Route_43_Warp_Points.ROUTE_43_TO_ROUTE_43_GATE_BOTTOM_WP,
        Route_43_Gate_Warp_Points.ROUTE_43_GATE_TO_ROUTE_43_TOP_WP,
        "Route43",10
    )

    Route_43_Links["ROUTE_43_TO_ROUTE_43_GATE_TOP_LINK"] = WarpLink(
        Route_43_Warp_Points.ROUTE_43_TO_ROUTE_43_GATE_TOP_WP,
        Route_43_Gate_Warp_Points.ROUTE_43_GATE_TO_ROUTE_43_BOTTOM_WP,
        "Route43" ,15,dual_width=True
    )

    
    Route_44_Links["ROUTE_44_TO_ICE_PATH_1F_LINK"] = WarpLink(
        Route_44_Warp_Points.ROUTE_44_TO_ICE_PATH_1F_WP,
        Ice_Path_1F_Warp_Points.ICE_PATH_1F_TO_ROUTE_44_1_WP,
        "Route44"
    )

    
    Route_45_Links["ROUTE_45_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_LINK"] = WarpLink(
        Route_45_Warp_Points.ROUTE_45_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_WP,
        Dark_Cave_Blackthorn_Entrance_Warp_Points.DARK_CAVE_BLACKTHORN_ENTRANCE_TO_ROUTE_45_WP,
        "Route45"
    )

    
    Route_46_Links["ROUTE_46_TO_ROUTE_29_ROUTE_46_GATE_LINK"] = WarpLink(
        Route_46_Warp_Points.ROUTE_46_TO_ROUTE_29_ROUTE_46_GATE_WP,
        Route_29_Route_46_Gate_Warp_Points.ROUTE_29_AND_46_GATE_EXIT_TO_ROUTE_46_WP,
        "Route46", dual_width=True
    )

    Route_46_Links["ROUTE_46_TO_DARK_CAVE_VIOLET_ENTRANCE_LINK"] = WarpLink(
        Route_46_Warp_Points.ROUTE_46_TO_DARK_CAVE_VIOLET_ENTRANCE_WP,
        Dark_Cave_Violet_Entrance_Warp_Points.DARK_CAVE_VIOLET_ENTRANCE_TO_ROUTE_46_WP,
        "Route46" , 10
    )


#######################################################################
#                    Violet Group                                     #
#######################################################################
    

    Violet_City_Links["VIOLET_CITY_TO_VIOLET_MART_LINK"] = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_MART_WP,
        Violet_Mart_Warp_Points.VIOLET_MART_TO_VIOLET_CITY_WP,
        "VioletCity"
    )

    Violet_City_Links["VIOLET_CITY_TO_VIOLET_GYM_LINK"] = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_GYM_WP,
        Violet_Gym_Warp_Points.VIOLET_GYM_TO_VIOLET_CITY_WP,
        "VioletCity" , 5
    )

    Violet_City_Links["VIOLET_CITY_TO_EARLS_POKEMON_ACADEMY_LINK"] = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_EARLS_POKEMON_ACADEMY_WP,
        Earls_Pokemon_Academy_Warp_Points.EARLS_POKEMON_ACADEMY_TO_VIOLET_CITY_WP,
        "VioletCity" , 10
    )

    Violet_City_Links["VIOLET_CITY_TO_GUIDE_NICKNAME_SPEECH_HOUSE_LINK"] = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_NICKNAME_SPEECH_HOUSE_WP,
        Violet_Nickname_Speech_House_Warp_Points.VIOLET_NICKNAME_SPEECH_HOUSE_TO_VIOLET_CITY_WP,
        "VioletCity" , 15
    )

    Violet_City_Links["VIOLET_CITY_TO_VIOLET_POKECENTER_1F_LINK"] = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_POKECENTER_1F_WP,
        Violet_Pokecenter_Warp_Points.VIOLET_POKECENTER_TO_VIOLET_CITY_WP,
        "VioletCity" , 20
    )

    Violet_City_Links["VIOLET_CITY_TO_VIOLET_KYLES_HOUSE_LINK"] = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_KYLES_HOUSE_WP,
        Violet_Kyles_House_Warp_Points.VIOLET_KYLES_HOUSE_TO_VIOLET_CITY_WP,
        "VioletCity" , 25
    )

    Violet_City_Links["VIOLET_CITY_TO_SPROUT_TOWER_1F_LINK"] = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_TO_SPROUT_TOWER_1F_WP,
        Sprout_Tower_1F_Warp_Points.SPROUT_TOWER_1F_TO_VIOLET_CITY_WP,
        "VioletCity" , 30
    )

    Violet_City_Links["VIOLET_CITY_ROUTE_31_VIOLET_GATE_LINK"] = WarpLink(
        Violet_City_Warp_Points.VIOLET_CITY_ROUTE_31_VIOLET_GATE_WP,
        Route_31_Violet_Gate_Warp_Points.ROUTE_31_VIOLET_GATE_TO_VIOLET_CITY_WP,
        "VioletCity" , 35,
        dual_width=True
    )

    

    Earls_Pokemon_Academy_Links["EARLS_POKEMON_ACADEMY_TO_VIOLET_CITY_LINK"] = WarpLink(
        Earls_Pokemon_Academy_Warp_Points.EARLS_POKEMON_ACADEMY_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_EARLS_POKEMON_ACADEMY_WP,
        "EarlsPokemonAcademy",
        dual_width=True
    )

    

    Violet_City_Mart_Links["VIOLET_MART_TO_VIOLET_CITY_LINK"] = WarpLink(
        Violet_Mart_Warp_Points.VIOLET_MART_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_MART_WP,
        "VioletMart",
        dual_width=True
    )

    

    Violet_City_Pokecenter_Links["VIOLET_POKECENTER_TO_VIOLET_CITY_LINK"] = WarpLink(
        Violet_Pokecenter_Warp_Points.VIOLET_POKECENTER_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_POKECENTER_1F_WP,
        "VioletPokecenter1F",
        dual_width=True
    )

    Violet_City_Pokecenter_Links["VIOLET_POKECENTER_1F_TO_VIOLET_POKECENTER_2F_LINK"] = WarpLink(
        Violet_Pokecenter_Warp_Points.VIOLET_POKECENTER_TO_VIOLET_POKECENTER_2F_WP,
        Pokecenter_2F_Warp_Points.POKECENTER_2F_TO_POKECENTER_1F_WP,
        "VioletPokecenter1F", 10
    )

    

    Violet_City_Gym_Links["VIOLET_GYM_TO_VIOLET_CITY_LINK"] = WarpLink(
        Violet_Gym_Warp_Points.VIOLET_GYM_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_GYM_WP,
        "VioletGym",
        dual_width=True, unlocks=[Unlock_Keys.BADGE_1]
    )

    

    Violet_City_Kyles_House_Links["VIOLET_KYLES_HOUSE_TO_VIOLET_CITY_LINK"] = WarpLink(
        Violet_Kyles_House_Warp_Points.VIOLET_KYLES_HOUSE_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_VIOLET_KYLES_HOUSE_WP,
        "VioletKylesHouse",
        dual_width=True
    )

    

    Violet_Nickname_Speech_House_Links["VIOLET_NICKNAME_SPEECH_HOUSE_TO_VIOLET_CITY_LINK"] = WarpLink(
        Violet_Nickname_Speech_House_Warp_Points.VIOLET_NICKNAME_SPEECH_HOUSE_TO_VIOLET_CITY_WP,
        Violet_City_Warp_Points.VIOLET_CITY_TO_NICKNAME_SPEECH_HOUSE_WP,
        "VioletNicknameSpeechHouse",
        dual_width=True
    )

    

    Victory_Road_Gate_Links["VICTORY_ROAD_GATE_TO_ROUTE_22_1_LINK"] = WarpLink(
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_ROUTE_22_1_WP,
        Route_22_Warp_Points.ROUTE_22_TO_VICTORY_ROAD_GATE_1_WP,
        "VictoryRoadGate", dual_width=True)

    Victory_Road_Gate_Links["VICTORY_ROAD_GATE_TO_ROUTE_26_1_LINK"] = WarpLink(
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_ROUTE_26_1_WP,
        Route_26_Warp_Points.ROUTE_26_TO_VICTORY_ROAD_GATE_3_WP,
        "VictoryRoadGate", 10, dual_width=True, unlocks=[Unlock_Keys.VICTORY_ROAD_GATE_ACCESS])

    Victory_Road_Gate_Links["VICTORY_ROAD_GATE_TO_VICTORY_ROAD_1_LINK"] = WarpLink(
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_VICTORY_ROAD_1_WP,
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_GATE_5_WP,
        "VictoryRoadGate", 20, dual_width=True)

    Victory_Road_Gate_Links["VICTORY_ROAD_GATE_TO_ROUTE_28_2_LINK"] = WarpLink(
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_ROUTE_28_2_WP,
        Silver_Cave_Room_3_Warp_Points.SILVER_CAVE_ROOM_3_TO_SILVER_CAVE_ROOM_2_2_WP, #todo - might have to import route 28 (will probably keep route 28 vanilla though)
        "VictoryRoadGate", 30, dual_width=True)

    

    Victory_Road_Links["VICTORY_ROAD_TO_VICTORY_ROAD_GATE_5_LINK"] = WarpLink(
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_GATE_5_WP,
        Victory_Road_Gate_Warp_Points.VICTORY_ROAD_GATE_TO_VICTORY_ROAD_1_WP,
        "VictoryRoad")

    Victory_Road_Links["VICTORY_ROAD_TO_VICTORY_ROAD_3_LINK"] = WarpLink(
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_3_WP,
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_2_WP,
        "VictoryRoad", 5)

    Victory_Road_Links["VICTORY_ROAD_TO_VICTORY_ROAD_2_LINK"] = WarpLink(
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_2_WP,
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_3_WP,
        "VictoryRoad", 10)

    Victory_Road_Links["VICTORY_ROAD_TO_VICTORY_ROAD_5_LINK"] = WarpLink(
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_5_WP,
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_4_WP,
        "VictoryRoad", 15)

    Victory_Road_Links["VICTORY_ROAD_TO_VICTORY_ROAD_4_LINK"] = WarpLink(
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_4_WP,
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_5_WP,
        "VictoryRoad", 20)

    Victory_Road_Links["VICTORY_ROAD_TO_VICTORY_ROAD_7_LINK"] = WarpLink(
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_7_WP,
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_6_WP,
        "VictoryRoad", 25)

    Victory_Road_Links["VICTORY_ROAD_TO_VICTORY_ROAD_6_LINK"] = WarpLink(
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_6_WP,
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_7_WP,
        "VictoryRoad", 30)

    Victory_Road_Links["VICTORY_ROAD_TO_VICTORY_ROAD_9_LINK"] = WarpLink(
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_9_WP,
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_VICTORY_ROAD_8_WP,
        "VictoryRoad", 35)

    Victory_Road_Links["VICTORY_ROAD_TO_ROUTE_23_3_LINK"] = WarpLink(
        Victory_Road_Warp_Points.VICTORY_ROAD_TO_ROUTE_23_3_WP,
        Route23_Warp_Points.ROUTE23_TO_VICTORY_ROAD_10_WP,
        "VictoryRoad", 45)

    

    Tohjo_Falls_Links["TOHJO_FALLS_TO_ROUTE_27_2_LINK"] = WarpLink(
        Tohjo_Falls_Warp_Points.TOHJO_FALLS_TO_ROUTE_27_2_WP,
        Route_27_Warp_Points.ROUTE_27_TO_TOHJO_FALLS_1_WP,
        "TohjoFalls")

    Tohjo_Falls_Links["TOHJO_FALLS_TO_ROUTE_27_3_LINK"] = WarpLink(
        Tohjo_Falls_Warp_Points.TOHJO_FALLS_TO_ROUTE_27_3_WP,
        Route_27_Warp_Points.ROUTE_27_TO_TOHJO_FALLS_2_WP,
        "TohjoFalls", 5)

    warpGroups = dict()

    warpGroups["Azalea_Gym_Links"] = dict(Azalea_Gym_Links)
    warpGroups["Azalea_Mart_Links"] = dict(Azalea_Mart_Links)
    warpGroups["Azalea_Pokecenter_Links"] = dict(Azalea_Pokecenter_Links)
    warpGroups["Azalea_Town_Links"] = dict(Azalea_Town_Links)
    warpGroups["Charcoal_Kiln_Links"] = dict(Charcoal_Kiln_Links)
    warpGroups["Kurts_House_Links"] = dict(Kurts_House_Links)
    warpGroups["Blackthorn_City_Links"] = dict(Blackthorn_City_Links)
    warpGroups["Blackthorn_Dragon_Speech_House_Links"] = dict(Blackthorn_Dragon_Speech_House_Links)
    warpGroups["Blackthorn_Emys_House_Links"] = dict(Blackthorn_Emys_House_Links)
    warpGroups["Blackthorn_Gym_Links"] = dict(Blackthorn_Gym_Links)
    warpGroups["Blackthorn_Mart_Links"] = dict(Blackthorn_Mart_Links)
    warpGroups["Blackthorn_Pokecenter_Links"] = dict(Blackthorn_Pokecenter_Links)
    warpGroups["Move_Deleters_House_Links"] = dict(Move_Deleters_House_Links)
    warpGroups["Cherrygrove_City_Links"] = dict(Cherrygrove_City_Links)
    warpGroups["Cherrygrove_Pokecenter_Links"] = dict(Cherrygrove_Pokecenter_Links)
    warpGroups["Cherrygrove_Evolution_Speech_House_Links"] = dict(Cherrygrove_Evolution_Speech_House_Links)
    warpGroups["Cherrygrove_Mart_Links"] = dict(Cherrygrove_Mart_Links)
    warpGroups["Cherrygrove_Gym_Speech_House_Links"] = dict(Cherrygrove_Gym_Speech_House_Links)
    warpGroups["Guide_Gents_House_Links"] = dict(Guide_Gents_House_Links)
    warpGroups["Mr_Pokemons_House_Links"] = dict(Mr_Pokemons_House_Links)
    warpGroups["Route_30_Berry_House_Links"] = dict(Route_30_Berry_House_Links)
    warpGroups["Cianwood_City_Links"] = dict(Cianwood_City_Links)
    warpGroups["Cianwood_Gym_Links"] = dict(Cianwood_Gym_Links)
    warpGroups["Cianwood_Lugia_Speech_House_Links"] = dict(Cianwood_Lugia_Speech_House_Links)
    warpGroups["Cianwood_Pharmacy_Links"] = dict(Cianwood_Pharmacy_Links)
    # warpGroups["Cianwood_Photo_Studio_Links"] = dict(Cianwood_Photo_Studio_Links)
    warpGroups["Cianwood_Pokecenter_Links"] = dict(Cianwood_Pokecenter_Links)
    warpGroups["Manias_House_Links"] = dict(Manias_House_Links)
    warpGroups["Poke_Seers_House_Links"] = dict(Poke_Seers_House_Links)
    warpGroups["Mount_Mortar_1F_Outside_Links"] = dict(Mount_Mortar_1F_Outside_Links)
    warpGroups["Mount_Mortar_B1F_Links"] = dict(Mount_Mortar_B1F_Links)
    warpGroups["Mount_Mortar_2F_Inside_Links"] = dict(Mount_Mortar_2F_Inside_Links)
    warpGroups["Mount_Mortar_1F_Inside_Links"] = dict(Mount_Mortar_1F_Inside_Links)
    warpGroups["Ice_Path_1F_Links"] = dict(Ice_Path_1F_Links)
    warpGroups["Ice_Path_B1F_Links"] = dict(Ice_Path_B1F_Links)
    warpGroups["Ice_Path_B2F_Blackthorn_Side_Links"] = dict(Ice_Path_B2F_Blackthorn_Side_Links)
    warpGroups["Ice_Path_B3F_Links"] = dict(Ice_Path_B3F_Links)
    warpGroups["Ice_Path_B2F_Mahogany_Side_Links"] = dict(Ice_Path_B2F_Mahogany_Side_Links)
    warpGroups["Burned_Tower_1F_Links"] = dict(Burned_Tower_1F_Links)
    warpGroups["Dark_Cave_Violet_Entrance_Links"] = dict(Dark_Cave_Violet_Entrance_Links)
    warpGroups["Dark_Cave_Blackthorn_Entrance_Links"] = dict(Dark_Cave_Blackthorn_Entrance_Links)
    warpGroups["Ilex_Forest_Links"] = dict(Ilex_Forest_Links)
    warpGroups["National_Park_Bug_Contest_Links"] = dict(National_Park_Bug_Contest_Links)
    warpGroups["National_Park_Links"] = dict(National_Park_Links)
    warpGroups["Ruins_Of_Alph_Outside_Links"] = dict(Ruins_Of_Alph_Outside_Links)
    warpGroups["Ruins_Of_Alph_Research_Center_Links"] = dict(Ruins_Of_Alph_Research_Center_Links)
    warpGroups["Ruins_Of_Alph_Inner_Chamber_Links"] = dict(Ruins_Of_Alph_Inner_Chamber_Links)
    warpGroups["Ruins_Of_Alph_Aerodactyl_Chamber_Links"] = dict(Ruins_Of_Alph_Aerodactyl_Chamber_Links)
    warpGroups["Ruins_Of_Alph_Aerodactyl_Item_Room_Links"] = dict(Ruins_Of_Alph_Aerodactyl_Item_Room_Links)
    warpGroups["Ruins_Of_Alph_Ho_Oh_Chamber_Links"] = dict(Ruins_Of_Alph_Ho_Oh_Chamber_Links)
    warpGroups["Ruins_Of_Alph_Ho_Oh_Item_Room_Links"] = dict(Ruins_Of_Alph_Ho_Oh_Item_Room_Links)
    warpGroups["Ruins_Of_Alph_Kabuto_Chamber_Links"] = dict(Ruins_Of_Alph_Kabuto_Chamber_Links)
    warpGroups["Ruins_Of_Alph_Kabuto_Item_Room_Links"] = dict(Ruins_Of_Alph_Kabuto_Item_Room_Links)
    warpGroups["Ruins_Of_Alph_Omanyte_Chamber_Links"] = dict(Ruins_Of_Alph_Omanyte_Chamber_Links)
    warpGroups["Ruins_Of_Alph_Omanyte_Item_Room_Links"] = dict(Ruins_Of_Alph_Omanyte_Item_Room_Links)
    warpGroups["Slowpoke_Well_B1F_Links"] = dict(Slowpoke_Well_B1F_Links)
    warpGroups["Slowpoke_Well_B2F_Links"] = dict(Slowpoke_Well_B2F_Links)
    warpGroups["Dragons_Den_1F_Links"] = dict(Dragons_Den_1F_Links)
    warpGroups["Dragons_Den_B1F_Links"] = dict(Dragons_Den_B1F_Links)
    warpGroups["Dragon_Shrine_Links"] = dict(Dragon_Shrine_Links)
    warpGroups["Sprout_Tower_1F_Links"] = dict(Sprout_Tower_1F_Links)
    warpGroups["Sprout_Tower_2F_Links"] = dict(Sprout_Tower_2F_Links)
    warpGroups["Sprout_Tower_3F_Links"] = dict(Sprout_Tower_3F_Links)
    warpGroups["Tin_Tower_1F_Links"] = dict(Tin_Tower_1F_Links)
    warpGroups["Tin_Tower_2F_Links"] = dict(Tin_Tower_2F_Links)
    warpGroups["Tin_Tower_3F_Links"] = dict(Tin_Tower_3F_Links)
    warpGroups["Tin_Tower_4F_Links"] = dict(Tin_Tower_4F_Links)
    warpGroups["Tin_Tower_5F_Links"] = dict(Tin_Tower_5F_Links)
    warpGroups["Tin_Tower_6F_Links"] = dict(Tin_Tower_6F_Links)
    warpGroups["Tin_Tower_7F_Links"] = dict(Tin_Tower_7F_Links)
    warpGroups["Tin_Tower_8F_Links"] = dict(Tin_Tower_8F_Links)
    warpGroups["Tin_Tower_9F_Links"] = dict(Tin_Tower_9F_Links)
    warpGroups["Union_Cave_1F_Links"] = dict(Union_Cave_1F_Links)
    warpGroups["Union_Cave_B1F_Links"] = dict(Union_Cave_B1F_Links)
    warpGroups["Union_Cave_B2F_Links"] = dict(Union_Cave_B2F_Links)
    warpGroups["Lake_Of_Rage_Links"] = dict(Lake_Of_Rage_Links)
    warpGroups["Lake_Of_Rage_Hidden_Power_House_Links"] = dict(Lake_Of_Rage_Hidden_Power_House_Links)
    warpGroups["Lake_Of_Rage_Magikarp_House_Links"] = dict(Lake_Of_Rage_Magikarp_House_Links)
    warpGroups["Whirl_Island_NW_Links"] = dict(Whirl_Island_NW_Links)
    warpGroups["Whirl_Island_NE_Links"] = dict(Whirl_Island_NE_Links)
    warpGroups["Whirl_Island_SW_Links"] = dict(Whirl_Island_SW_Links)
    warpGroups["Whirl_Island_SE_Links"] = dict(Whirl_Island_SE_Links)
    warpGroups["Whirl_Island_Cave_Links"] = dict(Whirl_Island_Cave_Links)
    warpGroups["Whirl_Island_B1F_Links"] = dict(Whirl_Island_B1F_Links)
    warpGroups["Whirl_Island_B2F_Links"] = dict(Whirl_Island_B2F_Links)
    warpGroups["Whirl_Island_Lugia_Chamber_Links"] = dict(Whirl_Island_Lugia_Chamber_Links)
    warpGroups["Tin_Tower_Roof_Links"] = dict(Tin_Tower_Roof_Links)
    warpGroups["Dance_Theatre_Links"] = dict(Dance_Theatre_Links)
    warpGroups["Ecruteak_City_Links"] = dict(Ecruteak_City_Links)
    warpGroups["Ecruteak_Gym_Links"] = dict(Ecruteak_Gym_Links)
    warpGroups["Ecruteak_Item_Finder_House_Links"] = dict(Ecruteak_Item_Finder_House_Links)
    warpGroups["Ecruteak_Lugia_Speech_House_Links"] = dict(Ecruteak_Lugia_Speech_House_Links)
    warpGroups["Ecruteak_Mart_Links"] = dict(Ecruteak_Mart_Links)
    warpGroups["Ecruteak_Pokecenter_Links"] = dict(Ecruteak_Pokecenter_Links)
    warpGroups["Ecruteak_Tin_Tower_Entrance_Links"] = dict(Ecruteak_Tin_Tower_Entrance_Links)
    warpGroups["Wise_Trios_Room_Links"] = dict(Wise_Trios_Room_Links)
    warpGroups["Ilex_Forest_Azalea_Gate_Links"] = dict(Ilex_Forest_Azalea_Gate_Links)
    warpGroups["Route_29_Route_46_Gate_Links"] = dict(Route_29_Route_46_Gate_Links)
    warpGroups["Route_31_Violet_Gate_Links"] = dict(Route_31_Violet_Gate_Links)
    warpGroups["Route_32_Ruins_Of_Alph_Gate_Links"] = dict(Route_32_Ruins_Of_Alph_Gate_Links)
    warpGroups["Route_34_Ilex_Forest_Gate_Links"] = dict(Route_34_Ilex_Forest_Gate_Links)
    warpGroups["Route_35_Goldenrod_Gate_Links"] = dict(Route_35_Goldenrod_Gate_Links)
    warpGroups["Route_35_National_Park_Gate_Links"] = dict(Route_35_National_Park_Gate_Links)
    warpGroups["Route_36_National_Park_Gate_Links"] = dict(Route_36_National_Park_Gate_Links)
    warpGroups["Route_36_Ruins_Of_Alph_Gate_Links"] = dict(Route_36_Ruins_Of_Alph_Gate_Links)
    warpGroups["Route_38_Ecruteak_Gate_Links"] = dict(Route_38_Ecruteak_Gate_Links)
    warpGroups["Route_42_Ecruteak_Gate_Links"] = dict(Route_42_Ecruteak_Gate_Links)
    warpGroups["Route_43_Gate_Links"] = dict(Route_43_Gate_Links)
    warpGroups["Route_43_Mahogany_Gate_Links"] = dict(Route_43_Mahogany_Gate_Links)
    warpGroups["Goldenrod_City_Links"] = dict(Goldenrod_City_Links)
    warpGroups["Bills_Familys_House_Links"] = dict(Bills_Familys_House_Links)
    warpGroups["Day_Care_Links"] = dict(Day_Care_Links)
    warpGroups["Goldenrod_Bike_Shop_Links"] = dict(Goldenrod_Bike_Shop_Links)
    warpGroups["Goldenrod_Dept_Store_B1F_Links"] = dict(Goldenrod_Dept_Store_B1F_Links)
    warpGroups["Goldenrod_Dept_Store_1F_Links"] = dict(Goldenrod_Dept_Store_1F_Links)
    warpGroups["Goldenrod_Dept_Store_2F_Links"] = dict(Goldenrod_Dept_Store_2F_Links)
    warpGroups["Goldenrod_Dept_Store_3F_Links"] = dict(Goldenrod_Dept_Store_3F_Links)
    warpGroups["Goldenrod_Dept_Store_4F_Links"] = dict(Goldenrod_Dept_Store_4F_Links)
    warpGroups["Goldenrod_Dept_Store_5F_Links"] = dict(Goldenrod_Dept_Store_5F_Links)
    warpGroups["Goldenrod_Dept_Store_6F_Links"] = dict(Goldenrod_Dept_Store_6F_Links)
    warpGroups["Goldenrod_Dept_Store_Roof_Links"] = dict(Goldenrod_Dept_Store_Roof_Links)
    warpGroups["Goldenrod_Flower_Shop_Links"] = dict(Goldenrod_Flower_Shop_Links)
    warpGroups["Goldenrod_Game_Corner_Links"] = dict(Goldenrod_Game_Corner_Links)
    warpGroups["Goldenrod_Gym_Links"] = dict(Goldenrod_Gym_Links)
    warpGroups["Goldenrod_Happiness_Rater_Links"] = dict(Goldenrod_Happiness_Rater_Links)
    warpGroups["Goldenrod_Magnet_Train_Station_Links"] = dict(Goldenrod_Magnet_Train_Station_Links)
    warpGroups["Goldenrod_Name_Rater_Links"] = dict(Goldenrod_Name_Rater_Links)
    warpGroups["Goldenrod_Pokecenter_Links"] = dict(Goldenrod_Pokecenter_Links)
    warpGroups["Goldenrod_PP_Speech_House_Links"] = dict(Goldenrod_PP_Speech_House_Links)
    warpGroups["Goldenrod_Underground_Warehouse_Links"] = dict(Goldenrod_Underground_Warehouse_Links)
    warpGroups["Goldenrod_Underground_Switch_Room_Entrance_Links"] = dict(Goldenrod_Underground_Switch_Room_Entrance_Links)
    warpGroups["Goldenrod_Underground_Links"] = dict(Goldenrod_Underground_Links)
    warpGroups["Radio_Tower_1F_Links"] = dict(Radio_Tower_1F_Links)
    warpGroups["Kogas_Room_Links"] = dict(Kogas_Room_Links)
    warpGroups["Wills_Room_Links"] = dict(Wills_Room_Links)
    warpGroups["Karens_Room_Links"] = dict(Karens_Room_Links)
    warpGroups["Brunos_Room_Links"] = dict(Brunos_Room_Links)
    warpGroups["Lances_Room_Links"] = dict(Lances_Room_Links)
    warpGroups["Mahogany_Town_Links"] = dict(Mahogany_Town_Links)
    warpGroups["Mahogany_Gym_Links"] = dict(Mahogany_Gym_Links)
    warpGroups["Mahogany_Mart_Links"] = dict(Mahogany_Mart_Links)
    warpGroups["Mahogany_Pokecenter_Links"] = dict(Mahogany_Pokecenter_Links)
    warpGroups["Mahogany_Red_Gyarados_Speech_House_Links"] = dict(Mahogany_Red_Gyarados_Speech_House_Links)
    warpGroups["New_Bark_Links"] = dict(New_Bark_Links)
    warpGroups["Players_Neighbors_House_Links"] = dict(Players_Neighbors_House_Links)
    warpGroups["Elms_House_Links"] = dict(Elms_House_Links)
    warpGroups["Olivine_City_Links"] = dict(Olivine_City_Links)
    warpGroups["Olivine_Cafe_Links"] = dict(Olivine_Cafe_Links)
    warpGroups["Olivine_Good_Rod_House_Links"] = dict(Olivine_Good_Rod_House_Links)
    warpGroups["Olivine_Gym_Links"] = dict(Olivine_Gym_Links)
    warpGroups["Olivine_Lighthouse_1F_Links"] = dict(Olivine_Lighthouse_1F_Links)
    warpGroups["Olivine_Lighthouse_2F_Links"] = dict(Olivine_Lighthouse_2F_Links)
    warpGroups["Olivine_Lighthouse_3F_Links"] = dict(Olivine_Lighthouse_3F_Links)
    warpGroups["Olivine_Lighthouse_4F_Links"] = dict(Olivine_Lighthouse_4F_Links)
    warpGroups["Olivine_Lighthouse_5F_Links"] = dict(Olivine_Lighthouse_5F_Links)
    warpGroups["Olivine_Lighthouse_6F_Links"] = dict(Olivine_Lighthouse_6F_Links)
    warpGroups["Olivine_Mart_Links"] = dict(Olivine_Mart_Links)
    warpGroups["Olivine_Pokecenter_Links"] = dict(Olivine_Pokecenter_Links)
    warpGroups["Olivine_Port_Passage_Links"] = dict(Olivine_Port_Passage_Links)
    warpGroups["Olivine_Punishment_Speech_House_Links"] = dict(Olivine_Punishment_Speech_House_Links)
    warpGroups["Olivine_Tims_House_Links"] = dict(Olivine_Tims_House_Links)
    warpGroups["Indigo_Plateau_Pokecenter_1F_Links"] = dict(Indigo_Plateau_Pokecenter_1F_Links)
    warpGroups["Route23_Links"] = dict(Route23_Links)
    warpGroups["Day_Of_Week_Siblings_House_Links"] = dict(Day_Of_Week_Siblings_House_Links)
    warpGroups["Route_26_Heal_House_Links"] = dict(Route_26_Heal_House_Links)
    warpGroups["Route_27_Sandstorm_House_Links"] = dict(Route_27_Sandstorm_House_Links)
    warpGroups["Route_26_Links"] = dict(Route_26_Links)
    warpGroups["Route_27_Links"] = dict(Route_27_Links)
    warpGroups["Route_41_Links"] = dict(Route_41_Links)
    warpGroups["Route_29_Links"] = dict(Route_29_Links)
    warpGroups["Route_30_Links"] = dict(Route_30_Links)
    warpGroups["Route_31_Links"] = dict(Route_31_Links)
    warpGroups["Route_32_Links"] = dict(Route_32_Links)
    warpGroups["Route_32_Pokecenter_Links"] = dict(Route_32_Pokecenter_Links)
    warpGroups["Route_33_Links"] = dict(Route_33_Links)
    warpGroups["Route_34_Links"] = dict(Route_34_Links)
    warpGroups["Route_35_Links"] = dict(Route_35_Links)
    warpGroups["Route_36_Links"] = dict(Route_36_Links)
    warpGroups["Route_38_Links"] = dict(Route_38_Links)
    warpGroups["Route_39_Links"] = dict(Route_39_Links)
    warpGroups["Route_39_Barn_Links"] = dict(Route_39_Barn_Links)
    warpGroups["Route_39_Farmhouse_Links"] = dict(Route_39_Farmhouse_Links)
    warpGroups["Route_40_Links"] = dict(Route_40_Links)
    warpGroups["Route_40_Battle_Tower_Gate_Links"] = dict(Route_40_Battle_Tower_Gate_Links)
    warpGroups["Battle_Tower_Outside_Links"] = dict(Battle_Tower_Outside_Links)
    warpGroups["Route_42_Links"] = dict(Route_42_Links)
    warpGroups["Route_43_Links"] = dict(Route_43_Links)
    warpGroups["Route_44_Links"] = dict(Route_44_Links)
    warpGroups["Route_45_Links"] = dict(Route_45_Links)
    warpGroups["Route_46_Links"] = dict(Route_46_Links)
    warpGroups["Violet_City_Links"] = dict(Violet_City_Links)
    warpGroups["Earls_Pokemon_Academy_Links"] = dict(Earls_Pokemon_Academy_Links)
    warpGroups["Violet_City_Mart_Links"] = dict(Violet_City_Mart_Links)
    warpGroups["Violet_City_Pokecenter_Links"] = dict(Violet_City_Pokecenter_Links)
    warpGroups["Violet_City_Gym_Links"] = dict(Violet_City_Gym_Links)
    warpGroups["Violet_City_Kyles_House_Links"] = dict(Violet_City_Kyles_House_Links)
    warpGroups["Violet_Nickname_Speech_House_Links"] = dict(Violet_Nickname_Speech_House_Links)
    warpGroups["Victory_Road_Gate_Links"] = dict(Victory_Road_Gate_Links)
    warpGroups["Victory_Road_Links"] = dict(Victory_Road_Links)
    warpGroups["Tohjo_Falls_Links"] = dict(Tohjo_Falls_Links)

    return warpGroups
#######################################################################
#                    END OF GROUPS                                    #
#######################################################################