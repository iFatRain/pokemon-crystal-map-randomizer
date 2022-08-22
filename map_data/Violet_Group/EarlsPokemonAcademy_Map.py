from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Violet

mapGroup = MapGroup.VIOLET
specificMap = Violet.EARLS_POKEMON_ACADEMY

class EARLS_POKEMON_ACADEMY(IntEnum):
    def __str__(self):
        return str(self.value)

    VIOLET_CITY = 1  # dual width


class Earls_Pokemon_Academy_Warp_Points(Enum):

    Violet_City_School_Exit_WP = WarpInstruction(
        getHex(EARLS_POKEMON_ACADEMY.VIOLET_CITY),
        getHex(mapGroup),
        getHex(specificMap),
        )
