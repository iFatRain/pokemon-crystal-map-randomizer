from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Mahogany

mapGroup = MapGroup.MAHOGANY
specificMap = Mahogany.MAHOGANY_POKECENTER_1F

class MAHOGANY_POKECENTER_1F(IntEnum):
    def __str__(self):
        return str(self.value)

    MAHOGANY_TOWN = 1 # dual wide
    POKECENTER_2F = 3


class Mahogany_Pokecenter_Warp_Points(Enum):

    MAHOGANY_POKECENTER_1F_TO_MAHOGANY_TOWN_WP = WarpInstruction(
        getHex(MAHOGANY_POKECENTER_1F.MAHOGANY_TOWN),
        getHex(mapGroup),
        getHex(specificMap))

    MAHOGANY_POKECENTER_TO_MAHOGANY_POKECENTER_2F_WP = WarpInstruction(
        getHex(MAHOGANY_POKECENTER_1F.POKECENTER_2F),
        getHex(mapGroup),
        getHex(specificMap))
