from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Vermilion
mapGroup = MapGroup.VERMILION
specificMap = Vermilion.ROUTE_6_SAFFRON_GATE

class ROUTE_6_SAFFRON_GATE(IntEnum):
	def __str__(self):
		return str(self.value)

	SAFFRON_CITY_12 = 1
	ROUTE_6_2 = 3


class Route_6_Saffron_Gate_Warp_Points(Enum): 

	ROUTE_6_SAFFRON_GATE_TO_SAFFRON_CITY_12_WP = WarpInstruction( 
		getHex(ROUTE_6_SAFFRON_GATE.SAFFRON_CITY_12), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_6_SAFFRON_GATE_TO_ROUTE_6_2_WP = WarpInstruction( 
		getHex(ROUTE_6_SAFFRON_GATE.ROUTE_6_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

