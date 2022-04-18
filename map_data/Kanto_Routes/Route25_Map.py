from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.ROUTE_25

class ROUTE_25(IntEnum):
	def __str__(self):
		return str(self.value)

	BILLS_HOUSE_1 = 1


class Route_25_Warp_Points(Enum): 

	ROUTE_25_TO_BILLS_HOUSE_1_WP = WarpInstruction( 
		getHex(ROUTE_25.BILLS_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

