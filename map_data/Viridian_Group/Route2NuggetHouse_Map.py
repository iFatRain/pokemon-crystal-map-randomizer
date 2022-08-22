from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Viridian
mapGroup = MapGroup.VIRIDIAN
specificMap = Viridian.ROUTE_2_NUGGET_HOUSE

class ROUTE_2_NUGGET_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_2_1 = 1


class Route_2_Nugget_House_Warp_Points(Enum): 

	Route_2_Nugget_House_Exit_WP = WarpInstruction(
		getHex(ROUTE_2_NUGGET_HOUSE.ROUTE_2_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

