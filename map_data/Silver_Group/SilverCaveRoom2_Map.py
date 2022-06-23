from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.SILVER_CAVE_ROOM_2

class SILVER_CAVE_ROOM_2(IntEnum):
	def __str__(self):
		return str(self.value)

	SILVER_CAVE_ROOM_1_2 = 1
	SILVER_CAVE_ROOM_3_1 = 2
	SILVER_CAVE_ITEM_ROOMS_1 = 3
	SILVER_CAVE_ITEM_ROOMS_2 = 4


class Silver_Cave_Room_2_Warp_Points(Enum):

	SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_1_2_WP = WarpInstruction(
		getHex(SILVER_CAVE_ROOM_2.SILVER_CAVE_ROOM_1_2),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ROOM_3_1_WP = WarpInstruction(
		getHex(SILVER_CAVE_ROOM_2.SILVER_CAVE_ROOM_3_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_1_WP = WarpInstruction(
		getHex(SILVER_CAVE_ROOM_2.SILVER_CAVE_ITEM_ROOMS_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SILVER_CAVE_ROOM_2_TO_SILVER_CAVE_ITEM_ROOMS_2_WP = WarpInstruction(
		getHex(SILVER_CAVE_ROOM_2.SILVER_CAVE_ITEM_ROOMS_2),
		getHex(mapGroup),
		getHex(specificMap)
		) 

