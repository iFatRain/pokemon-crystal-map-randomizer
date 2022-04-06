from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.DRAGON_SHRINE

class DRAGON_SHRINE(IntEnum):
	def __str__(self):
		return str(self.value)

	DRAGONS_DEN_B1F_2 = 1


class Dragon_Shrine_Warp_Points(Enum): 

	DRAGON_SHRINE_TO_DRAGONS_DEN_B1F_2_WP = WarpInstruction( 
		getHex(DRAGON_SHRINE.DRAGONS_DEN_B1F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 
