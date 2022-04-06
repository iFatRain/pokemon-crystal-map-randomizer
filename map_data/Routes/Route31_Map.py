from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cherrygrove

mapGroup = MapGroup.CHERRYGROVE
specificMap = Cherrygrove.ROUTE_31

class ROUTE_31(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_31_VIOLET_GATE = 1  # dual wide
    DARK_CAVE_VIOLET_ENTRANCE = 3

class Route_31_Warp_Points(Enum):

    ROUTE_31_TO_ROUTE_31_VIOLET_GATE_WP = WarpInstruction(
        getHex(ROUTE_31.ROUTE_31_VIOLET_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_31_TO_DARK_CAVE_VIOLET_ENTRANCE_WP = WarpInstruction(
        getHex(ROUTE_31.DARK_CAVE_VIOLET_ENTRANCE),
        getHex(mapGroup),
        getHex(specificMap))
