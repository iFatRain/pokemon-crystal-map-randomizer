from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_BIKE_SHOP

class GOLDENROD_BIKE_SHOP(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_CITY = 1  # dual wide


class Goldenrod_Bike_Shop_Warp_Points(Enum):

    GOLDENROD_BIKE_SHOP_TO_GOLDENROD_CITY_WP = WarpInstruction(
        getHex(GOLDENROD_BIKE_SHOP.GOLDENROD_CITY),
        getHex(mapGroup),
        getHex(specificMap))