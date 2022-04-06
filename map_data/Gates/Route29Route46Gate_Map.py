from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, New_Bark

mapGroup = MapGroup.NEW_BARK
specificMap = New_Bark.ROUTE_29_ROUTE_46_GATE

class ROUTE_29_ROUTE_46_GATE(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_46 = 1  # dual width
    ROUTE_29 = 3  # dual width


class Route_29_Route_46_Gate_Warp_Points(Enum):

    ROUTE_29_ROUTE_46_GATE_TO_ROUTE_46_WP = WarpInstruction(
        getHex(ROUTE_29_ROUTE_46_GATE.ROUTE_46),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_29_ROUTE_46_GATE_TO_ROUTE_29_WP = WarpInstruction(
        getHex(ROUTE_29_ROUTE_46_GATE.ROUTE_29),
        getHex(mapGroup),
        getHex(specificMap))
