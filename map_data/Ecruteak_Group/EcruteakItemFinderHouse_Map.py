from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Ecruteak

mapGroup = MapGroup.ECRUTEAK
specificMap = Ecruteak.ECRUTEAK_ITEMFINDER_HOUSE

class ECRUTEAK_ITEMFINDER_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    ECRUTEAK_CITY = 1  # dual wide


class Ecruteak_Itemfinder_House_Warp_Points(Enum):

    ECRUTEAK_ITEMFINDER_HOUSE_TO_ECRUTEAK_CITY_WP = WarpInstruction(
        getHex(ECRUTEAK_ITEMFINDER_HOUSE.ECRUTEAK_CITY),
        getHex(mapGroup),
        getHex(specificMap))