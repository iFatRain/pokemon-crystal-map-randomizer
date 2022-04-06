from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.MOUNT_MORTAR_1F_INSIDE

class MOUNT_MORTAR_1F_INSIDE(IntEnum):
	def __str__(self):
		return str(self.value)

	MOUNT_MORTAR_1F_OUTSIDE_5 = 1
	MOUNT_MORTAR_1F_OUTSIDE_6 = 2
	MOUNT_MORTAR_1F_OUTSIDE_8 = 3
	MOUNT_MORTAR_1F_OUTSIDE_9 = 4
	MOUNT_MORTAR_B1F_1 = 5
	MOUNT_MORTAR_2F_INSIDE_2 = 6


class Mount_Mortar_1F_Inside_Warp_Points(Enum): 

	MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_5_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_INSIDE.MOUNT_MORTAR_1F_OUTSIDE_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_6_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_INSIDE.MOUNT_MORTAR_1F_OUTSIDE_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_8_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_INSIDE.MOUNT_MORTAR_1F_OUTSIDE_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_9_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_INSIDE.MOUNT_MORTAR_1F_OUTSIDE_9), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_B1F_1_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_INSIDE.MOUNT_MORTAR_B1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_INSIDE_TO_MOUNT_MORTAR_2F_INSIDE_2_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_INSIDE.MOUNT_MORTAR_2F_INSIDE_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

