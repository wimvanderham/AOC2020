# Day 5 - Immediate boarding, go to the gate
#

import time

start = time.time()

input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2020\\input_5.txt")

max_seatID = 0

seat_plan = {}
my_seat = 0

counter = 0
# Read Input lines
for line in input_file:
    counter += 1

    row_code = line.strip()[0:7]
    col_code = line.strip()[-3:]

    #print counter, line.strip(), "Row code:", row_code, "Column code:", col_code

    # Search row_seat
    row_range = (1,128)
    row_seat = 0
    for direction in row_code:
        available = row_range[1] - row_range[0] + 1
        half = available / 2
        # Cut down seat range in half
        if direction == "F":
            row_range = (row_range[0], row_range[1] - half)
        elif direction == "B":
            row_range = (row_range[0] + half, row_range[1])
        #print available, direction, row_range
    if row_range[0] == row_range[1]:
        # Go back to 0-based indexing
        row_seat = row_range[0] - 1
        #print "Found row seat:", row_seat
    else:
        print "*** Search error!"


    # Search col_seat
    col_range = (1,8)
    col_seat = 0
    for direction in col_code:
        available = col_range[1] - col_range[0] + 1
        half = available / 2
        # Cut down seat range in half
        if direction == "L":
            col_range = (col_range[0], col_range[1] - half)
        elif direction == "R":
            col_range = (col_range[0] + half, col_range[1])
        #print available, direction, col_range
    if col_range[0] == col_range[1]:
        # Go back to 0-based indexing
        col_seat = col_range[0] - 1
        #print "Found col seat:", col_seat
    else:
        print "*** Search error!"
        
    seat_id = row_seat * 8 + col_seat
    seat_plan[(row_seat, col_seat)] = "[__]"
    
    #print "seat ID:", seat_id
    if seat_id > max_seatID:
        max_seatID = seat_id

get_seat = False
print_seat_plan = False

if print_seat_plan:
    print "FINAL SEAT PLAN"
    print "    Columns"
    print "Row | 0| | 1| | 2| | 3| | 4| | 5| | 6| | 7|"
    
for row_seat in range(128):
    if print_seat_plan:
        print "%03d" % row_seat,
    for col_seat in range(8):
        if (row_seat, col_seat) in seat_plan:
            if print_seat_plan:
                print seat_plan[(row_seat,col_seat)],
            if my_seat == 0:
                # My seat not yet found and this
                # seat is occupied so try to find my seat now
                get_seat = True
        else:
            seat_id = row_seat * 8 + col_seat
            if print_seat_plan:
                print "%04d" % seat_id,
            if get_seat == True:
                # First free seat after all have been occupied
                # take this seat
                my_seat = seat_id
                get_seat = False
            
    if print_seat_plan:
        print
if print_seat_plan:
    print
        
end = time.time()

print "Found solution in:", end - start, "seconds"
print

print "Part 1: ", max_seatID
print "Part 2: ", my_seat

