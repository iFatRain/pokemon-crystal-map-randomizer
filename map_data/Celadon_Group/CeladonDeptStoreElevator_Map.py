from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_DEPT_STORE_ELEVATOR

class CELADON_DEPT_STORE_ELEVATOR(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_DEPT_STORE_1F_-1 = 1
	CELADON_DEPT_STORE_1F_-1 = 2


class Celadon_Dept_Store_Elevator_Warp_Points(Enum): 

	CELADON_DEPT_STORE_ELEVATOR_TO_CELADON_DEPT_STORE_1F_-1_WP = WarpInstruction( 
		getHex(CELADON_DEPT_STORE_ELEVATOR.CELADON_DEPT_STORE_1F_-1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	CELADON_DEPT_STORE_ELEVATOR_TO_CELADON_DEPT_STORE_1F_-1_WP = WarpInstruction( 
		getHex(CELADON_DEPT_STORE_ELEVATOR.CELADON_DEPT_STORE_1F_-1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

