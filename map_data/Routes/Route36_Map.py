from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.ROUTE_36

class ROUTE_36(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_36_NATIONAL_PARK_GATE = 1  # dual wide
    ROUTE_36_RUINS_OF_ALPH_GATE = 3  # dual wide

class Route_36_Warp_Points(Enum):

    ROUTE_36_TO_ROUTE_36_NATIONAL_PARK_GATE_WP = WarpInstruction(
        getHex(ROUTE_36.ROUTE_36_NATIONAL_PARK_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_36_TO_ROUTE_36_RUINS_OF_ALPH_GATE_WP = WarpInstruction(
        getHex(ROUTE_36.ROUTE_36_RUINS_OF_ALPH_GATE),
        getHex(mapGroup),
        getHex(specificMap))