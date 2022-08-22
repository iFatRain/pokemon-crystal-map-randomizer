from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_CAFE

class CELADON_CAFE(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_CITY_9 = 1



class Celadon_Cafe_Warp_Points(Enum): 

	Celadon_City_Cafe_Exit_WP = WarpInstruction(
		getHex(CELADON_CAFE.CELADON_CITY_9), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

