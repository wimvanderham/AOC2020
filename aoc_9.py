# Day 9 - Checking XMAS protocol
#

import time

start = time.time()

counter = 0
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_9.txt"
input_file = open(filename)

p1 = 0
p2 = 0

# Global Variables
number_list = []
preamble    = 25

# Functions
def check_input (numbers, start_pos, length, sum_value):
    # Get two values from numbers list and see if they sum up to the sum_value
    #print "check_input:", numbers[start_pos:start_pos + length], sum_value
    
    a = 0
    b = 0
    end_pos = start_pos + length
    found_sum = False
    for a in range(start_pos, start_pos + length):
        #print "Number a:", a
        for b in range(a + 1, end_pos):
            #print "Number b:", b
            #print "Sum =", numbers[a], "+", numbers[b],
            #if (numbers[a] + numbers[b]) == sum_value:
                #print "==",
            #else:
                #print "<>",
            #print sum_value
            if (numbers[a] + numbers[b]) == sum_value:
                found_sum = True
                break
        if found_sum:
            break
    #print "check input:", found_sum
    return found_sum
        
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

    new_number = int(line)
    number_list.append(new_number)
# END of # Read input lines

# Part 1: Find the first invalid number
for counter in range(num_lines):
    new_number = number_list[counter]
    if counter >= preamble:
        # Got preamble, now look for sums
        if check_input(number_list, counter - preamble, preamble, new_number) == False:
            p1 = new_number
            break

# Part 2: Find the contiguous set of at least two numbers which sum up to the invalid
for counter in range(num_lines):
    sum_set = 0
    sub_list = []
    start_pos = counter
    while sum_set < p1:
        sub_list.append(number_list[start_pos])
        sum_set += number_list[start_pos]
        start_pos += 1
    if sum_set == p1:
        # Found the contiguous set of numbers
        #print "Found sub_list:", sub_list
        p2 = min(sub_list) + max(sub_list)
        break
    
end = time.time()

print "Found solution in:", end - start, "seconds"
print

print "Part 1: ", p1
print "Part 2: ", p2


