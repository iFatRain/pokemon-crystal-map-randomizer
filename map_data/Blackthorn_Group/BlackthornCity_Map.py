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

    Blackthorn_City_Gym_Entrance_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.BLACKTHORN_GYM_1F),
        getHex(mapGroup),
        getHex(specificMap))

    Blackthorn_City_Dragon_Speech_House_Entrance_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.BLACKTHORN_DRAGON_SPEECH_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    Blackthorn_City_Emys_House_Entrance_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.BLACKTHORN_EMYS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    Blackthorn_City_Mart_Entrance_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.BLACKTHORN_MART),
        getHex(mapGroup),
        getHex(specificMap))

    Blackthorn_City_Pokecenter_Entrance_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.BLACKTHORN_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap))

    Move_Deleters_House_Entrance_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.MOVE_DELETERS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    Blackthorn_City_Ice_Path_Entrance_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.ICE_PATH_1F),
        getHex(mapGroup),
        getHex(specificMap))

    Blackthorn_City_Dragons_Den_Entrance_WP = WarpInstruction(
        getHex(BLACKTHORN_CITY.DRAGONS_DEN_1F),
        getHex(mapGroup),
        getHex(specificMap))



