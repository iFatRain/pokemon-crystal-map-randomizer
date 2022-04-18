from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Vermilion
mapGroup = MapGroup.VERMILION
specificMap = Vermilion.ROUTE_6_UNDERGROUND_PATH_ENTRANCE

class ROUTE_6_UNDERGROUND_PATH_ENTRANCE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_6_1 = 1
	UNDERGROUND_PATH_2 = 3


class Route_6_Underground_Path_Entrance_Warp_Points(Enum): 

	ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_6_1_WP = WarpInstruction( 
		getHex(ROUTE_6_UNDERGROUND_PATH_ENTRANCE.ROUTE_6_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	ROUTE_6_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_2_WP = WarpInstruction( 
		getHex(ROUTE_6_UNDERGROUND_PATH_ENTRANCE.UNDERGROUND_PATH_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

