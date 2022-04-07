import os
import random

import links_and_nodes.all_warp_points
from class_definitions import Unlock_Keys, Node
from links_and_nodes.node_containers import MajorNodes, UselessDeadEndNodes, ImportantDeadEndNodes, TwoWayCorridorNodes, HubNodes
from logic.MemoryAddressReader import buildMemoryLocationsFromSym


def getRandomNode(nodeList, excludedNode = None):
    checkedNodes = []

    # While we haven't checked each node keep searching for a random unused node
    while len(checkedNodes) != len(nodeList):

        sampleNode = random.choice(nodeList)
        if sampleNode in checkedNodes:
            continue
        else:
            checkedNodes.append(sampleNode)
            if sampleNode == excludedNode:
                continue
                # Specific logic for making sure Radio Tower and Underground aren't placed in Goldenrod
            if excludedNode == links_and_nodes.node_containers.ImportantDeadEndNodes.Radio_Tower_1F_Node or  excludedNode == links_and_nodes.node_containers.TwoWayCorridorNodes.Goldenrod_Underground_Warehouse_Node:
                if sampleNode == links_and_nodes.node_containers.MajorNodes.Goldenrod_City_Node:
                    continue
            # If we find a node that has an open link, we return that node
            if sampleNode.value.USED_LINKS != sampleNode.value.TOTAL_LINKS:
                return sampleNode
    return None


def getRandomLinkOnlyIncluding(inputNode, inclusionList):
    while True:
        # print("Looking for a random link from",inputNode)
        sampleLink = random.choice(inputNode.value.LINKS)
        if sampleLink not in inclusionList:
            continue
        if sampleLink.value.MODIFIED == False:
            if sampleLink.value.OWN.value.USED == True:
                print("THIS LINKS VALUE HAS ALREADY BEEN USED")
            sampleLink.value.MODIFIED = True
            sampleLink.value.OWN.value.USED = True
            return sampleLink


def getRandomLink(inputNode):
    checkedLinks = []
    if inputNode.value.USED_LINKS == inputNode.value.TOTAL_LINKS:
        return None
    while len(checkedLinks) != inputNode.value.TOTAL_LINKS:
        sampleLink = random.choice(inputNode.value.LINKS)
        if sampleLink in checkedLinks:
            continue
        else:
            checkedLinks.append(sampleLink)
            if sampleLink.value.MODIFIED == False:
                markLinkAsUsed(sampleLink)
                return sampleLink
    return None


def getRandomNodeIgnoringUsage(nodeList):
    sampleNode = random.choice(nodeList)
    return sampleNode



def getRandomLinkIgnoreUsage(inputNode):
        sampleLink = random.choice(inputNode.value.LINKS)
        return sampleLink

def getUnusedNode(nodeList):
    checkedNodes = []
    while len(checkedNodes) != len(nodeList):
        sampleNode = random.choice(nodeList)
        if sampleNode in checkedNodes:
            continue
        else:
            checkedNodes.append(sampleNode)
            if sampleNode.value.USED_LINKS == 0:
                return sampleNode
    return None

# This method has no restrictions for node linking
def linkNodes(nodeA, nodeB):
    print("====Starting node linking====")
    print(nodeA, "<===>", nodeB)

    randomLinkA = getRandomLink(nodeA)
    randomLinkB = getRandomLink(nodeB)

    connectTwoLinks(randomLinkA, randomLinkB)

    Node.incrementUsedLinks(nodeA.value)
    Node.incrementUsedLinks(nodeB.value)

    return nodeA, nodeB

# This method has some logics to make sure overworld connections are never blocked by rockets in Goldenrod
def linkOverworldNodes(nodeA, nodeB):
    print("\t",nodeA,"<===>", nodeB)

    # Specific logic to make sure that Goldenrod's overworld connections don't become locked behind rocket
    if nodeA is MajorNodes.Goldenrod_City_Node:
        randomLinkA = getRandomLinkOnlyIncluding(nodeA,
            [links_and_nodes.all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_ROUTE_35_GOLDENROD_GATE_LINK,
             links_and_nodes.all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_GYM_LINK,
             links_and_nodes.all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_POKECENTER_1F_LINK,
             links_and_nodes.all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_DEPT_STORE_1F_LINK,
             links_and_nodes.all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_RADIO_TOWER_1F_LINK,
             links_and_nodes.all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_MAGNET_TRAIN_STATION_LINK])
        randomLinkB = getRandomLink(nodeB)
    elif nodeB is MajorNodes.Goldenrod_City_Node:
        randomLinkA = getRandomLink(nodeA)
        randomLinkB = getRandomLinkOnlyIncluding(nodeB,
            [links_and_nodes.all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_ROUTE_35_GOLDENROD_GATE_LINK,
             links_and_nodes.all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_GYM_LINK,
             links_and_nodes.all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_POKECENTER_1F_LINK,
             links_and_nodes.all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_DEPT_STORE_1F_LINK,
             links_and_nodes.all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_RADIO_TOWER_1F_LINK,
             links_and_nodes.all_warp_points.Goldenrod_City_Links.GOLDENROD_CITY_TO_GOLDENROD_MAGNET_TRAIN_STATION_LINK])

    else:
        randomLinkA = getRandomLink(nodeA)
        randomLinkB = getRandomLink(nodeB)

    connectTwoLinks(randomLinkA,randomLinkB)

    Node.incrementUsedLinks(nodeA.value)
    Node.incrementUsedLinks(nodeB.value)

    return nodeA, nodeB

