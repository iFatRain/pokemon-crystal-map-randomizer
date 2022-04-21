from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.TIN_TOWER_3F

class TIN_TOWER_3F(IntEnum):
	def __str__(self):
		return str(self.value)

	TIN_TOWER_2F_1 = 1
	TIN_TOWER_4F_2 = 2


class Tin_Tower_3F_Warp_Points(Enum): 

	TIN_TOWER_3F_TO_TIN_TOWER_2F_1_WP = WarpInstruction( 
		getHex(TIN_TOWER_3F.TIN_TOWER_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_3F_TO_TIN_TOWER_4F_2_WP = WarpInstruction( 
		getHex(TIN_TOWER_3F.TIN_TOWER_4F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

