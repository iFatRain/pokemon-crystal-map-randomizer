from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Olivine

mapGroup = MapGroup.OLIVINE
specificMap = Olivine.OLIVINE_GOOD_ROD_HOUSE

class OLIVINE_GOOD_ROD_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_CITY = 1 # dual wide


class Olivine_Good_Rod_House_Warp_Points(Enum):

    OLIVINE_GOOD_ROD_HOUSE_TO_OLIVINE_CITY_WP = WarpInstruction(
        getHex(OLIVINE_GOOD_ROD_HOUSE.OLIVINE_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )