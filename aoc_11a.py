# Day 11 - 
#

import time

start = time.time()

counter = 0
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_11.txt"
input_file = open(filename)

# Solutions
p1 = 0
p2 = 0

# Global Variables
waiting = {}

# Functions
    
# Count lines in file to determine EOF
num_lines = sum(1 for line in input_file)
print "Input file has:", num_lines, "lines"

input_file = open(filename)
EOF = False

x = 0
y = 0

# Read All Input lines
for line in input_file:
    # Read input lines
    counter += 1

    line = line.strip()

    #print counter, line
    if counter == num_lines:
        EOF = True

    x = 0
    for seat in line:
        waiting[(x,y)] = seat
        x += 1

    max_x = x
    
    y += 1

max_y = y

# END of # Read input lines

def occupied(x, y, plan):
    nr_occupied = 0
    for diff_x in [-1,0,1]:
        for diff_y in [-1,0,1]:
            if diff_x == 0 and diff_y == 0:
                # Don't check your own seat
                continue
            check_seat = (x + diff_x, y + diff_y)
            if check_seat in plan:
                if plan[check_seat] == "#":
                    nr_occupied += 1
    return nr_occupied

def printplan(plan):
    for y in range(max_y):
        for x in range(max_x):
            seat = (x,y)
            print plan[seat],
        print

#printplan(waiting)

old_occupied = 0
while True:
    new_occupied = 0
    new_waiting = {}
    
    #print waiting
    for y in range(max_y):
        for x in range(max_x):
            seat = (x, y)
            # Otherwise, the seat's state does not change.
            new_waiting[seat] = waiting[seat]
            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if waiting[seat] == "L":
                if occupied(x, y, waiting) == 0:
                    new_waiting[seat] = "#"
            # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            if waiting[seat] == "#":
                if occupied(x, y, waiting) >= 4:
                    new_waiting[seat] = "L"
            
            #print "Y:", y, "X:", x, "Seat:", waiting[x,y]
            if new_waiting[seat] == "#":
                new_occupied += 1
    if new_occupied == old_occupied:
        # No change, break
        p1 = new_occupied
        break

    #printplan(new_waiting)
    #print
    
    old_occupied = new_occupied
    waiting = dict(new_waiting)
    
# Part 1: 
    
end = time.time()

print "Found solution to Part 1 in:", end - start, "seconds"

# Part 2: 


end = time.time()

#print "Found solution to Part 2 in:", end - start, "seconds"
#print

print "Part 1: ", p1
#print "Part 2: ", p2


