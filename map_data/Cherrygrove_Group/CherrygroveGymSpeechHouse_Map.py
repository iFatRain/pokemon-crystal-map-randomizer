from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cherrygrove

mapGroup = MapGroup.CHERRYGROVE
specificMap = Cherrygrove.CHERRYGROVE_GYM_SPEECH_HOUSE

class CHERRYGROVE_GYM_SPEECH_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    CHERRYGROVE_CITY = 1  # dual width


class Cherrygrove_Gym_Speech_House_Warp_Points(Enum):

    CHERRYGROVE_GYM_SPEECH_HOUSE_TO_CHERRYGROVE_CITY = WarpInstruction(
        getHex(CHERRYGROVE_GYM_SPEECH_HOUSE.CHERRYGROVE_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )
