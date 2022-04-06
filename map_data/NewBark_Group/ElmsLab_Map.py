from enum import IntEnum, Enum

from class_definitions import getHex, WarpInstruction
from map_data.map_constants import New_Bark, MapGroup

mapGroup = MapGroup.NEW_BARK
specificMap = New_Bark.ELMS_LAB

class ELMS_LAB(IntEnum):
    def __str__(self):
        return str(self.value)

    NEW_BARK_TOWN = 1  # dual wide

class Elms_Lab_Warp_Points(Enum):

    ELMS_LAB_TO_NEW_BARK_WP = WarpInstruction(
        getHex(ELMS_LAB.NEW_BARK_TOWN),
        getHex(mapGroup),
        getHex(specificMap),
        )


