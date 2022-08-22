from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Azalea

mapGroup = MapGroup.AZALEA
specificMap = Azalea.AZALEA_GYM

class AZALEA_GYM(IntEnum):
    def __str__(self):
        return str(self.value)

    AZALEA_TOWN = 1  # dual wide


class Azalea_Gym_Warp_Points(Enum):

    Azalea_Gym_Exit_WP = WarpInstruction(
        getHex(AZALEA_GYM.AZALEA_TOWN),
        getHex(mapGroup),
        getHex(specificMap))