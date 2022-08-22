from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Fast_Ship
mapGroup = MapGroup.FAST_SHIP
specificMap = Fast_Ship.VERMILION_PORT_PASSAGE

class VERMILION_PORT_PASSAGE(IntEnum):
	def __str__(self):
		return str(self.value)

	VERMILION_CITY_8 = 1
	VERMILION_PORT_PASSAGE_4 = 3
	VERMILION_PORT_PASSAGE_3 = 4
	VERMILION_PORT_1 = 5


class Vermilion_Port_Passage_Warp_Points(Enum): 

	Vermilion_Upper_Port_Passage_To_Vermilion_City_WP = WarpInstruction(
		getHex(VERMILION_PORT_PASSAGE.VERMILION_CITY_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Vermilion_Upper_Port_Passage_To_Underground_Passage_North_WP = WarpInstruction(
		getHex(VERMILION_PORT_PASSAGE.VERMILION_PORT_PASSAGE_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Vermilion_Underground_Passage_North_To_Upper_Port_Passage_WP = WarpInstruction(
		getHex(VERMILION_PORT_PASSAGE.VERMILION_PORT_PASSAGE_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Vermilion_Port_Passage_To_Vermilion_Port_WP = WarpInstruction(
		getHex(VERMILION_PORT_PASSAGE.VERMILION_PORT_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

