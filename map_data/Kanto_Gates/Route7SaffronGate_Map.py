from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon
mapGroup = MapGroup.CELADON
specificMap = Celadon.ROUTE_7_SAFFRON_GATE

class ROUTE_7_SAFFRON_GATE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_7_1 = 1
	SAFFRON_CITY_10 = 3


class Route_7_Saffron_Gate_Warp_Points(Enum): 

	ROUTE_7_SAFFRON_GATE_TO_ROUTE_7_1_WP = WarpInstruction( 
		getHex(ROUTE_7_SAFFRON_GATE.ROUTE_7_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_7_SAFFRON_GATE_TO_SAFFRON_CITY_10_WP = WarpInstruction( 
		getHex(ROUTE_7_SAFFRON_GATE.SAFFRON_CITY_10), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


