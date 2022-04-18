import time

import links_and_nodes.johto_all_warp_points
from logic import AutomaticWarpLocator
from logic.MemoryAddressReader import buildMemoryLocationsFromSym
from logic.NewRandomizerLogic import randomizationStep1, randomizationStep2, randomizationStep3, randomizationStep4, \
    checkJohtoCompletability, randomizationStep5
from class_definitions import WarpInstruction, getHex

def randomizeWarps():
    fullyCompletable = False
    while fullyCompletable is False:
        print("Randomizing..")
        print("Doing Step 1")
        randomizedNodes = randomizationStep1()
        print("Doing Step 2")
        randomizedNodes = randomizationStep2(randomizedNodes)
        print("Doing Step 3")
        randomizedNodes = randomizationStep3(randomizedNodes)
        print("Doing Step 4")
        randomizedNodes = randomizationStep4(randomizedNodes)
        print("Doing Step 5")
        randomizedNodes = randomizationStep5(randomizedNodes)
        fullyCompletable = True #Todo Create logic for Kanto and fix the checker :P
        # print("Checking the seed....")
        # fullyCompletable = checkJohtoCompletability(randomizedNodes)

    return randomizedNodes

def checkForDoubles(inputLink, inputROM, warpLocations):
    if inputLink is links_and_nodes.johto_all_warp_points.Ruins_Of_Alph_Kabuto_Chamber_Links.RUINS_OF_ALPH_KABUTO_CHAMBER_TO_RUINS_OF_ALPH_INNER_CHAMBER_4_LINK:
        inputROM.seek(warpLocations[links_and_nodes.johto_all_warp_points.Ruins_Of_Alph_Kabuto_Item_Room_Links.RUINS_OF_ALPH_KABUTO_ITEM_ROOM_TO_RUINS_OF_ALPH_KABUTO_WORD_ROOM_1_LINK.value.MEMORY_ORIGIN]
                      +links_and_nodes.johto_all_warp_points.Ruins_Of_Alph_Kabuto_Item_Room_Links.RUINS_OF_ALPH_KABUTO_ITEM_ROOM_TO_RUINS_OF_ALPH_KABUTO_WORD_ROOM_1_LINK.value.OFFSET)
        inputROM.write(WarpInstruction.getInstruction(inputLink.value.LINK.value))
        inputROM.read(2)
        inputROM.write(WarpInstruction.getInstruction(inputLink.value.LINK.value))
        print("FOUND KABUTO NODE SO MAKING ITEM ROOM LINK BACK ALSO")

