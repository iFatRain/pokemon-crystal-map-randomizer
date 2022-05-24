from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.ICE_PATH_B1F

class ICE_PATH_B1F(IntEnum):
	def __str__(self):
		return str(self.value)

	ICE_PATH_1F_3 = 1
	ICE_PATH_B2F_MAHOGANY_SIDE_1 = 2
	ICE_PATH_B2F_MAHOGANY_SIDE_3 = 3  # hole = 3
	ICE_PATH_B2F_MAHOGANY_SIDE_4 = 4  # hole = 4
	ICE_PATH_B2F_MAHOGANY_SIDE_5 = 5  # hole = 5
	ICE_PATH_B2F_MAHOGANY_SIDE_6 = 6  # hole = 6
	ICE_PATH_1F_4 = 7
	ICE_PATH_B2F_BLACKTHORN_SIDE_1 = 8


class Ice_Path_B1F_Warp_Points(Enum):

	ICE_PATH_B1F_TO_ICE_PATH_1F_3_WP = WarpInstruction( 
		getHex(ICE_PATH_B1F.ICE_PATH_1F_3),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_1_WP = WarpInstruction(
		getHex(ICE_PATH_B1F.ICE_PATH_B2F_MAHOGANY_SIDE_1),
		getHex(mapGroup),
		getHex(specificMap)
		)

	ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_3_WP = WarpInstruction(
		getHex(ICE_PATH_B1F.ICE_PATH_B2F_MAHOGANY_SIDE_3),
		getHex(mapGroup),
		getHex(specificMap)
		)

	ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_4_WP = WarpInstruction(
		getHex(ICE_PATH_B1F.ICE_PATH_B2F_MAHOGANY_SIDE_4),
		getHex(mapGroup),
		getHex(specificMap)
		)

	ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_5_WP = WarpInstruction(
		getHex(ICE_PATH_B1F.ICE_PATH_B2F_MAHOGANY_SIDE_5),
		getHex(mapGroup),
		getHex(specificMap)
		)

	ICE_PATH_B1F_TO_ICE_PATH_B2F_MAHOGANY_SIDE_6_WP = WarpInstruction(
		getHex(ICE_PATH_B1F.ICE_PATH_B2F_MAHOGANY_SIDE_6),
		getHex(mapGroup),
		getHex(specificMap)
		)

	ICE_PATH_B1F_TO_ICE_PATH_1F_4_WP = WarpInstruction( 
		getHex(ICE_PATH_B1F.ICE_PATH_1F_4),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ICE_PATH_B1F_TO_ICE_PATH_B2F_BLACKTHORN_SIDE_1_WP = WarpInstruction( 
		getHex(ICE_PATH_B1F.ICE_PATH_B2F_BLACKTHORN_SIDE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

