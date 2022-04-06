from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons

mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.RUINS_OF_ALPH_RESEARCH_CENTER

class RUINS_OF_ALPH_RESEARCH_CENTER(IntEnum):
    def __str__(self):
        return str(self.value)

    RUINS_OF_ALPH_OUTSIDE = 1  # dual wide



class Ruins_Of_Alph_Research_Center_Warp_Points(Enum):

    RUINS_OF_ALPH_RESEARCH_CENTER_TO_RUINS_OF_ALPH_OUTSIDE_WP = WarpInstruction(
        getHex(RUINS_OF_ALPH_RESEARCH_CENTER.RUINS_OF_ALPH_OUTSIDE),
        getHex(mapGroup),
        getHex(specificMap))


