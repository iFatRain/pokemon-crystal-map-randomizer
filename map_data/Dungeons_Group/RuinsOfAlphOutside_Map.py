from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.RUINS_OF_ALPH_OUTSIDE

class RUINS_OF_ALPH_OUTSIDE(IntEnum):
    def __str__(self):
        return str(self.value)

    RUINS_OF_ALPH_HO_OH_CHAMBER = 1
    RUINS_OF_ALPH_KABUTO_CHAMBER = 2
    RUINS_OF_ALPH_OMANYTE_CHAMBER = 3
    RUINS_OF_ALPH_AERODACTYL_CHAMBER = 4
    RUINS_OF_ALPH_INNER_CHAMBER = 5
    RUINS_OF_ALPH_RESEARCH_CENTER = 6
    UNION_CAVE_B1FA = 7
    UNION_CAVE_B1FB = 8
    ROUTE_36_RUINS_OF_ALPH_GATE = 9
    ROUTE_32_RUINS_OF_ALPH_GATE = 10  # dual wide



class Ruins_Of_Alph_Outside_Warp_Points(Enum):

    RUINS_OF_ALPH_OUTSIDE_TO_RUINS_OF_ALPH_RESEARCH_CENTER_WP = WarpInstruction(
        getHex(RUINS_OF_ALPH_OUTSIDE.RUINS_OF_ALPH_RESEARCH_CENTER),
        getHex(mapGroup),
        getHex(specificMap))

    RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_36_RUINS_OF_ALPH_GATE_WP = WarpInstruction(
        getHex(RUINS_OF_ALPH_OUTSIDE.ROUTE_36_RUINS_OF_ALPH_GATE),
        getHex(mapGroup),
        getHex(specificMap))

    RUINS_OF_ALPH_OUTSIDE_TO_ROUTE_32_RUINS_OF_ALPH_GATE_WP = WarpInstruction(
        getHex(RUINS_OF_ALPH_OUTSIDE.ROUTE_32_RUINS_OF_ALPH_GATE),
        getHex(mapGroup),
        getHex(specificMap))

#     THERE ARE MORE WARPS TO BE ADDED POTENTIALLY


