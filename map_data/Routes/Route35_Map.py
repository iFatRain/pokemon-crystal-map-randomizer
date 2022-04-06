from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.ROUTE_35

class ROUTE_35(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_35_GOLDENROD_GATE = 1  # dual wide
    ROUTE_35_NATIONAL_PARK_GATE = 3


class Route_35_Warp_Points(Enum):

    ROUTE_35_TO_ROUTE_35_GOLDENROD_GATE_WP = WarpInstruction(
        getHex(ROUTE_35.ROUTE_35_GOLDENROD_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_35_TO_NATIONAL_PARK_GATE_WP = WarpInstruction(
        getHex(ROUTE_35.ROUTE_35_NATIONAL_PARK_GATE),
        getHex(mapGroup),
        getHex(specificMap))


