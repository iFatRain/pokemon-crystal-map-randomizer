from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.OLIVINE_LIGHTHOUSE_3F

class OLIVINE_LIGHTHOUSE_3F(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_LIGHTHOUSE_4FA = 1 #right stair to 4F
    OLIVINE_LIGHTHOUSE_2FA = 2 #left stair from 2f
    OLIVINE_LIGHTHOUSE_4FB = 3  #center stair to 4F
    OLIVINE_LIGHTHOUSE_2FB = 4  # dual width drop to below
    OLIVINE_LIGHTHOUSE_4FC = 6  # dual width drop from above right
    OLIVINE_LIGHTHOUSE_4FD = 8  # dual width drop from above center


class Olivine_Lighthouse_3F_Warp_Points(Enum):

    OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FA_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_3F.OLIVINE_LIGHTHOUSE_4FA),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_2FA_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_3F.OLIVINE_LIGHTHOUSE_2FA),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FB_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_3F.OLIVINE_LIGHTHOUSE_4FB),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_2FB_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_3F.OLIVINE_LIGHTHOUSE_2FB),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FC_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_3F.OLIVINE_LIGHTHOUSE_4FC),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_3F_TO_OLIVINE_LIGHTHOUSE_4FD_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_3F.OLIVINE_LIGHTHOUSE_4FD),
        getHex(mapGroup),
        getHex(specificMap))