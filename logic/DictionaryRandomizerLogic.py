import os
import random
from class_definitions import Unlock_Keys, Node

#TODO ADD COMMENTED PROTOTYPES/available methods

def outputify(input):
    return str(input).split('.')[1].removesuffix('WP').replace('_',' ').title()

def validateNodeCounts(nodeToValidate):
    usedCount = 0
    for link in nodeToValidate[1].LINKS:
        if link.MODIFIED is True:
            usedCount += 1
    if usedCount != nodeToValidate[1].USED_LINKS:
        raise Exception("Inaccurate Used Links for ", nodeToValidate[0], ". expected: ", nodeToValidate[1].USED_LINKS, " found: ", usedCount)
    if nodeToValidate[1].TOTAL_LINKS != nodeToValidate[1].ORIGINAL_TOTAL:
        raise Exception("Somehow more links were added to ", nodeToValidate[0])

def getRandomNode(nodePool, excludedNode = None):
    checkedNodes = []

    # While we haven't checked each node keep searching for a random unused node
    while len(checkedNodes) != len(nodePool):

        sampleNode = random.choice(nodePool)  # Choose a random node from the nodePool

        if sampleNode in checkedNodes:
            continue  # If we have already checked this node, go back to get a new sample
        else:
            checkedNodes.append(sampleNode)  # Mark as checked by appending to our checkedNodes
            if excludedNode is not None:
                if sampleNode == excludedNode:
                    continue
                # Specific logic for making sure Radio Tower and Underground aren't placed in Goldenrod - Can be softlock without the setting
                # TODO EXPLORE OPTION TO TURN THIS OFF IF THE WANDERING ROCKETS IS ENABLED
                if excludedNode[0] == "Radio Tower 1F Node" or excludedNode == "Goldenrod Underground Warehouse Node": #TODO FIX THESE NODE NAMES, LIKELY INCORRECT
                    if sampleNode[0] == "Goldenrod City Node":
                        continue
            # If we find a node that has an open link, we return that node
            if sampleNode[1].USED_LINKS != sampleNode[1].TOTAL_LINKS:
                # Before we return the node, we want to validate that it's not had any unexpected modifications
                validateNodeCounts(sampleNode)
                return sampleNode
    return None  # This shouldn't ever happen because of the validation

def getRandomLink(inputNode):
    validateNodeCounts(inputNode)  # Before we do anything, make sure node is good to go
    checkedLinks = []
    if inputNode[1].USED_LINKS == inputNode[1].TOTAL_LINKS:
        return None  # This should never happen with validation elsewhere
    while len(checkedLinks) != inputNode[1].TOTAL_LINKS:
        sampleLink = random.choice(inputNode[1].LINKS)
        if sampleLink in checkedLinks:
            continue
        else:
            checkedLinks.append(sampleLink)
            if sampleLink.MODIFIED == False:
                markLinkAsUsed(sampleLink)
                Node.incrementUsedLinks(inputNode[1])  # Before we return this link to be used, we make it known as such
                return sampleLink
    return None  # Should never happen because validation elsewhere

def getRandomOverworldLink(inputNode):
    validateNodeCounts(inputNode)  # Before we do anything, make sure node is good to go
    checkedLinks = []
    if inputNode[1].USED_LINKS == inputNode[1].TOTAL_LINKS:
        return None  # This should never happen with validation elsewhere
    while len(checkedLinks) != inputNode[1].TOTAL_LINKS:
        sampleLink = random.choice(inputNode[1].LINKS)
        if sampleLink in checkedLinks:
            continue
        if sampleLink.LOCKED_BY is not None:
            continue
        else:
            checkedLinks.append(sampleLink)
            if sampleLink.MODIFIED == False:
                markLinkAsUsed(sampleLink)
                Node.incrementUsedLinks(inputNode[1])  # Before we return this link to be used, we make it known as such
                return sampleLink
    return None

def getUnusedNode(nodeList):
    checkedNodes = []
    while len(checkedNodes) != len(nodeList):
        sampleNode = random.choice(nodeList)
        if sampleNode in checkedNodes:
            continue
        else:
            checkedNodes.append(sampleNode)
            if sampleNode[1].USED_LINKS == 0:
                return sampleNode
    raise Exception("There was no unused node found in node list!")
    return None

# This method has no restrictions for node linking
def linkNodes(nodeA, nodeB):
    print("====Starting node linking====")
    print(nodeA, "<===>", nodeB)

    randomLinkA = getRandomLink(nodeA)
    randomLinkB = getRandomLink(nodeB)

    connectTwoLinks(randomLinkA, randomLinkB)

    Node.incrementUsedLinks(nodeA[1])
    Node.incrementUsedLinks(nodeB[1])

    return nodeA, nodeB

