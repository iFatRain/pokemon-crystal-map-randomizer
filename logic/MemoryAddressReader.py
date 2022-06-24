import os, sys


def buildMemoryLocationsFromSym(detectedROMName):
    memoryMapWarps = dict()
    memoryMapScripts = dict()
    print(sys.executable)
    if detectedROMName == "Pokemon - Crystal Version 1.1":
        print("\nLoading Vanilla Scripts...")
        # file = os.path.join(os.path.dirname(os.path.realpath(__file__)),"vanilla.sym")
        file = os.path.join(os.path.dirname(sys.executable),"syms\\vanilla.sym")
    elif detectedROMName == "Pokemon - Crystal Speedchoice Version 7.2":
        print("\nLoading Speedchoice 7.2 Scripts...")
        # file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "crystal-speedchoice7.2.sym")
        file = os.path.join(os.path.dirname(sys.executable),"syms\\crystal-speedchoice7.2.sym")
    elif detectedROMName == "Pokemon - Crystal Speedchoice Version 7.31":
        print("\nLoading Speedchoice 7.31 Scripts...")
        # file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "crystal-speedchoice7.31.sym")
        file = os.path.join(os.path.dirname(sys.executable),"syms\\crystal-speedchoice7.31.sym")
    # else:
    #     file = "C:/Users/theje/PycharmProjects/pythonProject/logic/crystal-speedchoice7.2.sym"
    #     print("DIDN'T LOAD FULLY SUPPORTED ROM!!")

    with open(file, "r") as memLoc:

        for line in memLoc.read().splitlines():
            if "_MapEvents" in line:
                memInfo = line.split(" ")[0]
                mapName = line.split(" ")[1].split("_MapEvents")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]

                print("{} warp mem is at {}".format(mapName, hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000)))

                memoryMapWarps[mapName] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000

            if "GoldenrodUndergroundWarehouseDirectorScript" in line:
                if line.split(" ")[1] == "GoldenrodUndergroundWarehouseDirectorScript":
                    memInfo = line.split(" ")[0]
                    bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                    memoryMapScripts["DirectorKeycard"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 11
                    print("DIRECTORS BADGE CHECK IS AT ",hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 11))

            if "MapScripts.Lugia" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["LugiaToggle"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 12
                #print("LugiaToggle is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 12))

            if "sRoomDoors" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1].split(".")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 8
                #print(line.split(" ")[1].split(".")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 8))

            if "sRoom_EnterMovement" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000))
            # 14 offset for lance
            if "DoorLocksBehindYou" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1].split(".")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 13
                #print(line.split(" ")[1].split(".")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 13)) #technically its at 14 but we go back 1 to move which tile is changed

            if "LockBasementDoor" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1].split(".")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3
                #print(line.split(" ")[1].split(".")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "TilesetChampionsRoomColl" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 0xC6
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 0xC6))

            if "AideScript_GivePotion" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 6
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 6))

            if "AideScript_GivePotion" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 6
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 6))

            if "CyndaquilPokeBallScript" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49))

            if "TotodilePokeBallScript" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49))

            if "ChikoritaPokeBallScript" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49
                #print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49))

            if "Pokemon - Crystal Speedchoice" in detectedROMName:
                if "MapScripts.NoE4Check" in line:
                    memInfo = line.split(" ")[0]
                    bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                    memoryMapScripts["HoOhToggle"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 12
            else:
                if "MapScripts.HoOh" in line:
                    memInfo = line.split(" ")[0]
                    bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                    memoryMapScripts["HoOhToggle"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 12

            if "InitializeEventsScript" in line and "InitializeEventsScriptStdScript" not in line and "SkipDirector" not in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                if "Pokemon - Crystal Speedchoice" in detectedROMName:
                    memoryMapScripts["InitializeEventsScript"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 76
                    print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 76))
                else:
                    memoryMapScripts["InitializeEventsScript"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 73
                    print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 73))

            if "BlackthornCity_Blocks" in line and "Beta" not in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["BlackthornCity_Blocks"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "MountMortar2FInside_Blocks" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["MountMortar2FInside_Blocks"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 65

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 65))

            if "VermilionCity_Blocks" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["VermilionCity_Blocks"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 95

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 95))

            if "RuinsOfAlphOutside_Blocks" in line and "Beta" not in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["RuinsOfAlphOutside_Blocks"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 153

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 153))

            if "VictoryRoad_Blocks" in line and "Beta" not in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["VictoryRoad_Blocks"] = (int(bank, 16) * 0x4000) + int(address,16) - 0x4000 + 144

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 144))


            if "RuinsOfAlphKabutoChamber_MapScripts.FloorClosed" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["RuinsOfAlphKabutoChamber_MapScripts.FloorClosed"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "RuinsOfAlphHoOhChamber_MapScripts.FloorClosed" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["RuinsOfAlphHoOhChamber_MapScripts.FloorClosed"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "RuinsOfAlphOmanyteChamber_MapScripts.FloorClosed" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["RuinsOfAlphOmanyteChamber_MapScripts.FloorClosed"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "RuinsOfAlphAerodactylChamber_MapScripts.FloorClosed" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["RuinsOfAlphAerodactylChamber_MapScripts.FloorClosed"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "EcruteakGymClosed" in line and "EcruteakGymClosedText" not in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["EcruteakGymClosed"] = (int(bank,16) * 0x4000) + int(address, 16) - 0x4000 + 30

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 30))

            if "TrainerGruntM1.Script" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["TrainerGruntM1.Script"] = (int(bank,16) * 0x4000) + int(address, 16) - 0x4000 + 92

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 92))


            if "MountMoon_MapScripts.RivalEncounter" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["MountMoon_MapScripts.RivalEncounter"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 1

                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 1))

        memLoc.close() #memoryMapWarps,
    return memoryMapScripts