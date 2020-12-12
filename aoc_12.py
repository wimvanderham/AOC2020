# Day 12 - 
#

import time

start = time.time()

counter = 0
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_12.txt"
input_file = open(filename)

# Solutions
p1 = 0
p2 = 0

# Global Variables

direction = "E"

current_x = 0
current_y = 0

# List of navigation input: (Action, Value)
# Action = N(orth), S(outh), E(ast), W(est), L(eft), R(right), F(orward)
# Value = Integer number indicating steps or degrees
navigation = []

# Order of new direction in steps of 90 degrees
newDirections = ["E", "S", "W", "N"]

# Functions
def getNewDirection(direction, action, value):
    if direction in newDirections:
        steps = int(value / 90)
        if action == "L":
            # Counterclockwise
            steps *= -1
        #print "From direction:", direction, "add", steps
        new_direction = (newDirections.index(direction) + steps) % len(newDirections)
        return newDirections[new_direction]
    else:
        return ""

def getNewWay(way_x, way_y, action, value):
    if action == "R":
        multiply_x = 1
        multiply_y = -1
    elif action == "L":
        multiply_x = -1
        multiply_y = 1

    #print "From:", way_x, way_y, "apply:", action, value
    
    if value == 90:
        new_y = way_x * multiply_x
        new_x = way_y * multiply_y
    if value == 180:
        new_x = -1 * way_x
        new_y = -1 * way_y
    if value == 270:
        # Invert direction
        multiply_x *= -1
        multiply_y *= -1
        new_y = way_x * multiply_x
        new_x = way_y * multiply_y
    #print "New_x:", new_x, "New y:", new_y
    return new_x, new_y

# Count lines in file to determine EOF
num_lines = sum(1 for line in input_file)
print "Input file has:", num_lines, "lines"

input_file = open(filename)
EOF = False


# Test getNewDirection function:
assert (getNewDirection("E", "R", 90) == "S")
assert (getNewDirection("S", "L", 90) == "E")
assert (getNewDirection("E", "R", 270) == "N")
assert (getNewDirection("N", "R", 90) == "E")
assert (getNewDirection("N", "R", 180) == "S")

# Test getNewWay function:
new_x = 0
new_y = 0
new_x, new_y = getNewWay(3, -2, "R", 90)
assert (new_x == 2 and new_y == 3)
new_x, new_y = getNewWay(3, -2, "L", 90)
assert (new_x == -2 and new_y == -3)
new_x, new_y = getNewWay(3, -2, "R", 270)
assert (new_x == -2 and new_y == -3)

# Read All Input lines
for line in input_file:
    # Read input lines
    counter += 1

    line = line.strip()

    # print counter, line
    if counter == num_lines:
        EOF = True

    action = line[0]
    value  = int(line[1:])

    navigation.append((action, value))

    #if action == "R" or action == "L":
    #    print action, value

# END of # Read input lines


    
# Part 1: Use input to navigate the ship directly

current_x = 0
current_y = 0
    
for step in navigation:
    action = step[0]
    value  = step[1]

    #print "X:", current_x, "Y:", current_y, "Going:", direction "Action:", action, "Value:", value
    
    if action == "F":
        # Forward is like moving in direction without changing direction
        action = direction

    
    if action == "E":
        current_x += value
    if action == "S":
        current_y += value
    if action == "W":
        current_x -= value
    if action == "N":
        current_y -= value
    if action == "R" or action == "L":
        # Change direction
        direction = getNewDirection(direction, action, value)

    #print "X:" current_x

p1 = abs(current_x) + abs(current_y)

end = time.time()

print "Found solution to Part 1 in:", end - start, "seconds"

# Part 2: Use a waypoint to move the ship
way_x = 10
way_y = -1

current_x = 0
current_y = 0

for step in navigation:
    action = step[0]
    value  = step[1]

    #print "X:", current_x, "Y:", current_y, "Going:", direction "Action:", action, "Value:", value
    
    if action == "F":
        # Move to the waypoint a number of times
        current_x += way_x * value
        current_y += way_y * value
    
    if action == "E":
        way_x += value
    if action == "S":
        way_y += value
    if action == "W":
        way_x -= value
    if action == "N":
        way_y -= value
    if action == "R" or action == "L":
        # Change waypoint direction
        way_x, way_y = getNewWay(way_x, way_y, action, value)

    
    #print "X:" current_x

p2 = abs(current_x) + abs(current_y)
    

end = time.time()

print "Found solution to Part 2 in:", end - start, "seconds"
print

print "Part 1: ", p1
print "Part 2: ", p2


