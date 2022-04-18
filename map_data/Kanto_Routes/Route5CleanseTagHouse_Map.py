from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.ROUTE_5_CLEANSE_TAG_HOUSE

class ROUTE_5_CLEANSE_TAG_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_5_4 = 1


class Route_5_Cleanse_Tag_House_Warp_Points(Enum): 

	ROUTE_5_CLEANSE_TAG_HOUSE_TO_ROUTE_5_4_WP = WarpInstruction( 
		getHex(ROUTE_5_CLEANSE_TAG_HOUSE.ROUTE_5_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


