from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Blackthorn

mapGroup = MapGroup.BLACKTHORN
specificMap = Blackthorn.BLACKTHORN_MART


class BLACKTHORN_MART(IntEnum):
    def __str__(self):
        return str(self.value)

    BLACKTHORN_CITY = 1


class Blackthorn_Mart_Warp_Points(Enum):

    BLACKTHORN_MART_TO_BLACKTHORN_CITY_WP = WarpInstruction(
        getHex(BLACKTHORN_MART.BLACKTHORN_CITY),
        getHex(mapGroup),
        getHex(specificMap))
