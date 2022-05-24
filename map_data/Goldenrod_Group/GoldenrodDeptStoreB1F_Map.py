from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.GOLDENROD_DEPT_STORE_B1F

class GOLDENROD_DEPT_STORE_B1F(IntEnum):
	def __str__(self):
		return str(self.value)

	GOLDENROD_UNDERGROUND_WAREHOUSE_3 = 1


class Goldenrod_Dept_Store_B1F_Warp_Points(Enum):

	GOLDENROD_DEPT_STORE_B1F_TO_GOLDENROD_UNDERGROUND_WAREHOUSE_3_WP = WarpInstruction(
		getHex(GOLDENROD_DEPT_STORE_B1F.GOLDENROD_UNDERGROUND_WAREHOUSE_3),
		getHex(mapGroup),
		getHex(specificMap)
		)



