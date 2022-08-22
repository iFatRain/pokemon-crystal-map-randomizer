from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_MANSION_2F

class CELADON_MANSION_2F(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_MANSION_1F_4 = 1
	CELADON_MANSION_3F_2 = 2
	CELADON_MANSION_3F_3 = 3
	CELADON_MANSION_1F_5 = 4


class Celadon_Mansion_2F_Warp_Points(Enum): 

	Celadon_City_Mansion_2F_Far_Left_Stairs_WP = WarpInstruction(
		getHex(CELADON_MANSION_2F.CELADON_MANSION_1F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Mansion_2F_Left_Center_Stairs_WP = WarpInstruction(
		getHex(CELADON_MANSION_2F.CELADON_MANSION_3F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Mansion_2F_Right_Center_Stairs_WP = WarpInstruction(
		getHex(CELADON_MANSION_2F.CELADON_MANSION_3F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	Celadon_City_Mansion_2F_Far_Right_Stairs_WP = WarpInstruction(
		getHex(CELADON_MANSION_2F.CELADON_MANSION_1F_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

