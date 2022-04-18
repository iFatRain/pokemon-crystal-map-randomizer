from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fast_Ship
mapGroup = MapGroup.FAST_SHIP
specificMap = Fast_Ship.FAST_SHIP_B1F

class FAST_SHIP_B1F(IntEnum):
	def __str__(self):
		return str(self.value)

	FAST_SHIP_1F_11 = 1
	FAST_SHIP_1F_12 = 2


class Fast_Ship_B1F_Warp_Points(Enum): 

	FAST_SHIP_B1F_TO_FAST_SHIP_1F_11_WP = WarpInstruction( 
		getHex(FAST_SHIP_B1F.FAST_SHIP_1F_11), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	FAST_SHIP_B1F_TO_FAST_SHIP_1F_12_WP = WarpInstruction( 
		getHex(FAST_SHIP_B1F.FAST_SHIP_1F_12), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