def markLinkAsUsed(inputLink):
    inputLink.value.MODIFIED = True
    inputLink.value.OWN.value.USED = True

def insertCorridorBetweenLinks(corridorToInsert, linkA, linkB):
    enterancePoint = getRandomLink(corridorToInsert)
    exitPoint = getRandomLink(corridorToInsert)

    connectTwoLinks(linkA, enterancePoint)
    connectTwoLinks(linkB,exitPoint)

    print("\t[",linkA,"<===>",enterancePoint, "]   [", exitPoint,"<===>", linkB,"]")


def findConnectedLink(randomizedNodes, linkA):
    for destinationNode in randomizedNodes:
        for reverseLink in destinationNode.value.LINKS:
            if reverseLink.value.OWN == linkA.value.LINK and reverseLink.value.MODIFIED:
                linkB = reverseLink
                return linkB



def randomizationStep1():
    # Step 1 links the Major Nodes Directly (Cities + Their Walkable Overworld)

    unconnectedNodes = list(MajorNodes)

    # From our major nodes, we randomly select one to begin linking
    randomStart = random.choice(unconnectedNodes)
    unconnectedNodes.pop(unconnectedNodes.index(randomStart))
    connectedNodes = [randomStart]

    # While we still have unconnected Major Nodes, we want to continue to connect
    print("\n====Starting Overworld linking====\n")
    while len(unconnectedNodes) != 0:

        # We randomly select an already connected node to pair with an unconnected node
        nodeA = getRandomNode(connectedNodes)
        nodeB = getRandomNode(unconnectedNodes)

        # Link the two nodes together
        nodeA, nodeB = linkOverworldNodes(nodeA,nodeB)

        # Place the newly connected node into the connected list
        unconnectedNodes.pop(unconnectedNodes.index(nodeB))
        connectedNodes.append(nodeB)

    return connectedNodes



def randomizationStep2(randomizedNodes):

    print("\n Inserting Hubs\n")
    hubNodes = list(HubNodes)
    changedLinks = []

    # For each Overworld node, check the links to find which ones have the Overworld connection
    for sourceNode in randomizedNodes:
        for forwardLink in sourceNode.value.LINKS:
            if forwardLink.value.MODIFIED and forwardLink not in changedLinks:

                linkA = forwardLink
                linkB = findConnectedLink(randomizedNodes,linkA)
                unusedHubNode = getUnusedNode(hubNodes)
                # In this case, we're treating the hubs like corridors
                insertCorridorBetweenLinks(unusedHubNode,linkA, linkB)

                # Put the newly changed links into the list
                changedLinks.append(linkA)
                changedLinks.append(linkB)

                Node.incrementUsedLinks(unusedHubNode.value, 2)
                hubNodes.pop(hubNodes.index(unusedHubNode))
                randomizedNodes.append(unusedHubNode)

                # If we run out of hub nodes to place, this step is done
                if len(hubNodes) == 0:
                    return randomizedNodes

def connectTwoLinks(linkA, linkB):
    linkA.value.LINK = linkB.value.OWN
    linkB.value.LINK = linkA.value.OWN
    markLinkAsUsed(linkA)
    markLinkAsUsed(linkB)


def getAvailableLinkCount(randomizedNodes):
    available = 0
    for node in randomizedNodes:
        available += node.value.TOTAL_LINKS - node.value.USED_LINKS
    return available

