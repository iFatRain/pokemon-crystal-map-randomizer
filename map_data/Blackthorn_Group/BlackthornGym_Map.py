from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Blackthorn

mapGroup = MapGroup.BLACKTHORN
specificMap = Blackthorn.BLACKTHORN_GYM_1F


class BLACKTHORN_GYM_1F(IntEnum):
    def __str__(self):
        return str(self.value)

    BLACKTHORN_CITY = 1


class Blackthorn_Gym_1F_Warp_Points(Enum):

    Blackthorn_City_Gym_Exit_WP = WarpInstruction(
        getHex(BLACKTHORN_GYM_1F.BLACKTHORN_CITY),
        getHex(mapGroup),
        getHex(specificMap))
