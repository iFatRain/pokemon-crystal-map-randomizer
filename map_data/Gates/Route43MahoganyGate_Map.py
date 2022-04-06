from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lake_Of_Rage

mapGroup = MapGroup.LAKE_OF_RAGE
specificMap = Lake_Of_Rage.ROUTE_43_MAHOGANY_GATE

class ROUTE_43_MAHOGANY_GATE(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_43 = 1
    MAHOGANY_TOWN = 3


class Route_43_Mahogany_Gate_Warp_Points(Enum):

    ROUTE_43_MAHOGANY_GATE_TO_ROUTE_43_WP = WarpInstruction(
        getHex(ROUTE_43_MAHOGANY_GATE.ROUTE_43),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_43_MAHOGANY_GATE_TO_MAHOGANY_TOWN_WP = WarpInstruction(
        getHex(ROUTE_43_MAHOGANY_GATE.MAHOGANY_TOWN),
        getHex(mapGroup),
        getHex(specificMap))