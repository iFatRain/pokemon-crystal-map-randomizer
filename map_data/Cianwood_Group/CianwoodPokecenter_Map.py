from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cianwood

mapGroup = MapGroup.CIANWOOD
specificMap = Cianwood.CIANWOOD_POKECENTER_1F

class CIANWOOD_POKECENTER_1F(IntEnum):
    def __str__(self):
        return str(self.value)

    CIANWOOD_CITY = 1  # dual wide
    POKECENTER_2F = 3


class Cianwood_Pokecenter_Warp_Points(Enum):

    CIANWOOD_POKECENTER_1F_TO_CIANWOOD_CITY_WP = WarpInstruction(
        getHex(CIANWOOD_POKECENTER_1F.CIANWOOD_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    CIANWOOD_POKECENTER_TO_CIANWOOD_POKECENTER_2F_WP = WarpInstruction(
        getHex(CIANWOOD_POKECENTER_1F.POKECENTER_2F),
        getHex(mapGroup),
        getHex(specificMap))