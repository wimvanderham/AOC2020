# Day 10 - 
#

import time

start = time.time()

counter = 0
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_10.txt"
input_file = open(filename)

# Solutions
p1 = 0
p2 = 0

# Global Variables
# List of joltages
joltage = []
# List of possible jumps from a specific joltage (jumps can be diff 1, 2 or 3 from previous joltage)
jumps = {}

# Functions

    
# Count lines in file to determine EOF
num_lines = sum(1 for line in input_file)
print "Input file has:", num_lines, "lines"

input_file = open(filename)
EOF = False

# Read All Input lines into number_list list
for line in input_file:
    # Read input lines
    counter += 1

    line = line.strip()

    #print counter, line
    if counter == num_lines:
        EOF = True

    joltage.append(int(line))

# END of # Read input lines
#print "Before:", joltage
# Start with 0 joltage
#joltage.append(0)
joltage = sorted(joltage)
# Add last jump of three
joltage.append(joltage[len(joltage) - 1] + 3)

# Part 1: Count jumps of 1 and 3 joltage and return multiplication
output = 0
jolt_diff = [0, 0, 0]
counter = 0
#print "After:", joltage
for jolt in joltage:
    counter += 1 
    diff = jolt - output
    #print "#", counter, "Output:", output, "+ diff", diff, "=", jolt, "New output = ", output + diff,
    jolt_diff[diff - 1] += 1
    #print "Counters:", jolt_diff
    output += diff

    # Number of subsequent numbers
    numbers_left = len(joltage) - counter
    #print "Numbers left:", numbers_left
    options = 0
    option_list = []
    if numbers_left >= 1:
        diff = joltage[counter] - joltage[counter - 1]
        if diff <= 3:
            options += 1
            option_list.append(joltage[counter])
            if numbers_left >= 2:
                diff = joltage[counter + 1] - joltage[counter - 1]
                if diff <= 3:
                    options += 1
                    option_list.append(joltage[counter + 1])
                    if numbers_left >= 3:
                        diff = joltage[counter + 2] - joltage[counter - 1]
                        if diff <= 3:
                            options += 1
                            option_list.append(joltage[counter + 2])
    jumps[jolt] = option_list

p1 = jolt_diff[0] * jolt_diff[2]
    
end = time.time()

print "Found solution to Part 1 in:", end - start, "seconds"

# Part 2: Count number of possible paths from start to end

JUMPS = {}
def count_jumps(start):
    # To count jumps from here we have several options
    #print "Start:", start
    if start == joltage[len(joltage) - 1]:
        # We're at the end of the list, only one path leads to it
        #print "==", len(joltage), " -->", 1
        return 1
    if start in JUMPS:
        # Already been here, return previous calculated value
        #print "In JUMPS -->", JUMPS[start]
        return JUMPS[start]
    # First time this start point, calculate possible paths from here
    total_count = 0
    for end in jumps[start]:
        # Using the possible jumps
        #print "Jump to:", end
        total_count += count_jumps(end)
        #print "-->", total_count
    # Save value for later
    JUMPS[start] = total_count
    return total_count

# Add initial jumps
jumps[0] = [1,2,3]
# Count all paths starting from 0
p2 = count_jumps(0)

end = time.time()

print "Found solution to Part 2 in:", end - start, "seconds"
print

print "Part 1: ", p1
print "Part 2: ", p2


