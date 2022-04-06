from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_PP_SPEECH_HOUSE

class GOLDENROD_PP_SPEECH_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_CITY = 1  # dual wide


class Goldenrod_PP_Speech_House_Warp_Points(Enum):

    GOLDENROD_PP_SPEECH_HOUSE_TO_GOLDENROD_CITY_WP = WarpInstruction(
        getHex(GOLDENROD_PP_SPEECH_HOUSE.GOLDENROD_CITY),
        getHex(mapGroup),
        getHex(specificMap))