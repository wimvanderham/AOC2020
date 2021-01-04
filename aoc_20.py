# Day 20 - Putting the tiles together
#
import math
from collections import deque

import time

start = time.time()

counter = 0
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_20.txt"
input_file = open(filename)

# Solutions
p1 = 0
p2 = 0

# Global Variables
tiles = {}
tile = {}
section = "title"
numberoftiles = 0
max_x = 0
max_y = 0
start_x = 0
start_y = 0
max_max_x = 0
max_max_y = 0
finaltiles = {}
finaltile = {}

# Functions

def printtile(tile):
    for y in range(max_y):
        line = ""
        for x in range(max_x):
            bit = (x,y)
            line = line + str(tile[bit])
        print line

def printFinalTile(finaltile):
    count_x = 0
    for y in range(max_max_y):
        line = ""
        for x in range(max_max_x):
            bit = (x,y)
            line = line + str(finaltile[bit])
            if finaltile[bit] == "#":
                count_x += 1
        print line
    #print "Number of #'s:", count_x
    return count_x

def printtiles(tileIDlist, start_x, start_y, max_max_x, max_max_y):
    # Print list of tiles without borders
    for y in range(1, max_y - 1):
        start_x = 0
        line = ""
        for tileID in tileIDlist:
            tile = tiles[tileID]
            for x in range(1, max_x - 1):
                bit = (x,y)
                line = line + str(tile[bit])
                finalbit = (start_x + x - 1, start_y + y - 1)
                if (start_x + x) > max_max_x:
                    max_max_x = (start_x + x)
                #print finalbit, tile[bit]
                finaltile[finalbit] = str(tile[bit])
            start_x += max_x - 2
        if (start_y + y) > max_max_y:
            max_max_y = (start_y + y)
        print line
    start_y += max_y - 2
    return start_x, start_y, max_max_x, max_max_y

