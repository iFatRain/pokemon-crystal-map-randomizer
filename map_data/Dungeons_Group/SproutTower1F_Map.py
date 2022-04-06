from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.SPROUT_TOWER_1F

class SPROUT_TOWER_1F(IntEnum):
    def __str__(self):
        return str(self.value)

    VIOLET_CITY = 1  # dual width
    SPROUT_TOWER_2FA = 3
    SPROUT_TOWER_2FB = 4
    SPROUT_TOWER_2FC = 5


class Sprout_Tower_1F_Warp_Points(Enum):

    SPROUT_TOWER_1F_TO_VIOLET_CITY_WP = WarpInstruction(
        getHex(SPROUT_TOWER_1F.VIOLET_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FA_WP = WarpInstruction(
        getHex(SPROUT_TOWER_1F.SPROUT_TOWER_2FA),
        getHex(mapGroup),
        getHex(specificMap))

    SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FB_WP = WarpInstruction(
        getHex(SPROUT_TOWER_1F.SPROUT_TOWER_2FB),
        getHex(mapGroup),
        getHex(specificMap))

    SPROUT_TOWER_1F_TO_SPROUT_TOWER_2FC_WP = WarpInstruction(
        getHex(SPROUT_TOWER_1F.SPROUT_TOWER_2FC),
        getHex(mapGroup),
        getHex(specificMap))