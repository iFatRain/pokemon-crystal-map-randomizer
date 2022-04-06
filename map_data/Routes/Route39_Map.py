from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Olivine

mapGroup = MapGroup.OLIVINE
specificMap = Olivine.ROUTE_39

class ROUTE_39(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_39_BARN = 1
    ROUTE_39_FARMHOUSE = 2

class Route_39_Warp_Points(Enum):

    ROUTE_39_TO_ROUTE_39_BARN_WP = WarpInstruction(
        getHex(ROUTE_39.ROUTE_39_BARN),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_39_TO_ROUTE_39_FARMHOUSE_WP = WarpInstruction(
        getHex(ROUTE_39.ROUTE_39_FARMHOUSE),
        getHex(mapGroup),
        getHex(specificMap))