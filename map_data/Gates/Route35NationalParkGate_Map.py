from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.ROUTE_35_NATIONAL_PARK_GATE

class ROUTE_35_NATIONAL_PARK_GATE(IntEnum):
    def __str__(self):
        return str(self.value)

    NATIONAL_PARK = 1   # dual width
    ROUTE_35 = 3  # dual width


class Route_35_National_Park_Gate_Warp_Points(Enum):

    ROUTE_35_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_WP = WarpInstruction(
        getHex(ROUTE_35_NATIONAL_PARK_GATE.NATIONAL_PARK),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_35_NATIONAL_PARK_GATE_TO_ROUTE_35_WP = WarpInstruction(
        getHex(ROUTE_35_NATIONAL_PARK_GATE.ROUTE_35),
        getHex(mapGroup),
        getHex(specificMap))
