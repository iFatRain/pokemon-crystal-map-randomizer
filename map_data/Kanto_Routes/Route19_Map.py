from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cinnabar
mapGroup = MapGroup.CINNABAR
specificMap = Cinnabar.ROUTE_19

class ROUTE_19(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_19_FUCHSIA_GATE_3 = 1


class Route_19_Warp_Points(Enum): 

	ROUTE_19_TO_ROUTE_19_FUCHSIA_GATE_3_WP = WarpInstruction( 
		getHex(ROUTE_19.ROUTE_19_FUCHSIA_GATE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

