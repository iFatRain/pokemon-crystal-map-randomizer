from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.VIOLET_NICKNAME_SPEECH_HOUSE

class VIOLET_NICKNAME_SPEECH_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    VIOLET_CITY = 1  # dual width



class Violet_Nickname_Speech_House_Warp_Points(Enum):

    VIOLET_NICKNAME_SPEECH_HOUSE_TO_VIOLET_CITY_WP = WarpInstruction(
        getHex(VIOLET_NICKNAME_SPEECH_HOUSE.VIOLET_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )
