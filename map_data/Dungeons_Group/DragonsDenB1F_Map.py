from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.DRAGONS_DEN_B1F

class DRAGONS_DEN_B1F(IntEnum):
	def __str__(self):
		return str(self.value)

	DRAGONS_DEN_1F_3 = 1
	DRAGON_SHRINE_1 = 2


class Dragons_Den_B1F_Warp_Points(Enum): 

	DRAGONS_DEN_B1F_TO_DRAGONS_DEN_1F_3_WP = WarpInstruction( 
		getHex(DRAGONS_DEN_B1F.DRAGONS_DEN_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	DRAGONS_DEN_B1F_TO_DRAGON_SHRINE_1_WP = WarpInstruction( 
		getHex(DRAGONS_DEN_B1F.DRAGON_SHRINE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

