from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.ROUTE_32_POKECENTER_1F

class ROUTE_32_POKECENTER(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_32 = 1 # dualwide
    POKECENTER_2F = 3


class Route_32_Pokecenter_Warp_Points(Enum):

    ROUTE_32_POKECENTER_TO_ROUTE_32_WP = WarpInstruction(
        getHex(ROUTE_32_POKECENTER.ROUTE_32),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_32_POKECENTER_TO_ROUTE_32_POKECENTER_2F_WP = WarpInstruction(
        getHex(ROUTE_32_POKECENTER.POKECENTER_2F),
        getHex(mapGroup),
        getHex(specificMap))