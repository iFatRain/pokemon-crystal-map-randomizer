from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Vermilion
mapGroup = MapGroup.VERMILION
specificMap = Vermilion.VERMILION_POKECENTER_1F

class VERMILION_POKECENTER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	VERMILION_CITY_2 = 1
	POKECENTER_2F_1 = 3


class Vermilion_Pokecenter_1F_Warp_Points(Enum): 

	Vermilion_City_Pokecenter_Exit_WP = WarpInstruction(
		getHex(VERMILION_POKECENTER_1F.VERMILION_CITY_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	Vermilion_City_Pokecenter_Stairs_WP = WarpInstruction(
		getHex(VERMILION_POKECENTER_1F.POKECENTER_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

