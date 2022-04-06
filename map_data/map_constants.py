from enum import IntEnum

class MapGroup(IntEnum):

    def __str__(self):
        return str(self.value)

    OLIVINE = 1
    MAHOGANY = 2
    DUNGEONS = 3
    ECRUTEAK = 4
    BLACKTHORN = 5
    CINNABAR = 6
    CERULEAN = 7
    AZALEA = 8
    LAKE_OF_RAGE = 9
    VIOLET = 10
    GOLDENROD = 11
    VERMILION = 12
    PALLET = 13
    PEWTER = 14
    FAST_SHIP = 15
    INDIGO = 16
    FUCHSIA = 17
    LAVENDER = 18
    SILVER = 19
    CABLE_CLUB = 20
    CELADON = 21
    CIANWOOD = 22
    VIRIDIAN = 23
    NEW_BARK = 24
    SAFFRON = 25
    CHERRYGROVE = 26


class Olivine(IntEnum):

    def __str__(self):
        return str(self.value)

    OLIVINE_POKECENTER_1F = 1
    OLIVINE_GYM = 2
    OLIVINE_TIMS_HOUSE = 3
    OLIVINE_HOUSE_BETA = 4
    OLIVINE_PUNISHMENT_SPEECH_HOUSE = 5
    OLIVINE_GOOD_ROD_HOUSE = 6
    OLIVINE_CAFE = 7
    OLIVINE_MART = 8
    ROUTE_38_ECRUTEAK_GATE = 9
    ROUTE_39_BARN = 10
    ROUTE_39_FARMHOUSE = 11
    ROUTE_38 = 12
    ROUTE_39 = 13
    OLIVINE_CITY = 14


class Mahogany(IntEnum):

    def __str__(self):
        return str(self.value)
    
    MAHOGANY_RED_GYARADOS_SPEECH_HOUSE = 1
    MAHOGANY_GYM = 2
    MAHOGANY_POKECENTER_1F = 3
    ROUTE_42_ECRUTEAK_GATE = 4
    ROUTE_42 = 5
    ROUTE_44 = 6
    MAHOGANY_TOWN = 7
    

