from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cherrygrove

mapGroup = MapGroup.CHERRYGROVE
specificMap = Cherrygrove.CHERRYGROVE_EVOLUTION_SPEECH_HOUSE

class CHERRYGROVE_EVOLUITION_SPEECH_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    CHERRYGROVE_CITY = 1  # dual width


class Cherrygrove_Evolution_Speech_House_Warp_Points(Enum):

    CHERRYGROVE_EVOLUTION_SPEECH_HOUSE_TO_CHERRYGROVE_CITY_WP = WarpInstruction(
        getHex(CHERRYGROVE_EVOLUITION_SPEECH_HOUSE.CHERRYGROVE_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )
