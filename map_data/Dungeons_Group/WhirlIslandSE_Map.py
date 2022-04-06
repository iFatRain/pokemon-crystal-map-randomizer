from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.WHIRL_ISLAND_SE

class WHIRL_ISLAND_SE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_41_4 = 1
	WHIRL_ISLAND_B1F_6 = 2


class Whirl_Island_SE_Warp_Points(Enum):

	WHIRL_ISLAND_S_E_TO_ROUTE_41_4_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_SE.ROUTE_41_4),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_S_E_TO_WHIRL_ISLAND_B1F_6_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_SE.WHIRL_ISLAND_B1F_6),
		getHex(mapGroup),
		getHex(specificMap)
		) 

