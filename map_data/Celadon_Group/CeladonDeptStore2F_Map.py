from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_DEPT_STORE_2F

class CELADON_DEPT_STORE_2F(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_DEPT_STORE_3F_1 = 1
	CELADON_DEPT_STORE_1F_3 = 2
	CELADON_DEPT_STORE_ELEVATOR_1 = 3


class Celadon_Dept_Store_2F_Warp_Points(Enum): 

	CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_3F_1_WP = WarpInstruction( 
		getHex(CELADON_DEPT_STORE_2F.CELADON_DEPT_STORE_3F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_1F_3_WP = WarpInstruction( 
		getHex(CELADON_DEPT_STORE_2F.CELADON_DEPT_STORE_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_DEPT_STORE_2F_TO_CELADON_DEPT_STORE_ELEVATOR_1_WP = WarpInstruction( 
		getHex(CELADON_DEPT_STORE_2F.CELADON_DEPT_STORE_ELEVATOR_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

