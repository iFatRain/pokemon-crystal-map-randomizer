from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fast_Ship
mapGroup = MapGroup.FAST_SHIP
specificMap = Fast_Ship.FAST_SHIP_CABINS_SW_SSW_NW

class FAST_SHIP_CABINS_SW_SSW_NW(IntEnum):
	def __str__(self):
		return str(self.value)

	FAST_SHIP_1F_5 = 1
	FAST_SHIP_1F_6 = 2
	FAST_SHIP_1F_7 = 4


class Fast_Ship_Cabins_SW_SSW_NW_Warp_Points(Enum): 

	FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_5_WP = WarpInstruction( 
		getHex(FAST_SHIP_CABINS_SW_SSW_NW.FAST_SHIP_1F_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_6_WP = WarpInstruction( 
		getHex(FAST_SHIP_CABINS_SW_SSW_NW.FAST_SHIP_1F_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_CABINS_SW_SSW_NW_TO_FAST_SHIP_1F_7_WP = WarpInstruction( 
		getHex(FAST_SHIP_CABINS_SW_SSW_NW.FAST_SHIP_1F_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


