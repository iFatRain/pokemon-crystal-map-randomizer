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
        self.ORIGINAL_TOTAL = len(links)

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
    HAS_ALL_JOHTO_BADGES = "All Johto Badges"

    E4_KOGA = "Koga"
    E4_WILL = "Will"
    E4_KAREN = "Karen"
    E4_BRUNO = "Bruno"
    CHAMPION_LANCE = "Champion"

    #Kanto Keys
    HAS_ALL_KANTO_BADGES = "All Kanto Badges"
    BADGE_9 = "Badge 9"
    BADGE_10 = "Badge 10"
    BADGE_11 = "Badge 11"
    BADGE_12 = "Badge 12"
    BADGE_13 = "Badge 13"
    BADGE_14 = "Badge 14"
    BADGE_15 = "Badge 15"
    BADGE_16 = "Badge 16"

    RADIO_CARD = "Radio Card"
    EXPN_CARD = "Expansion Card"
    MACHINE_PART = "Machine Part"
    POWER_PLANT_ACCESS = "Power Plant"
    OAKS_LAB_ACCESS = "Oaks Lab"
    CERULEAN_GYM_ACCESS = "Cerulean Gym Access"
    FOUND_BLUE = "Blues Clues Lead You Here"
    VICTORY_ROAD_GATE_ACCESS = "Welcome to Kanto Friend"


def getHexBytes(hexInput):
    return bytes.fromhex(hexInput)

def getHex(integerInput):
    hexbyte =  hex(integerInput).removeprefix("0x")
    if len(hexbyte) == 1:
        hexbyte = '0'+hexbyte
    return hexbyte

