from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.ROUTE_12

class ROUTE_12(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_12_SUPER_ROD_HOUSE_1 = 1


class Route_12_Warp_Points(Enum): 

	ROUTE_12_TO_ROUTE_12_SUPER_ROD_HOUSE_1_WP = WarpInstruction( 
		getHex(ROUTE_12.ROUTE_12_SUPER_ROD_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

