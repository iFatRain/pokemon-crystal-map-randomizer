from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.WHIRL_ISLAND_SW

class WHIRL_ISLAND_SW(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_41_3 = 1
	WHIRL_ISLAND_B1F_5 = 2
	WHIRL_ISLAND_B1F_4 = 3
	WHIRL_ISLAND_NW_3 = 4
	WHIRL_ISLAND_B2F_4 = 5


class Whirl_Island_SW_Warp_Points(Enum):

	WHIRL_ISLAND_S_W_TO_ROUTE_41_3_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_SW.ROUTE_41_3),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_5_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_SW.WHIRL_ISLAND_B1F_5),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B1F_4_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_SW.WHIRL_ISLAND_B1F_4),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_NW_3_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_SW.WHIRL_ISLAND_NW_3),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_S_W_TO_WHIRL_ISLAND_B2F_4_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_SW.WHIRL_ISLAND_B2F_4),
		getHex(mapGroup),
		getHex(specificMap)
		) 

