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

    CHERRYGROVE_CITY_TO_CHERRYGROVE_MART_WP = WarpInstruction(
        getHex(CHERRYGROVE_CITY.CHERRYGROVE_MART),
        getHex(mapGroup),
        getHex(specificMap))

    CHERRYGROVE_CITY_TO_CHERRYGROVE_POKECENTER_1F_WP = WarpInstruction(
        getHex(CHERRYGROVE_CITY.CHERRYGROVE_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap),
        )

    CHERRYGROVE_CITY_TO_CHERRYGROVE_GYM_SPEECH_HOUSE_WP = WarpInstruction(
        getHex(CHERRYGROVE_CITY.CHERRYGROVE_GYM_SPEECH_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )

    CHERRYGROVE_CITY_TO_GUIDE_GENTS_HOUSE_WP = WarpInstruction(
        getHex(CHERRYGROVE_CITY.GUIDE_GENTS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )

    CHERRYGROVE_CITY_TO_CHERRYGROVE_EVOLUTION_SPEECH_HOUSE_WP = WarpInstruction(
        getHex(CHERRYGROVE_CITY.CHERRYGROVE_EVOLUTION_SPEECH_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )
