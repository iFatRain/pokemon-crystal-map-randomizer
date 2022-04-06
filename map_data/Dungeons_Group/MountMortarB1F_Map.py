from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.MOUNT_MORTAR_B1F

class MOUNT_MORTAR_B1F(IntEnum):
	def __str__(self):
		return str(self.value)

	MOUNT_MORTAR_1F_INSIDE_5 = 1
	MOUNT_MORTAR_1F_OUTSIDE_7 = 2


class Mount_Mortar_B1F_Warp_Points(Enum):

	MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_INSIDE_5_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_B1F.MOUNT_MORTAR_1F_INSIDE_5),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_B1_F_TO_MOUNT_MORTAR_1F_OUTSIDE_7_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_B1F.MOUNT_MORTAR_1F_OUTSIDE_7),
		getHex(mapGroup),
		getHex(specificMap)
		) 

