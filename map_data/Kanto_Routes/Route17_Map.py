from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon
mapGroup = MapGroup.CELADON
specificMap = Celadon.ROUTE_17

class ROUTE_17(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_17_ROUTE_18_GATE_1 = 1


class Route_17_Warp_Points(Enum): 

	ROUTE_17_TO_ROUTE_17_ROUTE_18_GATE_1_WP = WarpInstruction( 
		getHex(ROUTE_17.ROUTE_17_ROUTE_18_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


