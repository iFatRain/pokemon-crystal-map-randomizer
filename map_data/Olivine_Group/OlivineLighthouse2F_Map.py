from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.OLIVINE_LIGHTHOUSE_2F

class OLIVINE_LIGHTHOUSE_2F(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_LIGHTHOUSE_1FA = 1
    OLIVINE_LIGHTHOUSE_3FA = 2
    OLIVINE_LIGHTHOUSE_1FB = 3 # dual wide INTO drop
    OLIVINE_LIGHTHOUSE_3FB = 5 # dual wide FROM drop




class Olivine_Lighthouse_2F_Warp_Points(Enum):

    OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_1FA_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_2F.OLIVINE_LIGHTHOUSE_1FA),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_3FA_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_2F.OLIVINE_LIGHTHOUSE_3FA),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_1FB_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_2F.OLIVINE_LIGHTHOUSE_1FB),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_2F_TO_OLIVINE_LIGHTHOUSE_3FB_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_2F.OLIVINE_LIGHTHOUSE_3FB),
        getHex(mapGroup),
        getHex(specificMap))
