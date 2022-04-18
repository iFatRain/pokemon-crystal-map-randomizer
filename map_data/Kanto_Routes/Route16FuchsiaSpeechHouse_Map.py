from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon
mapGroup = MapGroup.CELADON
specificMap = Celadon.ROUTE_16_FUCHSIA_SPEECH_HOUSE

class ROUTE_16_FUCHSIA_SPEECH_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	ROUTE_16_1 = 1


class Route_16_Fuchsia_Speech_House_Warp_Points(Enum): 

	ROUTE_16_FUCHSIA_SPEECH_HOUSE_TO_ROUTE_16_1_WP = WarpInstruction( 
		getHex(ROUTE_16_FUCHSIA_SPEECH_HOUSE.ROUTE_16_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

