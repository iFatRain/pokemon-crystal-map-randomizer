from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_DEPT_STORE_5F

class CELADON_DEPT_STORE_5F(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_DEPT_STORE_4F_1 = 1
	CELADON_DEPT_STORE_6F_1 = 2
	CELADON_DEPT_STORE_ELEVATOR_1 = 3


class Celadon_Dept_Store_5F_Warp_Points(Enum): 

	CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_4F_1_WP = WarpInstruction( 
		getHex(CELADON_DEPT_STORE_5F.CELADON_DEPT_STORE_4F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_6F_1_WP = WarpInstruction( 
		getHex(CELADON_DEPT_STORE_5F.CELADON_DEPT_STORE_6F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_DEPT_STORE_5F_TO_CELADON_DEPT_STORE_ELEVATOR_1_WP = WarpInstruction( 
		getHex(CELADON_DEPT_STORE_5F.CELADON_DEPT_STORE_ELEVATOR_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

