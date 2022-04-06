from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod
mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_DEPT_STORE_ROOF

class GOLDENROD_DEPT_STORE_ROOF(IntEnum):
	def __str__(self):
		return str(self.value)

	GOLDENROD_DEPT_STORE_6F_3 = 1


class Goldenrod_Dept_Store_Roof_Warp_Points(Enum): 

	GOLDENROD_DEPT_STORE_ROOF_TO_GOLDENROD_DEPT_STORE_6F_3_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE_ROOF.GOLDENROD_DEPT_STORE_6F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

