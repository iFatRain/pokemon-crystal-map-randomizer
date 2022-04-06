from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.WHIRL_ISLAND_NW

class WHIRL_ISLAND_NW(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_41_1 = 1
	WHIRL_ISLAND_B1F_1 = 2
	WHIRL_ISLAND_SW_4 = 3
	WHIRL_ISLAND_CAVE_2 = 4


class Whirl_Island_NW_Warp_Points(Enum):

	WHIRL_ISLAND_N_W_TO_ROUTE_41_1_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_NW.ROUTE_41_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_B1F_1_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_NW.WHIRL_ISLAND_B1F_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_SW_4_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_NW.WHIRL_ISLAND_SW_4),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_N_W_TO_WHIRL_ISLAND_CAVE_2_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_NW.WHIRL_ISLAND_CAVE_2),
		getHex(mapGroup),
		getHex(specificMap)
		) 

