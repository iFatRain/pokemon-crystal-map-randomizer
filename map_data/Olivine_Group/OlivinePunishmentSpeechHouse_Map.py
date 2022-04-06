from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Olivine

mapGroup = MapGroup.OLIVINE
specificMap = Olivine.OLIVINE_PUNISHMENT_SPEECH_HOUSE

class OLIVINE_PUNISHMENT_SPEECH_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_CITY = 1  # dual width


class Olivine_Punishment_Speech_House_Warp_Points(Enum):

    OLIVINE_PUNISHMENT_SPEECH_HOUSE_TO_OLIVINE_CITY_WP = WarpInstruction(
        getHex(OLIVINE_PUNISHMENT_SPEECH_HOUSE.OLIVINE_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )