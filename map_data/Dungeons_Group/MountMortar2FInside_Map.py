from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.MOUNT_MORTAR_2F_INSIDE

class MOUNT_MORTAR_2F_INSIDE(IntEnum):
	def __str__(self):
		return str(self.value)

	MOUNT_MORTAR_1F_OUTSIDE_4 = 1
	MOUNT_MORTAR_1F_INSIDE_6 = 2


class Mount_Mortar_2F_Inside_Warp_Points(Enum): 

	MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_OUTSIDE_4_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_2F_INSIDE.MOUNT_MORTAR_1F_OUTSIDE_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_2F_INSIDE_TO_MOUNT_MORTAR_1F_INSIDE_6_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_2F_INSIDE.MOUNT_MORTAR_1F_INSIDE_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

