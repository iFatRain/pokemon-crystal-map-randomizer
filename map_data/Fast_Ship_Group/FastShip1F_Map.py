from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fast_Ship
mapGroup = MapGroup.FAST_SHIP
specificMap = Fast_Ship.FAST_SHIP_1F

class FAST_SHIP_1F(IntEnum):
	def __str__(self):
		return str(self.value)


	FAST_SHIP_CABINS_NNW_NNE_NE_1 = 2
	FAST_SHIP_CABINS_NNW_NNE_NE_2 = 3
	FAST_SHIP_CABINS_NNW_NNE_NE_3 = 4
	FAST_SHIP_CABINS_SW_SSW_NW_1 = 5
	FAST_SHIP_CABINS_SW_SSW_NW_2 = 6
	FAST_SHIP_CABINS_SW_SSW_NW_4 = 7
	FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_1 = 8
	FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_3 = 9
	FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5 = 10
	FAST_SHIP_B1F_1 = 11
	FAST_SHIP_B1F_2 = 12


class Fast_Ship_1F_Warp_Points(Enum): 


	FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_1_WP = WarpInstruction( 
		getHex(FAST_SHIP_1F.FAST_SHIP_CABINS_NNW_NNE_NE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_2_WP = WarpInstruction( 
		getHex(FAST_SHIP_1F.FAST_SHIP_CABINS_NNW_NNE_NE_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_1F_TO_FAST_SHIP_CABINS_NNW_NNE_NE_3_WP = WarpInstruction( 
		getHex(FAST_SHIP_1F.FAST_SHIP_CABINS_NNW_NNE_NE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_1_WP = WarpInstruction( 
		getHex(FAST_SHIP_1F.FAST_SHIP_CABINS_SW_SSW_NW_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_2_WP = WarpInstruction( 
		getHex(FAST_SHIP_1F.FAST_SHIP_CABINS_SW_SSW_NW_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SW_SSW_NW_4_WP = WarpInstruction( 
		getHex(FAST_SHIP_1F.FAST_SHIP_CABINS_SW_SSW_NW_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_1_WP = WarpInstruction( 
		getHex(FAST_SHIP_1F.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_3_WP = WarpInstruction( 
		getHex(FAST_SHIP_1F.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_1F_TO_FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5_WP = WarpInstruction( 
		getHex(FAST_SHIP_1F.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_1F_TO_FAST_SHIP_B1F_1_WP = WarpInstruction( 
		getHex(FAST_SHIP_1F.FAST_SHIP_B1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_1F_TO_FAST_SHIP_B1F_2_WP = WarpInstruction( 
		getHex(FAST_SHIP_1F.FAST_SHIP_B1F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

