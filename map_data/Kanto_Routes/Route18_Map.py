from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fuchsia
mapGroup = MapGroup.FUCHSIA
specificMap = Fuchsia.ROUTE_18

class ROUTE_18(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_17_ROUTE_18_GATE_3 = 1


class Route_18_Warp_Points(Enum): 

	ROUTE_18_TO_ROUTE_17_ROUTE_18_GATE_3_WP = WarpInstruction( 
		getHex(ROUTE_18.ROUTE_17_ROUTE_18_GATE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