class Dungeons(IntEnum):

    def __str__(self):
        return str(self.value)
    SPROUT_TOWER_1F = 1
    SPROUT_TOWER_2F = 2
    SPROUT_TOWER_3F = 3
    TIN_TOWER_1F = 4
    TIN_TOWER_2F = 5
    TIN_TOWER_3F = 6
    TIN_TOWER_4F = 7
    TIN_TOWER_5F = 8
    TIN_TOWER_6F = 9
    TIN_TOWER_7F = 10
    TIN_TOWER_8F = 11
    TIN_TOWER_9F = 12
    BURNED_TOWER_1F = 13
    BURNED_TOWER_B1F = 14
    NATIONAL_PARK = 15
    NATIONAL_PARK_BUG_CONTEST = 16
    RADIO_TOWER_1F = 17
    RADIO_TOWER_2F = 18
    RADIO_TOWER_3F = 19
    RADIO_TOWER_4F = 20
    RADIO_TOWER_5F = 21
    RUINS_OF_ALPH_OUTSIDE = 22
    RUINS_OF_ALPH_HO_OH_CHAMBER = 23
    RUINS_OF_ALPH_KABUTO_CHAMBER = 24
    RUINS_OF_ALPH_OMANYTE_CHAMBER = 25
    RUINS_OF_ALPH_AERODACTYL_CHAMBER = 26
    RUINS_OF_ALPH_INNER_CHAMBER = 27
    RUINS_OF_ALPH_RESEARCH_CENTER = 28
    RUINS_OF_ALPH_HO_OH_ITEM_ROOM = 29
    RUINS_OF_ALPH_KABUTO_ITEM_ROOM = 30
    RUINS_OF_ALPH_OMANYTE_ITEM_ROOM = 31
    RUINS_OF_ALPH_AERODACTYL_ITEM_ROOM = 32
    RUINS_OF_ALPH_HO_OH_WORD_ROOM = 33
    RUINS_OF_ALPH_KABUTO_WORD_ROOM = 34
    RUINS_OF_ALPH_OMANYTE_WORD_ROOM = 35
    RUINS_OF_ALPH_AERODACTYL_WORD_ROOM = 36
    UNION_CAVE_1F = 37
    UNION_CAVE_B1F = 38
    UNION_CAVE_B2F = 39
    SLOWPOKE_WELL_B1F = 40
    SLOWPOKE_WELL_B2F = 41
    OLIVINE_LIGHTHOUSE_1F = 42  # This is radio tower??
    OLIVINE_LIGHTHOUSE_2F = 43 #Ruins of alph outside
    OLIVINE_LIGHTHOUSE_3F = 44
    OLIVINE_LIGHTHOUSE_4F = 45
    OLIVINE_LIGHTHOUSE_5F = 46
    OLIVINE_LIGHTHOUSE_6F = 47
    MAHOGANY_MART_1F = 48
    TEAM_ROCKET_BASE_B1F = 49
    TEAM_ROCKET_BASE_B2F = 50
    TEAM_ROCKET_BASE_B3F = 51
    ILEX_FOREST = 52
    GOLDENROD_UNDERGROUND = 53
    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCES = 54
    GOLDENROD_DEPT_STORE_B1F = 55
    GOLDENROD_UNDERGROUND_WAREHOUSE = 56
    MOUNT_MORTAR_1F_OUTSIDE = 57
    MOUNT_MORTAR_1F_INSIDE = 58
    MOUNT_MORTAR_2F_INSIDE = 59
    MOUNT_MORTAR_B1F = 60
    ICE_PATH_1F = 61
    ICE_PATH_B1F = 62
    ICE_PATH_B2F_MAHOGANY_SIDE = 63
    ICE_PATH_B2F_BLACKTHORN_SIDE = 64
    ICE_PATH_B3F = 65
    WHIRL_ISLAND_NW = 66
    WHIRL_ISLAND_NE = 67
    WHIRL_ISLAND_SW = 68
    WHIRL_ISLAND_CAVE = 69
    WHIRL_ISLAND_SE = 70
    WHIRL_ISLAND_B1F = 71
    WHIRL_ISLAND_B2F = 72
    WHIRL_ISLAND_LUGIA_CHAMBER = 73
    SILVER_CAVE_ROOM_1 = 74
    SILVER_CAVE_ROOM_2 = 75
    SILVER_CAVE_ROOM_3 = 76
    SILVER_CAVE_ITEM_ROOMS = 77
    DARK_CAVE_VIOLET_ENTRANCE = 78
    DARK_CAVE_BLACKTHORN_ENTRANCE = 79
    DRAGONS_DEN_1F = 80
    DRAGONS_DEN_B1F = 81
    DRAGON_SHRINE = 82
    TOHJO_FALLS = 83
    DIGLETTS_CAVE = 84
    MOUNT_MOON = 85
    UNDERGROUND_PATH = 86
    ROCK_TUNNEL_1F = 87
    ROCK_TUNNEL_B1F = 88
    SAFARI_ZONE_FUCHSIA_GATE_BETA = 89
    SAFARI_ZONE_BETA = 90
    VICTORY_ROAD = 91
    

class Ecruteak(IntEnum):

    def __str__(self):
        return str(self.value)
        
    ECRUTEAK_TIN_TOWER_ENTRANCE = 1
    WISE_TRIOS_ROOM = 2
    ECRUTEAK_POKECENTER_1F = 3
    ECRUTEAK_LUGIA_SPEECH_HOUSE = 4
    DANCE_THEATRE = 5
    ECRUTEAK_MART = 6
    ECRUTEAK_GYM = 7
    ECRUTEAK_ITEMFINDER_HOUSE = 8
    ECRUTEAK_CITY = 9
    

class Blackthorn(IntEnum):

    def __str__(self):
        return str(self.value)
        
    BLACKTHORN_GYM_1F = 1
    BLACKTHORN_GYM_2F = 2
    BLACKTHORN_DRAGON_SPEECH_HOUSE = 3
    BLACKTHORN_EMYS_HOUSE = 4
    BLACKTHORN_MART = 5
    BLACKTHORN_POKECENTER_1F = 6
    MOVE_DELETERS_HOUSE = 7
    ROUTE_45 = 8
    ROUTE_46 = 9
    BLACKTHORN_CITY = 10
    

class Cinnabar(IntEnum):

    def __str__(self):
        return str(self.value)

    CINNABAR_POKECENTER_1F = 1
    CINNABAR_POKECENTER_2F_BETA = 2
    ROUTE_19_FUCHSIA_GATE = 3
    SEAFOAM_GYM = 4
    ROUTE_19 = 5
    ROUTE_20 = 6
    ROUTE_21 = 7
    CINNABAR_ISLAND = 8


