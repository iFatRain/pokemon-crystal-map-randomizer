from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_POKECENTER_2F_BETA

class CELADON_POKECENTER_2F_BETA(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_POKECENTER_1F_3 = 1


class Celadon_Pokecenter_2F_Beta_Warp_Points(Enum): 

	CELADON_POKECENTER_2F_BETA_TO_CELADON_POKECENTER_1F_3_WP = WarpInstruction( 
		getHex(CELADON_POKECENTER_2F_BETA.CELADON_POKECENTER_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

