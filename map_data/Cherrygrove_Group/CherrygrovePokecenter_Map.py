from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cherrygrove

mapGroup = MapGroup.CHERRYGROVE
specificMap = Cherrygrove.CHERRYGROVE_POKECENTER_1F

class CHERRYGROVE_POKECENTER(IntEnum):
    def __str__(self):
        return str(self.value)

    CHERRYGROVE_CITY = 1  # dual width
    POKECENTER_2F = 3


class Cherrygrove_Pokecenter_Warp_Points(Enum):

    CHERRYGROVE_POKECENTER_TO_CHERRYGROVE_CITY = WarpInstruction(
        getHex(CHERRYGROVE_POKECENTER.CHERRYGROVE_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )

    CHERRYGROVE_POKECENTER_TO_CHERRYGROVE_POKECENTER_2F_WP = WarpInstruction(
        getHex(CHERRYGROVE_POKECENTER.POKECENTER_2F),
        getHex(mapGroup),
        getHex(specificMap))