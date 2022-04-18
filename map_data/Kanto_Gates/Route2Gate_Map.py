from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Viridian
mapGroup = MapGroup.VIRIDIAN
specificMap = Viridian.ROUTE_2_GATE

class ROUTE_2_GATE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_2_3 = 1
	ROUTE_2_2 = 3


class Route_2_Gate_Warp_Points(Enum): 

	ROUTE_2_GATE_TO_ROUTE_2_3_WP = WarpInstruction( 
		getHex(ROUTE_2_GATE.ROUTE_2_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_2_GATE_TO_ROUTE_2_2_WP = WarpInstruction( 
		getHex(ROUTE_2_GATE.ROUTE_2_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


