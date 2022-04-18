from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.ROUTE_5_SAFFRON_GATE

class ROUTE_5_SAFFRON_GATE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_5_2 = 1
	SAFFRON_CITY_9 = 3


class Route_5_Saffron_Gate_Warp_Points(Enum): 

	ROUTE_5_SAFFRON_GATE_TO_ROUTE_5_2_WP = WarpInstruction( 
		getHex(ROUTE_5_SAFFRON_GATE.ROUTE_5_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_5_SAFFRON_GATE_TO_SAFFRON_CITY_9_WP = WarpInstruction( 
		getHex(ROUTE_5_SAFFRON_GATE.SAFFRON_CITY_9), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

