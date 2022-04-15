from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod
mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_DEPT_STORE_5F

class GOLDENROD_DEPT_STORE_5F(IntEnum):
	def __str__(self):
		return str(self.value)

	GOLDENROD_DEPT_STORE_4F_1 = 1
	GOLDENROD_DEPT_STORE_6F_1 = 2
	GOLDENROD_DEPT_STORE_ELEVATOR_1 = 3


class Goldenrod_Dept_Store_5F_Warp_Points(Enum): 

	GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_4F_1_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE_5F.GOLDENROD_DEPT_STORE_4F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_6F_1_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE_5F.GOLDENROD_DEPT_STORE_6F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	GOLDENROD_DEPT_STORE_5F_TO_GOLDENROD_DEPT_STORE_ELEVATOR_1_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE_5F.GOLDENROD_DEPT_STORE_ELEVATOR_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

