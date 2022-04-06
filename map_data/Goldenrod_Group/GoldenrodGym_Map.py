from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_GYM

class GOLDENROD_GYM(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_CITY = 1  # dual wide


class Goldenrod_Gym_Warp_Points(Enum):

    GOLDENROD_GYM_TO_GOLDENROD_CITY_WP = WarpInstruction(
        getHex(GOLDENROD_GYM.GOLDENROD_CITY),
        getHex(mapGroup),
        getHex(specificMap))