# This method has some logics to make sure overworld connections are never blocked by rockets in Goldenrod
def linkOverworldNodes(nodeA, nodeB):
    print("\t",nodeA[0],"<===>", nodeB[0])

    # Specific logic to make sure that Goldenrod's overworld connections don't become locked behind rocket
    # if nodeA[0] == "Goldenrod_City_Node":
    #     print("GOLDENROD CITY NODE A")
    #     # randomLinkA = getRandomLinkOnlyIncluding(nodeA,
    #     #     [links_and_nodes.johto_all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_ROUTE_35_GOLDENROD_GATE_LINK,
    #     #      links_and_nodes.johto_all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_GYM_LINK,
    #     #      links_and_nodes.johto_all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_POKECENTER_1F_LINK,
    #     #      links_and_nodes.johto_all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_DEPT_STORE_1F_LINK,
    #     #      links_and_nodes.johto_all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_RADIO_TOWER_1F_LINK,
    #     #      links_and_nodes.johto_all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_MAGNET_TRAIN_STATION_LINK])
    #     # randomLinkB = getRandomOverworldLink(nodeB)
    # elif nodeB[0] == "Goldenrod_City_Node":
    #     print("GOLDENROD CITY NODE B")
        # randomLinkA = getRandomOverworldLink(nodeA)
        # randomLinkB = getRandomLinkOnlyIncluding(nodeB,
        #     [links_and_nodes.johto_all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_ROUTE_35_GOLDENROD_GATE_LINK,
        #      links_and_nodes.johto_all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_GYM_LINK,
        #      links_and_nodes.johto_all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_POKECENTER_1F_LINK,
        #      links_and_nodes.johto_all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_DEPT_STORE_1F_LINK,
        #      links_and_nodes.johto_all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_RADIO_TOWER_1F_LINK,
        #      links_and_nodes.johto_all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_MAGNET_TRAIN_STATION_LINK])

    # else:
    randomLinkA = getRandomOverworldLink(nodeA)
    randomLinkB = getRandomOverworldLink(nodeB)

    connectTwoLinks(randomLinkA,randomLinkB)

    return nodeA, nodeB

def markLinkAsUsed(inputLink):
    inputLink.MODIFIED = True
    inputLink.OWN.USED = True

def insertCorridorBetweenLinks(corridorToInsert, linkA, linkB):
    entrancePoint = getRandomLink(corridorToInsert)
    exitPoint = getRandomLink(corridorToInsert)
    connectTwoLinks(linkA, entrancePoint)
    connectTwoLinks(linkB, exitPoint)
    print("\t Corridor Layout --> [",outputify(linkA.OWN),"<===>",outputify(entrancePoint.OWN), "]   [", outputify(exitPoint.OWN),"<===>", outputify(linkB.OWN),"]")


def findConnectedLink(randomizedNodes, linkA):
    for destinationNode in randomizedNodes:
        for reverseLink in destinationNode[1].LINKS:
            if reverseLink.OWN == linkA.LINK and reverseLink.MODIFIED:
                return reverseLink
    raise Exception("The connected link for ", outputify(linkA.OWN), " was not found!")
    return None

def connectTwoLinks(linkA, linkB):
    print("Connecting [", outputify(linkA.OWN),outputify(linkB.OWN),"]")
    linkA.LINK = linkB.OWN
    linkB.LINK = linkA.OWN

def getAvailableLinkCount(randomizedNodes):
    available = 0
    for node in randomizedNodes:
        available += node[1].TOTAL_LINKS - node[1].USED_LINKS
    return available

def randomizationStep1(nodeGroups):
    # Step 1 links the Major Nodes Directly (Cities + Their Walkable Overworld)

    unconnectedNodes = list(nodeGroups.items())

    print("\n====Starting Overworld linking====\n")
    # From our major nodes, we randomly select one to begin linking
    randomStart = random.choice(unconnectedNodes)
    unconnectedNodes.pop(unconnectedNodes.index(randomStart))
    connectedNodes = [randomStart]

    # While we still have unconnected Major Nodes, we want to continue to connect
    while len(unconnectedNodes) != 0:

        # We randomly select an already connected node to pair with an unconnected node
        nodeA = getRandomNode(connectedNodes)
        nodeB = getRandomNode(unconnectedNodes)

        # Link the two nodes together
        linkOverworldNodes(nodeA,nodeB)

        # Place the newly connected node into the connected list
        unconnectedNodes.pop(unconnectedNodes.index(nodeB))
        connectedNodes.append(nodeB)
    return connectedNodes

def randomizationStep2(randomizedNodes, nodeGroups):

    print("\n Inserting Hubs\n")
    hubNodes = list(nodeGroups.items())
    changedLinks = []

    # For each Overworld node, check the links to find which ones have the Overworld connection
    for sourceNode in randomizedNodes:
        for forwardLink in sourceNode[1].LINKS:
            if forwardLink.MODIFIED is True and forwardLink not in changedLinks:

                linkA = forwardLink
                linkB = findConnectedLink(randomizedNodes,linkA)
                unusedHubNode = getUnusedNode(hubNodes)
                # In this case, we're treating the hubs like corridors
                insertCorridorBetweenLinks(unusedHubNode,linkA, linkB)

                # Put the newly changed links into the list
                changedLinks.append(linkA)
                changedLinks.append(linkB)

                hubNodes.pop(hubNodes.index(unusedHubNode))
                randomizedNodes.append(unusedHubNode)

                for node in randomizedNodes:
                    validateNodeCounts(node)
                # If we run out of hub nodes to place, this step is done
                if len(hubNodes) == 0:
                    return randomizedNodes


# def placeDeadend():
#     deadEndNode = getRandomNode(deadEnds)
#     linkA = deadEndNode[1].LINKS[0]
#     if linkA.MODIFIED == False:
#         markLinkAsUsed(linkA)
#         Node.incrementUsedLinks(deadEndNode[1])
#     destinationNode = getRandomNode(randomizedNodes, deadEndNode)
#     linkB = getRandomLink(destinationNode)
#     connectTwoLinks(linkA, linkB)
#     randomizedNodes.append(deadEndNode)
#     deadEnds.pop(deadEnds.index(deadEndNode))


def randomizationStep3(randomizedNodes, important, reachableUseless, unreachableUseless):

#TODO Clean up duplication of the 3 stages of step 3
    available = getAvailableLinkCount(randomizedNodes)
    deadEnds = list(important.items())

    print("\nPlacing Dead Ends\n")
    while len(deadEnds) != 0:

        deadEndNode = getRandomNode(deadEnds)
        linkA = getRandomLink(deadEndNode)
        destinationNode = getRandomNode(randomizedNodes, deadEndNode)
        linkB = getRandomLink(destinationNode)
        connectTwoLinks(linkA,linkB)
        randomizedNodes.append(deadEndNode)
        deadEnds.pop(deadEnds.index(deadEndNode))

        available -= 1
        print("\t", outputify(linkA.OWN), "<===>", outputify(linkB.OWN), "There are still", available, "links left and ", len(deadEnds),"remaining IMPORTANT deadEnds")
        if available == 0:
            return randomizedNodes
    for node in randomizedNodes:
        validateNodeCounts(node)

    print("Doing the Reachable")
    deadEnds = list(reachableUseless.items())


    while len(deadEnds) != 0:

        deadEndNode = getRandomNode(deadEnds)
        linkA = getRandomLink(deadEndNode)
        destinationNode = getRandomNode(randomizedNodes, deadEndNode)
        linkB = getRandomLink(destinationNode)
        connectTwoLinks(linkA, linkB)
        randomizedNodes.append(deadEndNode)
        deadEnds.pop(deadEnds.index(deadEndNode))

        available -= 1
        print("\t", outputify(linkA.OWN), "<===>", outputify(linkB.OWN), "There are still", available, "links left and ", len(deadEnds),"remaining reachable deadEnds")
        if available == 0:
            return randomizedNodes

    for node in randomizedNodes:
        validateNodeCounts(node)

    print("Doing the Unreachable")
    deadEnds = list(unreachableUseless.items())
    while len(deadEnds) != 0:

        deadEndNode = getRandomNode(deadEnds)
        linkA = getRandomLink(deadEndNode)
        destinationNode = getRandomNode(randomizedNodes, deadEndNode)
        linkB = getRandomLink(destinationNode)
        connectTwoLinks(linkA, linkB)
        randomizedNodes.append(deadEndNode)
        deadEnds.pop(deadEnds.index(deadEndNode))

        available -= 1
        print("\t", outputify(linkA.OWN), "<===>", outputify(linkB.OWN), "There are still", available, "links left and ", len(deadEnds),"remaining  useless deadEnds")
        if len(deadEnds) == 1 and available % 2 == 0:
            return randomizedNodes
        if available == 0:
            return randomizedNodes

    return randomizedNodes

def randomizationStep4(randomizedNodes):
    print("\nThese are unlinked Nodes\n")
    unchangedLinks = []
    for node in randomizedNodes:
        validateNodeCounts(node)
        for link in node[1].LINKS:
            if link.MODIFIED is False:
                unchangedLinks.append(link)

    for link in unchangedLinks:
        print("\t",outputify(link.LINK))

    while len(unchangedLinks) > 1:
        linkA = getRandomLinkFromList(unchangedLinks)
        linkB = getRandomLinkFromList(unchangedLinks)

        connectTwoLinks(linkA,linkB)
        unchangedLinks.remove(linkA)
        unchangedLinks.remove(linkB)

    return randomizedNodes

