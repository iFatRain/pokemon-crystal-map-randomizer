from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cianwood

mapGroup = MapGroup.CIANWOOD
specificMap = Cianwood.CIANWOOD_LUGIA_SPEECH_HOUSE

class CIANWOOD_LUGIA_SPEECH_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    CIANWOOD_CITY = 1  # dual wide


class Cianwood_Lugia_Speech_House_Warp_Points(Enum):

    Cianwood_City_Lugia_Speech_House_Exit_WP = WarpInstruction(
        getHex(CIANWOOD_LUGIA_SPEECH_HOUSE.CIANWOOD_CITY),
        getHex(mapGroup),
        getHex(specificMap))