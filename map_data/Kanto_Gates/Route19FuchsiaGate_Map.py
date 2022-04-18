from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cinnabar
mapGroup = MapGroup.CINNABAR
specificMap = Cinnabar.ROUTE_19_FUCHSIA_GATE

class ROUTE_19_FUCHSIA_GATE(IntEnum):
	def __str__(self):
		return str(self.value)

	FUCHSIA_CITY_10 = 1
	ROUTE_19_1 = 3


class Route_19_Fuchsia_Gate_Warp_Points(Enum): 

	ROUTE_19_FUCHSIA_GATE_TO_FUCHSIA_CITY_10_WP = WarpInstruction( 
		getHex(ROUTE_19_FUCHSIA_GATE.FUCHSIA_CITY_10), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_19_FUCHSIA_GATE_TO_ROUTE_19_1_WP = WarpInstruction( 
		getHex(ROUTE_19_FUCHSIA_GATE.ROUTE_19_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

