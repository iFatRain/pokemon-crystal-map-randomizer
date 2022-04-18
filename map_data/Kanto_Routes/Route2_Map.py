from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Viridian
mapGroup = MapGroup.VIRIDIAN
specificMap = Viridian.ROUTE_2

class ROUTE_2(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_2_NUGGET_HOUSE_1 = 1
	ROUTE_2_GATE_3 = 2
	ROUTE_2_GATE_1 = 3
	DIGLETTS_CAVE_3 = 5


class Route_2_Warp_Points(Enum): 

	ROUTE_2_TO_ROUTE_2_NUGGET_HOUSE_1_WP = WarpInstruction( 
		getHex(ROUTE_2.ROUTE_2_NUGGET_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_2_TO_ROUTE_2_GATE_3_WP = WarpInstruction( 
		getHex(ROUTE_2.ROUTE_2_GATE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_2_TO_ROUTE_2_GATE_1_WP = WarpInstruction( 
		getHex(ROUTE_2.ROUTE_2_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_2_TO_DIGLETTS_CAVE_3_WP = WarpInstruction( 
		getHex(ROUTE_2.DIGLETTS_CAVE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

