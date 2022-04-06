from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Blackthorn

mapGroup = MapGroup.BLACKTHORN
specificMap = Blackthorn.BLACKTHORN_EMYS_HOUSE


class BLACKTHORN_EMYS_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    BLACKTHORN_CITY = 1


class Blackthorn_Emys_House_Warp_Points(Enum):

    BLACKTHORN_EMYS_HOUSE_TO_BLACKTHORN_CITY_WP = WarpInstruction(
        getHex(BLACKTHORN_EMYS_HOUSE.BLACKTHORN_CITY),
        getHex(mapGroup),
        getHex(specificMap))
