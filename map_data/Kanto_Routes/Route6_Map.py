from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Vermilion
mapGroup = MapGroup.VERMILION
specificMap = Vermilion.ROUTE_6

class ROUTE_6(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_6_UNDERGROUND_PATH_ENTRANCE_1 = 1
	ROUTE_6_SAFFRON_GATE_3 = 2


class Route_6_Warp_Points(Enum): 

	ROUTE_6_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_1_WP = WarpInstruction( 
		getHex(ROUTE_6.ROUTE_6_UNDERGROUND_PATH_ENTRANCE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_6_TO_ROUTE_6_SAFFRON_GATE_3_WP = WarpInstruction( 
		getHex(ROUTE_6.ROUTE_6_SAFFRON_GATE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

