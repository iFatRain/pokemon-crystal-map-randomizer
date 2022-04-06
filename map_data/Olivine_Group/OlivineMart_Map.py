from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Olivine

mapGroup = MapGroup.OLIVINE
specificMap = Olivine.OLIVINE_MART

class OLIVINE_MART(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_CITY = 1  # dual width


class Olivine_Mart_Warp_Points(Enum):

    OLIVINE_MART_TO_OLIVINE_CITY_WP = WarpInstruction(
        getHex(OLIVINE_MART.OLIVINE_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )
