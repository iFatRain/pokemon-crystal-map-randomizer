from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.VIOLET_GYM

class VIOLET_GYM(IntEnum):
    def __str__(self):
        return str(self.value)

    VIOLET_CITY = 1  # dual width


class Violet_Gym_Warp_Points(Enum):

    Violet_City_Gym_Exit_WP = WarpInstruction(
        getHex(VIOLET_GYM.VIOLET_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )
