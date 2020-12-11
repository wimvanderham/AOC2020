# Day 11 - Seating system
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

x = 0
y = 0

max_x = 0
max_y = 0

# Waiting holds a grid with all the locations inside the waiting room
# x  ---------------->
# y (0,0) (1,0) (2,0)
# | (0,1) (1,1) (2,1)
# | (0,2) (1,2) (2,2)
# v
waiting = {}

# Functions
# Count the number of occupied seats "around" a specific one
# Input x,y coordinates of the seat we're checking
# plan the seat plan (copy of waiting)

def occupied(x, y, plan):
    nr_occupied = 0
    for diff_x in [-1,0,1]:
        # Move x from one to the left to one to the right
        for diff_y in [-1,0,1]:
            # Move y from one to the top to one to the bottom
            if diff_x == 0 and diff_y == 0:
                # Don't check your own seat
                continue
            # Part 2, continue until you see a seat
            new_x = x + diff_x
            new_y = y + diff_y
            check_seat = (new_x, new_y)
            if check_seat in plan:
                while plan[check_seat] == ".":
                    # Continue searching
                    new_x = new_x + diff_x
                    new_y = new_y + diff_y
                    check_seat = (new_x, new_y)
                    if check_seat not in plan:
                        # If we go off the plan, break
                        break
            if check_seat in plan:
                if plan[check_seat] == "#":
                    nr_occupied += 1
    return nr_occupied

# Function to output the seat plan
def printplan(plan):
    for y in range(max_y):
        for x in range(max_x):
            seat = (x,y)
            print plan[seat],
        print

    
# Count lines in file to determine EOF
num_lines = sum(1 for line in input_file)
print "Input file has:", num_lines, "lines"

input_file = open(filename)
EOF = False

# Read All Input lines
for line in input_file:
    # Read input lines
    counter += 1

    line = line.strip()

    #print counter, line
    if counter == num_lines:
        EOF = True

    # Load data in waiting
    x = 0
    for seat in line:
        waiting[(x,y)] = seat
        x += 1
    # Set max_x
    max_x = x
    
    y += 1

# Set max_y
max_y = y

# END of # Read input lines

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
            # Start by setting new seat = old seat
            new_waiting[seat] = waiting[seat]
            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if waiting[seat] == "L":
                if occupied(x, y, waiting) == 0:
                    new_waiting[seat] = "#"
            # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            # Part 2: Five or more
            if waiting[seat] == "#":
                if occupied(x, y, waiting) >= 5:
                    new_waiting[seat] = "L"
            
            #print "Y:", y, "X:", x, "Seat:", waiting[x,y]
            if new_waiting[seat] == "#":
                new_occupied += 1
    if new_occupied == old_occupied:
        # No change, break
        p2 = new_occupied
        break

    #printplan(new_waiting)
    #print
    
    old_occupied = new_occupied
    waiting = dict(new_waiting)
    
# Part 1: 
    
end = time.time()

#print "Found solution to Part 1 in:", end - start, "seconds"

# Part 2: 


end = time.time()

print "Found solution to Part 2 in:", end - start, "seconds"
print

#print "Part 1: ", p1
print "Part 2: ", p2