def randomizationStep3(randomizedNodes):


    available = getAvailableLinkCount(randomizedNodes)
    deadEnds = list(ImportantDeadEndNodes)

    print("\nPlacing Dead Ends\n")
    while len(deadEnds) != 0:

        deadEndNode = getRandomNode(deadEnds)
        linkA = deadEndNode.value.LINKS[0]
        destinationNode = getRandomNode(randomizedNodes, deadEndNode)
        linkB = getRandomLink(destinationNode)


        connectTwoLinks(linkA,linkB)
        Node.incrementUsedLinks(deadEndNode.value)
        Node.incrementUsedLinks(destinationNode.value)

        randomizedNodes.append(deadEndNode)
        deadEnds.pop(deadEnds.index(deadEndNode))

        print("\t",linkA,"<===>",linkB)
        if available == 0:
            return randomizedNodes

    deadEnds = list(UselessDeadEndNodes)

    while len(deadEnds) != 0:

        deadEndNode = getRandomNode(deadEnds)
        linkA = deadEndNode.value.LINKS[0]
        destinationNode = getRandomNode(randomizedNodes)
        linkB = getRandomLink(destinationNode)

        connectTwoLinks(linkA, linkB)
        Node.incrementUsedLinks(deadEndNode.value)
        Node.incrementUsedLinks(destinationNode.value)

        randomizedNodes.append(deadEndNode)
        deadEnds.pop(deadEnds.index(deadEndNode))

        available -= 1
        print("\t",linkA,"<===>",linkB)
        if available == 0:
            return randomizedNodes

    return randomizedNodes



def randomizationStep4(randomizedNodes):
    corridorNodes = list(TwoWayCorridorNodes)

    print("\nInserting Corridors\n")
    while len(corridorNodes) != 0:

        randomTarget = getRandomNodeIgnoringUsage(randomizedNodes)
        linkA = getRandomLinkIgnoreUsage(randomTarget)
        linkB = findConnectedLink(randomizedNodes, linkA)
        randomCorridor = getRandomNode(corridorNodes)

        insertCorridorBetweenLinks(randomCorridor, linkA, linkB)

        Node.incrementUsedLinks(randomCorridor.value, 2)
        corridorNodes.pop(corridorNodes.index(randomCorridor))
        randomizedNodes.append(randomCorridor)


    # Resetting Nodes In case of re-randomization
    # for node in randomizedNodes:
    #     node.value.USED_LINKS = 0
    #     for link in node.value.LINKS:
    #         link.value.MODIFIED = False
    #         link.value.OWN.value.USED = False
    #         link.value.LINK.value.USED = False

    return randomizedNodes

def getRandomLinkFromList(inputList):
    while True:
        sampleLink = random.choice(inputList)
        if sampleLink.value.MODIFIED == False:
            if sampleLink.value.OWN.value.USED == True:
                print("THIS LINKS VALUE HAS ALREADY BEEN USED")
            sampleLink.value.MODIFIED = True
            sampleLink.value.OWN.value.USED = True
            print("Returning ", sampleLink)
            return sampleLink

def randomizationStep5(randomizedNodes):
    print("\nThese are unlinked Nodes\n")
    unchangedLinks = []
    for node in randomizedNodes:
        for link in node.value.LINKS:
            if link.value.MODIFIED is False:
                unchangedLinks.append(link)

    for link in unchangedLinks:
        print("\t",link)

    print("Getting first random unlinked")
    linkA = getRandomLinkFromList(unchangedLinks)
    print("Getting second random unlinked")
    linkB = getRandomLinkFromList(unchangedLinks)

    connectTwoLinks(linkA,linkB)


    return randomizedNodes