class Cerulean(IntEnum):

    def __str__(self):
        return str(self.value)

    CERULEAN_GYM_BADGE_SPEECH_HOUSE = 1
    CERULEAN_POLICE_STATION = 2
    CERULEAN_TRADE_SPEECH_HOUSE = 3
    CERULEAN_POKECENTER_1F = 4
    CERULEAN_POKECENTER_2F_BETA = 5
    CERULEAN_GYM = 6
    CERULEAN_MART = 7
    ROUTE_10_POKECENTER_1F = 8
    ROUTE_10_POKECENTER_2F_BETA = 9
    POWER_PLANT = 10
    BILLS_HOUSE = 11
    ROUTE_4 = 12
    ROUTE_9 = 13
    ROUTE_10_NORTH = 14
    ROUTE_24 = 15
    ROUTE_25 = 16
    CERULEAN_CITY = 17


class Azalea(IntEnum):

    def __str__(self):
        return str(self.value)

    AZALEA_POKECENTER_1F = 1
    CHARCOAL_KILN = 2
    AZALEA_MART = 3
    KURTS_HOUSE = 4
    AZALEA_GYM = 5
    ROUTE_33 = 6
    AZALEA_TOWN = 7


class Lake_Of_Rage(IntEnum):

    def __str__(self):
        return str(self.value)

    LAKE_OF_RAGE_HIDDEN_POWER_HOUSE = 1
    LAKE_OF_RAGE_MAGIKARP_HOUSE = 2
    ROUTE_43_MAHOGANY_GATE = 3
    ROUTE_43_GATE = 4
    ROUTE_43 = 5
    LAKE_OF_RAGE = 6


class Violet(IntEnum):

    def __str__(self):
        return str(self.value)

    ROUTE_32 = 1
    ROUTE_35 = 2
    ROUTE_36 = 3
    ROUTE_37 = 4
    VIOLET_CITY = 5
    VIOLET_MART = 6
    VIOLET_GYM = 7
    EARLS_POKEMON_ACADEMY = 8
    VIOLET_NICKNAME_SPEECH_HOUSE = 9
    VIOLET_POKECENTER_1F = 10
    VIOLET_KYLES_HOUSE = 11
    ROUTE_32_RUINS_OF_ALPH_GATE = 12
    ROUTE_32_POKECENTER_1F = 13
    ROUTE_35_GOLDENROD_GATE = 14
    ROUTE_35_NATIONAL_PARK_GATE = 15
    ROUTE_36_RUINS_OF_ALPH_GATE = 16
    ROUTE_36_NATIONAL_PARK_GATE = 17


class Goldenrod(IntEnum):

    def __str__(self):
        return str(self.value)

    ROUTE_34 = 1
    GOLDENROD_CITY = 2
    GOLDENROD_GYM = 3
    GOLDENROD_BIKE_SHOP = 4
    GOLDENROD_HAPPINESS_RATER = 5
    BILLS_FAMILYS_HOUSE = 6
    GOLDENROD_MAGNET_TRAIN_STATION = 7
    GOLDENROD_FLOWER_SHOP = 8
    GOLDENROD_PP_SPEECH_HOUSE = 9
    GOLDENROD_NAME_RATER = 10
    GOLDENROD_DEPT_STORE_1F = 11
    GOLDENROD_DEPT_STORE_2F = 12
    GOLDENROD_DEPT_STORE_3F = 13
    GOLDENROD_DEPT_STORE_4F = 14
    GOLDENROD_DEPT_STORE_5F = 15
    GOLDENROD_DEPT_STORE_6F = 16
    GOLDENROD_DEPT_STORE_ELEVATOR = 17
    GOLDENROD_DEPT_STORE_ROOF = 18
    GOLDENROD_GAME_CORNER = 19
    GOLDENROD_POKECENTER_1F = 20
    POKECOM_CENTER_ADMIN_OFFICE_MOBILE = 21
    ILEX_FOREST_AZALEA_GATE = 22
    ROUTE_34_ILEX_FOREST_GATE = 23
    DAY_CARE = 24


class Vermilion(IntEnum):

    def __str__(self):
        return str(self.value)

    ROUTE_6 = 1
    ROUTE_11 = 2
    VERMILION_CITY = 3
    VERMILION_FISHING_SPEECH_HOUSE = 4
    VERMILION_POKECENTER_1F = 5
    VERMILION_POKECENTER_2F_BETA = 6
    POKEMON_FAN_CLUB = 7
    VERMILION_MAGNET_TRAIN_SPEECH_HOUSE = 8
    VERMILION_MART = 9
    VERMILION_DIGLETTS_CAVE_SPEECH_HOUSE = 10
    VERMILION_GYM = 11
    ROUTE_6_SAFFRON_GATE = 12
    ROUTE_6_UNDERGROUND_PATH_ENTRANCE = 13


