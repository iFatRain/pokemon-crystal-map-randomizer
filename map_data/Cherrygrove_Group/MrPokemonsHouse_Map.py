from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cherrygrove

mapGroup = MapGroup.CHERRYGROVE
specificMap = Cherrygrove.MR_POKEMONS_HOUSE

class MR_POKEMONS_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_30 = 1  # dual width


class Mr_Pokemons_House_Warp_Points(Enum):

    Mr_Pokemons_House_Exit_WP = WarpInstruction(
        getHex(MR_POKEMONS_HOUSE.ROUTE_30),
        getHex(mapGroup),
        getHex(specificMap),
        )
