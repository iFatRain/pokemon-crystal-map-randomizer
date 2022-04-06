from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Mahogany

mapGroup = MapGroup.MAHOGANY
specificMap = Mahogany.ROUTE_44

class ROUTE_44(IntEnum):
    def __str__(self):
        return str(self.value)

    ICE_PATH_1F = 1  #


class Route_44_Warp_Points(Enum):

    ROUTE_44_TO_ICE_PATH_1F_WP = WarpInstruction(
        getHex(ROUTE_44.ICE_PATH_1F),
        getHex(mapGroup),
        getHex(specificMap))


