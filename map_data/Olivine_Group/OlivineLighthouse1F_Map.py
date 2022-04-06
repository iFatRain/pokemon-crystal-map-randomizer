from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.OLIVINE_LIGHTHOUSE_1F

class OLIVINE_LIGHTHOUSE_1F(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_CITY = 1  # dual wide
    OLIVINE_LIGHTHOUSE_2FA = 3
    OLIVINE_LIGHTHOUSE_2FB = 4 # FROM DROP



class Olivine_Lighthouse_1F_Warp_Points(Enum):

    OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_CITY_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_1F.OLIVINE_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_LIGHTHOUSE_2FA_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_1F.OLIVINE_LIGHTHOUSE_2FA),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_1F_TO_OLIVINE_LIGHTHOUSE_2FB_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_1F.OLIVINE_LIGHTHOUSE_2FB),
        getHex(mapGroup),
        getHex(specificMap))