from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Olivine

mapGroup = MapGroup.OLIVINE
specificMap = Olivine.OLIVINE_CAFE

class OLIVINE_CAFE(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_CITY = 1 # dual wide


class Olivine_Cafe_Warp_Points(Enum):

    OLIVINE_CAFE_TO_OLIVINE_CITY_WP = WarpInstruction(
        getHex(OLIVINE_CAFE.OLIVINE_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )