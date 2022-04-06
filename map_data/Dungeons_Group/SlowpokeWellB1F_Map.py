from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.SLOWPOKE_WELL_B1F

class SLOWPOKE_WELL_B1F(IntEnum):
	def __str__(self):
		return str(self.value)

	AZALEA_TOWN_6 = 1
	SLOWPOKE_WELL_B2F_1 = 2


class Slowpoke_Well_B1F_Warp_Points(Enum):

	SLOWPOKE_WELL_B1_F_TO_AZALEA_TOWN_6_WP = WarpInstruction( 
		getHex(SLOWPOKE_WELL_B1F.AZALEA_TOWN_6),
		getHex(mapGroup),
		getHex(specificMap)
		) 

	SLOWPOKE_WELL_B1_F_TO_SLOWPOKE_WELL_B2F_1_WP = WarpInstruction( 
		getHex(SLOWPOKE_WELL_B1F.SLOWPOKE_WELL_B2F_1),
		getHex(mapGroup),
		getHex(specificMap)
		) 

