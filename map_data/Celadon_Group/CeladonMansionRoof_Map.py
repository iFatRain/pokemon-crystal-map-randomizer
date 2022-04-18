from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_MANSION_ROOF

class CELADON_MANSION_ROOF(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_MANSION_3F_1 = 1
	CELADON_MANSION_3F_4 = 2
	CELADON_MANSION_ROOF_HOUSE_1 = 3


class Celadon_Mansion_Roof_Warp_Points(Enum): 

	CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_1_WP = WarpInstruction( 
		getHex(CELADON_MANSION_ROOF.CELADON_MANSION_3F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_MANSION_ROOF_TO_CELADON_MANSION_3F_4_WP = WarpInstruction( 
		getHex(CELADON_MANSION_ROOF.CELADON_MANSION_3F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_MANSION_ROOF_TO_CELADON_MANSION_ROOF_HOUSE_1_WP = WarpInstruction( 
		getHex(CELADON_MANSION_ROOF.CELADON_MANSION_ROOF_HOUSE_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

