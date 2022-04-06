from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.ROUTE_32_RUINS_OF_ALPH_GATE

class ROUTE_32_RUINS_OF_ALPH_GATE(IntEnum):
    def __str__(self):
        return str(self.value)

    RUINS_OF_ALPH_OUTSIDE = 1  # dual width
    ROUTE_32 = 3  # dual width


class Route_32_Ruins_Of_Alph_Gate_Warp_Points(Enum):

    ROUTE_32_RUINS_OF_ALPH_GATE_TO_RUINS_OF_ALPH_OUTSIDE_WP = WarpInstruction(
        getHex(ROUTE_32_RUINS_OF_ALPH_GATE.RUINS_OF_ALPH_OUTSIDE),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_32_RUINS_OF_ALPH_GATE_TO_ROUTE_32_WP = WarpInstruction(
        getHex(ROUTE_32_RUINS_OF_ALPH_GATE.ROUTE_32),
        getHex(mapGroup),
        getHex(specificMap))
