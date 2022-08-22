from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Celadon

mapGroup = MapGroup.CELADON
specificMap = Celadon.CELADON_DEPT_STORE_6F

class CELADON_DEPT_STORE_6F(IntEnum):
	def __str__(self):
		return str(self.value)

	CELADON_DEPT_STORE_5F_2 = 1
	CELADON_DEPT_STORE_ELEVATOR_1 = 2


class Celadon_Dept_Store_6F_Warp_Points(Enum): 

	Celadon_City_Dept_Store_6F_Stairs_WP = WarpInstruction(
		getHex(CELADON_DEPT_STORE_6F.CELADON_DEPT_STORE_5F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 
	#Elevator Unused
	# Celadon_City_Dept_Store_6F_Elevator_WP = WarpInstruction(
	# 	getHex(CELADON_DEPT_STORE_6F.CELADON_DEPT_STORE_ELEVATOR_1),
	# 	getHex(mapGroup),
	# 	getHex(specificMap)
	# 	)

