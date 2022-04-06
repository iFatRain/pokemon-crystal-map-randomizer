from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_GAME_CORNER

class GOLDENROD_GAME_CORNER(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_CITY = 1  # dual wide


class Goldenrod_Game_Corner_Warp_Points(Enum):

    GOLDENROD_GAME_CORNER_TO_GOLDENROD_CITY_WP = WarpInstruction(
        getHex(GOLDENROD_GAME_CORNER.GOLDENROD_CITY),
        getHex(mapGroup),
        getHex(specificMap))