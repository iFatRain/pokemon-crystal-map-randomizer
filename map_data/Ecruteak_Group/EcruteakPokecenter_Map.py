from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Ecruteak

mapGroup = MapGroup.ECRUTEAK
specificMap = Ecruteak.ECRUTEAK_POKECENTER_1F

class ECRUTEAK_POKECENTER_1F(IntEnum):
    def __str__(self):
        return str(self.value)

    ECRUTEAK_CITY = 1  # dual wide
    POKECENTER_2F = 3

class Ecruteak_Pokecenter_Warp_Points(Enum):

    ECRUTEAK_POKECENTER_1F_TO_ECRUTEAK_CITY_WP = WarpInstruction(
        getHex(ECRUTEAK_POKECENTER_1F.ECRUTEAK_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    ECRUTEAK_POKECENTER_TO_ECRUTEAK_POKECENTER_2F_WP = WarpInstruction(
        getHex(ECRUTEAK_POKECENTER_1F.POKECENTER_2F),
        getHex(mapGroup),
        getHex(specificMap))