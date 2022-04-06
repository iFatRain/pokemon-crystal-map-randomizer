from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Indigo
mapGroup = MapGroup.INDIGO
specificMap = Indigo.ROUTE_23

class ROUTE23(IntEnum):
	def __str__(self):
		return str(self.value)

	INDIGO_PLATEAU_POKECENTER_1F_1 = 1
	VICTORY_ROAD_10 = 3



class Route23_Warp_Points(Enum): 

	ROUTE23_TO_INDIGO_PLATEAU_POKECENTER_1F_1_WP = WarpInstruction( 
		getHex(ROUTE23.INDIGO_PLATEAU_POKECENTER_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		)

	ROUTE23_TO_VICTORY_ROAD_10_WP = WarpInstruction( 
		getHex(ROUTE23.VICTORY_ROAD_10), 
		getHex(mapGroup),
		getHex(specificMap)
		) 
