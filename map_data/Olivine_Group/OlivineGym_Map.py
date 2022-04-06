from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Olivine

mapGroup = MapGroup.OLIVINE
specificMap = Olivine.OLIVINE_GYM

class OLIVINE_GYM(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_CITY = 1 # dual wide


class Olivine_Gym_Warp_Points(Enum):

    OLIVINE_GYM_TO_OLIVINE_CITY_WP = WarpInstruction(
        getHex(OLIVINE_GYM.OLIVINE_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )