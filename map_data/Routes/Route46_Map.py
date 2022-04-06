from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Blackthorn

mapGroup = MapGroup.BLACKTHORN
specificMap = Blackthorn.ROUTE_46

class ROUTE_46(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_29_ROUTE_46_GATE = 1  # dual wide
    DARK_CAVE_VIOLET_ENTRANCE = 3


class Route_46_Warp_Points(Enum):

    ROUTE_46_TO_ROUTE_29_ROUTE_46_GATE_WP = WarpInstruction(
        getHex(ROUTE_46.ROUTE_29_ROUTE_46_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_46_TO_DARK_CAVE_VIOLET_ENTRANCE_WP = WarpInstruction(
            getHex(ROUTE_46.DARK_CAVE_VIOLET_ENTRANCE),
            getHex(mapGroup),
            getHex(specificMap))