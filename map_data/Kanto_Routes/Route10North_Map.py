from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.ROUTE_10_NORTH

class ROUTE_10_NORTH(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_10_POKECENTER_1F_1 = 1
	POWER_PLANT_1 = 2


class Route_10_North_Warp_Points(Enum): 

	ROUTE_10_NORTH_TO_ROUTE_10_POKECENTER_1F_1_WP = WarpInstruction( 
		getHex(ROUTE_10_NORTH.ROUTE_10_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_10_NORTH_TO_POWER_PLANT_1_WP = WarpInstruction( 
		getHex(ROUTE_10_NORTH.POWER_PLANT_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

