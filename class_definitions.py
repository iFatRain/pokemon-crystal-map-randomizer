from enum import Enum


class WarpLink:

    def __init__(self, own_warp, linked_warp, memory_origin, offset = 0, dual_width = False,
                 unlocks = None, locked_by = None):
        self.DUAL_WIDTH = dual_width
        self.MODIFIED = False
        self.OWN = own_warp
        self.LINK = linked_warp
        self.MEMORY_ORIGIN = memory_origin
        self.OFFSET = offset
        self.LOCKED_BY = locked_by
        self.UNLOCKS = unlocks
        self.OUTPUT_TO_LOG = False
        self.DEFAULT_LINK = linked_warp

class WarpInstruction:
    def __init__(self, destination_warp_num, map_group, map_name):
        self.USED = False
        self.INSTRUCTION = destination_warp_num + map_group + map_name

    @classmethod
    def getInstruction(cls, warppoint):
        return bytes.fromhex(warppoint.INSTRUCTION)


class Node:

    def __init__(self, links):
        self.LINKS = links
        self.TOTAL_LINKS = len(links)
        self.USED_LINKS = 0
        self.HAS_LOCKED = False

    def incrementUsedLinks(self, incrementAmount=1):
        self.USED_LINKS += incrementAmount


class Unlock_Keys(Enum):
    KURTS_HOUSE_FOUND = "Triggers Rocket Removal From Well entrance"
    SLOWPOKE_WELL_FOUND = "Triggers Rocket Removal from Azalea Gym"
    CAN_CLEAR_SLOWPOKE_WELL = "Found Well and Kurt to trigger in proper order"

    ENTERED_BURNED_TOWER = "Entered Burned Tower"
    FOUND_CIANWOOD = "Found Cianwood for Fly HM"

    TOP_OF_LIGHTHOUSE_FOUND = "Begin Medicine Quest"
    CIANNWOOD_PHARMACY_FOUND = "Can Get Medicine for Quest"
    OLIVINE_MEDICINE = "Olivine Medicine Obtained"

    HM_STRENGTH = "Strength"
    HM_SURF = "Surf"
    HM_CUT = "Cut"
    HM_FLY = "Fly"
    HM_FLASH = "Flash"
    HM_WATERFALL = "Waterfall"
    HM_WHIRLPOOL = "Whirlpool"
    BADGE_1 = "Flash Gym Badge"
    BADGE_2 = "Cut Gym Badge"
    BADGE_3 = "Strength Gym Badge"
    BADGE_4 = "Surf Gym Badge"
    BADGE_5 = "Fly Gym Badge"
    BADGE_6 = "Useless Gym Badge"
    BADGE_7 = "Waterfall Gym Badge"
    BADGE_8 = "Whirlpool Gym Badge"

    #Conditionals to make logic easier
    CAN_SURF = "Have HM and Badge for Surf"
    CAN_CUT = "Have HM and Badge for Cut"
    CAN_SURF_OR_CUT = "Have HM+Badge for Surf/Cut"
    CAN_USE_STRENGTH = "HM+Badge for Strength"
    LAKE_OF_RAGE_FOUND = "Found Lake of Rage for Lance Questline"

    GYM_BATTLE_8 = "Battle Gym 8 Opens Dragon Shrine Entrance"

    CAN_CLEAR_MAHOGANY_ROCKETS = "Team Rocket Mahogany"
    CAN_CLEAR_RADIO_TOWER_ROCKETS = "Team Rocket Radio Tower"
    KEY_CARD = "Keycard for Radio Tower"

    HAS_7_BADGES = "Badge Count of 7"

    E4_KOGA = "Koga"
    E4_WILL = "Will"
    E4_KAREN = "Karen"
    E4_BRUNO = "Bruno"
    CHAMPION_LANCE = "Champion"


def getHexBytes(hexInput):
    return bytes.fromhex(hexInput)

def getHex(integerInput):
    hexbyte =  hex(integerInput).removeprefix("0x")
    if len(hexbyte) == 1:
        hexbyte = '0'+hexbyte
    return hexbyte

