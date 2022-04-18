from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fast_Ship
mapGroup = MapGroup.FAST_SHIP
specificMap = Fast_Ship.FAST_SHIP_CABINS_NNW_NNE_NE

class FAST_SHIP_CABINS_NNW_NNE_NE(IntEnum):
	def __str__(self):
		return str(self.value)

	FAST_SHIP_1F_2 = 1
	FAST_SHIP_1F_3 = 2
	FAST_SHIP_1F_4 = 3


class Fast_Ship_Cabins_NNW_NNE_NE_Warp_Points(Enum): 

	FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_2_WP = WarpInstruction( 
		getHex(FAST_SHIP_CABINS_NNW_NNE_NE.FAST_SHIP_1F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_3_WP = WarpInstruction( 
		getHex(FAST_SHIP_CABINS_NNW_NNE_NE.FAST_SHIP_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_CABINS_NNW_NNE_NE_TO_FAST_SHIP_1F_4_WP = WarpInstruction( 
		getHex(FAST_SHIP_CABINS_NNW_NNE_NE.FAST_SHIP_1F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

