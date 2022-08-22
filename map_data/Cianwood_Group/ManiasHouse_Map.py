from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cianwood

mapGroup = MapGroup.CIANWOOD
specificMap = Cianwood.MANIAS_HOUSE

class MANIAS_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    CIANWOOD_CITY = 1  # dual wide


class Manias_House_Warp_Points(Enum):

    Cianwood_City_Shuckle_House_Exit_WP = WarpInstruction(
        getHex(MANIAS_HOUSE.CIANWOOD_CITY),
        getHex(mapGroup),
        getHex(specificMap))