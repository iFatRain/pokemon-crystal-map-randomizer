from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod
mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_DEPT_STORE_1F

class GOLDENROD_DEPT_STORE_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	GOLDENROD_CITY_9 = 1

	GOLDENROD_DEPT_STORE_2F_2 = 3
	GOLDENROD_DEPT_STORE_ELEVATOR_1 = 4


class Goldenrod_Dept_Store_1F_Warp_Points(Enum): 

	GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_CITY_9_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE_1F.GOLDENROD_CITY_9), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_DEPT_STORE_2F_2_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE_1F.GOLDENROD_DEPT_STORE_2F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	GOLDENROD_DEPT_STORE_1F_TO_GOLDENROD_DEPT_STORE_ELEVATOR_1_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE_1F.GOLDENROD_DEPT_STORE_ELEVATOR_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

