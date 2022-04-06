from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.ROUTE_34_ILEX_FOREST_GATE

class ROUTE_34_ILEX_FOREST_GATE(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_34 = 1  # dual width
    ILEX_FOREST = 3  # dual width


class Route_34_Ilex_Forest_Gate_Warp_Points(Enum):

    ROUTE_34_ILEX_FOREST_GATE_TO_ROUTE_34_WP = WarpInstruction(
        getHex(ROUTE_34_ILEX_FOREST_GATE.ROUTE_34),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_34_ILEX_FOREST_GATE_TO_ILEX_FOREST_WP = WarpInstruction(
        getHex(ROUTE_34_ILEX_FOREST_GATE.ILEX_FOREST),
        getHex(mapGroup),
        getHex(specificMap))
