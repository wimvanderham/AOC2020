# Day 17 - Part 1 - Game of Life in 3D
#

import time

start = time.time()

counter = 0
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_17.txt"
input_file = open(filename)

# Solutions
p1 = 0
p2 = 0

# Global Variables

# Three dimensional S(pace)
S = {}

x = 0
y = 0
z = 0

# Functions
def getActiveNeighbours((x, y, z)):
    #print "Count Active Neighbours from:", x, y, z
    active = 0
    count  = 0
    D = [-1,0,1]
    for dx in D:
        new_x = x + dx
        for dy in D:
            new_y = y + dy
            for dz in D:
                new_z = z + dz
                new_coordinates = (new_x, new_y, new_z)
                if new_coordinates != (x, y, z): 
                    if new_coordinates in S:
                        if S[new_coordinates]== "#":
                            active += 1
                    count += 1
                    #print "new:", new_x, new_y, new_z, "New active:", active, "count:", count
    return active

def printPlanes(min_x, max_x, min_y, max_y, min_z, max_z, S):
    for z in range(min_z, max_z + 1):
        print "z=" + str(z)
        for y in range(min_y, max_y + 1):
            line = ""
            for x in range(min_x, max_x + 1):
                coordinate = (x, y, z)
                if coordinate in S:
                    line += S[coordinate]
                else:
                    line += "."
            print line
        print

# Count lines in file to determine EOF
num_lines = sum(1 for line in input_file)
print "Input file has:", num_lines, "line(s)"

input_file = open(filename)
EOF = False

# Read All Input lines
x = 0
y = 0
z = 0
cube = ""

min_x = 0
min_y = 0
min_z = 0
max_x = 0
max_y = 0
max_z = 0

for line in input_file:
    # Read input lines
    counter += 1

    line = line.strip()
    #print counter, line
    if counter == num_lines:
        EOF = True

    x = 0
    for cube in line:
        if cube == "#":
            # Only store Active cubes
            coordinates = (x, y, z)
            S[coordinates] = cube
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        if z < min_z:
            min_z = z
        if z > max_z:
            max_z = z
        x += 1
    y += 1
    
# END of # Read input lines

#print "Before any cycles:"
#print
#printPlanes(min_x, max_x, min_y, max_y, min_z, max_z, S)

# Test functions
#assert getActiveNeighbours((0, 0, 0)) == 1
#assert getActiveNeighbours((1, 2, 0)) == 3

    
# Part 1:
p1 = 0

D = [-1, 0, 1]

for cycle in range(6):
    newS = {}
    for coordinate in S.keys():
        #During a cycle, all cubes simultaneously change their state according to the following rules:
        for dx in D:
            for dy in D:
                for dz in D:
                    new_x = coordinate[0] + dx
                    new_y = coordinate[1] + dy
                    new_z = coordinate[2] + dz
                    if new_x < min_x:
                        min_x = new_x
                    if new_x > max_x:
                        max_x = new_x
                    if new_y < min_y:
                        min_y = new_y
                    if new_y > max_y:
                        max_y = new_y
                    if new_z < min_z:
                        min_z = new_z
                    if new_z > max_z:
                        max_z = new_z
                    
                    new_coordinate = (new_x, new_y, new_z)
                    activeNeighbours = getActiveNeighbours(new_coordinate)
                    #print "Checking:", new_coordinate, "with", activeNeighbours, "active Neighbours",
                    if new_coordinate not in newS:
                        # Determine new state based on current situation
                        if new_coordinate in S:
                            cube = S[new_coordinate]
                        else:
                            # Not in S(pace) so inactive
                            cube = "."
                        if cube == "#":
                            #If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
                            # Otherwise, the cube becomes inactive.
                            if 2 <= activeNeighbours <= 3:
                                newS[new_coordinate] = "#"
                        else:
                            #If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
                            # Otherwise, the cube remains inactive.
                            if activeNeighbours == 3:
                                newS[new_coordinate] = "#"
                    #print "new state -->", newS[new_coordinate]

    #print "After", cycle, "cycle(s):"
    #print
    #printPlanes(min_x, max_x, min_y, max_y, min_z, max_z, newS)
                   
    S = newS


p1 = len(S.keys())
        
end = time.time()

print "Found solution to Part 1 in:", end - start, "seconds"

print

print "Part 1: ", p1