class Pallet(IntEnum):

    def __str__(self):
        return str(self.value)

    ROUTE_1 = 1
    PALLET_TOWN = 2
    REDS_HOUSE_1F = 3
    REDS_HOUSE_2F = 4
    BLUES_HOUSE = 5
    OAKS_LAB = 6


class Pewter(IntEnum):

    def __str__(self):
        return str(self.value)

    ROUTE_3 = 1
    PEWTER_CITY = 2
    PEWTER_NIDORAN_SPEECH_HOUSE = 3
    PEWTER_GYM = 4
    PEWTER_MART = 5
    PEWTER_POKECENTER_1F = 6
    PEWTER_POKECENTER_2F_BETA = 7
    PEWTER_SNOOZE_SPEECH_HOUSE = 8


class Fast_Ship(IntEnum):

    def __str__(self):
        return str(self.value)

    OLIVINE_PORT = 1
    VERMILION_PORT = 2
    FAST_SHIP_1F = 3
    FAST_SHIP_CABINS_NNW_NNE_NE = 4
    FAST_SHIP_CABINS_SW_SSW_NW = 5
    FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN = 6
    FAST_SHIP_B1F = 7
    OLIVINE_PORT_PASSAGE = 8
    VERMILION_PORT_PASSAGE = 9
    MOUNT_MOON_SQUARE = 10
    MOUNT_MOON_GIFT_SHOP = 11
    TIN_TOWER_ROOF = 12


class Indigo(IntEnum):

    def __str__(self):
        return str(self.value)

    ROUTE_23 = 1
    INDIGO_PLATEAU_POKECENTER_1F = 2
    WILLS_ROOM = 3
    KOGAS_ROOM = 4
    BRUNOS_ROOM = 5
    KARENS_ROOM = 6
    LANCES_ROOM = 7
    HALL_OF_FAME = 8


class Fuchsia(IntEnum):

    def __str__(self):
        return str(self.value)

    ROUTE_13 = 1
    ROUTE_14 = 2
    ROUTE_15 = 3
    ROUTE_18 = 4
    FUCHSIA_CITY = 5
    FUCHSIA_MART = 6
    SAFARI_ZONE_MAIN_OFFICE = 7
    FUCHSIA_GYM = 8
    BILLS_BROTHERS_HOUSE = 9
    FUCHSIA_POKECENTER_1F = 10
    FUCHSIA_POKECENTER_2F_BETA = 11
    SAFARI_ZONE_WARDENS_HOME = 12
    ROUTE_15_FUCHSIA_GATE = 13


class Lavender(IntEnum):

    def __str__(self):
        return str(self.value)

    ROUTE_8 = 1
    ROUTE_12 = 2
    ROUTE_10_SOUTH = 3
    LAVENDER_TOWN = 4
    LAVENDER_POKECENTER_1F = 5
    LAVENDER_POKECENTER_2F_BETA = 6
    MR_FUJIS_HOUSE = 7
    LAVENDER_SPEECH_HOUSE = 8
    LAVENDER_NAME_RATER = 9
    LAVENDER_MART = 10
    SOUL_HOUSE = 11
    LAV_RADIO_TOWER_1F = 12
    ROUTE_8_SAFFRON_GATE = 13
    ROUTE_12_SUPER_ROD_HOUSE = 14


class Silver(IntEnum):

    def __str__(self):
        return str(self.value)

    ROUTE_28 = 1
    SILVER_CAVE_OUTSIDE = 2
    SILVER_CAVE_POKECENTER_1F = 3
    ROUTE_28_STEEL_WING_HOUSE = 4


class Cable_Club(IntEnum):

    def __str__(self):
        return str(self.value)

    POKECENTER_2F = 1
    TRADE_CENTER = 2
    COLOSSEUM = 3
    TIME_CAPSULE = 4
    MOBILE_TRADE_ROOM = 5
    MOBILE_BATTLE_ROOM = 6


