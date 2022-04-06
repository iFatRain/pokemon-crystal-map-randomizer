from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Blackthorn

mapGroup = MapGroup.BLACKTHORN
specificMap = Blackthorn.BLACKTHORN_POKECENTER_1F


class BLACKTHORN_POKECENTER_1F(IntEnum):
    def __str__(self):
        return str(self.value)

    BLACKTHORN_CITY = 1
    POKECENTER_2F = 3


class Blackthorn_Pokecenter_Warp_Points(Enum):

    BLACKTHORN_POKECENTER_1F_TO_BLACKTHORN_CITY_WP = WarpInstruction(
        getHex(BLACKTHORN_POKECENTER_1F.BLACKTHORN_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    BLACKTHORN_POKECENTER_TO_BLACKTHORN_POKECENTER_2F_WP = WarpInstruction(
        getHex(BLACKTHORN_POKECENTER_1F.POKECENTER_2F),
        getHex(mapGroup),
        getHex(specificMap))