from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Mahogany

mapGroup = MapGroup.MAHOGANY
specificMap = Mahogany.MAHOGANY_GYM

class MAHOGANY_GYM(IntEnum):
    def __str__(self):
        return str(self.value)

    MAHOGANY_TOWN = 1



class Mahogany_Gym_Warp_Points(Enum):

    MAHOGANY_GYM_TO_MAHOGANY_TOWN_WP = WarpInstruction(
        getHex(MAHOGANY_GYM.MAHOGANY_TOWN),
        getHex(mapGroup),
        getHex(specificMap))



