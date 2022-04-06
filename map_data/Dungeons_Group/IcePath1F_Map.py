from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.ICE_PATH_1F

class ICE_PATH_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_44_1 = 1
	BLACKTHORN_CITY_7 = 2
	ICE_PATH_B1F_1 = 3
	ICE_PATH_B1F_7 = 4


class Ice_Path_1F_Warp_Points(Enum): 

	ICE_PATH_1F_TO_ROUTE_44_1_WP = WarpInstruction( 
		getHex(ICE_PATH_1F.ROUTE_44_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ICE_PATH_1F_TO_BLACKTHORN_CITY_7_WP = WarpInstruction( 
		getHex(ICE_PATH_1F.BLACKTHORN_CITY_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ICE_PATH_1F_TO_ICE_PATH_B1F_1_WP = WarpInstruction( 
		getHex(ICE_PATH_1F.ICE_PATH_B1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ICE_PATH_1F_TO_ICE_PATH_B1F_7_WP = WarpInstruction( 
		getHex(ICE_PATH_1F.ICE_PATH_B1F_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

