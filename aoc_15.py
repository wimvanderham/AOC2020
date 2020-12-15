# Day 15 - Stupid number calling game
#

import time

start = time.time()

counter = 0
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_15.txt"
input_file = open(filename)

# Solutions
p1 = 0
p2 = 0

# Global Variables


# Functions

# Test function


# Count lines in file to determine EOF
num_lines = sum(1 for line in input_file)
print "Input file has:", num_lines, "line(s)"

input_file = open(filename)
EOF = False

# Read All Input lines
for line in input_file:
    # Read input lines
    counter += 1

    line = line.strip()

    print counter, line
    if counter == num_lines:
        EOF = True

    start_list = line.split(",")
    
# END of # Read input lines

    
# Part 1:
p1 = 0

print "Start:", start_list

turn = 0
speak = {}

while turn < 30000000:
    if turn < len(start_list):
        speak_number = int(start_list[turn])
        #print "Starting turn:", turn, "Speak:", speak_number
        speak[speak_number] = turn
    else:
        if turn == 2020:
            end = time.time()
            print "Found solution to Part 1 in:", end - start, "seconds"
            p1 = speak_number
        
        if speak_number in speak:
            #print "Already spoken", speak_number, "in turn:", speak[speak_number]
            new_number = turn - speak[speak_number] - 1
        else:
            #print "First time"
            new_number = 0

        # Remember when the previous number was called (during the previous turn)
        speak[speak_number] = turn - 1

        # "Call" the new number
        speak_number = new_number

        
    turn += 1

p2 = speak_number

# Part 2: 

end = time.time()

print "Found solution to Part 2 in:", end - start, "seconds"
print

print "Part 1: ", p1
print "Part 2: ", p2


