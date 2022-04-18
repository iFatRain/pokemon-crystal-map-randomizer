from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon
mapGroup = MapGroup.CELADON
specificMap = Celadon.ROUTE_16

class ROUTE_16(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_16_FUCHSIA_SPEECH_HOUSE_1 = 1
	ROUTE_16_GATE_3 = 2
	ROUTE_16_GATE_1 = 4


class Route_16_Warp_Points(Enum): 

	ROUTE_16_TO_ROUTE_16_FUCHSIA_SPEECH_HOUSE_1_WP = WarpInstruction( 
		getHex(ROUTE_16.ROUTE_16_FUCHSIA_SPEECH_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_16_TO_ROUTE_16_GATE_3_WP = WarpInstruction( 
		getHex(ROUTE_16.ROUTE_16_GATE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ROUTE_16_TO_ROUTE_16_GATE_1_WP = WarpInstruction( 
		getHex(ROUTE_16.ROUTE_16_GATE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