def checkSeedCompletability(randomizedNodes):

    nodesToCheck = list(randomizedNodes)

    completableSeed = False
    obtainedKeys = []
    lockedLinks = []
    alreadyExploredLinks = []
    toBeExploredLinks = []
    fullyUnlockedNodes = []
    stuckCount = 0

    print("There are ",len(nodesToCheck), "to check in total")

    badgeList = [Unlock_Keys.BADGE_1,
                 Unlock_Keys.BADGE_2,
                 Unlock_Keys.BADGE_3,
                 Unlock_Keys.BADGE_4,
                 Unlock_Keys.BADGE_5,
                 Unlock_Keys.BADGE_6,
                 Unlock_Keys.BADGE_7,
                 Unlock_Keys.BADGE_8,
                ]

    explorableNodes = [node for node in nodesToCheck if node is MajorNodes.New_Bark_Town_Node]
    nodesToCheck.pop(nodesToCheck.index(MajorNodes.New_Bark_Town_Node))
    #
    # while completableSeed

    while len(explorableNodes) != 0:
        for node in list(explorableNodes):
            print(node)
            for additionalLink in node.value.LINKS:
                if additionalLink not in alreadyExploredLinks:
                    print("      with a new link to ==>",additionalLink)
            for link in node.value.LINKS:
                if link not in alreadyExploredLinks:
                    if link.value.LOCKED_BY is None:
                        # print(link, "was unlocked so we're going to explore it")
                        alreadyExploredLinks.append(link)
                        toBeExploredLinks.append(link.value.LINK)
                        if link.value.UNLOCKS is not None:

                            for key in link.value.UNLOCKS:
                                if key not in obtainedKeys:
                                    print("We got ",key,"after visiting from",link.value.LINK)
                                    obtainedKeys.append(key)

                    else:
                        print("\n",link,"was locked...")
                        if all(neededKey in obtainedKeys for neededKey in link.value.LOCKED_BY):
                            print("    ... but we have all the keys!!")
                            print("    ... now we can visit", link.value.LINK)
                            print("    ... and we should have key(s)",link.value.UNLOCKS)
                            alreadyExploredLinks.append(link)
                            toBeExploredLinks.append(link.value.LINK)

                            if link in lockedLinks:
                                lockedLinks.remove(link)
                                explorableNodes[explorableNodes.index(node)].value.HAS_LOCKED = False
                            if link.value.UNLOCKS is not None:
                                for key in link.value.UNLOCKS:
                                    if key not in obtainedKeys:
                                        print("We got ", key, "from an unlocked link")
                                        obtainedKeys.append(key)
                        else:
                            print("   ... and we don't have the needed keys yet")
                            if link not in lockedLinks:
                                lockedLinks.append(link)
                                explorableNodes[explorableNodes.index(node)].value.HAS_LOCKED = True
                                # print(node,"Has a locked enterance")

        obtainedBadges = []
        for key in obtainedKeys:
            if key in badgeList:
                obtainedBadges.append(key)
        print("So far I have",len(obtainedBadges),"badges.")
        if len(obtainedBadges) >= 7:
            if Unlock_Keys.HAS_7_BADGES not in obtainedKeys:
                obtainedKeys.append(Unlock_Keys.HAS_7_BADGES)
        if len(obtainedBadges) == 8 and Unlock_Keys.HM_SURF in obtainedKeys:
            completableSeed = True

        for node in list(explorableNodes):
            if node.value.HAS_LOCKED is False:
                fullyUnlockedNodes.append(node)
                explorableNodes.remove(node)

        newNodes = 0
        for node in list(nodesToCheck):
            for link in node.value.LINKS:
                if link.value.OWN in toBeExploredLinks:
                    if node not in explorableNodes:
                        explorableNodes.append(node)

        for node in explorableNodes:
            if node in list(nodesToCheck):
                newNodes += 1
                nodesToCheck.remove(node)


        if newNodes == 0:
            print("Adding to stuck count: ",stuckCount+1)
            stuckCount += 1;
            if stuckCount > 6:
                break;

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
        print("This is locked:",link, " [hides]===>",link.value.LINK)
    print()
    print()
    if completableSeed:
        print("This seed is completable!!!")
    else:
        print("RESETTING NODE LIST TO DEFAULT LINKS")
        for node in randomizedNodes:
            node.value.USED_LINKS = 0
            for link in node.value.LINKS:
                link.value.LINK.value.USED = False
                link.value.LINK = link.value.DEFAULT_LINK
                link.value.LINK.value.USED = False
                link.value.OWN.value.USED = False
                link.value.MODIFIED = False



        print("-ERROR- -ERROR- -ERROR- CANT COMPLETE THE SEED -ERROR- -ERROR- -ERROR-")

    allItemsObtainable = all(key in obtainedKeys for key in Unlock_Keys)
    if allItemsObtainable:
        print("   AND I CAN GET ALL ITEMS")

    return completableSeed, allItemsObtainable


# completable = False
# fullyCompletable = False
# while not completable:
#     print("\n"*40)
#     randomizedNodes = randomizationStep1()
#     randomizedNodes = randomizationStep2(randomizedNodes)
#     randomizedNodes = randomizationStep3(randomizedNodes)
#     randomizedNodes = randomizationStep4(randomizedNodes)
#     completable, fullyCompletable = checkSeedCompletability(list(randomizedNodes))
# #
# randomizedNodes = randomizationStep1()
# randomizedNodes = randomizationStep2(randomizedNodes)
# randomizedNodes = randomizationStep3(randomizedNodes)
# randomizedNodes = randomizationStep4(randomizedNodes)
# randomizedNodes = randomizationStep5(randomizedNodes)
