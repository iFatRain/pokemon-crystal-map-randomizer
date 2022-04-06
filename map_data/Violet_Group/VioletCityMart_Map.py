from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.VIOLET_MART

class VIOLET_MART(IntEnum):
    def __str__(self):
        return str(self.value)

    VIOLET_CITY = 1  # dual width


class Violet_Mart_Warp_Points(Enum):

    VIOLET_MART_TO_VIOLET_CITY_WP = WarpInstruction(
        getHex(VIOLET_MART.VIOLET_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )
