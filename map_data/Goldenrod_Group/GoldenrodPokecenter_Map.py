from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_POKECENTER_1F

class GOLDENROD_POKECENTER(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_CITY = 1  # dual wide
    POKECENTER_2F = 4


class Goldenrod_Pokecenter_Warp_Points(Enum):

    GOLDENROD_POKECENTER_TO_GOLDENROD_CITY_WP = WarpInstruction(
        getHex(GOLDENROD_POKECENTER.GOLDENROD_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    GOLDENROD_POKECENTER_TO_GOLDENROD_POKECENTER_2F_WP = WarpInstruction(
        getHex(GOLDENROD_POKECENTER.POKECENTER_2F),
        getHex(mapGroup),
        getHex(specificMap))