# Function to rotate the matrix
# 90 degree clockwise
def rotateTile(tile):
    newtile = tile
    for y in range(max_x // 2):
        for x in range(y, max_y - y - 1):
            temp = tile[(x, y)]
            newtile[(x,y)] = tile[(max_y - 1 - y, x)]
            newtile[(max_y - 1 - y, x)] = tile[(max_x - 1 - x, max_y - 1 - y)]
            newtile[(max_x - 1 - x, max_y - 1 - y)] = tile[(y, max_x - 1 - x)]
            newtile[(y, max_x - 1 - x)] = temp
    
    return newtile

def flipTile(tile):
    newtile = {}
    for x in range(max_x):
        for y in range(max_y):
            newtile[(max_x - 1 - x, y)] = tile[(x,y)]
    return newtile

def flipFinalTile(finaltile):
    newfinaltile = {}
    for x in range(max_max_x):
        for y in range(max_max_y):
            newfinaltile[(max_max_x - 1 - x, y)] = finaltile[(x,y)]
    return newfinaltile

def rotateFinalTile(finaltile):
    newfinaltile = finaltile
    for y in range(max_max_x // 2):
        for x in range(y, max_max_y - y - 1):
            temp = finaltile[(x, y)]
            newfinaltile[(x,y)] = finaltile[(max_max_y - 1 - y, x)]
            newfinaltile[(max_max_y - 1 - y, x)] = finaltile[(max_max_x - 1 - x, max_max_y - 1 - y)]
            newfinaltile[(max_max_x - 1 - x, max_max_y - 1 - y)] = finaltile[(y, max_max_x - 1 - x)]
            newfinaltile[(y, max_max_x - 1 - x)] = temp
    
    return newfinaltile
 
def getBorders(tile):
    # Borders are:
    # +-----U------+
    # | .##.#..#.# |
    # | #.##.....# |
    # | ...#..#... |
    # | ....##..## |
    # L ###....### R
    # | ##..#..#.# |
    # | #...#....# |
    # | ..#....#.. |
    # | ...#.....# |
    # | #.#..#.#.. |
    # +-----D------+
    borders = {}
    whichone = ""
    for y in [0, max_y - 1]:
        if y == 0:
            whichone = "U"
            bitstring = ""
            for x in range(max_x):
                if tile[(x, y)] == "#":
                    bitstring += "1"
                else:
                    bitstring += "0"
            borders[whichone] = int(bitstring, 2)
        else:
            whichone = "D"
            bitstring = ""
            for x in range(max_x):
                if tile[(x, y)] == "#":
                    bitstring += "1"
                else:
                    bitstring += "0"
            borders[whichone] = int(bitstring, 2)
    for x in [0, max_x - 1]:
        bitstring = ""
        if x == 0:
            whichone = "L"
            bitstring = ""
            for y in range(max_y):
                if tile[(x,y)] == "#":
                    bitstring += "1"
                else:
                    bitstring += "0"
            borders[whichone] = int(bitstring, 2)
        else:
            whichone = "R"
            for y in range(max_y):
                if tile[(x,y)] == "#":
                    bitstring += "1"
                else:
                    bitstring += "0"
            borders[whichone] = int(bitstring, 2)
    return borders

# Count lines in file to determine EOF
num_lines = sum(1 for line in input_file)
print "Input file has:", num_lines, "lines"

input_file = open(filename)
EOF = False

x = 0
y = 0
tileID = 0

# Read All Input lines
for line in input_file:
    # Read input lines
    counter += 1

    line = line.strip()

    #print counter, line
    if counter == num_lines:
        EOF = True

    if section == "title":
        tileID = int (line.split(" ")[1][:-1])
        section = "tile"
        y = 0
        tile = {}
        continue
    
    if section == "tile":
        if line == "":
            # Finished reading this tile
            section = "title"
            max_y = y
            # Store base value as TileID * 100
            tiles[tileID * 100] = dict(tile)
            numberoftiles += 1
            #print numberoftiles, tileID
            for trans in range(7):
                # Create 7 transitions
                newtile = dict(rotateTile(tile))
                tiles[tileID * 100 + 1 + trans] = newtile
                if trans == 2:
                    # After first 3, flip the tile
                    tile = dict(flipTile(newtile))
                else:
                    tile = dict(newtile)
        else:
            # Continue reading lines belonging to tile
            x = 0
            for bit in line:
                tile[(x,y)] = bit
                x += 1

            max_x = x

            y += 1


#printtile(tile)
#printtiles([370900, 203900])

# END of # Read input lines
    
# Part 1: 
print "Part 1"

# Determine for each tile their border "value" and add to global dictionary
tileborders = {}

counter = 0
for tileID in tiles.keys():
    counter += 1
    borders = {}
    #print counter, "/", len(tiles.keys()), "Tile", str(tileID) + ":"
    #printtile (tiles[tileID])
    borders = getBorders(tiles[tileID])
    #if tileID // 100 == 1427 or tileID // 100 == 2311:
    #print "Tile", tileID, "Borders:", borders
    for border in borders.keys():
        whereused = (tileID, border)
        bordervalue = borders[border]
        if bordervalue in tileborders:
            list_ = tileborders[bordervalue]
            list_.append(whereused)
        else:
            list_ = [whereused]
        tileborders[bordervalue] = list_
        
# At this point we have all bordervalues ordered in tileborders dictionary
couple = {"L": "R", "R": "L", "U": "D", "D": "U"}
couples = []

for bordervalue in sorted(tileborders.keys()):
    #if len(tileborders[bordervalue]) == 2:
    #    print bordervalue, tileborders[bordervalue]
    # Search for tiles that can be connected
    subborderlist = []
    for tile1 in range(len(tileborders[bordervalue]) - 1):
        (tileID1, borderside1) = tileborders[bordervalue][tile1]
        baseID1 = tileID1 // 100
        if baseID1 not in subborderlist:
            subborderlist.append(baseID1)
        for tile2 in range(tile1, len(tileborders[bordervalue])):
            (tileID2, borderside2) = tileborders[bordervalue][tile2]
            baseID2 = tileID2 // 100
            if baseID1 == baseID2:
                continue
            if baseID2 not in subborderlist:
                subborderlist.append(baseID2)
            if couple[borderside1] == borderside2:
                if [(tileID1,borderside1), (tileID2, borderside2)] not in couples:
                    couples.append([(tileID1,borderside1), (tileID2, borderside2)])
                    #print "Found couple:", (tileID1, borderside1), "=", (tileID2, borderside2)
    #print "Bordervalue:", bordervalue, subborderlist
                
    #print "Side:", borderside
    #print "Tile", str(tileID) + ":"
    #printtile (tiles[tileID])
    #break

print "Found:", numberoftiles, "tiles"

centralpieces = []
connectpieces = {}
for tileID in tiles.keys():
    countsides = 0
    for side in ["L", "R", "D", "U"]:
        left = (tileID, side)
        for couplelist in couples:
            if left in couplelist:
                countsides += 1

    if countsides in connectpieces:
        list_ = connectpieces[countsides]
        baseID = tileID // 100
        if not baseID in list_:
            list_.append(baseID)
    else:
        baseID = tileID // 100
        list_ = [baseID]
    connectpieces[countsides] = list_

finalgrid = {}
usedtiles = []

numberofcols = int(math.sqrt(numberoftiles))
numberofrows = numberofcols

for countsides in sorted(connectpieces.keys()):
    #print countsides, connectpieces[countsides]
    if countsides == 2:
        p1 = 1
        for tileID in connectpieces[countsides]:
            p1 *= tileID


end = time.time()

print "Found solution to Part 1 in:", end - start, "seconds"

# Part 2: 
# Construct finalgrid by putting the pieces together respecting the transformation and border values
for row in range(numberofrows):
    for col in range(numberofcols):
        #print "Col:", col, "Row:", row
        if (col,row) in finalgrid:
            #print finalgrid[(col, row)]
            continue

        if col == 0 and (row == 0 or row == numberofrows - 1):
            #print "Case: if col == 0 and (row == 0 or row == numberofrows - 1):"
            if row == 0:
                #print "Case: if row == 0:"
                # Select a corner without U and L borders
                tileFound = False
                for baseID in connectpieces[2]:
                    if baseID in usedtiles:
                        continue
                    for transformation in range(8):
                        countUp   = 0
                        countLeft = 0
                        tileOption = baseID * 100 + transformation
                        borders = getBorders(tiles[tileOption])
                        for border in borders.keys():
                            for couplelist in couples:
                                if (tileOption, "U") in couplelist:
                                    countUp += 1
                                if (tileOption, "L") in couplelist:
                                    countLeft += 1
                        if countUp == 0 and countLeft == 0:
                            finalgrid[(col, row)] = tileOption
                            tileFound = True
                            #print "------> Col", col, "Row", row, "Tile:", tileOption
                            usedtiles.append(tileOption // 100)
                            break
                    if tileFound:
                        break
            else:
                #print "Case: else: # Row == numberofrows - 1"
                # Select a corner without D and L borders and under upTile
                upTile = finalgrid[(col, row - 1)]
                tileFound = False
                for baseID in connectpieces[2]:
                    #print "Checking:", baseID
                    if baseID in usedtiles:
                        #print "Already used"
                        continue
                    for transformation in range(8):
                        countDown = 0
                        countLeft = 0
                        coupleOK  = False
                        tileOption = baseID * 100 + transformation
                        borders = getBorders(tiles[tileOption])
                        for couplelist in couples:
                            if (tileOption, "D") in couplelist:
                                countDown += 1
                            if (tileOption, "L") in couplelist:
                                countLeft += 1
                            if (tileOption, "U") in couplelist:
                                #print "Valid option?", couplelist,
                                if (upTile, "D") in couplelist:
                                    coupleOK = True
                                    #print "Yes"
                                #else:
                                    #print "No"
                        if countDown == 0 and countLeft == 0 and coupleOK == True:
                            finalgrid[(col, row)] = tileOption
                            tileFound = True
                            #print "------> Col", col, "Row", row, "Tile:", tileOption
                            usedtiles.append(tileOption // 100)
                            break
                    if tileFound:
                        break
            continue
        
        if col > 0 and col < numberofcols - 1:
            #print "Case: if col > 0 and col < numberofcols - 1:"
            if row == 0 or row == numberofrows - 1:
                #print "Case: if row == 0 or row == numberofrows - 1:"
                # External rows
                lefttile = finalgrid[(col - 1, row)]
                #print "Search for tile on the right of this one:", lefttile
                tileFound = False
                # Middle pieces on external rows require three connections
                for baseID in connectpieces[3]:
                    #print "Checking:", baseID
                    if baseID in usedtiles:
                        #print "Already used"
                        continue
                    for transformation in range(8):
                        countUp   = 0
                        countDown = 0
                        coupleOK  = False
                        tileOption = baseID * 100 + transformation
                        for couplelist in couples:
                            if (tileOption, "U") in couplelist:
                                countUp += 1
                            if (tileOption, "D") in couplelist:
                                countDown += 1
                            if (tileOption, "L") in couplelist:
                                #print "Valid option?", couplelist,
                                if (lefttile, "R") in couplelist:
                                    coupleOK = True
                                    #print "Yes"
                                #else:
                                    #print "No"
                        if row == 0:
                            if countUp == 0 and coupleOK == True:
                                finalgrid[(col, row)] = tileOption
                                tileFound = True
                                #print "------> Col", col, "Row", row, "Tile:", tileOption
                                usedtiles.append(tileOption // 100)
                                break
                        else:
                            if countDown == 0 and coupleOK == True:
                                finalgrid[(col, row)] = tileOption
                                tileFound = True
                                #print "------> Col", col, "Row", row, "Tile:", tileOption
                                usedtiles.append(tileOption // 100)
                                break
                    if tileFound:
                        break
                continue
            else:
                # Internal rows
                #print "Case: # Internal rows"
                lefttile = finalgrid[(col - 1, row)]
                uptile   = finalgrid[(col, row - 1)]
                #print "Search for middle tile on the right of this one:", lefttile
                coupleOK = False
                # Middle pieces on internal rows require four connections
                for baseID in connectpieces[4]:
                    #print "Checking:", baseID
                    if baseID in usedtiles:
                        #print "Already used"
                        continue
                    for transformation in range(8):
                        leftOK = False
                        upOK   = False
                        tileOption = baseID * 100 + transformation
                        #print "Transformation:", tileOption
                        for couplelist in couples:
                            if (tileOption, "L") in couplelist:
                                #print "Valid option?", couplelist,
                                if (lefttile, "R") in couplelist:
                                    leftOK = True
                                    #print "Yes"
                                #else:
                                    #print "No"
                            if (tileOption, "U") in couplelist:
                                #print "Valid option?", couplelist,
                                if (uptile, "D") in couplelist:
                                    upOK = True
                                    #print "Yes"
                                #else:
                                    #print "No"
                        if leftOK == True:
                            #and upOK == True:
                            finalgrid[(col, row)] = tileOption
                            coupleOK = True
                            #print "------> Col", col, "Row", row, "Tile:", tileOption
                            usedtiles.append(tileOption // 100)
                            break
                    if coupleOK == True:
                        break
                continue
                
        if (col == numberofcols - 1) and (row == 0 or row == numberofrows - 1):
            if row == 0:
                lefttile = finalgrid[(col - 1, row)]
                #print "Search for corner tile on the right of this one:", lefttile
                # Select a corner without U and R borders
                tileFound = False
                for baseID in connectpieces[2]:
                    if baseID in usedtiles:
                        continue
                    for transformation in range(8):
                        countUp    = 0
                        countRight = 0
                        coupleOK   = False
                        tileOption = baseID * 100 + transformation
                        for couplelist in couples:
                            if (tileOption, "U") in couplelist:
                                countUp += 1
                            if (tileOption, "R") in couplelist:
                                countRight += 1
                            if (tileOption, "L") in couplelist:
                                #print "Valid option?", couplelist,
                                if (lefttile, "R") in couplelist:
                                    coupleOK = True
                                    #print "Yes"
                                    break
                                #else:
                                    #print "No"
                        if countUp == 0 and countRight == 0 and coupleOK == True:
                            finalgrid[(col, row)] = tileOption
                            tileFound = True
                            #print "------> Col", col, "Row", row, "Tile:", tileOption
                            usedtiles.append(tileOption // 100)
                            break
                    if tileFound:
                        break
                continue
            else:
                lefttile = finalgrid[(col - 1, row)]
                upTile   = finalgrid[(col, row - 1)]
                #print "Search for corner tile on the right of this one:", lefttile, "and under this one", upTile
                # Select a corner without D and R borders
                tileFound = False
                for baseID in connectpieces[2]:
                    if baseID in usedtiles:
                        continue
                    for transformation in range(8):
                        countDown  = 0
                        countRight = 0
                        leftOK     = False
                        upOK       = False
                        tileOption = baseID * 100 + transformation
                        for couplelist in couples:
                            if (tileOption, "D") in couplelist:
                                countDown += 1
                            if (tileOption, "R") in couplelist:
                                countRight += 1
                            if (tileOption, "L") in couplelist:
                                #print "Valid option?", couplelist,
                                if (lefttile, "R") in couplelist:
                                    leftOK = True
                                    #print "Yes"
                                #else:
                                    #print "No"
                            if (tileOption, "U") in couplelist:
                                #print "Valid option?", couplelist,
                                if (upTile, "D") in couplelist:
                                    upOK = True
                                    #print "Yes"
                                #else:
                                    #print "No"
                        if countDown == 0 and countRight == 0 and leftOK == True and upOK == True:
                            finalgrid[(col, row)] = tileOption
                            tileFound = True
                            #print "------> Col", col, "Row", row, "Tile:", tileOption
                            usedtiles.append(tileOption // 100)
                            break
                    if tileFound:
                        break
                continue
        if (col == numberofcols - 1) and row == 0:
            lefttile = finalgrid[(col - 1, row)]
            #print "Search for corner tile on the right of this one:", lefttile
            # Select a corner without U and R borders
            tileFound = False
            for baseID in connectpieces[2]:
                if baseID in usedtiles:
                    continue
                for transformation in range(8):
                    countUp    = 0
                    countRight = 0
                    coupleOK   = False
                    tileOption = baseID * 100 + transformation
                    for couplelist in couples:
                        if (tileOption, "U") in couplelist:
                            countUp += 1
                        if (tileOption, "R") in couplelist:
                            countRight += 1
                        if (tileOption, "L") in couplelist:
                            #print "Valid option?", couplelist,
                            if (lefttile, "R") in couplelist:
                                coupleOK = True
                                #print "Yes"
                            #else:
                                #print "No"
                                
                    if countUp == 0 and countRight == 0 and coupleOK == True:
                        finalgrid[(col, row)] = tileOption
                        tileFound = True
                        #print "------> Col", col, "Row", row, "Tile:", tileOption
                        usedtiles.append(tileOption // 100)
                        break
                if tileFound:
                    break
            continue
        
        if col == 0 and row > 0 and row < numberofrows - 1:
            uptile = finalgrid[(col, row - 1)]
            #print "Search for tile under this one:", uptile
            # Middle pieces require three connections
            tileFound = False
            for baseID in connectpieces[3]:
                #print "Checking:", baseID
                if baseID in usedtiles:
                    #print "Already used"
                    continue
                for transformation in range(8):
                    countLeft = 0
                    coupleOK  = False
                    tileOption = baseID * 100 + transformation
                    for couplelist in couples:
                        if (tileOption, "L") in couplelist:
                            countLeft += 1
                        if (tileOption, "U") in couplelist:
                            #print "Valid option?", couplelist,
                            if (uptile, "D") in couplelist:
                                coupleOK = True
                                #print "Yes"
                                #break
                            #else:
                                #print "No"
                    if countLeft == 0 and coupleOK == True:
                        finalgrid[(col, row)] = tileOption
                        tileFound = True
                        #print "------> Col", col, "Row", row, "Tile:", tileOption
                        usedtiles.append(tileOption // 100)
                        break
                if tileFound:
                    break
            continue

        if col == numberofcols - 1 and row > 0 and row < numberofrows - 1:
            #print "Case: if col == numberofcols - 1 and row > 0 and row < numberofrows - 1:"
            uptile   = finalgrid[(col, row - 1)]
            lefttile = finalgrid[(col - 1, row)]
            #print "Search for middle right border tile under this one:", uptile, "and right to this one:", lefttile
            # Middle pieces require three connections
            tileFound = False
            for baseID in connectpieces[3]:
                #print "Checking:", baseID
                if baseID in usedtiles:
                    #print "Already used"
                    continue
                for transformation in range(8):
                    countRight = 0
                    tileUpOK   = False
                    tileLeftOK = False
                    tileOption = baseID * 100 + transformation
                    for couplelist in couples:
                        if (tileOption, "R") in couplelist:
                            countRight += 1
                        if (tileOption, "U") in couplelist:
                            #print "Valid option?", couplelist,
                            if (uptile, "D") in couplelist:
                                tileUpOK = True
                                #print "Yes"
                            #else:
                                #print "No"
                        if (tileOption, "L") in couplelist:
                            #print "Valid option?", couplelist,
                            if (lefttile, "R") in couplelist:
                                tileLeftOK = True
                                #print "Yes"
                            #else:
                                #print "No"
                    if countRight == 0 and tileUpOK == True and tileLeftOK == True:
                        finalgrid[(col, row)] = tileOption
                        tileFound = True
                        #print "------> Col", col, "Row", row, "Tile:", tileOption
                        usedtiles.append(tileOption // 100)
                        break
                if tileFound:
                    break
            continue

        if col > 0 and col < numberofcols - 1:
            lefttile = finalgrid[(col - 1, row)]
            #print "Search for tile on the right of this one:", lefttile
            # Middle pieces require three connections
            for baseID in connectpieces[3]:
                #print "Checking:", baseID
                if baseID in usedtiles:
                    #print "Already used"
                    continue
                for transformation in range(8):
                    countUp   = 0
                    coupleOK  = False
                    tileOption = baseID * 100 + transformation
                    for couplelist in couples:
                        if (tileOption, "U") in couplelist:
                            countUp += 1
                        if (tileOption, "L") in couplelist:
                            #print "Valid option?", couplelist,
                            if (lefttile, "R") in couplelist:
                                coupleOK = True
                                #print "Yes"
                            #else:
                                #print "No"
                    if countUp == 0 and coupleOK == True:
                        finalgrid[(col, row)] = tileOption
                        #print "------> Col", col, "Row", row, "Tile:", tileOption
                        usedtiles.append(tileOption // 100)
                        break
                if coupleOK == True:
                    break
            continue
        
        if (col == 0) and row == numberofrows - 1:
            uptile = finalgrid[(col, row - 1)]
            #print "Search for corner tile under this one:", lefttile
            # Select a corner without U and R borders
            tileFound = False
            for baseID in connectpieces[2]:
                if baseID in usedtiles:
                    continue
                for transformation in range(8):
                    countDown = 0
                    countLeft = 0
                    coupleOK  = False
                    tileOption = baseID * 100 + transformation
                    for couplelist in couples:
                        if (tileOption, "D") in couplelist:
                            countDown += 1
                        if (tileOption, "L") in couplelist:
                            countLeft += 1
                        if (tileOption, "U") in couplelist:
                            #print "Valid option?", couplelist,
                            if (lefttile, "D") in couplelist:
                                coupleOK = True
                                #print "Yes"
                            #else:
                                #print "No"
                    if countDown == 0 and countLeft == 0 and coupleOK == True:
                        finalgrid[(col, row)] = tileOption
                        tileFound = True
                        #print "------> Col", col, "Row", row, "Tile:", tileOption
                        usedtiles.append(tileOption // 100)
                        break
                if tileFound:
                    break
            continue
        
        if (col == numberofcols - 1) and row == 0:
            lefttile = finalgrid[(col - 1, row)]
            #print "Search for left corner tile on the right of this one:", lefttile
            # Select a corner without U and R borders
            tileFound = False
            for baseID in connectpieces[2]:
                if baseID in usedtiles:
                    continue
                for transformation in range(8):
                    countUp    = 0
                    countRight = 0
                    coupleOK   = False
                    tileOption = baseID * 100 + transformation
                    for couplelist in couples:
                        if (tileOption, "U") in couplelist:
                            countUp += 1
                        if (tileOption, "R") in couplelist:
                            countRight += 1
                        if (tileOption, "L") in couplelist:
                            #print "Valid option?", couplelist,
                            if (lefttile, "R") in couplelist:
                                coupleOK = True
                                #print "Yes"
                            #else:
                                #print "No"
                    if countUp == 0 and countRight == 0 and coupleOK == True:
                        finalgrid[(col, row)] = tileOption
                        tileFound = True
                        #print "------> Col", col, "Row", row, "Tile:", tileOption
                        usedtiles.append(tileOption // 100)
                        break
                if tileFound:
                    break
            continue
        
        if (col == numberofcols - 1) and row == numberofrows - 1:
            uptile = finalgrid[(col, row - 1)]
            #print "Search for right corner tile under this one:", lefttile
            # Select a corner without U and R borders
            tileFound = False
            for baseID in connectpieces[2]:
                if baseID in usedtiles:
                    continue
                for transformation in range(8):
                    countDown  = 0
                    countRight = 0
                    coupleOK   = False
                    tileOption = baseID * 100 + transformation
                    for couplelist in couples:
                        if (tileOption, "D") in couplelist:
                            countDown += 1
                        if (tileOption, "R") in couplelist:
                            countRight += 1
                        if (tileOption, "U") in couplelist:
                            #print "Valid option?", couplelist,
                            if (lefttile, "D") in couplelist:
                                coupleOK = True
                                #print "Yes"
                            #else:
                                #print "No"
                    if countDown == 0 and countRight == 0 and coupleOK == True:
                        finalgrid[(col, row)] = tileOption
                        tileFound = True
                        #print "------> Col", col, "Row", row, "Tile:", tileOption
                        usedtiles.append(tileOption // 100)
                        break
                if tileFound:
                    break
            continue

            
#print "Final grid:"
#for row in range(numberofrows):
    #for col in range(numberofcols):
        #print finalgrid[(col, row)],
        #if col == numberofcols - 1:
            #print
        #else:
            #print " ",
#print


x = 0
y = 0
start_x = 0
start_y = 0
finaltile = {}

for row in range(numberofrows):
    rowlist = []
    for col in range(numberofcols):
        rowlist.append(finalgrid[(col, row)])
    start_x, start_y, max_max_x, max_max_y = printtiles(rowlist, start_x, start_y, max_max_x, max_max_y)

# Store base value as TileID * 100
tileID = 0
finaltiles[tileID * 100] = dict(finaltile)
for trans in range(7):
    # Create 7 transitions
    newfinaltile = dict(rotateFinalTile(finaltile))
    finaltiles[tileID * 100 + 1 + trans] = newfinaltile
    if trans == 2:
        # After first 3, flip the tile
        finaltile = dict(flipFinalTile(newfinaltile))
    else:
        finaltile = dict(newfinaltile)

# Monster:
#   000000000011111111112
#   012345678901234567890
# 0                   # 
# 1 #    ##    ##    ###
# 2  #  #  #  #  #  #

# Store bits (x,y) of the moster in list
monster = [(18,0),
           (0,1), (5,1), (6,1), (11,1), (12,1), (17,1), (18,1), (19,1),
           (1,2), (4,2), (7,2), (10,2), (13,2), (16,2)]
                                                                         
for tileID in sorted(finaltiles.keys()):
    finaltile = finaltiles[tileID]
    monsters = 0
    for offset_x in range(max_max_x - 19):
        for offset_y in range(max_max_y - 2):
            monsterFound = True
            for bit in monster:
                checkbit = (offset_x + bit[0], offset_y + bit[1])
                if finaltile[checkbit] != "#":
                    monsterFound = False
                    break
            if monsterFound == True:
                if monsters == 0:
                    print "Tile " + str(tileID) + ":"
                #print "Found monster at offset X:", offset_x, "Y:", offset_y
                monsters += 1
                for bit in monster:
                    checkbit = (offset_x + bit[0], offset_y + bit[1])
                    finaltile[checkbit] = "O"
    if monsters > 0:
        p2 = printFinalTile(finaltile)
 
end = time.time()

print
print "Found solution to Part 2 in:", end - start, "seconds"
print

print "Part 1: ", p1
print "Part 2: ", p2


