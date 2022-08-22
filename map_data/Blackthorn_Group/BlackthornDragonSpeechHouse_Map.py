from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Blackthorn

mapGroup = MapGroup.BLACKTHORN
specificMap = Blackthorn.BLACKTHORN_DRAGON_SPEECH_HOUSE


class BLACKTHORN_DRAGON_SPEECH_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    BLACKTHORN_CITY = 1


class Blackthorn_Dragon_Speech_House_Warp_Points(Enum):

    Blackthorn_City_Dragon_Speech_House_Exit_WP = WarpInstruction(
        getHex(BLACKTHORN_DRAGON_SPEECH_HOUSE.BLACKTHORN_CITY),
        getHex(mapGroup),
        getHex(specificMap))
