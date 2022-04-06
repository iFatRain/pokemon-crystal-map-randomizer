from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_NAME_RATER

class GOLDENROD_NAME_RATER(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_CITY = 1  # dual wide


class Goldenrod_Name_Rater_Warp_Points(Enum):

    GOLDENROD_NAME_RATER_TO_GOLDENROD_CITY_WP = WarpInstruction(
        getHex(GOLDENROD_NAME_RATER.GOLDENROD_CITY),
        getHex(mapGroup),
        getHex(specificMap))