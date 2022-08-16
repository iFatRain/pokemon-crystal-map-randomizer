from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cherrygrove

mapGroup = MapGroup.CHERRYGROVE
specificMap = Cherrygrove.CHERRYGROVE_CITY

class CHERRYGROVE_CITY(IntEnum):
    def __str__(self):
        return str(self.value)

    CHERRYGROVE_MART = 1
    CHERRYGROVE_POKECENTER_1F = 2
    CHERRYGROVE_GYM_SPEECH_HOUSE = 3
    GUIDE_GENTS_HOUSE = 4
    CHERRYGROVE_EVOLUTION_SPEECH_HOUSE = 5


class Cherrygrove_City_Warp_Points(Enum):

    Cherrygrove_City_Mart_Entrance_WP = WarpInstruction(
        getHex(CHERRYGROVE_CITY.CHERRYGROVE_MART),
        getHex(mapGroup),
        getHex(specificMap))

    Cherrygrove_City_Pokecenter_Entrance_WP = WarpInstruction(
        getHex(CHERRYGROVE_CITY.CHERRYGROVE_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap),
        )

    Cherrygrove_City_West_House_Entrance_WP = WarpInstruction(
        getHex(CHERRYGROVE_CITY.CHERRYGROVE_GYM_SPEECH_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )

    Cherrygrove_City_Guide_Gents_House_Entrance_WP = WarpInstruction(
        getHex(CHERRYGROVE_CITY.GUIDE_GENTS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )

    Cherrygrove_City_East_House_Entrance_WP = WarpInstruction(
        getHex(CHERRYGROVE_CITY.CHERRYGROVE_EVOLUTION_SPEECH_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )
