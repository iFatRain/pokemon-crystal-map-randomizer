from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Vermilion
mapGroup = MapGroup.VERMILION
specificMap = Vermilion.VERMILION_MAGNET_TRAIN_SPEECH_HOUSE

class VERMILION_MAGNET_TRAIN_SPEECH_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	VERMILION_CITY_4 = 1


class Vermilion_Magnet_Train_Speech_House_Warp_Points(Enum): 

	Vermilion_City_Magnet_Train_Speech_House_Exit_WP = WarpInstruction(
		getHex(VERMILION_MAGNET_TRAIN_SPEECH_HOUSE.VERMILION_CITY_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

