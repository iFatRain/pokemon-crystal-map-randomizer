from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Olivine

mapGroup = MapGroup.OLIVINE
specificMap = Olivine.ROUTE_38

class ROUTE_38(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_38_ECRUTEAK_GATE = 1  # dual wide

class Route_38_Warp_Points(Enum):

    ROUTE_38_TO_ROUTE_38_ECRUTEAK_GATE_WP = WarpInstruction(
        getHex(ROUTE_38.ROUTE_38_ECRUTEAK_GATE),
        getHex(mapGroup),
        getHex(specificMap))