def randomizationStep5(randomizedNodes, corridorInputList):
    corridorNodes = list(corridorInputList.items())

    print("\nInserting Corridors\n")
    while len(corridorNodes) != 0:

        linkA = random.choice(random.choice(randomizedNodes)[1].LINKS)  # This will randomly grab ANY link ignoring usage/modification
        linkB = findConnectedLink(randomizedNodes, linkA)
        randomCorridor = getRandomNode(corridorNodes)

        insertCorridorBetweenLinks(randomCorridor, linkA, linkB)

        corridorNodes.pop(corridorNodes.index(randomCorridor))
        randomizedNodes.append(randomCorridor)

    return randomizedNodes

def getRandomLinkFromList(inputList):
    while True:
        sampleLink = random.choice(inputList)
        if sampleLink.MODIFIED == False:
            sampleLink.MODIFIED = True
            sampleLink.USED = True
            return sampleLink

def checkJohtoCompletability(randomizedNodes):


    print("Starting Johto Check")
    nodesToCheck = list(randomizedNodes)

    completableSeed = False
    obtainedKeys = []
    lockedLinks = []
    alreadyExploredLinks = []
    toBeExploredLinks = []
    fullyUnlockedNodes = []
    stuckCount = 0

    badgeList = [Unlock_Keys.BADGE_1,
                 Unlock_Keys.BADGE_2,
                 Unlock_Keys.BADGE_3,
                 Unlock_Keys.BADGE_4,
                 Unlock_Keys.BADGE_5,
                 Unlock_Keys.BADGE_6,
                 Unlock_Keys.BADGE_7,
                 Unlock_Keys.BADGE_8,
                ]
    listOfHM = [Unlock_Keys.HM_CUT,
                Unlock_Keys.HM_FLY,
                Unlock_Keys.HM_SURF,
                Unlock_Keys.HM_STRENGTH,
                Unlock_Keys.HM_FLASH,
                Unlock_Keys.HM_WATERFALL,
                Unlock_Keys.HM_WHIRLPOOL]

    explorableNodes = [node for node in nodesToCheck if node[0] == "New Bark and Cherrygrove Node"]
    print("Explorable!:", explorableNodes)
    nodesToCheck.remove(explorableNodes[0])
    #
    # while completableSeed
    # print("There are ",len(nodesToCheck), "to check in total")

    while len(explorableNodes) != 0:
        for node in list(explorableNodes):
            # print(node)
            # for additionalLink in node.LINKS:
                # if additionalLink not in alreadyExploredLinks:
                    # print("      with a new link to ==>",additionalLink)
            for link in node[1].LINKS:
                if link not in alreadyExploredLinks:
                    if link.LOCKED_BY is None:
                        print(link, "was unlocked so we're going to explore it")
                        alreadyExploredLinks.append(link)
                        toBeExploredLinks.append(link.LINK)
                        if link.UNLOCKS is not None:

                            for key in link.UNLOCKS:
                                if key not in obtainedKeys:
                                    print("We got ",key,"after visiting from",link.LINK)
                                    obtainedKeys.append(key)

                    else:
                        # print("\n",link,"was locked...")
                        if all(neededKey in obtainedKeys for neededKey in link.LOCKED_BY):
                            # print("    ... but we have all the keys!!")
                            # print("    ... now we can visit", link.LINK)
                            # print("    ... and we should have key(s)",link.UNLOCKS)
                            alreadyExploredLinks.append(link)
                            toBeExploredLinks.append(link.LINK)

                            if link in lockedLinks:
                                lockedLinks.remove(link)
                                explorableNodes[explorableNodes.index(node)][1].HAS_LOCKED = False
                            if link.UNLOCKS is not None:
                                for key in link.UNLOCKS:
                                    if key not in obtainedKeys:
                                        # print("We got ", key, "from an unlocked link")
                                        obtainedKeys.append(key)
                        else:
                            # print("   ... and we don't have the needed keys yet")
                            if link not in lockedLinks:
                                lockedLinks.append(link)
                                explorableNodes[explorableNodes.index(node)][1].HAS_LOCKED = True
                                # print(node,"Has a locked enterance")

        print("\n-------Status Report -------")
        obtainedBadges = []
        for key in obtainedKeys:
            if key in badgeList:
                obtainedBadges.append(key)
        print("So far I have",len(obtainedBadges),"badges.")
        if len(obtainedBadges) >= 7:
            if Unlock_Keys.HAS_7_BADGES not in obtainedKeys:
                obtainedKeys.append(Unlock_Keys.HAS_7_BADGES)

        if len(obtainedBadges) == 8 and all(neededHM in obtainedKeys for neededHM in listOfHM) and Unlock_Keys.VICTORY_ROAD_GATE_ACCESS and Unlock_Keys.GYM_BATTLE_8:
            completableSeed = True


        for node in list(explorableNodes):
            if node[1].HAS_LOCKED is False:
                fullyUnlockedNodes.append(node)
                explorableNodes.remove(node)

        newNodes = 0
        for node in list(nodesToCheck):
            for link in node[1].LINKS:
                if link.OWN in toBeExploredLinks:
                    if node not in explorableNodes:
                        explorableNodes.append(node)

        for node in explorableNodes:
            if node in list(nodesToCheck):
                newNodes += 1
                nodesToCheck.remove(node)

        obtainedKeys = checkForAdditionalKeys(obtainedKeys)

        for key in obtainedKeys:
            print("Currently I have", key)

        if newNodes == 0:
            print("Adding to stuck count: ",stuckCount+1)
            stuckCount += 1
            if stuckCount > 6:
                break

        # print("Total nodes unlocked = ",len(fullyUnlockedNodes))
        # print("Nodes not yet checked:", len(nodesToCheck))
        print()


    # for node in fullyUnlockedNodes:
        # print("These are all unlocked nodes:", node)

    for key in obtainedKeys:
        print("I obtained: ", key)

    for key in Unlock_Keys:
        if key not in obtainedKeys:
            print("I couldn't ever get", key)

    # for link in lockedLinks:
    #     print("This is locked:",link, " [hides]===>",link.LINK)
    # print()
    # print()
    if completableSeed:
        print("This seed is completable!!!")
    else:
        print("RESETTING NODE LIST TO DEFAULT LINKS")
        for node in randomizedNodes:
            node[1].USED_LINKS = 0
            for link in node[1].LINKS:
                link.LINK.USED = False
                link.LINK = link.DEFAULT_LINK
                link.LINK.USED = False
                link.OWN.USED = False
                link.MODIFIED = False
        print("-ERROR- -ERROR- -ERROR- CANT COMPLETE THE SEED -ERROR- -ERROR- -ERROR-")

    allItemsObtainable = all(key in obtainedKeys for key in Unlock_Keys)
    if allItemsObtainable:
        print("   AND I CAN GET ALL ITEMS")

    return completableSeed

