from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cherrygrove

mapGroup = MapGroup.CHERRYGROVE
specificMap = Cherrygrove.CHERRYGROVE_MART

class CHERRYGROVE_MART(IntEnum):
    def __str__(self):
        return str(self.value)

    CHERRYGROVE_CITY = 1  # dual width


class Cherrygrove_Mart_Warp_Points(Enum):

    CHERRYGROVE_MART_TO_CHERRYGROVE_CITY_WP = WarpInstruction(
        getHex(CHERRYGROVE_MART.CHERRYGROVE_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )
