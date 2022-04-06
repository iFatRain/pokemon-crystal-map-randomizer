from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.RADIO_TOWER_1F

class RADIO_TOWER_1F(IntEnum):
    def __str__(self):
        return str(self.value)

    GOLDENROD_CITY = 1  # dual wide
    RADIO_TOWER_2F = 3


class Radio_Tower_1F_Warp_Points(Enum):

    RADIO_TOWER_1F_TO_GOLDENROD_CITY_WP = WarpInstruction(
        getHex(RADIO_TOWER_1F.GOLDENROD_CITY),
        getHex(mapGroup),
        getHex(specificMap))

    RADIO_TOWER_1F_TO_RADIO_TOWER_2F_WP = WarpInstruction(
        getHex(RADIO_TOWER_1F.RADIO_TOWER_2F),
        getHex(mapGroup),
        getHex(specificMap))