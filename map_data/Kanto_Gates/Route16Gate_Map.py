from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon
mapGroup = MapGroup.CELADON
specificMap = Celadon.ROUTE_16_GATE

class ROUTE_16_GATE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_16_4 = 1
	ROUTE_16_2 = 3


class Route_16_Gate_Warp_Points(Enum): 

	ROUTE_16_GATE_TO_ROUTE_16_4_WP = WarpInstruction( 
		getHex(ROUTE_16_GATE.ROUTE_16_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_16_GATE_TO_ROUTE_16_2_WP = WarpInstruction( 
		getHex(ROUTE_16_GATE.ROUTE_16_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


