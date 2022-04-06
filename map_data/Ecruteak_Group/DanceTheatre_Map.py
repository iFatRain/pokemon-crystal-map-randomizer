from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Ecruteak

mapGroup = MapGroup.ECRUTEAK
specificMap = Ecruteak.DANCE_THEATRE

class DANCE_THEATRE(IntEnum):
    def __str__(self):
        return str(self.value)

    ECRUTEAK_CITY = 1  # dual wide


class Dance_Theatre_Warp_Points(Enum):

    DANCE_THEATRE_TO_ECRUTEAK_CITY_WP = WarpInstruction(
        getHex(DANCE_THEATRE.ECRUTEAK_CITY),
        getHex(mapGroup),
        getHex(specificMap))