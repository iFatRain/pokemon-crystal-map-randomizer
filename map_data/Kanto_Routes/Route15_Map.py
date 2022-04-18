from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fuchsia
mapGroup = MapGroup.FUCHSIA
specificMap = Fuchsia.ROUTE_15

class ROUTE_15(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_15_FUCHSIA_GATE_3 = 1


class Route_15_Warp_Points(Enum): 

	ROUTE_15_TO_ROUTE_15_FUCHSIA_GATE_3_WP = WarpInstruction( 
		getHex(ROUTE_15.ROUTE_15_FUCHSIA_GATE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

