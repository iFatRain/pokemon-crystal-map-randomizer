from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Silver
mapGroup = MapGroup.SILVER
specificMap = Silver.SILVER_CAVE_OUTSIDE

class SILVER_CAVE_OUTSIDE(IntEnum):
	def __str__(self):
		return str(self.value)

	SILVER_CAVE_POKECENTER_1F_1 = 1
	SILVER_CAVE_ROOM_1_1 = 2


class Silver_Cave_Outside_Warp_Points(Enum): 

	SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_POKECENTER_1F_1_WP = WarpInstruction( 
		getHex(SILVER_CAVE_OUTSIDE.SILVER_CAVE_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SILVER_CAVE_OUTSIDE_TO_SILVER_CAVE_ROOM_1_1_WP = WarpInstruction( 
		getHex(SILVER_CAVE_OUTSIDE.SILVER_CAVE_ROOM_1_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

