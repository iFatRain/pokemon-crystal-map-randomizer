from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.TIN_TOWER_2F

class TIN_TOWER_2F(IntEnum):
	def __str__(self):
		return str(self.value)

	TIN_TOWER_3F_1 = 1
	TIN_TOWER_1F_3 = 2


class Tin_Tower_2F_Warp_Points(Enum): 

	TIN_TOWER_2F_TO_TIN_TOWER_3F_1_WP = WarpInstruction( 
		getHex(TIN_TOWER_2F.TIN_TOWER_3F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_2F_TO_TIN_TOWER_1F_3_WP = WarpInstruction( 
		getHex(TIN_TOWER_2F.TIN_TOWER_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

