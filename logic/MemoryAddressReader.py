def buildMemoryLocationsFromSym(detectedROMName):
    memoryMapWarps = dict()
    memoryMapScripts = dict()

    if detectedROMName == "Pokemon - Crystal Version 1.1":
        print("Loading Vanilla Sym")
        file = "C:/Users/theje/PycharmProjects/pythonProject/logic/pokecrystal11.sym"  # Change this to hide path
    elif detectedROMName == "Pokemon - Crystal Speedchoice Version 7.2":
        print("Loading Speedchoice Sym")
        file = "C:/Users/theje/PycharmProjects/pythonProject/logic/crystal-speedchoice.sym"  # Change this to hide path
    # else:
    #     file = "C:/Users/theje/PycharmProjects/pythonProject/logic/crystal-speedchoice.sym"
    #     print("DIDN'T LOAD FULLY SUPPORTED ROM!!")

    with open(file, "r") as memLoc:
        for line in memLoc.read().splitlines():
            if "_MapEvents" in line:
                memInfo = line.split(" ")[0]
                mapName = line.split(" ")[1].split("_")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]

                print("{} warp mem is at {}".format(mapName, hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 0x5)))

                memoryMapWarps[mapName] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000

            if "MapScripts.Lugia" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts["LugiaToggle"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 12

            if "sRoomDoors" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1].split(".")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 8
                print(line.split(" ")[1].split(".")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 8))

            if "sRoom_EnterMovement" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000
                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000))
            # 14 offset for lance
            if "DoorLocksBehindYou" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1].split(".")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 13
                print(line.split(" ")[1].split(".")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 13)) #technically its at 14 but we go back 1 to move which tile is changed

            if "LockBasementDoor" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1].split(".")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3
                print(line.split(" ")[1].split(".")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 3))

            if "TilesetChampionsRoomColl" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 0xC6
                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 0xC6))

            if "AideScript_GivePotion" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 6
                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 6))

            if "AideScript_GivePotion" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 6
                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 6))

            if "CyndaquilPokeBallScript" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49
                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49))

            if "TotodilePokeBallScript" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49
                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49))

            if "ChikoritaPokeBallScript" in line:
                memInfo = line.split(" ")[0]
                bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                memoryMapScripts[line.split(" ")[1]] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49
                print(line.split(" ")[1], "is at", hex((int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 49))

            if detectedROMName == "Pokemon - Crystal Speedchoice Version 7.2":
                if "MapScripts.NoE4Check" in line:
                    memInfo = line.split(" ")[0]
                    bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                    memoryMapScripts["HoOhToggle"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 12
            else:
                if "MapScripts.HoOh" in line:
                    memInfo = line.split(" ")[0]
                    bank, address = memInfo.split(":")[0], memInfo.split(":")[1]
                    memoryMapScripts["HoOhToggle"] = (int(bank, 16) * 0x4000) + int(address, 16) - 0x4000 + 12




        memLoc.close()
    return memoryMapWarps, memoryMapScripts