def checkKantoCompletability(randomizedNodes):


    print("Starting Kanto Check")

    nodesToCheck = list(randomizedNodes)

    completableSeed = False
    obtainedKeys = [Unlock_Keys.CAN_SURF_OR_CUT, Unlock_Keys.RADIO_CARD]
    lockedLinks = []
    alreadyExploredLinks = []
    toBeExploredLinks = []
    fullyUnlockedNodes = []
    stuckCount = 0

    badgeList = [Unlock_Keys.BADGE_9,
                 Unlock_Keys.BADGE_10,
                 Unlock_Keys.BADGE_11,
                 Unlock_Keys.BADGE_12,
                 Unlock_Keys.BADGE_13,
                 Unlock_Keys.BADGE_14,
                 Unlock_Keys.BADGE_15,
                 Unlock_Keys.BADGE_16]

    explorableNodes = [node for node in nodesToCheck if node[0] == "Vermilion City Node" or node[0] == "Victory Road Gate Kanto Node"]
    for node in explorableNodes:
        nodesToCheck.remove(node)
    #
    # while completableSeed
    # print("There are ",len(nodesToCheck), "to check in total")

    while len(explorableNodes) != 0:
        print("We've gotta explore these:",explorableNodes)
        for node in list(explorableNodes):
            print(node)
            for additionalLink in node[1].LINKS:
                if additionalLink not in alreadyExploredLinks:
                    print("      with a new link to ==>",additionalLink)
            for link in node[1].LINKS:
                if link not in alreadyExploredLinks:
                    if link.LOCKED_BY is None:
                        print(link, "was unlocked so we're going to explore it")
                        alreadyExploredLinks.append(link)
                        toBeExploredLinks.append(link.LINK)
                        if link.UNLOCKS is not None:

                            for key in link.UNLOCKS:
                                if key not in obtainedKeys:
                                    print("We got ",key,"after visiting from",link.LINK)
                                    obtainedKeys.append(key)

                    else:
                        print("\n",link,"was locked...")
                        if all(neededKey in obtainedKeys for neededKey in link.LOCKED_BY):
                            print("    ... but we have all the keys!!")
                            print("    ... now we can visit", link.LINK)
                            print("    ... and we should have key(s)",link.UNLOCKS)
                            alreadyExploredLinks.append(link)
                            toBeExploredLinks.append(link.LINK)

                            if link in lockedLinks:
                                lockedLinks.remove(link)
                                explorableNodes[explorableNodes.index(node)][1].HAS_LOCKED = False
                            if link.UNLOCKS is not None:
                                for key in link.UNLOCKS:
                                    if key not in obtainedKeys:
                                        print("We got ", key, "from an unlocked link")
                                        obtainedKeys.append(key)
                        else:
                            # print("   ... and we don't have the needed keys yet")
                            if link not in lockedLinks:
                                lockedLinks.append(link)
                                explorableNodes[explorableNodes.index(node)][1].HAS_LOCKED = True
                                # print(node,"Has a locked enterance")

        print("\n-------Status Report -------")
        obtainedBadges = []
        for key in obtainedKeys:
            if key in badgeList:
                obtainedBadges.append(key)
        print("So far I have",len(obtainedBadges)," Kanto badges.")
        if len(obtainedBadges) == 8:
            if Unlock_Keys.HAS_ALL_KANTO_BADGES not in obtainedKeys:
                obtainedKeys.append(Unlock_Keys.HAS_ALL_KANTO_BADGES)

        if len(obtainedBadges) == 8 and Unlock_Keys.OAKS_LAB_ACCESS in obtainedKeys:
            completableSeed = True


        for node in list(explorableNodes):
            if node[1].HAS_LOCKED is False:
                fullyUnlockedNodes.append(node)
                explorableNodes.remove(node)

        newNodes = 0
        for node in list(nodesToCheck):
            for link in node[1].LINKS:
                if link.OWN in toBeExploredLinks:
                    if node not in explorableNodes:
                        explorableNodes.append(node)

        for node in explorableNodes:
            if node in list(nodesToCheck):
                newNodes += 1
                nodesToCheck.remove(node)

        obtainedKeys = checkForAdditionalKantoKeys(obtainedKeys)

        for key in obtainedKeys:
            print("Currently I have", key)

        if newNodes == 0:
            print("Adding to stuck count: ",stuckCount+1)
            stuckCount += 1
            if stuckCount > 6:
                print("I'm breaking now")
                break

        # print("Total nodes unlocked = ",len(fullyUnlockedNodes))
        # print("Nodes not yet checked:", len(nodesToCheck))
        print()


    # for node in fullyUnlockedNodes:
        # print("These are all unlocked nodes:", node)

    for key in obtainedKeys:
        print("I obtained: ", key)

    for key in Unlock_Keys:
        if key not in obtainedKeys:
            print("I couldn't ever get", key)

    for link in lockedLinks:
        print("This is locked:",link, " [hides]===>",link.LINK)
    # print()
    # print()
    if completableSeed:
        print("This seed is completable!!!")
    else:
        print("RESETTING NODE LIST TO DEFAULT LINKS")
        for node in randomizedNodes:
            node[1].USED_LINKS = 0
            for link in node[1].LINKS:
                link.LINK.USED = False
                link.LINK = link.DEFAULT_LINK
                link.LINK.USED = False
                link.OWN.USED = False
                link.MODIFIED = False
        print("-ERROR- -ERROR- -ERROR- CANT COMPLETE THE SEED -ERROR- -ERROR- -ERROR-")

    allItemsObtainable = all(key in obtainedKeys for key in Unlock_Keys)
    if allItemsObtainable:
        print("   AND I CAN GET ALL ITEMS")

    return completableSeed

