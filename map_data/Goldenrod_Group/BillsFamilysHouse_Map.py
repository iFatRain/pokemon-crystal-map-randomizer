from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.BILLS_FAMILYS_HOUSE

class BILLS_FAMILYS_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_CITY = 1  # dual wide


class Bills_Familys_House_Warp_Points(Enum):

    BILLS_FAMILYS_HOUSE_TO_GOLDENROD_CITY_WP = WarpInstruction(
        getHex(BILLS_FAMILYS_HOUSE.GOLDENROD_CITY),
        getHex(mapGroup),
        getHex(specificMap))