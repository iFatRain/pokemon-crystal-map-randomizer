from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.TIN_TOWER_4F

class TIN_TOWER_4F(IntEnum):
	def __str__(self):
		return str(self.value)

	TIN_TOWER_5F_2 = 1
	TIN_TOWER_3F_2 = 2
	TIN_TOWER_5F_3 = 3
	TIN_TOWER_5F_4 = 4


class Tin_Tower_4F_Warp_Points(Enum): 

	TIN_TOWER_4F_TO_TIN_TOWER_5F_2_WP = WarpInstruction( 
		getHex(TIN_TOWER_4F.TIN_TOWER_5F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_4F_TO_TIN_TOWER_3F_2_WP = WarpInstruction( 
		getHex(TIN_TOWER_4F.TIN_TOWER_3F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_4F_TO_TIN_TOWER_5F_3_WP = WarpInstruction( 
		getHex(TIN_TOWER_4F.TIN_TOWER_5F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_4F_TO_TIN_TOWER_5F_4_WP = WarpInstruction( 
		getHex(TIN_TOWER_4F.TIN_TOWER_5F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

