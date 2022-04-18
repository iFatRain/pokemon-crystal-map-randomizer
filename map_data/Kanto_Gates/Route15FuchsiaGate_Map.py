from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fuchsia
mapGroup = MapGroup.FUCHSIA
specificMap = Fuchsia.ROUTE_15_FUCHSIA_GATE

class ROUTE_15_FUCHSIA_GATE(IntEnum):
	def __str__(self):
		return str(self.value)

	FUCHSIA_CITY_8 = 1
	ROUTE_15_1 = 3


class Route_15_Fuchsia_Gate_Warp_Points(Enum): 

	ROUTE_15_FUCHSIA_GATE_TO_FUCHSIA_CITY_8_WP = WarpInstruction( 
		getHex(ROUTE_15_FUCHSIA_GATE.FUCHSIA_CITY_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_15_FUCHSIA_GATE_TO_ROUTE_15_1_WP = WarpInstruction( 
		getHex(ROUTE_15_FUCHSIA_GATE.ROUTE_15_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


