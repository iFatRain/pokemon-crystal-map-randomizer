from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Mahogany

mapGroup = MapGroup.MAHOGANY
specificMap = Mahogany.MAHOGANY_RED_GYARADOS_SPEECH_HOUSE

class MAHOGANY_RED_GYARADOS_SPEECH_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    MAHOGANY_TOWN = 1


class Mahogany_Red_Gyarados_Speech_House_Warp_Points(Enum):

    MAHOGANY_RED_GYARADOS_SPEECH_HOUSE_TO_MAHOGANY_TOWN_WP = WarpInstruction(
        getHex(MAHOGANY_RED_GYARADOS_SPEECH_HOUSE.MAHOGANY_TOWN),
        getHex(mapGroup),
        getHex(specificMap))