def checkFullCompletability(randomizedNodes):

    nodesToCheck = list(randomizedNodes)

    completableSeed = False
    obtainedKeys = []
    lockedLinks = []
    alreadyExploredLinks = []
    toBeExploredLinks = []
    fullyUnlockedNodes = []
    stuckCount = 0

    badgeList = [Unlock_Keys.BADGE_1,
                 Unlock_Keys.BADGE_2,
                 Unlock_Keys.BADGE_3,
                 Unlock_Keys.BADGE_4,
                 Unlock_Keys.BADGE_5,
                 Unlock_Keys.BADGE_6,
                 Unlock_Keys.BADGE_7,
                 Unlock_Keys.BADGE_8,
                 Unlock_Keys.BADGE_9,
                 Unlock_Keys.BADGE_10,
                 Unlock_Keys.BADGE_11,
                 Unlock_Keys.BADGE_12,
                 Unlock_Keys.BADGE_13,
                 Unlock_Keys.BADGE_14,
                 Unlock_Keys.BADGE_15,
                 Unlock_Keys.BADGE_16

                ]
    listOfHM = [Unlock_Keys.HM_CUT,
                Unlock_Keys.HM_FLY,
                Unlock_Keys.HM_SURF,
                Unlock_Keys.HM_STRENGTH,
                Unlock_Keys.HM_FLASH,
                Unlock_Keys.HM_WATERFALL,
                Unlock_Keys.HM_WHIRLPOOL]

    explorableNodes = [node for node in nodesToCheck if node[0] == "New Bark and Cherrygrove Node"]
    print(explorableNodes)

    nodesToCheck.remove(explorableNodes[0])
    #
    # while completableSeed
    # print("There are ",len(nodesToCheck), "to check in total")

    while len(explorableNodes) != 0:
        for node in list(explorableNodes):
            # print(node)
            # for additionalLink in node.LINKS:
                # if additionalLink not in alreadyExploredLinks:
                    # print("      with a new link to ==>",additionalLink)
            for link in node[1].LINKS:
                if link not in alreadyExploredLinks:
                    if link.LOCKED_BY is None:
                        # print(link, "was unlocked so we're going to explore it")
                        alreadyExploredLinks.append(link)
                        toBeExploredLinks.append(link.LINK)
                        if link.UNLOCKS is not None:

                            for key in link.UNLOCKS:
                                if key not in obtainedKeys:
                                    print("We got ",key,"after visiting from",link.LINK)
                                    obtainedKeys.append(key)

                    else:
                        print("\n",link.OWN,"was locked...")
                        if all(neededKey in obtainedKeys for neededKey in link.LOCKED_BY):
                            # print("    ... but we have all the keys!!")
                            # print("    ... now we can visit", link.LINK)
                            # print("    ... and we should have key(s)",link.UNLOCKS)
                            alreadyExploredLinks.append(link)
                            toBeExploredLinks.append(link.LINK)

                            if link in lockedLinks:
                                lockedLinks.remove(link)
                                explorableNodes[explorableNodes.index(node)][1].HAS_LOCKED = False
                            if link.UNLOCKS is not None:
                                for key in link.UNLOCKS:
                                    if key not in obtainedKeys:
                                        # print("We got ", key, "from an unlocked link")
                                        obtainedKeys.append(key)
                        else:
                            print("   ... and we don't have the needed keys yet")
                            if link not in lockedLinks:
                                lockedLinks.append(link)
                                explorableNodes[explorableNodes.index(node)][1].HAS_LOCKED = True
                                # print(node,"Has a locked enterance")

        print("\n-------Status Report -------")
        obtainedBadges = []
        for key in obtainedKeys:
            if key in badgeList:
                obtainedBadges.append(key)
        print("So far I have",len(obtainedBadges),"badges.")
        if len(obtainedBadges) >= 7:
            if Unlock_Keys.HAS_7_BADGES not in obtainedKeys:
                obtainedKeys.append(Unlock_Keys.HAS_7_BADGES)

        if len(obtainedBadges) == 16 and all(neededHM in obtainedKeys for neededHM in listOfHM) and Unlock_Keys.VICTORY_ROAD_GATE_ACCESS and Unlock_Keys.GYM_BATTLE_8 in obtainedKeys:
            completableSeed = True


        for node in list(explorableNodes):
            if node[1].HAS_LOCKED is False:
                fullyUnlockedNodes.append(node)
                explorableNodes.remove(node)

        newNodes = 0
        for node in list(nodesToCheck):
            for link in node[1].LINKS:
                if link.OWN in toBeExploredLinks:
                    if node not in explorableNodes:
                        explorableNodes.append(node)

        for node in explorableNodes:
            if node in list(nodesToCheck):
                newNodes += 1
                nodesToCheck.remove(node)

        obtainedKeys = checkForAdditionalKeys(obtainedKeys)
        obtainedKeys = checkForAdditionalKantoKeys(obtainedKeys)

        for key in obtainedKeys:
            print("Currently I have", key)

        if newNodes == 0:
            print("Adding to stuck count: ",stuckCount+1)
            stuckCount += 1
            if stuckCount > 6:
                break

        print("Total nodes unlocked = ",len(fullyUnlockedNodes))
        print("Nodes not yet checked:", len(nodesToCheck))
        print()


    # for node in fullyUnlockedNodes:
        # print("These are all unlocked nodes:", node)

    for key in obtainedKeys:
        print("I obtained: ", key)

    for key in Unlock_Keys:
        if key not in obtainedKeys:
            print("I couldn't ever get", key)

    for link in lockedLinks:
        print("This is locked:",link.OWN, " [hides]===>",link.LINK)
    print()
    print()
    if completableSeed:
        print("This seed is completable!!!")
    else:
        print("RESETTING NODE LIST TO DEFAULT LINKS")
        for node in randomizedNodes:
            node[1].USED_LINKS = 0
            for link in node[1].LINKS:
                link.LINK.USED = False
                link.LINK = link.DEFAULT_LINK
                link.LINK.USED = False
                link.OWN.USED = False
                link.MODIFIED = False
        print("-ERROR- -ERROR- -ERROR- CANT COMPLETE THE SEED -ERROR- -ERROR- -ERROR-")
        print("-ERROR- -ERROR- -ERROR- CANT COMPLETE THE SEED -ERROR- -ERROR- -ERROR-")
        print("-ERROR- -ERROR- -ERROR- CANT COMPLETE THE SEED -ERROR- -ERROR- -ERROR-")
        print("-ERROR- -ERROR- -ERROR- CANT COMPLETE THE SEED -ERROR- -ERROR- -ERROR-")
        print("-ERROR- -ERROR- -ERROR- CANT COMPLETE THE SEED -ERROR- -ERROR- -ERROR-")



    allItemsObtainable = all(key in obtainedKeys for key in Unlock_Keys)
    if allItemsObtainable:
        print("   AND I CAN GET ALL ITEMS")

    return completableSeed

