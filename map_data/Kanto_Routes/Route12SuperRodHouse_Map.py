from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.ROUTE_12_SUPER_ROD_HOUSE

class ROUTE_12_SUPER_ROD_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_12_1 = 1


class Route_12_Super_Rod_House_Warp_Points(Enum): 

	ROUTE_12_SUPER_ROD_HOUSE_TO_ROUTE_12_1_WP = WarpInstruction( 
		getHex(ROUTE_12_SUPER_ROD_HOUSE.ROUTE_12_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

