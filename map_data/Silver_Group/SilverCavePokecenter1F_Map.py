from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Silver
mapGroup = MapGroup.SILVER
specificMap = Silver.SILVER_CAVE_POKECENTER_1F

class SILVER_CAVE_POKECENTER_1F(IntEnum):
	def __str__(self):
		return str(self.value)

	SILVER_CAVE_OUTSIDE_1 = 1
	POKECENTER_2F_1 = 3


class Silver_Cave_Pokecenter_1F_Warp_Points(Enum):

	SILVER_CAVE_POKECENTER_1F_TO_SILVER_CAVE_OUTSIDE_1_WP = WarpInstruction(
		getHex(SILVER_CAVE_POKECENTER_1F.SILVER_CAVE_OUTSIDE_1),
		getHex(mapGroup),
		getHex(specificMap)
		)

	SILVER_CAVE_POKECENTER_1F_TO_POKECENTER_2F_1_WP = WarpInstruction(
		getHex(SILVER_CAVE_POKECENTER_1F.POKECENTER_2F_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 

