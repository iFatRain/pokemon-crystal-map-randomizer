from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod

mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_FLOWER_SHOP

class GOLDENROD_FLOWER_SHOP(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_CITY = 1  # dual wide


class Goldenrod_Flower_Shop_Warp_Points(Enum):

    GOLDENROD_FLOWER_SHOP_TO_GOLDENROD_CITY_WP = WarpInstruction(
        getHex(GOLDENROD_FLOWER_SHOP.GOLDENROD_CITY),
        getHex(mapGroup),
        getHex(specificMap))