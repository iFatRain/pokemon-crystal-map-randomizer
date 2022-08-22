from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Viridian
mapGroup = MapGroup.VIRIDIAN
specificMap = Viridian.TRAINER_HOUSE_B1F

class TRAINER_HOUSE_B1F(IntEnum):
	def __str__(self):
		return str(self.value)

	TRAINER_HOUSE_1F_3 = 1


class Trainer_House_B1F_Warp_Points(Enum): 

	Trainer_House_B1F_Stairs_WP = WarpInstruction(
		getHex(TRAINER_HOUSE_B1F.TRAINER_HOUSE_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

