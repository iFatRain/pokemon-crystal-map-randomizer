from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.VIOLET_CITY

class VIOLET_CITY(IntEnum):
    def __str__(self):
        return str(self.value)

    VIOLET_MART = 1
    VIOLET_GYM = 2
    EARLS_POKEMON_ACADEMY = 3
    VIOLET_NICKNAME_SPEECH_HOUSE = 4
    VIOLET_POKECENTER_1F = 5
    VIOLET_KYLES_HOUSE = 6
    SPROUT_TOWER_1F = 7
    ROUTE_31_VIOLET_GATE = 8  # dual width



class Violet_City_Warp_Points(Enum):

    VIOLET_CITY_TO_VIOLET_MART_WP = WarpInstruction(
        getHex(VIOLET_CITY.VIOLET_MART),
        getHex(mapGroup),
        getHex(specificMap),
        )

    VIOLET_CITY_TO_VIOLET_GYM_WP = WarpInstruction(
        getHex(VIOLET_CITY.VIOLET_GYM),
        getHex(mapGroup),
        getHex(specificMap),
        )

    VIOLET_CITY_TO_EARLS_POKEMON_ACADEMY_WP = WarpInstruction(
        getHex(VIOLET_CITY.EARLS_POKEMON_ACADEMY),
        getHex(mapGroup),
        getHex(specificMap),
        )


    VIOLET_CITY_TO_NICKNAME_SPEECH_HOUSE_WP = WarpInstruction(
        getHex(VIOLET_CITY.VIOLET_NICKNAME_SPEECH_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )


    VIOLET_CITY_TO_VIOLET_POKECENTER_1F_WP = WarpInstruction(
        getHex(VIOLET_CITY.VIOLET_POKECENTER_1F),
        getHex(mapGroup),
        getHex(specificMap),
        )

    VIOLET_CITY_TO_VIOLET_KYLES_HOUSE_WP = WarpInstruction(
        getHex(VIOLET_CITY.VIOLET_KYLES_HOUSE),
        getHex(mapGroup),
        getHex(specificMap),
        )

    VIOLET_CITY_TO_SPROUT_TOWER_1F_WP = WarpInstruction(
        getHex(VIOLET_CITY.SPROUT_TOWER_1F),
        getHex(mapGroup),
        getHex(specificMap),
        )

    VIOLET_CITY_ROUTE_31_VIOLET_GATE_WP = WarpInstruction(
        getHex(VIOLET_CITY.ROUTE_31_VIOLET_GATE),
        getHex(mapGroup),
        getHex(specificMap),
        )