class Celadon(IntEnum):

    def __str__(self):
        return str(self.value)
    
    ROUTE_7 = 1
    ROUTE_16 = 2
    ROUTE_17 = 3
    CELADON_CITY = 4
    CELADON_DEPT_STORE_1F = 5
    CELADON_DEPT_STORE_2F = 6
    CELADON_DEPT_STORE_3F = 7
    CELADON_DEPT_STORE_4F = 8
    CELADON_DEPT_STORE_5F = 9
    CELADON_DEPT_STORE_6F = 10
    CELADON_DEPT_STORE_ELEVATOR = 11
    CELADON_MANSION_1F = 12
    CELADON_MANSION_2F = 13
    CELADON_MANSION_3F = 14
    CELADON_MANSION_ROOF = 15
    CELADON_MANSION_ROOF_HOUSE = 16
    CELADON_POKECENTER_1F = 17
    CELADON_POKECENTER_2F_BETA = 18
    CELADON_GAME_CORNER = 19
    CELADON_GAME_CORNER_PRIZE_ROOM = 20
    CELADON_GYM = 21
    CELADON_CAFE = 22
    ROUTE_16_FUCHSIA_SPEECH_HOUSE = 23
    ROUTE_16_GATE = 24
    ROUTE_7_SAFFRON_GATE = 25
    ROUTE_17_ROUTE_18_GATE = 26
    

class Cianwood(IntEnum):

    def __str__(self):
        return str(self.value)
    
    ROUTE_40 = 1
    ROUTE_41 = 2
    CIANWOOD_CITY = 3
    MANIAS_HOUSE = 4
    CIANWOOD_GYM = 5
    CIANWOOD_POKECENTER_1F = 6
    CIANWOOD_PHARMACY = 7
    CIANWOOD_PHOTO_STUDIO = 8
    CIANWOOD_LUGIA_SPEECH_HOUSE = 9
    POKE_SEERS_HOUSE = 10
    BATTLE_TOWER_1F = 11
    BATTLE_TOWER_BATTLE_ROOM = 12
    BATTLE_TOWER_ELEVATOR = 13
    BATTLE_TOWER_HALLWAY = 14
    ROUTE_40_BATTLE_TOWER_GATE = 15
    BATTLE_TOWER_OUTSIDE = 16


class Viridian(IntEnum):

    def __str__(self):
        return str(self.value)
    
    ROUTE_2 = 1
    ROUTE_22 = 2
    VIRIDIAN_CITY = 3
    VIRIDIAN_GYM = 4
    VIRIDIAN_NICKNAME_SPEECH_HOUSE = 5
    TRAINER_HOUSE_1F = 6
    TRAINER_HOUSE_B1F = 7
    VIRIDIAN_MART = 8
    VIRIDIAN_POKECENTER_1F = 9
    VIRIDIAN_POKECENTER_2F_BETA = 10
    ROUTE_2_NUGGET_HOUSE = 11
    ROUTE_2_GATE = 12
    VICTORY_ROAD_GATE = 13


class New_Bark(IntEnum):

    def __str__(self):
        return str(self.value)

    ROUTE_26 = 1
    ROUTE_27 = 2
    ROUTE_29 = 3
    NEW_BARK_TOWN = 4
    ELMS_LAB = 5
    PLAYERS_HOUSE_1F = 6
    PLAYERS_HOUSE_2F = 7
    PLAYERS_NEIGHBORS_HOUSE = 8
    ELMS_HOUSE = 9
    ROUTE_26_HEAL_HOUSE = 10
    DAY_OF_WEEK_SIBLINGS_HOUSE = 11
    ROUTE_27_SANDSTORM_HOUSE = 12
    ROUTE_29_ROUTE_46_GATE = 13


class Saffron(IntEnum):

    def __str__(self):
        return str(self.value)

    ROUTE_5 = 1
    SAFFRON_CITY = 2
    FIGHTING_DOJO = 3
    SAFFRON_GYM = 4
    SAFFRON_MART = 5
    SAFFRON_POKECENTER_1F = 6
    SAFFRON_POKECENTER_2F_BETA = 7
    MR_PSYCHICS_HOUSE = 8
    SAFFRON_MAGNET_TRAIN_STATION = 9
    SILPH_CO_1F = 10
    COPYCATS_HOUSE_1F = 11
    COPYCATS_HOUSE_2F = 12
    ROUTE_5_UNDERGROUND_PATH_ENTRANCE = 13
    ROUTE_5_SAFFRON_GATE = 14
    ROUTE_5_CLEANSE_TAG_HOUSE = 15


class Cherrygrove(IntEnum):

    def __str__(self):
        return str(self.value)

    ROUTE_30 = 1
    ROUTE_31 = 2
    CHERRYGROVE_CITY = 3
    CHERRYGROVE_MART = 4
    CHERRYGROVE_POKECENTER_1F = 5
    CHERRYGROVE_GYM_SPEECH_HOUSE = 6
    GUIDE_GENTS_HOUSE = 7
    CHERRYGROVE_EVOLUTION_SPEECH_HOUSE = 8
    ROUTE_30_BERRY_HOUSE = 9
    MR_POKEMONS_HOUSE = 10
    ROUTE_31_VIOLET_GATE = 11
