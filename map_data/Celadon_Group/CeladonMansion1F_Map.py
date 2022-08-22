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

	Celadon_City_Mansion_1F_Front_Exit_WP = WarpInstruction(
		getHex(CELADON_MANSION_1F.CELADON_CITY_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Mansion_1F_Rear_Exit_Central_Stairs_WP = WarpInstruction(
		getHex(CELADON_MANSION_1F.CELADON_CITY_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Mansion_1F_Left_Stairs_WP = WarpInstruction(
		getHex(CELADON_MANSION_1F.CELADON_MANSION_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Mansion_1F_Right_Stairs_WP = WarpInstruction(
		getHex(CELADON_MANSION_1F.CELADON_MANSION_2F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

