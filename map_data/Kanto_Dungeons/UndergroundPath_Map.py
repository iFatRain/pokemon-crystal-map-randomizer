from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.UNDERGROUND_PATH

class UNDERGROUND_PATH(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_5_UNDERGROUND_PATH_ENTRANCE_3 = 1
	ROUTE_6_UNDERGROUND_PATH_ENTRANCE_3 = 2


class Underground_Path_Warp_Points(Enum): 

	UNDERGROUND_PATH_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_3_WP = WarpInstruction( 
		getHex(UNDERGROUND_PATH.ROUTE_5_UNDERGROUND_PATH_ENTRANCE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	UNDERGROUND_PATH_TO_ROUTE_6_UNDERGROUND_PATH_ENTRANCE_3_WP = WarpInstruction( 
		getHex(UNDERGROUND_PATH.ROUTE_6_UNDERGROUND_PATH_ENTRANCE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