def randomizeROM(inputROM, settings):

    startTime = time.time()

    print("Randomizing Warps..")
    randomizedNodes = randomizeWarps()


    print("Writing New Warps to ROM...")
    rom = inputROM.read()
    lookupDict = AutomaticWarpLocator.getLookupDict()
    warpLocations = dict()
    for key in lookupDict.keys():

        foundLocation = rom.find(lookupDict[key])
        warpLocations[key] = foundLocation + 5

    for node in randomizedNodes:
        for link in node.value.LINKS:
            memLocation = warpLocations[link.value.MEMORY_ORIGIN] + link.value.OFFSET
            inputROM.seek(memLocation)
            inputROM.write(WarpInstruction.getInstruction(link.value.LINK.value))
            if link.value.DUAL_WIDTH is True:
                inputROM.read(2)
                inputROM.write(WarpInstruction.getInstruction(link.value.LINK.value))
            checkForDoubles(link, inputROM, warpLocations)
    randomizeTime = time.time() - startTime
    print("Time to randomize warps and write to ROM:", randomizeTime,"seconds")

    scriptLocations = buildMemoryLocationsFromSym(settings[0])
    if settings[1] == 1:
        print("\tEnabling Always Catchable Setting")
        memToSeekTo = (warpLocations["WhirlIslandLugiaChamber"] + 7)
        inputROM.seek(memToSeekTo)
        inputROM.write(bytes.fromhex(getHex(15)))
        inputROM.seek(scriptLocations["LugiaToggle"])
        inputROM.write(bytes.fromhex(getHex(18)))
        inputROM.seek(scriptLocations["HoOhToggle"])
        # if settings[1] == "Pokemon - Crystal Version 1.1":
        #     inputROM.write(bytes.fromhex(getHex(62)))
        # else:
        inputROM.write(bytes.fromhex(getHex(88)))

    if settings[3] == 1:
        disableDarkMode(inputROM, warpLocations)

    print("\tDisabling E4 Walking")
    inputROM.seek(scriptLocations["KogasRoom_EnterMovement"])
    inputROM.write(bytes.fromhex(getHex(71)))
    inputROM.seek(scriptLocations["KarensRoom_EnterMovement"])
    inputROM.write(bytes.fromhex(getHex(71)))
    inputROM.seek(scriptLocations["WillsRoom_EnterMovement"])
    inputROM.write(bytes.fromhex(getHex(71)))
    inputROM.seek(scriptLocations["BrunosRoom_EnterMovement"])
    inputROM.write(bytes.fromhex(getHex(71)))
    inputROM.seek(scriptLocations["LancesRoom_EnterMovement"])
    inputROM.write(bytes.fromhex(getHex(71)))

    print("\tOpening All E4 Doors")
    inputROM.seek(scriptLocations["KogasDoorLocksBehindYou"])
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek((scriptLocations["KarensDoorLocksBehindYou"]))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek((scriptLocations["WillsDoorLocksBehindYou"]))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek((scriptLocations["BrunosDoorLocksBehindYou"]))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek(scriptLocations["LancesDoorLocksBehindYou"])
    inputROM.read(1)
    inputROM.write(bytes.fromhex(getHex(49)))

    inputROM.seek(scriptLocations["KogasRoomDoors"])
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek((scriptLocations["KarensRoomDoors"]))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek((scriptLocations["WillsRoomDoors"]))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek((scriptLocations["BrunosRoomDoors"]))
    inputROM.write(bytes.fromhex(getHex(2)))
    inputROM.write(bytes.fromhex(getHex(22)))
    inputROM.seek(scriptLocations["LancesRoomDoors"])
    inputROM.read(1)
    inputROM.write(bytes.fromhex(getHex(49)))

    print("\tFixing Champions Room Tile Collision")
    inputROM.seek(scriptLocations["TilesetChampionsRoomColl"])
    inputROM.write(bytes.fromhex(getHex(112)))
    inputROM.write(bytes.fromhex(getHex(112)))


    print("\tMaking Aides Give Pokeballs")
    inputROM.seek(scriptLocations["AideScript_GivePotion"])
    inputROM.write(bytes.fromhex(getHex(5)))
    inputROM.write(bytes.fromhex(getHex(5)))

    print("\tUnlocking Basement without Keycard")
    inputROM.seek(scriptLocations['LockBasementDoor'])
    inputROM.write(bytes.fromhex(getHex(46)))

    print("\tMaking Director Always Appear in Underground Warehouse")
    inputROM.seek(warpLocations['GoldenrodUndergroundWarehouse'] + 66)
    inputROM.write(bytes.fromhex(getHex(255)))
    inputROM.write(bytes.fromhex(getHex(255)))
    print(hex(scriptLocations["DirectorKeycard"]))
    inputROM.seek(scriptLocations["DirectorKeycard"])
    inputROM.write(bytes.fromhex(getHex(0)))

    print("\tMaking starters lv100 for testing")
    inputROM.seek(scriptLocations["CyndaquilPokeBallScript"])
    inputROM.write(bytes.fromhex(getHex(100)))
    inputROM.seek(scriptLocations["TotodilePokeBallScript"])
    inputROM.write(bytes.fromhex(getHex(100)))
    inputROM.seek(scriptLocations["ChikoritaPokeBallScript"])
    inputROM.write(bytes.fromhex(getHex(100)))

    inputROM.close()

    return randomizedNodes

def disableDarkMode(inputROM, warpLocations):
    print(hex(warpLocations["DungeonsMapGroup"] +587)) #write 12, read 8, 9 times then read 35, then write, read 8, write, then read 72, write, read 8 , write
    inputROM.seek(warpLocations["DungeonsMapGroup"] +587)
    for i in range(9):
        inputROM.write(bytes.fromhex(getHex(18)))
        inputROM.read(8)
    inputROM.read(27)
    inputROM.write(bytes.fromhex(getHex(18)))
    inputROM.read(8)
    inputROM.write(bytes.fromhex(getHex(18)))
    inputROM.read(71)
    inputROM.write(bytes.fromhex(getHex(18)))
    inputROM.read(8)
    inputROM.write(bytes.fromhex(getHex(18)))