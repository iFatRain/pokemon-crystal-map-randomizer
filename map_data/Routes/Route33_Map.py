from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Azalea

mapGroup = MapGroup.AZALEA
specificMap = Azalea.ROUTE_33

class ROUTE_33(IntEnum):
    def __str__(self):
        return str(self.value)

    UNION_CAVE_1F = 1

class Route_33_Warp_Points(Enum):

    ROUTE_33_TO_UNION_CAVE_1F_WP = WarpInstruction(
        getHex(ROUTE_33.UNION_CAVE_1F),
        getHex(mapGroup),
        getHex(specificMap))
