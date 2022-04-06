from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Ecruteak

mapGroup = MapGroup.ECRUTEAK
specificMap = Ecruteak.ECRUTEAK_GYM

class ECRUTEAK_GYM(IntEnum):
    def __str__(self):
        return str(self.value)

    ECRUTEAK_CITY = 1  # dual wide


class Ecruteak_Gym_Warp_Points(Enum):

    ECRUTEAK_GYM_TO_ECRUTEAK_CITY_WP = WarpInstruction(
        getHex(ECRUTEAK_GYM.ECRUTEAK_CITY),
        getHex(mapGroup),
        getHex(specificMap))