from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.OLIVINE_LIGHTHOUSE_4F

class OLIVINE_LIGHTHOUSE_4F(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_LIGHTHOUSE_3FA = 1 #right stairs to 3F
    OLIVINE_LIGHTHOUSE_5FA = 2 #left stairs to 5F
    OLIVINE_LIGHTHOUSE_5FB = 3 #center stairs to 5F
    OLIVINE_LIGHTHOUSE_3FB = 4 #center stairs to 3F
    OLIVINE_LIGHTHOUSE_3FC = 5  # dual width top pit to 3f
    OLIVINE_LIGHTHOUSE_3FD = 7  # dual width bottom pit to 3f
    OLIVINE_LIGHTHOUSE_5FC = 9  # dual width from 5f


class Olivine_Lighthouse_4F_Warp_Points(Enum):

    OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FA_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_4F.OLIVINE_LIGHTHOUSE_3FA),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FA_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_4F.OLIVINE_LIGHTHOUSE_5FA),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FB_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_4F.OLIVINE_LIGHTHOUSE_5FB),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FB_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_4F.OLIVINE_LIGHTHOUSE_3FB),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FC_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_4F.OLIVINE_LIGHTHOUSE_3FC),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_3FD_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_4F.OLIVINE_LIGHTHOUSE_3FD),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_4F_TO_OLIVINE_LIGHTHOUSE_5FC_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_4F.OLIVINE_LIGHTHOUSE_5FC),
        getHex(mapGroup),
        getHex(specificMap))
