from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon
mapGroup = MapGroup.CELADON
specificMap = Celadon.ROUTE_7

class ROUTE_7(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_7_SAFFRON_GATE_1 = 1


class Route_7_Warp_Points(Enum): 

	ROUTE_7_TO_ROUTE_7_SAFFRON_GATE_1_WP = WarpInstruction( 
		getHex(ROUTE_7.ROUTE_7_SAFFRON_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


