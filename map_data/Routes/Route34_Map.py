from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.ROUTE_34

class ROUTE_34(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_34_ILEX_FOREST_GATE = 1  # dual wide
    DAY_CARE_FRONT = 3  # dual wide
    DAY_CARE_SIDE = 5

class Route_34_Warp_Points(Enum):

    ROUTE_34_TO_ROUTE_34_ILEX_FOREST_GATE_WP = WarpInstruction(
        getHex(ROUTE_34.ROUTE_34_ILEX_FOREST_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_34_TO_DAY_CARE_FRONT_WP = WarpInstruction(
        getHex(ROUTE_34.DAY_CARE_FRONT),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_34_TO_DAY_CARE_SIDE_WP = WarpInstruction(
        getHex(ROUTE_34.DAY_CARE_SIDE),
        getHex(mapGroup),
        getHex(specificMap))
