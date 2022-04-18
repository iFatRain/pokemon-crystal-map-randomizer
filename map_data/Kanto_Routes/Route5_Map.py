from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Saffron
mapGroup = MapGroup.SAFFRON
specificMap = Saffron.ROUTE_5

class ROUTE_5(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_5_UNDERGROUND_PATH_ENTRANCE_1 = 1
	ROUTE_5_SAFFRON_GATE_1 = 2
	ROUTE_5_CLEANSE_TAG_HOUSE_1 = 4


class Route_5_Warp_Points(Enum): 

	ROUTE_5_TO_ROUTE_5_UNDERGROUND_PATH_ENTRANCE_1_WP = WarpInstruction( 
		getHex(ROUTE_5.ROUTE_5_UNDERGROUND_PATH_ENTRANCE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_5_TO_ROUTE_5_SAFFRON_GATE_1_WP = WarpInstruction( 
		getHex(ROUTE_5.ROUTE_5_SAFFRON_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_5_TO_ROUTE_5_CLEANSE_TAG_HOUSE_1_WP = WarpInstruction( 
		getHex(ROUTE_5.ROUTE_5_CLEANSE_TAG_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

