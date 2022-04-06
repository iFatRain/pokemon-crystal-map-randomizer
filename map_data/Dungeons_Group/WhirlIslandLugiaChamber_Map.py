from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.WHIRL_ISLAND_LUGIA_CHAMBER

class WHIRL_ISLAND_LUGIA_CHAMBER(IntEnum):
    def __str__(self):
        return str(self.value)

    WHIRL_ISLAND_B2F = 1


class Whirl_Island_Lugia_Chamber_Warp_Points(Enum):

    WHIRL_ISLAND_LUGIA_CHAMBER_TO_WHIRL_ISLAND_B2F_WP = WarpInstruction(
        getHex(WHIRL_ISLAND_LUGIA_CHAMBER.WHIRL_ISLAND_B2F),
        getHex(mapGroup),
        getHex(specificMap))

