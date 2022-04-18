from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.MOUNT_MOON

class MOUNT_MOON(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_3_1 = 1
	ROUTE_4_1 = 2
	MOUNT_MOON_7 = 3
	MOUNT_MOON_8 = 4
	MOUNT_MOON_SQUARE_1 = 5
	MOUNT_MOON_SQUARE_2 = 6
	MOUNT_MOON_3 = 7
	MOUNT_MOON_4 = 8


class Mount_Moon_Warp_Points(Enum): 

	MOUNT_MOON_TO_ROUTE_3_1_WP = WarpInstruction( 
		getHex(MOUNT_MOON.ROUTE_3_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MOON_TO_ROUTE_4_1_WP = WarpInstruction( 
		getHex(MOUNT_MOON.ROUTE_4_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MOON_TO_MOUNT_MOON_7_WP = WarpInstruction( 
		getHex(MOUNT_MOON.MOUNT_MOON_7), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MOON_TO_MOUNT_MOON_8_WP = WarpInstruction( 
		getHex(MOUNT_MOON.MOUNT_MOON_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MOON_TO_MOUNT_MOON_SQUARE_1_WP = WarpInstruction( 
		getHex(MOUNT_MOON.MOUNT_MOON_SQUARE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MOON_TO_MOUNT_MOON_SQUARE_2_WP = WarpInstruction( 
		getHex(MOUNT_MOON.MOUNT_MOON_SQUARE_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MOON_TO_MOUNT_MOON_3_WP = WarpInstruction( 
		getHex(MOUNT_MOON.MOUNT_MOON_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MOON_TO_MOUNT_MOON_4_WP = WarpInstruction( 
		getHex(MOUNT_MOON.MOUNT_MOON_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

