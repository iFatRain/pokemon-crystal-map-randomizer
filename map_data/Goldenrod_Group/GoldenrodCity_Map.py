from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_CITY

class GOLDENROD_CITY(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_GYM = 1
    GOLDENROD_BIKE_SHOP = 2
    GOLDENROD_HAPPINESS_RATER = 3
    BILLS_FAMILYS_HOUSE = 4
    GOLDENROD_MAGNET_TRAIN_STATION = 5
    GOLDENROD_FLOWER_SHOP = 6
    GOLDENROD_PP_SPEECH_HOUSE = 7
    GOLDENROD_NAME_RATER = 8
    GOLDENROD_DEPT_STORE_1F = 9
    GOLDENROD_GAME_CORNER = 10
    RADIO_TOWER_1F = 11
    ROUTE_35_GOLDENROD_GATE = 12
    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_NORTH = 13
    GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_SOUTH = 14
    GOLDENROD_POKECENTER_1F = 15



class Goldenrod_City_Warp_Points(Enum):

    GOLDENROD_CITY_TO_GOLDENROD_GYM_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.GOLDENROD_GYM),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_GOLDENROD_BIKE_SHOP_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.GOLDENROD_BIKE_SHOP),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_GOLDENROD_HAPPINESS_RATER_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.GOLDENROD_HAPPINESS_RATER),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_BILLS_FAMILYS_HOUSE_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.BILLS_FAMILYS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_GOLDENROD_MAGNET_TRAIN_STATION_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.GOLDENROD_MAGNET_TRAIN_STATION),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_GOLDENROD_FLOWER_SHOP_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.GOLDENROD_FLOWER_SHOP),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_GOLDENROD_PP_SPEECH_HOUSE_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.GOLDENROD_PP_SPEECH_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_GOLDENROD_NAME_RATER_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.GOLDENROD_NAME_RATER),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_GOLDENROD_DEPT_STORE_1F_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.GOLDENROD_DEPT_STORE_1F),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_GOLDENROD_GAME_CORNER_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.GOLDENROD_GAME_CORNER),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_RADIO_TOWER_1F_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.RADIO_TOWER_1F),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_ROUTE_35_GOLDENROD_GATE_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.ROUTE_35_GOLDENROD_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_NORTH_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_NORTH),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_SOUTH_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.GOLDENROD_UNDERGROUND_SWITCH_ROOM_ENTRANCE_SOUTH),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_CITY_TO_GOLDENROD_POKECENTER_1F_WP = WarpInstruction(
        getHex(GOLDENROD_CITY.GOLDENROD_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap))
