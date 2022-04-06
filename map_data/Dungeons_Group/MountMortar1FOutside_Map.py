from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.MOUNT_MORTAR_1F_OUTSIDE

class MOUNT_MORTAR_1F_OUTSIDE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_42_3 = 1
	ROUTE_42_4 = 2
	ROUTE_42_5 = 3
	MOUNT_MORTAR_2F_INSIDE_1 = 4
	MOUNT_MORTAR_1F_INSIDE_1 = 5
	MOUNT_MORTAR_1F_INSIDE_2 = 6
	MOUNT_MORTAR_B1F_2 = 7
	MOUNT_MORTAR_1F_INSIDE_3 = 8
	MOUNT_MORTAR_1F_INSIDE_4 = 9


class Mount_Mortar_1F_Outside_Warp_Points(Enum): 

	MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_3_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_OUTSIDE.ROUTE_42_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_4_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_OUTSIDE.ROUTE_42_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_OUTSIDE_TO_ROUTE_42_5_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_OUTSIDE.ROUTE_42_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_2F_INSIDE_1_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_OUTSIDE.MOUNT_MORTAR_2F_INSIDE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_1_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_OUTSIDE.MOUNT_MORTAR_1F_INSIDE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_2_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_OUTSIDE.MOUNT_MORTAR_1F_INSIDE_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_B1F_2_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_OUTSIDE.MOUNT_MORTAR_B1F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_3_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_OUTSIDE.MOUNT_MORTAR_1F_INSIDE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MORTAR_1F_OUTSIDE_TO_MOUNT_MORTAR_1F_INSIDE_4_WP = WarpInstruction( 
		getHex(MOUNT_MORTAR_1F_OUTSIDE.MOUNT_MORTAR_1F_INSIDE_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

