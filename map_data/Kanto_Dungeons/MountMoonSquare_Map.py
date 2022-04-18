from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fast_Ship
mapGroup = MapGroup.FAST_SHIP
specificMap = Fast_Ship.MOUNT_MOON_SQUARE

class MOUNT_MOON_SQUARE(IntEnum):
	def __str__(self):
		return str(self.value)

	MOUNT_MOON_5 = 1
	MOUNT_MOON_6 = 2
	MOUNT_MOON_GIFT_SHOP_1 = 3


class Mount_Moon_Square_Warp_Points(Enum): 

	MOUNT_MOON_SQUARE_TO_MOUNT_MOON_5_WP = WarpInstruction( 
		getHex(MOUNT_MOON_SQUARE.MOUNT_MOON_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MOON_SQUARE_TO_MOUNT_MOON_6_WP = WarpInstruction( 
		getHex(MOUNT_MOON_SQUARE.MOUNT_MOON_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	MOUNT_MOON_SQUARE_TO_MOUNT_MOON_GIFT_SHOP_1_WP = WarpInstruction( 
		getHex(MOUNT_MOON_SQUARE.MOUNT_MOON_GIFT_SHOP_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

