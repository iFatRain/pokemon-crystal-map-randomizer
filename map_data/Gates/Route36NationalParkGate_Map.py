from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.ROUTE_36_NATIONAL_PARK_GATE

class ROUTE_36_NATIONAL_PARK_GATE(IntEnum):
    def __str__(self):
        return str(self.value)

    NATIONAL_PARK = 1   # dual width
    ROUTE_36 = 3  # dual width


class Route_36_National_Park_Gate_Warp_Points(Enum):

    ROUTE_36_NATIONAL_PARK_GATE_TO_NATIONAL_PARK_WP = WarpInstruction(
        getHex(ROUTE_36_NATIONAL_PARK_GATE.NATIONAL_PARK),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_36_NATIONAL_PARK_GATE_TO_ROUTE_36_WP = WarpInstruction(
        getHex(ROUTE_36_NATIONAL_PARK_GATE.ROUTE_36),
        getHex(mapGroup),
        getHex(specificMap))
