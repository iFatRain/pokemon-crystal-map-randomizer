from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Blackthorn

mapGroup = MapGroup.BLACKTHORN
specificMap = Blackthorn.BLACKTHORN_CITY

class BLACKTHORN_CITY(IntEnum):
    def __str__(self):
        return str(self.value)

    BLACKTHORN_GYM_1F = 1
    BLACKTHORN_DRAGON_SPEECH_HOUSE = 2
    BLACKTHORN_EMYS_HOUSE = 3
    BLACKTHORN_MART = 4
    BLACKTHORN_POKECENTER_1F = 5
    MOVE_DELETERS_HOUSE = 6
    ICE_PATH_1F = 7
    DRAGONS_DEN_1F = 8


class Blackthorn_City_Warp_Points(Enum):

    BLACKTHORN_CITY_TO_BLACKTHORN_GYM_1F_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.BLACKTHORN_GYM_1F),
        getHex(mapGroup),
        getHex(specificMap))

    BLACKTHORN_CITY_TO_BLACKTHORN_DRAGON_SPEECH_HOUSE_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.BLACKTHORN_DRAGON_SPEECH_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    BLACKTHORN_CITY_TO_BLACKTHORN_EMYS_HOUSE_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.BLACKTHORN_EMYS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    BLACKTHORN_CITY_TO_BLACKTHORN_MART_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.BLACKTHORN_MART),
        getHex(mapGroup),
        getHex(specificMap))

    BLACKTHORN_CITY_TO_BLACKTHORN_POKECENTER_1F_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.BLACKTHORN_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap))

    BLACKTHORN_CITY_TO_MOVE_DELETERS_HOUSE_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.MOVE_DELETERS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    BLACKTHORN_CITY_TO_ICE_PATH_1F_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.ICE_PATH_1F),
        getHex(mapGroup),
        getHex(specificMap))

    BLACKTHORN_CITY_TO_DRAGONS_DEN_1F_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.DRAGONS_DEN_1F),
        getHex(mapGroup),
        getHex(specificMap))



