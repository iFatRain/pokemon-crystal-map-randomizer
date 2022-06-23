from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.SILVER_CAVE_ROOM_3

class SILVER_CAVE_ROOM_3(IntEnum):
	def __str__(self):
		return str(self.value)

	SILVER_CAVE_ROOM_2_2 = 1


class Silver_Cave_Room_3_Warp_Points(Enum):

	SILVER_CAVE_ROOM_3_TO_SILVER_CAVE_ROOM_2_2_WP = WarpInstruction(
		getHex(SILVER_CAVE_ROOM_3.SILVER_CAVE_ROOM_2_2),
		getHex(mapGroup),
		getHex(specificMap)
		) 

