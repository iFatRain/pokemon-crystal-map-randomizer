from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_MANSION_1F

class CELADON_MANSION_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_CITY_2 = 1
	CELADON_CITY_3 = 3
	CELADON_MANSION_2F_1 = 4
	CELADON_MANSION_2F_4 = 5


class Celadon_Mansion_1F_Warp_Points(Enum): 

	CELADON_MANSION_1F_TO_CELADON_CITY_2_WP = WarpInstruction( 
		getHex(CELADON_MANSION_1F.CELADON_CITY_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_MANSION_1F_TO_CELADON_CITY_3_WP = WarpInstruction( 
		getHex(CELADON_MANSION_1F.CELADON_CITY_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_MANSION_1F_TO_CELADON_MANSION_2F_1_WP = WarpInstruction( 
		getHex(CELADON_MANSION_1F.CELADON_MANSION_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_MANSION_1F_TO_CELADON_MANSION_2F_4_WP = WarpInstruction( 
		getHex(CELADON_MANSION_1F.CELADON_MANSION_2F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

