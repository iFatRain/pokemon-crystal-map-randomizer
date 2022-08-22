from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.VIOLET_KYLES_HOUSE

class VIOLET_KYLES_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    VIOLET_CITY = 1  # dual width


class Violet_Kyles_House_Warp_Points(Enum):

    Violet_City_Trade_House_Exit_WP = WarpInstruction(
        getHex(VIOLET_KYLES_HOUSE.VIOLET_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )
