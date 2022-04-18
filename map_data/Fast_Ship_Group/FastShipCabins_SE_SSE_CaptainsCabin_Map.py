from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fast_Ship
mapGroup = MapGroup.FAST_SHIP
specificMap = Fast_Ship.FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN

class FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN(IntEnum):
	def __str__(self):
		return str(self.value)

	FAST_SHIP_1F_8 = 1
	FAST_SHIP_1F_9 = 3
	FAST_SHIP_1F_10 = 5


class Fast_Ship_Cabins_SE_SSE_Captains_Cabin_Warp_Points(Enum): 

	FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_8_WP = WarpInstruction( 
		getHex(FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN.FAST_SHIP_1F_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_9_WP = WarpInstruction( 
		getHex(FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN.FAST_SHIP_1F_9), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN_TO_FAST_SHIP_1F_10_WP = WarpInstruction( 
		getHex(FAST_SHIP_CABINS_SE_SSE_CAPTAINS_CABIN.FAST_SHIP_1F_10), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


