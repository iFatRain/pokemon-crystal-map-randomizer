from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.TIN_TOWER_7F

class TIN_TOWER_7F(IntEnum):
	def __str__(self):
		return str(self.value)

	TIN_TOWER_6F_1 = 1
	TIN_TOWER_8F_1 = 2
	TIN_TOWER_7F_4 = 3
	TIN_TOWER_7F_3 = 4
	TIN_TOWER_9F_5 = 5


class Tin_Tower_7F_Warp_Points(Enum): 

	TIN_TOWER_7F_TO_TIN_TOWER_6F_1_WP = WarpInstruction( 
		getHex(TIN_TOWER_7F.TIN_TOWER_6F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_7F_TO_TIN_TOWER_8F_1_WP = WarpInstruction( 
		getHex(TIN_TOWER_7F.TIN_TOWER_8F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_7F_TO_TIN_TOWER_7F_4_WP = WarpInstruction( 
		getHex(TIN_TOWER_7F.TIN_TOWER_7F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_7F_TO_TIN_TOWER_7F_3_WP = WarpInstruction( 
		getHex(TIN_TOWER_7F.TIN_TOWER_7F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_7F_TO_TIN_TOWER_9F_5_WP = WarpInstruction( 
		getHex(TIN_TOWER_7F.TIN_TOWER_9F_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

