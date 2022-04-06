from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.VIOLET_POKECENTER_1F

class VIOLET_POKECENTER(IntEnum):
    def __str__(self):
        return str(self.value)

    VIOLET_CITY = 1  # dual width
    POKECENTER_2F = 3


class Violet_Pokecenter_Warp_Points(Enum):

    VIOLET_POKECENTER_TO_VIOLET_CITY_WP = WarpInstruction(
        getHex(VIOLET_POKECENTER.VIOLET_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )

    VIOLET_POKECENTER_TO_VIOLET_POKECENTER_2F_WP = WarpInstruction(
        getHex(VIOLET_POKECENTER.POKECENTER_2F),
        getHex(mapGroup),
        getHex(specificMap))