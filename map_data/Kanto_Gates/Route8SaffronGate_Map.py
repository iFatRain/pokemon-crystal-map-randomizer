from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Lavender
mapGroup = MapGroup.LAVENDER
specificMap = Lavender.ROUTE_8_SAFFRON_GATE

class ROUTE_8_SAFFRON_GATE(IntEnum):
	def __str__(self):
		return str(self.value)

	SAFFRON_CITY_14 = 1
	ROUTE_8_1 = 3


class Route_8_Saffron_Gate_Warp_Points(Enum): 

	ROUTE_8_SAFFRON_GATE_TO_SAFFRON_CITY_14_WP = WarpInstruction( 
		getHex(ROUTE_8_SAFFRON_GATE.SAFFRON_CITY_14), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_8_SAFFRON_GATE_TO_ROUTE_8_1_WP = WarpInstruction( 
		getHex(ROUTE_8_SAFFRON_GATE.ROUTE_8_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