def checkForAdditionalKeys(obtainedKeys):
    obtainedKeys = checkForDualRequirements(Unlock_Keys.TOP_OF_LIGHTHOUSE_FOUND,
                             Unlock_Keys.CIANNWOOD_PHARMACY_FOUND,
                             obtainedKeys, Unlock_Keys.OLIVINE_MEDICINE)

    obtainedKeys = checkForDualRequirements(Unlock_Keys.KURTS_HOUSE_FOUND,
                             Unlock_Keys.SLOWPOKE_WELL_FOUND,
                             obtainedKeys, Unlock_Keys.CAN_CLEAR_SLOWPOKE_WELL)

    obtainedKeys = checkForDualRequirements(Unlock_Keys.HM_STRENGTH,
                                            Unlock_Keys.BADGE_3,
                                            obtainedKeys, Unlock_Keys.CAN_USE_STRENGTH)

    obtainedKeys = checkForDualRequirements(Unlock_Keys.HM_SURF,
                                            Unlock_Keys.BADGE_4,
                                            obtainedKeys, Unlock_Keys.CAN_SURF)

    obtainedKeys = checkForDualRequirements(Unlock_Keys.HM_CUT,
                                            Unlock_Keys.BADGE_2,
                                            obtainedKeys, Unlock_Keys.CAN_CUT)
    obtainedKeys = checkForDualRequirements(Unlock_Keys.FOUND_CIANWOOD,
                                            Unlock_Keys.BADGE_5,
                                            obtainedKeys, Unlock_Keys.HM_FLY)

    if Unlock_Keys.CAN_CUT in obtainedKeys or Unlock_Keys.CAN_SURF in obtainedKeys:
        if Unlock_Keys.CAN_SURF_OR_CUT not in obtainedKeys:
            print("I can surf or cut KEKW")
            obtainedKeys.append(Unlock_Keys.CAN_SURF_OR_CUT)


    return obtainedKeys

