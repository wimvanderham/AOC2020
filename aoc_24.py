# Day 24 - Hex grids and switching tiles
#        - Game of Life after that

import time

start = time.time()

counter = 0
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_24.txt"
input_file = open(filename)

# Solutions
p1 = 0
p2 = 0

# Global Variables
counter = 0

# Use the cube coordinate system for hex grid
# https://www.redblobgames.com/grids/hexagons/
delta = {"e": (+1,-1,0), "w": (-1,+1,0), "ne": (+1,0,-1), "sw": (-1,0,+1), "nw": (0,+1,-1), "se": (0,-1,+1)}
# Tiles is dictionary containing the "touched" tiles
# The key is the cube coordinate of the tile (0,0,0) is the starting point
# The value is False for a white tile, True for a black tile
# Initially all tiles are white (False)
tiles = {}

prevchar = ""

# Functions
def getNeighbours((x, y, z)):
    # Count the neighbours around the six positions next to an input position
    # Returns the number of black and white neighbours
    white = 0
    black = 0
    for direction in delta.keys():
        (deltaX, deltaY, deltaZ) = delta[direction]
        neighbour = (x + deltaX, y + deltaY, z + deltaZ)
        if neighbour in tiles:
            if tiles[neighbour] == True:
                black += 1
            else:
                white += 1
        else:
            # No neighbour stored, use original color white
            white += 1
    return black, white
    
# Test functions

# Count lines in file to determine EOF
num_lines = sum(1 for line in input_file)
print "Input file has:", num_lines, "line(s)"

# Part 1:
input_file = open(filename)
EOF = False

for line in input_file:
    # Read input lines
    counter += 1
    line = line.strip()
    
    #print str(counter) + ".", line

    startpos = (0,0,0)
    
    for char in line:
        
        if char == "s" or char == "n":
            # Wait for second character
            prevchar = char
        else:
            if prevchar <> "":
                direction = prevchar + char
                prevchar = ""
            else:
                direction = char
            # Get delta coordinates based on direction
            (deltaX, deltaY, deltaZ) = delta[direction]
            (X, Y, Z) = startpos
            #print "X:", X, "Y:", Y, "Z:", Z, "direction:", direction, "deltaX:", deltaX, "deltaY:", deltaY, "deltaZ:", deltaZ, "New pos:",
            
            startpos = (X + deltaX, Y + deltaY, Z + deltaZ)
            
            #print startpos
            #print (min_x, min_y, min_z), "-", (max_x, max_y, max_z)
            
            
    # Get color and invert it
    if startpos in tiles:
        #print "Change tile at pos:", startpos, "to",
        color = not tiles[startpos]
    else:
        # First time this tile, change it to black True
        #print "Set tile at pos:", startpos, "to",
        color = True
    #if color:
    #    print "Black"
    #else:
    #    print "White"
        
    tiles[startpos] = color

# Count the Black tiles
for startpos in tiles:
    if tiles[startpos] == True:
        p1 += 1


end = time.time()

print "Found solution to Part 1 in:", end - start, "seconds"
print

# Part 2: 

# Now play the game of life with the Hex grid
for day in range(100):
    p2 = 0
    for position in tiles.keys():
        # Extend grid
        if tiles[position] == True:
            # For every Black tile, check the six neighbours
            (x, y, z) = position
            for direction in delta.keys():
                (deltaX, deltaY, deltaZ) = delta[direction]
                neighbour = (x + deltaX, y + deltaY, z + deltaZ)
                if neighbour not in tiles:
                    # If a neighbour is not available,
                    # set it to the default color White
                    # so it will be included in evaluation loop
                    tiles[neighbour] = False
    # Construct new situation
    new_tiles = {}
    for position in tiles.keys():
        black, white = getNeighbours(position)
        if tiles[position] == True:
            # Tile is Black
            if black == 0 or black > 2:
                # Change to White
                new_tiles[position] = False
            else:
                new_tiles[position] = True
        else:
            # Tile is White
            if black == 2:
                new_tiles[position] = True

    tiles = new_tiles

    if (day % 10) == 0:
        # Show some progress every 10th day
        end = time.time()
        print "Day", day, end - start, "seconds"
        

p2 = 0
for startpos in tiles:
    if tiles[startpos] == True:
        p2 += 1
print "Day", str(day + 1) + ":", p2

end = time.time()

print "Found solution to Part 2 in:", end - start, "seconds"
print

print "Part 1: ", p1
print "Part 2: ", p2


