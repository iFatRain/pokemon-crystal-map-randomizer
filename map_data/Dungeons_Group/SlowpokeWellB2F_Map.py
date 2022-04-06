from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.SLOWPOKE_WELL_B2F

class SLOWPOKE_WELL_B2F(IntEnum):
	def __str__(self):
		return str(self.value)

	SLOWPOKE_WELL_B1F_2 = 1


class Slowpoke_Well_B2F_Warp_Points(Enum):

	SLOWPOKE_WELL_B2_F_TO_SLOWPOKE_WELL_B1F_2_WP = WarpInstruction( 
		getHex(SLOWPOKE_WELL_B2F.SLOWPOKE_WELL_B1F_2),
		getHex(mapGroup),
		getHex(specificMap)
		) 

