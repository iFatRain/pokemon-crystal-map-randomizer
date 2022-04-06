from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod
mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_DEPT_STORE3_F

class GOLDENROD_DEPT_STORE3_F(IntEnum):
	def __str__(self):
		return str(self.value)

	GOLDENROD_DEPT_STORE_2F_1 = 1
	GOLDENROD_DEPT_STORE_4F_2 = 2
	GOLDENROD_DEPT_STORE_ELEVATOR_1 = 3


class Goldenrod_Dept_Store3_F_Warp_Points(Enum): 

	GOLDENROD_DEPT_STORE3_F_TO_GOLDENROD_DEPT_STORE_2F_1_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE3_F.GOLDENROD_DEPT_STORE_2F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	GOLDENROD_DEPT_STORE3_F_TO_GOLDENROD_DEPT_STORE_4F_2_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE3_F.GOLDENROD_DEPT_STORE_4F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	GOLDENROD_DEPT_STORE3_F_TO_GOLDENROD_DEPT_STORE_ELEVATOR_1_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE3_F.GOLDENROD_DEPT_STORE_ELEVATOR_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

