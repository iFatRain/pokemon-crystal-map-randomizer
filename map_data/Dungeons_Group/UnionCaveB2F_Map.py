from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.UNION_CAVE_B2F

class UNION_CAVE_B2F(IntEnum):
	def __str__(self):
		return str(self.value)

	UNION_CAVE_B1F_5 = 1


class Union_Cave_B2F_Warp_Points(Enum): 

	UNION_CAVE_B2F_TO_UNION_CAVE_B1F_5_WP = WarpInstruction( 
		getHex(UNION_CAVE_B2F.UNION_CAVE_B1F_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

