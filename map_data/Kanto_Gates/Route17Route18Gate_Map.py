from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon
mapGroup = MapGroup.CELADON
specificMap = Celadon.ROUTE_17_ROUTE_18_GATE

class ROUTE_17_ROUTE_18_GATE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_17_1 = 1
	ROUTE_18_1 = 3



class Route_17_Route_18_Gate_Warp_Points(Enum): 

	ROUTE_17_ROUTE_18_GATE_TO_ROUTE_17_1_WP = WarpInstruction( 
		getHex(ROUTE_17_ROUTE_18_GATE.ROUTE_17_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_17_ROUTE_18_GATE_TO_ROUTE_18_1_WP = WarpInstruction( 
		getHex(ROUTE_17_ROUTE_18_GATE.ROUTE_18_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


