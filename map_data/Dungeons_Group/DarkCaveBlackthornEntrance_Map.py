from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.DARK_CAVE_BLACKTHORN_ENTRANCE

class DARK_CAVE_BLACKTHORN_ENTRANCE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_45 = 1
	DARK_CAVE_VIOLET_ENTRANCE = 2


class Dark_Cave_Blackthorn_Entrance_Warp_Points(Enum): 

	DARK_CAVE_BLACKTHORN_ENTRANCE_TO_ROUTE_45_WP = WarpInstruction(
		getHex(DARK_CAVE_BLACKTHORN_ENTRANCE.ROUTE_45),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	DARK_CAVE_BLACKTHORN_ENTRANCE_TO_DARK_CAVE_VIOLET_ENTRANCE_WP = WarpInstruction(
		getHex(DARK_CAVE_BLACKTHORN_ENTRANCE.DARK_CAVE_VIOLET_ENTRANCE),
		getHex(mapGroup),
		getHex(specificMap)
		) 

