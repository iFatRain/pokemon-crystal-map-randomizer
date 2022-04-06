from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Ecruteak

mapGroup = MapGroup.ECRUTEAK
specificMap = Ecruteak.ECRUTEAK_CITY

class ECRUTEAK_CITY(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_42_ECRUTEAK_GATE = 1 # dual width
    ECRUTEAK_TIN_TOWER_ENTRANCE = 3
    WISE_TRIOS_ROOM = 4  # dual width
    ECRUTEAK_POKECENTER_1F = 6
    ECRUTEAK_LUGIA_SPEECH_HOUSE = 7
    DANCE_THEATRE = 8
    ECRUTEAK_MART = 9
    ECRUTEAK_GYM = 10
    ECRUTEAK_ITEMFINDER_HOUSE = 11
    TIN_TOWER_1F = 12
    BURNED_TOWER_1F = 13
    ROUTE_38_ECRUTEAK_GATE = 14



class Ecruteak_City_Warp_Points(Enum):

    ECRUTEAK_CITY_TO_ECRUTEAK_GYM_WP = WarpInstruction(
        getHex(ECRUTEAK_CITY.ECRUTEAK_GYM),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_CITY_TO_ECRUTEAK_POKECENTER_1F = WarpInstruction(
        getHex(ECRUTEAK_CITY.ECRUTEAK_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_CITY_TO_ECRUTEAK_MART_WP = WarpInstruction(
        getHex(ECRUTEAK_CITY.ECRUTEAK_MART),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_CITY_TO_ROUTE_42_ECRUTEAK_GATE_WP = WarpInstruction(
        getHex(ECRUTEAK_CITY.ROUTE_42_ECRUTEAK_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_CITY_TO_ECRUTEAK_TIN_TOWER_ENTRANCE_WP = WarpInstruction(
        getHex(ECRUTEAK_CITY.ECRUTEAK_TIN_TOWER_ENTRANCE),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_CITY_TO_WISE_TRIOS_ROOM_WP = WarpInstruction(
        getHex(ECRUTEAK_CITY.WISE_TRIOS_ROOM),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_CITY_TO_ECRUTEAK_LUGIA_SPEECH_HOUSE_WP = WarpInstruction(
        getHex(ECRUTEAK_CITY.ECRUTEAK_LUGIA_SPEECH_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_CITY_TO_DANCE_THEATRE_WP = WarpInstruction(
        getHex(ECRUTEAK_CITY.DANCE_THEATRE),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_CITY_TO_ECRUTEAK_ITEMFINDER_HOUSE_WP = WarpInstruction(
        getHex(ECRUTEAK_CITY.ECRUTEAK_ITEMFINDER_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_CITY_TO_TIN_TOWER_1F_WP = WarpInstruction(
        getHex(ECRUTEAK_CITY.TIN_TOWER_1F),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_CITY_TO_BURNED_TOWER_1F_WP = WarpInstruction(
        getHex(ECRUTEAK_CITY.BURNED_TOWER_1F),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_CITY_TO_ROUTE_38_ECRUTEAK_GATE_WP = WarpInstruction(
        getHex(ECRUTEAK_CITY.ROUTE_38_ECRUTEAK_GATE),
        getHex(mapGroup),
        getHex(specificMap))

