from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.SPROUT_TOWER_3F

class SPROUT_TOWER_3F(IntEnum):
	def __str__(self):
		return str(self.value)

	SPROUT_TOWER_2F_4 = 1


class Sprout_Tower_3F_Warp_Points(Enum): 

	SPROUT_TOWER_3F_TO_SPROUT_TOWER_2F_4_WP = WarpInstruction( 
		getHex(SPROUT_TOWER_3F.SPROUT_TOWER_2F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

