from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.ILEX_FOREST_AZALEA_GATE

class ILEX_FOREST_AZALEA_GATE(IntEnum):
    def __str__(self):
        return str(self.value)

    ILEX_FOREST = 1  # dual width
    AZALEA_TOWN = 3  # dual width


class Ilex_Forest_Azalea_Gate_Warp_Points(Enum):

    ILEX_FOREST_AZALEA_GATE_TO_ILEX_FOREST_WP = WarpInstruction(
        getHex(ILEX_FOREST_AZALEA_GATE.ILEX_FOREST),
        getHex(mapGroup),
        getHex(specificMap))

    ILEX_FOREST_AZALEA_GATE_TO_AZALEA_TOWN_WP = WarpInstruction(
        getHex(ILEX_FOREST_AZALEA_GATE.AZALEA_TOWN),
        getHex(mapGroup),
        getHex(specificMap))