def checkForAdditionalKantoKeys(obtainedKeys):
    obtainedKeys = checkForDualRequirements(Unlock_Keys.POWER_PLANT_ACCESS,
                             Unlock_Keys.CERULEAN_GYM_ACCESS,
                             obtainedKeys, Unlock_Keys.MACHINE_PART)

    if Unlock_Keys.MACHINE_PART in obtainedKeys:
        print("We've got machine part, we should award badge 11 now!")
        if Unlock_Keys.BADGE_11 not in obtainedKeys:
            print("Adding Badge 11")
            obtainedKeys.append(Unlock_Keys.BADGE_11)

    return obtainedKeys

def checkForDualRequirements(firstKey, secondKey, keyList, keyToGive):
    if firstKey in keyList and secondKey in keyList:
        if keyToGive not in keyList:
            keyList.append(keyToGive)
    return keyList

# from links_and_nodes.johto_node_dictionary_containers import buildJohtoMajorNodes, buildJohtoHubs, buildJohtoImportantDeadEnds, buildJohtoReachableDeadEnds, buildJohtoUselessDeadEnds, buildJohtoCorridors
# from links_and_nodes.kanto_node_dictionary_containers import buildKantoMajorNodes, buildKantoHubNodes, buildKantoImportantDeadEnds, buildKantoUselessDeadEnds, buildKantoCorridors
# unrandomMart = False
# combinedFullyCompletable = False
# while not combinedFullyCompletable:
#     randomizedNodes = randomizationStep1(dict(**buildJohtoMajorNodes(unrandomMart),**buildKantoMajorNodes()))
#     randomizedNodes = randomizationStep2(randomizedNodes, dict(**buildJohtoHubs(),**buildKantoHubNodes()))
#     randomizedNodes = randomizationStep3(randomizedNodes,
#                                          dict(**buildJohtoImportantDeadEnds(unrandomMart),**buildKantoImportantDeadEnds()),
#                                          dict(**buildJohtoReachableDeadEnds()),
#                                          dict(**buildJohtoUselessDeadEnds(),**buildKantoUselessDeadEnds()))
#     randomizedNodes = randomizationStep4(randomizedNodes)
#     randomizedNodes = randomizationStep5(randomizedNodes, dict(**buildJohtoCorridors(),**buildKantoCorridors()))
#     combinedFullyCompletable = checkFullCompletability(randomizedNodes)
#
# print(combinedFullyCompletable)

# completable = False
# # fullyCompletable = False
# while not completable:
#     randomizedNodes = randomizationStep1()
#     randomizedNodes = randomizationStep2(randomizedNodes)
#     randomizedNodes = randomizationStep3(randomizedNodes)
#     randomizedNodes = randomizationStep4(randomizedNodes)
#     randomizedNodes = randomizationStep5(randomizedNodes)
#     print("\n"*40)
#     completable = checkJohtoCompletability(list(randomizedNodes))
# #
# randomizedNodes = randomizationStep1()
# randomizedNodes = randomizationStep2(randomizedNodes)
# randomizedNodes = randomizationStep3(randomizedNodes)
# randomizedNodes = randomizationStep4(randomizedNodes)
# randomizedNodes = randomizationStep5(randomizedNodes)
