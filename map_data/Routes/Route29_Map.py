from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, New_Bark

mapGroup = MapGroup.NEW_BARK
specificMap = New_Bark.ROUTE_29

class ROUTE_29(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_29_ROUTE_46_GATE = 1  # dual wide

class Route_29_Warp_Points(Enum):

    ROUTE_29_TO_ROUTE_46_GATE_WP = WarpInstruction(
        getHex(ROUTE_29.ROUTE_29_ROUTE_46_GATE),
        getHex(mapGroup),
        getHex(specificMap),
        )

