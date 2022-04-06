from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.ICE_PATH_B2F_MAHOGANY_SIDE

class ICE_PATH_B2F_MAHOGANY_SIDE(IntEnum):
	def __str__(self):
		return str(self.value)

	ICE_PATH_B1F_2 = 1
	ICE_PATH_B3F_1 = 2
	ICE_PATH_B1F_3 = 3
	ICE_PATH_B1F_4 = 4
	ICE_PATH_B1F_5 = 5
	ICE_PATH_B1F_6 = 6


class Ice_Path_B2F_Mahogany_Side_Warp_Points(Enum): 

	ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_2_WP = WarpInstruction( 
		getHex(ICE_PATH_B2F_MAHOGANY_SIDE.ICE_PATH_B1F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B3F_1_WP = WarpInstruction( 
		getHex(ICE_PATH_B2F_MAHOGANY_SIDE.ICE_PATH_B3F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_3_WP = WarpInstruction( 
		getHex(ICE_PATH_B2F_MAHOGANY_SIDE.ICE_PATH_B1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_4_WP = WarpInstruction( 
		getHex(ICE_PATH_B2F_MAHOGANY_SIDE.ICE_PATH_B1F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_5_WP = WarpInstruction( 
		getHex(ICE_PATH_B2F_MAHOGANY_SIDE.ICE_PATH_B1F_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ICE_PATH_B2F_MAHOGANY_SIDE_TO_ICE_PATH_B1F_6_WP = WarpInstruction( 
		getHex(ICE_PATH_B2F_MAHOGANY_SIDE.ICE_PATH_B1F_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

