from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cherrygrove

mapGroup = MapGroup.CHERRYGROVE
specificMap = Cherrygrove.ROUTE_30

class ROUTE_30(IntEnum):
    def __str__(self):
        return str(self.value)

    ROUTE_30_BERRY_HOUSE = 1
    MR_POKEMONS_HOUSE = 2    # dual wide

class Route_30_Warp_Points(Enum):

    ROUTE_30_TO_ROUTE_30_BERRY_HOUSE_WP = WarpInstruction(
        getHex(ROUTE_30.ROUTE_30_BERRY_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))

    ROUTE_30_TO_MR_POKEMONS_HOUSE_WP = WarpInstruction(
        getHex(ROUTE_30.MR_POKEMONS_HOUSE),
        getHex(mapGroup),
        getHex(specificMap))