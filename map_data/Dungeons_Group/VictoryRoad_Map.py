from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.VICTORY_ROAD

class VICTORY_ROAD(IntEnum):
	def __str__(self):
		return str(self.value)

	VICTORY_ROAD_GATE_5 = 1
	VICTORY_ROAD_3 = 2
	VICTORY_ROAD_2 = 3
	VICTORY_ROAD_5 = 4
	VICTORY_ROAD_4 = 5
	VICTORY_ROAD_7 = 6
	VICTORY_ROAD_6 = 7
	VICTORY_ROAD_9 = 8
	VICTORY_ROAD_8 = 9
	ROUTE_23_3 = 10


class Victory_Road_Warp_Points(Enum): 

	VICTORY_ROAD_TO_VICTORY_ROAD_GATE_5_WP = WarpInstruction( 
		getHex(VICTORY_ROAD.VICTORY_ROAD_GATE_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VICTORY_ROAD_TO_VICTORY_ROAD_3_WP = WarpInstruction( 
		getHex(VICTORY_ROAD.VICTORY_ROAD_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VICTORY_ROAD_TO_VICTORY_ROAD_2_WP = WarpInstruction( 
		getHex(VICTORY_ROAD.VICTORY_ROAD_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VICTORY_ROAD_TO_VICTORY_ROAD_5_WP = WarpInstruction( 
		getHex(VICTORY_ROAD.VICTORY_ROAD_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VICTORY_ROAD_TO_VICTORY_ROAD_4_WP = WarpInstruction( 
		getHex(VICTORY_ROAD.VICTORY_ROAD_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VICTORY_ROAD_TO_VICTORY_ROAD_7_WP = WarpInstruction( 
		getHex(VICTORY_ROAD.VICTORY_ROAD_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VICTORY_ROAD_TO_VICTORY_ROAD_6_WP = WarpInstruction( 
		getHex(VICTORY_ROAD.VICTORY_ROAD_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VICTORY_ROAD_TO_VICTORY_ROAD_9_WP = WarpInstruction( 
		getHex(VICTORY_ROAD.VICTORY_ROAD_9), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VICTORY_ROAD_TO_VICTORY_ROAD_8_WP = WarpInstruction( 
		getHex(VICTORY_ROAD.VICTORY_ROAD_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	VICTORY_ROAD_TO_ROUTE_23_3_WP = WarpInstruction( 
		getHex(VICTORY_ROAD.ROUTE_23_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

