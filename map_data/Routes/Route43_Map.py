from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lake_Of_Rage

mapGroup = MapGroup.LAKE_OF_RAGE
specificMap = Lake_Of_Rage.ROUTE_43

class ROUTE_43(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_43_MAHOGANY_GATE = 1  # dual wide
    ROUTE_43_GATE_BOTTOM = 3
    ROUTE_43_GATE_TOP = 4  # dual wide


class Route_43_Warp_Points(Enum):

    ROUTE_43_TO_ROUTE_43_MAHOGANY_GATE_WP = WarpInstruction(
        getHex(ROUTE_43.ROUTE_43_MAHOGANY_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_43_TO_ROUTE_43_GATE_BOTTOM_WP = WarpInstruction(
        getHex(ROUTE_43.ROUTE_43_GATE_BOTTOM),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_43_TO_ROUTE_43_GATE_TOP_WP = WarpInstruction(
        getHex(ROUTE_43.ROUTE_43_GATE_TOP),
        getHex(mapGroup),
        getHex(specificMap))

