from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.OLIVINE_LIGHTHOUSE_6F

class OLIVINE_LIGHTHOUSE_6F(IntEnum):
    def __str__(self):
        return str(self.value)

    OLIVINE_LIGHTHOUSE_5FA = 1 #Stairs to 4F
    OLIVINE_LIGHTHOUSE_5FB = 2  # dual width Pit to 4F


class Olivine_Lighthouse_6F_Warp_Points(Enum):

    OLIVINE_LIGHTHOUSE_6F_TO_OLIVINE_LIGHTHOUSE_5FA_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_6F.OLIVINE_LIGHTHOUSE_5FA),
        getHex(mapGroup),
        getHex(specificMap))

    OLIVINE_LIGHTHOUSE_6F_TO_OLIVINE_LIGHTHOUSE_5FB_WP = WarpInstruction(
        getHex(OLIVINE_LIGHTHOUSE_6F.OLIVINE_LIGHTHOUSE_5FB),
        getHex(mapGroup),
        getHex(specificMap))
