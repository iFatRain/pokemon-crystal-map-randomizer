from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Blackthorn

mapGroup = MapGroup.BLACKTHORN
specificMap = Blackthorn.ROUTE_45

class ROUTE_45(IntEnum):
    def __str__(self):
        return str(self.value)

    DARK_CAVE_BLACKTHORN_ENTRANCE = 1


class Route_45_Warp_Points(Enum):

    ROUTE_45_TO_DARK_CAVE_BLACKTHORN_ENTRANCE_WP = WarpInstruction(
        getHex(ROUTE_45.DARK_CAVE_BLACKTHORN_ENTRANCE),
        getHex(mapGroup),
        getHex(specificMap))
