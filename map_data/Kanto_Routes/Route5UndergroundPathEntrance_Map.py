from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.ROUTE_5_UNDERGROUND_PATH_ENTRANCE

class ROUTE_5_UNDERGROUND_PATH_ENTRANCE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_5_1 = 1
	UNDERGROUND_PATH_1 = 3


class Route_5_Underground_Path_Entrance_Warp_Points(Enum): 

	ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_ROUTE_5_1_WP = WarpInstruction( 
		getHex(ROUTE_5_UNDERGROUND_PATH_ENTRANCE.ROUTE_5_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	ROUTE_5_UNDERGROUND_PATH_ENTRANCE_TO_UNDERGROUND_PATH_1_WP = WarpInstruction( 
		getHex(ROUTE_5_UNDERGROUND_PATH_ENTRANCE.UNDERGROUND_PATH_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

