from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_POKECENTER_1F

class CELADON_POKECENTER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_CITY_5 = 1
	POKECENTER_2F_1 = 3


class Celadon_Pokecenter_1F_Warp_Points(Enum): 

	Celadon_City_Pokecenter_Exit_WP = WarpInstruction(
		getHex(CELADON_POKECENTER_1F.CELADON_CITY_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Pokecenter_Stairs_WP = WarpInstruction(
		getHex(CELADON_POKECENTER_1F.POKECENTER_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

