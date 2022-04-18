from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.ROUTE_8

class ROUTE_8(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_8_SAFFRON_GATE_3 = 1


class Route_8_Warp_Points(Enum): 

	ROUTE_8_TO_ROUTE_8_SAFFRON_GATE_3_WP = WarpInstruction( 
		getHex(ROUTE_8.ROUTE_8_SAFFRON_GATE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


