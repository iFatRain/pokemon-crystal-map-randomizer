from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.UNION_CAVE_B1F

class UNION_CAVE_B1F(IntEnum):
	def __str__(self):
		return str(self.value)

	RUINS_OF_ALPH_OUTSIDE_7 = 1
	RUINS_OF_ALPH_OUTSIDE_8 = 2
	UNION_CAVE_1F_1 = 3
	UNION_CAVE_1F_2 = 4
	UNION_CAVE_B2F_1 = 5


class Union_Cave_B1F_Warp_Points(Enum): 

	UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_7_WP = WarpInstruction( 
		getHex(UNION_CAVE_B1F.RUINS_OF_ALPH_OUTSIDE_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	UNION_CAVE_B1F_TO_RUINS_OF_ALPH_OUTSIDE_8_WP = WarpInstruction( 
		getHex(UNION_CAVE_B1F.RUINS_OF_ALPH_OUTSIDE_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	UNION_CAVE_B1F_TO_UNION_CAVE_1F_1_WP = WarpInstruction( 
		getHex(UNION_CAVE_B1F.UNION_CAVE_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	UNION_CAVE_B1F_TO_UNION_CAVE_1F_2_WP = WarpInstruction( 
		getHex(UNION_CAVE_B1F.UNION_CAVE_1F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	UNION_CAVE_B1F_TO_UNION_CAVE_B2F_1_WP = WarpInstruction( 
		getHex(UNION_CAVE_B1F.UNION_CAVE_B2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

