from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Viridian
mapGroup = MapGroup.VIRIDIAN
specificMap = Viridian.ROUTE_22

class ROUTE_22(IntEnum):
	def __str__(self):
		return str(self.value)

	VICTORY_ROAD_GATE_1 = 1


class Route_22_Warp_Points(Enum): 

	ROUTE_22_TO_VICTORY_ROAD_GATE_1_WP = WarpInstruction( 
		getHex(ROUTE_22.VICTORY_ROAD_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

