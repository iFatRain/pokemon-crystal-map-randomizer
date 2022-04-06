from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Viridian
mapGroup = MapGroup.VIRIDIAN
specificMap = Viridian.VICTORY_ROAD_GATE

class VICTORY_ROAD_GATE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_22_1 = 1
	ROUTE_26_1 = 3
	VICTORY_ROAD_1 = 5
	ROUTE_28_2 = 7

class Victory_Road_Gate_Warp_Points(Enum): 

	VICTORY_ROAD_GATE_TO_ROUTE_22_1_WP = WarpInstruction( 
		getHex(VICTORY_ROAD_GATE.ROUTE_22_1), 
		getHex(mapGroup),
		getHex(specificMap)
		)

	VICTORY_ROAD_GATE_TO_ROUTE_26_1_WP = WarpInstruction( 
		getHex(VICTORY_ROAD_GATE.ROUTE_26_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	VICTORY_ROAD_GATE_TO_VICTORY_ROAD_1_WP = WarpInstruction( 
		getHex(VICTORY_ROAD_GATE.VICTORY_ROAD_1), 
		getHex(mapGroup),
		getHex(specificMap)
		)

	VICTORY_ROAD_GATE_TO_ROUTE_28_2_WP = WarpInstruction( 
		getHex(VICTORY_ROAD_GATE.ROUTE_28_2), 
		getHex(mapGroup),
		getHex(specificMap)
		)
