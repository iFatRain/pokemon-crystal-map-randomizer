from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.SILVER_CAVE_ITEM_ROOMS

class SILVER_CAVE_ITEM_ROOMS(IntEnum):
	def __str__(self):
		return str(self.value)

	SILVER_CAVE_ROOM_2_3 = 1
	SILVER_CAVE_ROOM_2_4 = 2


class Silver_Cave_Item_Rooms_Warp_Points(Enum): 

	SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_3_WP = WarpInstruction( 
		getHex(SILVER_CAVE_ITEM_ROOMS.SILVER_CAVE_ROOM_2_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SILVER_CAVE_ITEM_ROOMS_TO_SILVER_CAVE_ROOM_2_4_WP = WarpInstruction( 
		getHex(SILVER_CAVE_ITEM_ROOMS.SILVER_CAVE_ROOM_2_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

