from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cianwood

mapGroup = MapGroup.CIANWOOD
specificMap = Cianwood.CIANWOOD_GYM

class CIANWOOD_GYM(IntEnum):
    def __str__(self):
        return str(self.value)

    CIANWOOD_CITY = 1  # dual wide


class Cianwood_Gym_Warp_Points(Enum):

    Cianwood_City_Gym_Exit_WP = WarpInstruction(
        getHex(CIANWOOD_GYM.CIANWOOD_CITY),
        getHex(mapGroup),
        getHex(specificMap))