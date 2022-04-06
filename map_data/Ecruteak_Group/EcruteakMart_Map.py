from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Ecruteak

mapGroup = MapGroup.ECRUTEAK
specificMap = Ecruteak.ECRUTEAK_MART

class ECRUTEAK_MART(IntEnum):
    def __str__(self):
        return str(self.value)

    ECRUTEAK_CITY = 1  # dual wide


class Ecruteak_Mart_Warp_Points(Enum):

    ECRUTEAK_MART_TO_ECRUTEAK_CITY_WP = WarpInstruction(
        getHex(ECRUTEAK_MART.ECRUTEAK_CITY),
        getHex(mapGroup),
        getHex(specificMap))