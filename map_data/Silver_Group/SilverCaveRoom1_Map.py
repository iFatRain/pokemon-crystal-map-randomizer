from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.SILVER_CAVE_ROOM_1

class SILVER_CAVE_ROOM_1(IntEnum):
	def __str__(self):
		return str(self.value)

	SILVER_CAVE_OUTSIDE_2 = 1
	SILVER_CAVE_ROOM_2_1 = 2


class Silver_Cave_Room_1_Warp_Points(Enum):

	SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_OUTSIDE_2_WP = WarpInstruction(
		getHex(SILVER_CAVE_ROOM_1.SILVER_CAVE_OUTSIDE_2),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SILVER_CAVE_ROOM_1_TO_SILVER_CAVE_ROOM_2_1_WP = WarpInstruction(
		getHex(SILVER_CAVE_ROOM_1.SILVER_CAVE_ROOM_2_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 

