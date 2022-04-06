from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.DRAGONS_DEN_1F

class DRAGONS_DEN_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	BLACKTHORN_CITY_8 = 1
	DRAGONS_DEN_1F_4 = 2
	DRAGONS_DEN_B1F_1 = 3
	DRAGONS_DEN_1F_2 = 4


class Dragons_Den_1F_Warp_Points(Enum): 

	DRAGONS_DEN_1F_TO_BLACKTHORN_CITY_8_WP = WarpInstruction( 
		getHex(DRAGONS_DEN_1F.BLACKTHORN_CITY_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_4_WP = WarpInstruction( 
		getHex(DRAGONS_DEN_1F.DRAGONS_DEN_1F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	DRAGONS_DEN_1F_TO_DRAGONS_DEN_B1F_1_WP = WarpInstruction( 
		getHex(DRAGONS_DEN_1F.DRAGONS_DEN_B1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	DRAGONS_DEN_1F_TO_DRAGONS_DEN_1F_2_WP = WarpInstruction( 
		getHex(DRAGONS_DEN_1F.DRAGONS_DEN_1F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

