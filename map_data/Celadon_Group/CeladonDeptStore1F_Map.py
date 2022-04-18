from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_DEPT_STORE_1F

class CELADON_DEPT_STORE_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_CITY_1 = 1
	CELADON_DEPT_STORE_2F_2 = 3
	CELADON_DEPT_STORE_ELEVATOR_1 = 4


class Celadon_Dept_Store_1F_Warp_Points(Enum): 

	CELADON_DEPT_STORE_1F_TO_CELADON_CITY_1_WP = WarpInstruction( 
		getHex(CELADON_DEPT_STORE_1F.CELADON_CITY_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_DEPT_STORE_1F_TO_CELADON_DEPT_STORE_2F_2_WP = WarpInstruction( 
		getHex(CELADON_DEPT_STORE_1F.CELADON_DEPT_STORE_2F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_DEPT_STORE_1F_TO_CELADON_DEPT_STORE_ELEVATOR_1_WP = WarpInstruction( 
		getHex(CELADON_DEPT_STORE_1F.CELADON_DEPT_STORE_ELEVATOR_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

