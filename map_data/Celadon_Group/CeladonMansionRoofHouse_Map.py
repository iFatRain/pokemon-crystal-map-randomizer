from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_MANSION_ROOF_HOUSE

class CELADON_MANSION_ROOF_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_MANSION_ROOF_3 = 1


class Celadon_Mansion_Roof_House_Warp_Points(Enum): 

	CELADON_MANSION_ROOF_HOUSE_TO_CELADON_MANSION_ROOF_3_WP = WarpInstruction( 
		getHex(CELADON_MANSION_ROOF_HOUSE.CELADON_MANSION_ROOF_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


