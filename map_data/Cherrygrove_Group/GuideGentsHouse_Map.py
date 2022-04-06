from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cherrygrove

mapGroup = MapGroup.CHERRYGROVE
specificMap = Cherrygrove.GUIDE_GENTS_HOUSE

class GUIDE_GENTS_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    CHERRYGROVE_CITY = 1  # dual width


class Guide_Gents_House_Warp_Points(Enum):

    GUIDE_GENTS_HOUSE_TO_CHERRYGROVE_CITY_WP = WarpInstruction(
        getHex(GUIDE_GENTS_HOUSE.CHERRYGROVE_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )
