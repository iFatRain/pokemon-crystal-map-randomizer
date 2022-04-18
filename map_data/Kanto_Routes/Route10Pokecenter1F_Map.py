from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.ROUTE_10_POKECENTER_1F

class ROUTE_10_POKECENTER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_10_NORTH_1 = 1
	POKECENTER_2F_1 = 3


class Route_10_Pokecenter_1F_Warp_Points(Enum): 

	ROUTE_10_POKECENTER_1F_TO_ROUTE_10_NORTH_1_WP = WarpInstruction( 
		getHex(ROUTE_10_POKECENTER_1F.ROUTE_10_NORTH_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_10_POKECENTER_1F_TO_POKECENTER_2F_1_WP = WarpInstruction( 
		getHex(ROUTE_10_POKECENTER_1F.POKECENTER_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

