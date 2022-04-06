from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Olivine

mapGroup = MapGroup.OLIVINE
specificMap = Olivine.OLIVINE_POKECENTER_1F

class OLIVINE_POKECENTER(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_CITY = 1  # dual width
    POKECENTER_2F = 3


class Olivine_Pokecenter_Warp_Points(Enum):

    OLIVINE_POKECENTER_TO_OLIVINE_CITY_WP = WarpInstruction(
        getHex(OLIVINE_POKECENTER.OLIVINE_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )

    OLIVINE_POKECENTER_TO_OLIVINE_POKECENTER_2F_WP = WarpInstruction(
        getHex(OLIVINE_POKECENTER.POKECENTER_2F),
        getHex(mapGroup),
        getHex(specificMap))