from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cianwood

mapGroup = MapGroup.CIANWOOD
specificMap = Cianwood.ROUTE_41

class ROUTE_41(IntEnum):
    def __str__(self):
        return str(self.value)

    WHIRL_ISLAND_NW = 1
    WHIRL_ISLAND_NE = 2
    WHIRL_ISLAND_SW = 3
    WHIRL_ISLAND_SE = 4

class Route_41_Warp_Points(Enum):

    ROUTE_41_TO_WHIRL_ISLAND_NW_WP = WarpInstruction(
        getHex(ROUTE_41. WHIRL_ISLAND_NW),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_41_TO_WHIRL_ISLAND_NE_WP = WarpInstruction(
        getHex(ROUTE_41.WHIRL_ISLAND_NE),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_41_TO_WHIRL_ISLAND_SW_WP = WarpInstruction(
        getHex(ROUTE_41.WHIRL_ISLAND_SW),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_41_TO_WHIRL_ISLAND_SE_WP = WarpInstruction(
        getHex(ROUTE_41.WHIRL_ISLAND_SE),
        getHex(mapGroup),
        getHex(specificMap))
