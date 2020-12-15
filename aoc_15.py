# Day 15 -  
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
print "Input file has:", num_lines, "lines"

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
        print "Starting turn:", turn, "Speak:", speak_number
        if speak_number in speak:
            speak[speak_number] = speak[speak_number].append(turn)
        else:
            speak[speak_number] = [turn]
    else:
        if speak_number in speak:
            #print "Already spoken", speak[speak_number], "Len:", len(speak[speak_number])
            turn_list = list(speak[speak_number])
            if len(turn_list) == 1:
                speak_number = 0
            else:
                speak_number = speak[speak_number][-1] - speak[speak_number][-2]
            #print "Turn:", turn, "Speak:", speak_number
        else:
            #print "First time"
            speak_number = 0
        if speak_number in speak:
            turn_list = speak[speak_number]
            turn_list.append(turn)
            speak[speak_number] = turn_list
        else:
            speak[speak_number] = [turn]
        #print "Turn:", turn, "Speak:", speak_number
            
    #print "Turn:", turn, "Speak_number:", speak_number, "Spoken:", speak
    if turn == 2020:
        p1 = speak_number
        
    turn += 1

    if turn % 100000 == 0:
        end = time.time()
        print turn, (end - start)

p2 = speak_number
print p1

end = time.time()

print "Found solution to Part 1 in:", end - start, "seconds"


# Part 2: 
print p2

end = time.time()

print "Found solution to Part 2 in:", end - start, "seconds"
print

print "Part 1: ", p1
print "Part 2: ", p2


