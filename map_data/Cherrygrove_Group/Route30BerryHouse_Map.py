from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cherrygrove

mapGroup = MapGroup.CHERRYGROVE
specificMap = Cherrygrove.ROUTE_30_BERRY_HOUSE

class ROUTE_30_BERRY_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_30 = 1  # dual width


class Route_30_Berry_House_Warp_Points(Enum):

    Route_30_Berry_House_Exit_WP = WarpInstruction(
        getHex(ROUTE_30_BERRY_HOUSE.ROUTE_30),
        getHex(mapGroup),
        getHex(specificMap),
        )
