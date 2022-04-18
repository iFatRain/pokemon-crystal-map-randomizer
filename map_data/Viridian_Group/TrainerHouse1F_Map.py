from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Viridian
mapGroup = MapGroup.VIRIDIAN
specificMap = Viridian.TRAINER_HOUSE_1F

class TRAINER_HOUSE_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	VIRIDIAN_CITY_3 = 1
	TRAINER_HOUSE_B1F_1 = 3


class Trainer_House_1F_Warp_Points(Enum): 

	TRAINER_HOUSE_1F_TO_VIRIDIAN_CITY_3_WP = WarpInstruction( 
		getHex(TRAINER_HOUSE_1F.VIRIDIAN_CITY_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


	TRAINER_HOUSE_1F_TO_TRAINER_HOUSE_B1F_1_WP = WarpInstruction( 
		getHex(TRAINER_HOUSE_1F.TRAINER_HOUSE_B1F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

