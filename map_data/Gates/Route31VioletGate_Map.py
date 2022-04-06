from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cherrygrove

mapGroup = MapGroup.CHERRYGROVE
specificMap = Cherrygrove.ROUTE_31_VIOLET_GATE

class ROUTE_31_VIOLET_GATE(IntEnum):
    def __str__(self):
        return str(self.value)

    VIOLET_CITY = 1  # dual width
    ROUTE_31 = 3  # dual width


class Route_31_Violet_Gate_Warp_Points(Enum):

    ROUTE_31_VIOLET_GATE_TO_VIOLET_CITY_WP = WarpInstruction(
        getHex(ROUTE_31_VIOLET_GATE.VIOLET_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_31_VIOLET_GATE_TO_ROUTE_31_WP = WarpInstruction(
        getHex(ROUTE_31_VIOLET_GATE.ROUTE_31),
        getHex(mapGroup),
        getHex(specificMap))