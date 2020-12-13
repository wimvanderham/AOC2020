# Day 13 - Shuttle search
#

import time

start = time.time()

counter = 0
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_13.txt"
input_file = open(filename)

# Solutions
p1 = 0
p2 = 0

# Global Variables
departure_list = []

# Functions
def getWaitTime (timestamp, bus):
    return (bus - (timestamp % bus)) % bus


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

    if counter == 1:
        my_timestamp = int(line)
    elif counter == 2:
        departure_list = list(line.split(","))
    else:
        # Too many input lines
        assert False

# END of # Read input lines

#print my_timestamp
#print departure_list
    
# Part 1:
busID = ""
wait_time = 0

takeBus = 0
min_wait = -1

sync_list = {}

offset = 0
for busID in departure_list:
    
    if busID == "x":
        # No bus
        offset += 1
        continue
    sync_list[offset] = int(busID)
    offset += 1
    
    wait_time = getWaitTime(my_timestamp, int(busID))
    
    if min_wait == -1 or wait_time < min_wait:
        # Found a better solution
        min_wait = wait_time
        takeBus  = int(busID)

p1 = min_wait * takeBus

end = time.time()

print "Found solution to Part 1 in:", end - start, "seconds"


# Part 2: 

iFactor = 1

iBusNr = 1
iTime = 0
for Bus in departure_list:
    if Bus == "x":
        iBusNr += 1
        continue
    
    while (iTime + iBusNr) % int(Bus) > 0:
        iTime += iFactor

    iFactor *= int(Bus)

    #print iBusNr, Bus, iTime, iFactor
    
    iBusNr += 1


p2 = iTime + 1

    
end = time.time()

print "Found solution to Part 2 in:", end - start, "seconds"
print

print "Part 1: ", p1
print "Part 2: ", p2


