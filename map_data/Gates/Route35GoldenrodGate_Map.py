from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.ROUTE_35_GOLDENROD_GATE

class ROUTE_35_GOLDENROD_GATE(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_35 = 1  # dual width
    GOLDENROD_CITY = 3  # dual width


class Route_35_Goldenrod_Gate_Warp_Points(Enum):

    ROUTE_35_GOLDENROD_GATE_TO_ROUTE_35_WP = WarpInstruction(
        getHex(ROUTE_35_GOLDENROD_GATE.ROUTE_35),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_35_GOLDENROD_GATE_TO_GOLDENROD_CITY_WP = WarpInstruction(
        getHex(ROUTE_35_GOLDENROD_GATE.GOLDENROD_CITY),
        getHex(mapGroup),
        getHex(specificMap))
