from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Cerulean
mapGroup = MapGroup.CERULEAN
specificMap = Cerulean.CERULEAN_TRADE_SPEECH_HOUSE

class CERULEAN_TRADE_SPEECH_HOUSE(IntEnum):
	def __str__(self):
		return str(self.value)

	CERULEAN_CITY_3 = 1



class Cerulean_Trade_Speech_House_Warp_Points(Enum): 

	Cerulean_City_Trade_Speech_House_Exit_WP = WarpInstruction(
		getHex(CERULEAN_TRADE_SPEECH_HOUSE.CERULEAN_CITY_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 


