# Day 7 - Counting bags at the airport
#

import time

start = time.time()

counter = 0
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_7.txt"
input_file = open(filename)

p1 = 0
p2 = 0

bag_rules = {}

# Count lines in file to determine EOF
num_lines = sum(1 for line in input_file)
print "Input file has:", num_lines, "lines"

input_file = open(filename)
EOF = False

# Read Input lines
for line in input_file:
    counter += 1

    line = line.strip()

    #print counter, line

    section = "main_bag"
    quantity = 1
    color    = ""

    bag_list = []
    
    for word in line.split(" "):
        if word == "contain":
            # Skip section of input line
            section = "sub_bag"
            continue

        if word.strip(",.") == "bags" or word.strip(",.") == "bag":
            # Completed a bag description
            if section == "main_bag":
                # Handle
                main_bag_color = color
                section = "sub_bag"
                color = ""
                
            if section == "sub_bag_color":
                if quantity != 0:
                    bag_list.append((color, quantity))
                color = ""
                section = "sub_bag"
            continue
        
        if section == "main_bag" or section == "sub_bag_color":
            # Main bag only has color description,
            # Sub bag color is separate section
            if color == "":
                color = word
            else:
                color = color + " " + word
            continue

        if section == "sub_bag":
            # First word of every sub bag is quantity or no
            if word == "no":
                quantity = 0
            else:
                quantity = int(word)
            section = "sub_bag_color"
            continue

    bag_rules[main_bag_color] = bag_list

# Got all the bag rules in a dict of format:
# key: main_bag_color
# value: list of tuples indicating (sub_bag color, quantity)

list_color = ["shiny gold"]

while True:
    new_colors = 0
    for color in list_color:
        for main_bag in bag_rules:
            for sub_bag in bag_rules[main_bag]:
                if sub_bag[0] == color:
                    new_color = main_bag
                    if (new_color in list_color) == False:
                        new_colors += 1
                        list_color.append(new_color)
                        #print "Added color:", new_color, "to list:", list_color
                    #else:
                        #print "Color:", new_color, "already there"
    if new_colors == 0:
        break
                    
#print "Found list:", list_color
p1 = len(list_color) - 1

# Part 2: Calculate the number of total bags inside a specific bag
def number_bags (bag):
    total_number = 1
    for sub_bag in bag_rules[bag]:
        total_number += sub_bag[1] * number_bags(sub_bag[0])
    return total_number
    
p2 = number_bags("shiny gold") - 1

end = time.time()

print "Found solution in:", end - start, "seconds"
print

print "Part 1: ", p1
print "Part 2: ", p2


