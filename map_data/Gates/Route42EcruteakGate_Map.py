from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Mahogany

mapGroup = MapGroup.MAHOGANY
specificMap = Mahogany.ROUTE_42_ECRUTEAK_GATE

class ROUTE_42_ECRUTEAK_GATE(IntEnum):
    def __str__(self):
        return str(self.value)

    ECRUTEAK_CITY = 1  # dual width
    ROUTE_42 = 3  # dual width


class Route_42_Ecruteak_Gate_Warp_Points(Enum):

    ROUTE_42_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_WP = WarpInstruction(
        getHex(ROUTE_42_ECRUTEAK_GATE.ECRUTEAK_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_42_ECRUTEAK_GATE_TO_ROUTE_42_WP = WarpInstruction(
        getHex(ROUTE_42_ECRUTEAK_GATE.ROUTE_42),
        getHex(mapGroup),
        getHex(specificMap))

