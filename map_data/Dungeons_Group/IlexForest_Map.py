from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.ILEX_FOREST

class ILEX_FOREST(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_34_ILEX_FOREST_GATE = 1
    ILEX_FOREST_AZALEA_GATE = 2  # dual width


class Ilex_Forest_Warp_Points(Enum):

    ILEX_FOREST_TO_ROUTE_34_ILEX_FOREST_GATE_WP = WarpInstruction(
        getHex(ILEX_FOREST.ROUTE_34_ILEX_FOREST_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    ILEX_FOREST_TO_ILEX_FOREST_AZALEA_GATE_WP = WarpInstruction(
        getHex(ILEX_FOREST.ILEX_FOREST_AZALEA_GATE),
        getHex(mapGroup),
        getHex(specificMap))

