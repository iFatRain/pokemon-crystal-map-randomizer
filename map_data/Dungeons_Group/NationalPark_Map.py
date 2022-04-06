from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.NATIONAL_PARK

class NATIONAL_PARK(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_36_NATIONAL_PARK_GATE = 1  # dual width
    ROUTE_35_NATIONAL_PARK_GATE = 3  # dual width


class National_Park_Warp_Points(Enum):

    NATIONAL_PARK_TO_ROUTE_36_NATIONAL_PARK_GATE_WP = WarpInstruction(
        getHex(NATIONAL_PARK.ROUTE_36_NATIONAL_PARK_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    NATIONAL_PARK_TO_ROUTE_35_NATIONAL_PARK_GATE_WP = WarpInstruction(
        getHex(NATIONAL_PARK.ROUTE_35_NATIONAL_PARK_GATE),
        getHex(mapGroup),
        getHex(specificMap))

