# Day 3 - A walk in the Forest, counting trees
#
# Soundtrack for this day:
# A Forest by The Cure
# https://open.spotify.com/track/4iVTSRiJAA18d3QglhyJ6Q?si=CsCp5HLLS2SQcwfYzl3KOw

import time

start = time.time()

input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2020\\input_3.txt")

terrain = {}
x = 0
y = 0
char = ""

max_x = 0
max_y = 0

delta_x = 3
delta_y = 1

# Read Input lines
for line in input_file:
    y += 1

    x = 0
    for char in line.strip():
        x += 1
        terrain[x,y] = char

    if max_x == 0:
        max_x = x
    
max_y = y

result2 = 1
trees = {}

for slopes in ["1 1", "3 1", "5 1", "7 1", "1 2"]:
    delta_x = int(slopes.split(" ")[0])
    delta_y = int(slopes.split(" ")[1])
    
    # print "Slope:", delta_x, delta_y


    # Start position
    x = 1
    y = 1
    counter = 0
    while True:
        # Inside "the Forest"
        x += delta_x
        y += delta_y

        if terrain[x,y] == "#":
            counter += 1
            
        #print x, y, terrain[x,y], trees
        
        if x + delta_x > max_x:
            x -= max_x
        if y + delta_y > max_y:
            # End of the forest
            break

        
    trees[slopes] = counter
        
    result2 = result2 * trees[slopes]

end = time.time()

print "Found solution in:", end - start, "seconds"
print

print "Part 1: ", trees["3 1"]
print "Part 2: ", result2
