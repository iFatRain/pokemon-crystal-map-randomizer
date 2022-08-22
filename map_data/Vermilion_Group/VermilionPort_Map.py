from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fast_Ship

mapGroup = MapGroup.FAST_SHIP
specificMap = Fast_Ship.VERMILION_PORT

class VERMILION_PORT(IntEnum):
	def __str__(self):
		return str(self.value)

	VERMILION_PORT_PASSAGE_5 = 1
	FAST_SHIP_1F_1 = 2


class Vermilion_Port_Warp_Points(Enum): 

	Vermilion_Port_To_Port_Passage_WP = WarpInstruction(
		getHex(VERMILION_PORT.VERMILION_PORT_PASSAGE_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Vermilion_Port_To_Fast_Ship_WP = WarpInstruction(
		getHex(VERMILION_PORT.FAST_SHIP_1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

