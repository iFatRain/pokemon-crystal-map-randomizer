from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_MANSION_3F

class CELADON_MANSION_3F(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_MANSION_ROOF_1 = 1
	CELADON_MANSION_2F_2 = 2
	CELADON_MANSION_2F_3 = 3
	CELADON_MANSION_ROOF_2 = 4


class Celadon_Mansion_3F_Warp_Points(Enum): 

	CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_1_WP = WarpInstruction( 
		getHex(CELADON_MANSION_3F.CELADON_MANSION_ROOF_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_MANSION_3F_TO_CELADON_MANSION_2F_2_WP = WarpInstruction( 
		getHex(CELADON_MANSION_3F.CELADON_MANSION_2F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_MANSION_3F_TO_CELADON_MANSION_2F_3_WP = WarpInstruction( 
		getHex(CELADON_MANSION_3F.CELADON_MANSION_2F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_MANSION_3F_TO_CELADON_MANSION_ROOF_2_WP = WarpInstruction( 
		getHex(CELADON_MANSION_3F.CELADON_MANSION_ROOF_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

