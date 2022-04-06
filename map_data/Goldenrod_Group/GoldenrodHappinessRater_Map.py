from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_HAPPINESS_RATER

class GOLDENROD_HAPPINESS_RATER(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_CITY = 1  # dual wide


class Goldenrod_Happiness_Rater_Warp_Points(Enum):

    GOLDENROD_HAPPINESS_RATER_TO_GOLDENROD_CITY_WP = WarpInstruction(
        getHex(GOLDENROD_HAPPINESS_RATER.GOLDENROD_CITY),
        getHex(mapGroup),
        getHex(specificMap))