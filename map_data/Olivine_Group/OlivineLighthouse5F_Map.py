from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.OLIVINE_LIGHTHOUSE_5F

class OLIVINE_LIGHTHOUSE_5F(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_LIGHTHOUSE_6FA = 1  #Bottom stairs to 6F
    OLIVINE_LIGHTHOUSE_4FA = 2  #Left 4F Stairs
    OLIVINE_LIGHTHOUSE_4FB = 3  #Middle 4F stairs
    OLIVINE_LIGHTHOUSE_4FC = 4  # dual width drop to below
    OLIVINE_LIGHTHOUSE_6FB = 6  # dual width drop from above


class Olivine_Lighthouse_5F_Warp_Points(Enum):

    OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_6FA_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_5F.OLIVINE_LIGHTHOUSE_6FA),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FA_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_5F.OLIVINE_LIGHTHOUSE_4FA),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FB_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_5F.OLIVINE_LIGHTHOUSE_4FB),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_4FC_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_5F.OLIVINE_LIGHTHOUSE_4FC),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_5F_TO_OLIVINE_LIGHTHOUSE_6FB_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_5F.OLIVINE_LIGHTHOUSE_6FB),
        getHex(mapGroup),
        getHex(specificMap))
