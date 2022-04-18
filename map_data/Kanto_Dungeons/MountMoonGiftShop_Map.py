from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fast_Ship
mapGroup = MapGroup.FAST_SHIP
specificMap = Fast_Ship.MOUNT_MOON_GIFT_SHOP

class MOUNT_MOON_GIFT_SHOP(IntEnum):
	def __str__(self):
		return str(self.value)

	MOUNT_MOON_SQUARE_3 = 1


class Mount_Moon_Gift_Shop_Warp_Points(Enum): 

	MOUNT_MOON_GIFT_SHOP_TO_MOUNT_MOON_SQUARE_3_WP = WarpInstruction( 
		getHex(MOUNT_MOON_GIFT_SHOP.MOUNT_MOON_SQUARE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

