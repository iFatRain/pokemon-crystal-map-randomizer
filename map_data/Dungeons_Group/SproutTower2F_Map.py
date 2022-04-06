from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.SPROUT_TOWER_2F

class SPROUT_TOWER_2F(IntEnum):
	def __str__(self):
		return str(self.value)

	SPROUT_TOWER_1F_3 = 1
	SPROUT_TOWER_1F_4 = 2
	SPROUT_TOWER_1F_5 = 3
	SPROUT_TOWER_3F_1 = 4


class Sprout_Tower_2F_Warp_Points(Enum): 

	SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_3_WP = WarpInstruction( 
		getHex(SPROUT_TOWER_2F.SPROUT_TOWER_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_4_WP = WarpInstruction( 
		getHex(SPROUT_TOWER_2F.SPROUT_TOWER_1F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SPROUT_TOWER_2F_TO_SPROUT_TOWER_1F_5_WP = WarpInstruction( 
		getHex(SPROUT_TOWER_2F.SPROUT_TOWER_1F_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SPROUT_TOWER_2F_TO_SPROUT_TOWER_3F_1_WP = WarpInstruction( 
		getHex(SPROUT_TOWER_2F.SPROUT_TOWER_3F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

