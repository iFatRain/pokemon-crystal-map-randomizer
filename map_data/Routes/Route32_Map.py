from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.ROUTE_32

class ROUTE_32(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_32_POKECENTER_1F = 1
    ROUTE_32_RUINS_OF_ALPH_GATE = 2  # dual wide
    UNION_CAVE_1F = 4

class Route_32_Warp_Points(Enum):

    ROUTE_32_TO_ROUTE_32_POKECENTER_WP = WarpInstruction(
        getHex(ROUTE_32.ROUTE_32_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_32_TO_ROUTE_32_RUINS_OF_ALPH_GATE_WP = WarpInstruction(
        getHex(ROUTE_32.ROUTE_32_RUINS_OF_ALPH_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_32_TO_UNION_CAVE_1F_WP = WarpInstruction(
        getHex(ROUTE_32.UNION_CAVE_1F),
        getHex(mapGroup),
        getHex(specificMap))