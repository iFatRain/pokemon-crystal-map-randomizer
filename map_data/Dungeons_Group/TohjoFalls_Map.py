from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.TOHJO_FALLS

class TOHJO_FALLS(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_27_2 = 1
	ROUTE_27_3 = 2


class Tohjo_Falls_Warp_Points(Enum): 

	TOHJO_FALLS_TO_ROUTE_27_2_WP = WarpInstruction( 
		getHex(TOHJO_FALLS.ROUTE_27_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TOHJO_FALLS_TO_ROUTE_27_3_WP = WarpInstruction( 
		getHex(TOHJO_FALLS.ROUTE_27_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

