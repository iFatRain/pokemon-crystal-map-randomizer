from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.WHIRL_ISLAND_NE

class WHIRL_ISLAND_NE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_41_2 = 1
	WHIRL_ISLAND_B1F_2 = 2
	WHIRL_ISLAND_B1F_3 = 3


class Whirl_Island_NE_Warp_Points(Enum):

	WHIRL_ISLAND_N_E_TO_ROUTE_41_2_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_NE.ROUTE_41_2),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_2_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_NE.WHIRL_ISLAND_B1F_2),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_N_E_TO_WHIRL_ISLAND_B1F_3_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_NE.WHIRL_ISLAND_B1F_3),
		getHex(mapGroup),
		getHex(specificMap)
		) 

