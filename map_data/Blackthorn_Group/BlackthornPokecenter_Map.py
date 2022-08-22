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

    Blackthorn_City_Pokecenter_Exit_WP = WarpInstruction(
        getHex(BLACKTHORN_POKECENTER_1F.BLACKTHORN_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    Blackthorn_City_Pokecenter_Stairs_WP = WarpInstruction(
        getHex(BLACKTHORN_POKECENTER_1F.POKECENTER_2F),
        getHex(mapGroup),
        getHex(specificMap))