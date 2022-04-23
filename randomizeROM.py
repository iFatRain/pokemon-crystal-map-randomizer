import time

import links_and_nodes.johto_all_warp_points
import links_and_nodes.johto_node_containers as Johto
import links_and_nodes.kanto_node_containers as Kanto
from logic import AutomaticWarpLocator
from logic.MemoryAddressReader import buildMemoryLocationsFromSym
from logic.NewRandomizerLogic import randomizationStep1, randomizationStep2, randomizationStep3, randomizationStep4, \
    checkJohtoCompletability, randomizationStep5
from class_definitions import WarpInstruction, getHex

def randomizeWarps(combinedRegions):
    print("Randomizing..")
    if combinedRegions:
        randomizedNodes = randomizationStep1(list(Johto.MajorNodes_Johto) + list(Kanto.MajorNodes_Kanto))
        randomizedNodes = randomizationStep2(randomizedNodes, list(Johto.HubNodes_Johto) + list(Kanto.HubNodes_Kanto))
        randomizedNodes = randomizationStep3(randomizedNodes,
                                             list(Johto.ImportantDeadEndNodes_Johto) + list(Kanto.ImportantDeadEndNodes_Kanto),
                                             list(Johto.ReachableUselessDeadEndNodes_Johto) + list(Kanto.ReachableUselessDeadEndNodes_Kanto),
                                             list(Johto.UnreachableUselessDeadEndNodes_Johto) + list(Kanto.UnreachableUselessDeadEndNodes_Kanto))
        randomizedNodes = randomizationStep4(randomizedNodes)
        randomizedNodes = randomizationStep5(randomizedNodes, list(Johto.TwoWayCorridorNodes_Johto) + list(Kanto.TwoWayCorridorNodes_Kanto))
    else:
        johtoFullyCompletable = False
        while johtoFullyCompletable is False:
            randomizedJohto = randomizationStep1(list(Johto.MajorNodes_Johto))
            randomizedJohto = randomizationStep2(randomizedJohto, list(Johto.HubNodes_Johto))
            randomizedJohto = randomizationStep3(randomizedJohto, list(Johto.ImportantDeadEndNodes_Johto),
                                                 list(Johto.ReachableUselessDeadEndNodes_Johto), list(Johto.UnreachableUselessDeadEndNodes_Johto))
            randomizedJohto = randomizationStep4(randomizedJohto)
            randomizedJohto = randomizationStep5(randomizedJohto, list(Johto.TwoWayCorridorNodes_Johto))
            johtoFullyCompletable = checkJohtoCompletability(randomizedJohto)

        # Now we randomize Kanto individually currently without checking
        randomizedKanto = randomizationStep1(list(Kanto.MajorNodes_Kanto))
        randomizedKanto = randomizationStep2(randomizedKanto, list(Kanto.HubNodes_Kanto))
        randomizedKanto = randomizationStep3(randomizedKanto, list(Kanto.ImportantDeadEndNodes_Kanto),
                                             list(Kanto.ReachableUselessDeadEndNodes_Kanto),
                                             list(Kanto.UnreachableUselessDeadEndNodes_Kanto))
        randomizedKanto = randomizationStep4(randomizedKanto)
        randomizedKanto = randomizationStep5(randomizedKanto, list(Kanto.TwoWayCorridorNodes_Kanto))

        randomizedNodes = randomizedJohto + randomizedKanto



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
    randomizedNodes = randomizeWarps(settings[2])


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

    if settings[5]:
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


    #Write IcePathFixes
    print("\t Making Rocks Always In Ice Path")
    inputROM.seek(warpLocations["IcePathB2FMahoganySide"] + 47)
    inputROM.write(bytes.fromhex(getHex(255)))
    inputROM.write(bytes.fromhex(getHex(255)))
    inputROM.read(11)
    inputROM.write(bytes.fromhex(getHex(255)))
    inputROM.write(bytes.fromhex(getHex(255)))
    inputROM.read(11)
    inputROM.write(bytes.fromhex(getHex(255)))
    inputROM.write(bytes.fromhex(getHex(255)))
    inputROM.read(11)
    inputROM.write(bytes.fromhex(getHex(255)))
    inputROM.write(bytes.fromhex(getHex(255)))
    print("\t Removing Rocks from Above")
    inputROM.seek(scriptLocations["InitializeEventsScript"])
    inputROM.write(bytes.fromhex(getHex(9)))
    inputROM.read(2)
    inputROM.write(bytes.fromhex(getHex(10)))
    inputROM.read(2)
    inputROM.write(bytes.fromhex(getHex(11)))
    inputROM.read(2)
    inputROM.write(bytes.fromhex(getHex(12)))


    if settings[4]:
        print("\t Blackthorn Map Block Changes")
        inputROM.seek(scriptLocations["BlackthornCity_Blocks"])
        inputROM.write(bytes.fromhex(getHex(111))) #6F
        inputROM.write(bytes.fromhex(getHex(114))) #72
        inputROM.write(bytes.fromhex(getHex(109)))
        inputROM.write(bytes.fromhex(getHex(113)))
        inputROM.write(bytes.fromhex(getHex(111)))  # 6F
        inputROM.write(bytes.fromhex(getHex(114))) #6C
        inputROM.read(14)
        inputROM.write(bytes.fromhex(getHex(105)))
        inputROM.read(4)
        inputROM.write(bytes.fromhex(getHex(2)))
        inputROM.write(bytes.fromhex(getHex(2)))
        inputROM.write(bytes.fromhex(getHex(2)))
        inputROM.write(bytes.fromhex(getHex(71))) #47
        inputROM.read(11)
        inputROM.write(bytes.fromhex(getHex(109))) #6D
        inputROM.write(bytes.fromhex(getHex(105)))
        inputROM.write(bytes.fromhex(getHex(2)))
        inputROM.write(bytes.fromhex(getHex(2)))
        inputROM.write(bytes.fromhex(getHex(2)))
        inputROM.write(bytes.fromhex(getHex(2)))
        inputROM.read(14)
        inputROM.write(bytes.fromhex(getHex(113)))
        inputROM.write(bytes.fromhex(getHex(105)))
        inputROM.write(bytes.fromhex(getHex(2))) #69
        inputROM.read(17)
        inputROM.write(bytes.fromhex(getHex(113)))
        inputROM.write(bytes.fromhex(getHex(105)))
        inputROM.write(bytes.fromhex(getHex(2)))
        inputROM.read(17)
        inputROM.write(bytes.fromhex(getHex(113)))  # 71
        inputROM.write(bytes.fromhex(getHex(105)))
        inputROM.write(bytes.fromhex(getHex(2)))  # 71
        inputROM.read(17)
        inputROM.write(bytes.fromhex(getHex(113)))  # 71
        inputROM.write(bytes.fromhex(getHex(105)))
        inputROM.write(bytes.fromhex(getHex(2)))  # 71
        inputROM.read(17)
        inputROM.write(bytes.fromhex(getHex(113)))  # 71
        inputROM.read(28)
        inputROM.write(bytes.fromhex(getHex(75)))  # 71
        inputROM.read(39)
        inputROM.write(bytes.fromhex(getHex(90)))  # 71
        inputROM.read(16)
        inputROM.write(bytes.fromhex(getHex(90)))  # 71
        inputROM.read(2)
        inputROM.write(bytes.fromhex(getHex(90)))  # 71

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