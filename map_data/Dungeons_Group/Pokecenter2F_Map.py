from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cable_Club

mapGroup = MapGroup.CABLE_CLUB
specificMap = Cable_Club.POKECENTER_2F

class POKECENTER_2F(IntEnum):
    def __str__(self):
        return str(self.value)

    POKECENTER_1F = 1  # dual wide


class Pokecenter_2F_Warp_Points(Enum):

    POKECENTER_2F_TO_POKECENTER_1F_WP = WarpInstruction(
        getHex(POKECENTER_2F.POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap))