# Day 6 - 
#

import time

start = time.time()
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_6.txt"
input_file = open(filename)
p1 = 0
p2 = 0

person = []

counter = 0
group = 0
persons_in_group = 0

# Count lines in file to determine EOF
num_lines = sum(1 for line in input_file)
#print "Input file has:", num_lines, "lines"

input_file = open(filename)
EOF = False

# Read Input lines
for line in input_file:
    counter += 1

    #print counter, list(line)

    line = line.strip()

    if line != "":
        person.append(line)
        persons_in_group += 1
    if counter == num_lines:
        EOF = True
        
    if line == "" or EOF:
        # End of group (or file), Analyse data
        group += 1
        yes_answers = {}
        #print person
        for answers in person:
            for yes in answers:
                if yes not in yes_answers:
                    yes_answers[yes] = 1
                else:
                    count_persons = int(yes_answers[yes])
                    count_persons += 1
                    yes_answers[yes] = count_persons
        p1 += len(yes_answers)
        for yes in yes_answers:
            if yes_answers[yes] == persons_in_group:
                p2 += 1
        #print counter, group, yes_answers, len(yes_answers), p1, p2

        person = []
        persons_in_group = 0
        
end = time.time()

print "Found solution in:", end - start, "seconds"
print

print "Part 1: ", p1
print "Part 2: ", p2


