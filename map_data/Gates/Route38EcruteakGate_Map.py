from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Olivine

mapGroup = MapGroup.OLIVINE
specificMap = Olivine.ROUTE_38_ECRUTEAK_GATE

class ROUTE_38_ECRUTEAK_GATE(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_38 = 1  # dual width
    ECRUTEAK_CITY = 3  # dual width


class Route_38_Ecruteak_Gate_Warp_Points(Enum):

    ROUTE_38_ECRUTEAK_GATE_TO_ROUTE_38_WP = WarpInstruction(
        getHex(ROUTE_38_ECRUTEAK_GATE.ROUTE_38),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_38_ECRUTEAK_GATE_TO_ECRUTEAK_CITY_WP = WarpInstruction(
        getHex(ROUTE_38_ECRUTEAK_GATE.ECRUTEAK_CITY),
        getHex(mapGroup),
        getHex(specificMap))
