from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.WHIRL_ISLAND_B1F

class WHIRL_ISLAND_B1F(IntEnum):
	def __str__(self):
		return str(self.value)

	WHIRL_ISLAND_NW_2 = 1
	WHIRL_ISLAND_NE_2 = 2
	WHIRL_ISLAND_NE_3 = 3
	WHIRL_ISLAND_SW_3 = 4
	WHIRL_ISLAND_SW_2 = 5
	WHIRL_ISLAND_SE_2 = 6
	WHIRL_ISLAND_B2F_1 = 7
	WHIRL_ISLAND_B2F_2 = 8
	WHIRL_ISLAND_CAVE_1 = 9


class Whirl_Island_B1F_Warp_Points(Enum): 

	WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NW_2_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B1F.WHIRL_ISLAND_NW_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_2_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B1F.WHIRL_ISLAND_NE_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_NE_3_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B1F.WHIRL_ISLAND_NE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_3_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B1F.WHIRL_ISLAND_SW_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SW_2_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B1F.WHIRL_ISLAND_SW_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_SE_2_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B1F.WHIRL_ISLAND_SE_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_1_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B1F.WHIRL_ISLAND_B2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_B2F_2_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B1F.WHIRL_ISLAND_B2F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	WHIRL_ISLAND_B1F_TO_WHIRL_ISLAND_CAVE_1_WP = WarpInstruction( 
		getHex(WHIRL_ISLAND_B1F.WHIRL_ISLAND_CAVE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

