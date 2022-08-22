from enum import IntEnum, Enum
#
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cianwood

mapGroup = MapGroup.CIANWOOD
specificMap = Cianwood.POKE_SEERS_HOUSE

class POKE_SEERS_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    CIANWOOD_CITY = 1  # dual wide


class Poke_Seers_House_Warp_Points(Enum):

    Cianwood_City_Poke_Seers_House_Exit_WP = WarpInstruction(
        getHex(POKE_SEERS_HOUSE.CIANWOOD_CITY),
        getHex(mapGroup),
        getHex(specificMap))