from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lake_Of_Rage

mapGroup = MapGroup.LAKE_OF_RAGE
specificMap = Lake_Of_Rage.ROUTE_43_GATE

class ROUTE_43_GATE(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_43_TOP = 1  # dual wide
    ROUTE_43_BOTTOM = 3  # dual wide


class Route_43_Gate_Warp_Points(Enum):

    ROUTE_43_GATE_TO_ROUTE_43_TOP_WP = WarpInstruction(
        getHex(ROUTE_43_GATE.ROUTE_43_TOP),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_43_GATE_TO_ROUTE_43_BOTTOM_WP = WarpInstruction(
        getHex(ROUTE_43_GATE.ROUTE_43_BOTTOM),
        getHex(mapGroup),
        getHex(specificMap))


