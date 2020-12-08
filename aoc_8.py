# Day 8 - Attenti al loop
# Soundtracks:
# https://open.spotify.com/track/2Jj6KtjINsAXzG7SQLzT8f
# https://open.spotify.com/track/6Fba9RZtC6vTY814JToDtP
# https://open.spotify.com/track/1FOt2ehcd3W6QLME02boGO

import time

start = time.time()

counter = 0
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_8.txt"
input_file = open(filename)

p1 = 0
p2 = 0

# Count lines in file to determine EOF
num_lines = sum(1 for line in input_file)
#print "Input file has:", num_lines, "lines"

input_file = open(filename)
EOF = False

program = []

operation = ""
argument  = 0

# Read Input lines
for line in input_file:
    counter += 1

    line = line.strip()

    #print counter, line

    word = line.split(' ')

    operation = word[0]
    argument  = int(word[1])

    program.append((operation, argument))

    #print program

    #if counter > 10:
        #break


# Loaded input
# Program is a list of tuples containing (operation, argument)
#for instruction in range(len(program)):
#    print "#" + str(instruction), "=", program[instruction]

# Save original program
original_program = list(program)

try_fix = 0
for bug in range(len(original_program)):
    # Bug fix loop
    if original_program[bug][0] == "nop":
        # Try changing this nop in jmp
        program = list(original_program)
        program[bug] = ("jmp", original_program[bug][1])
    if original_program[bug][0] == "jmp":
        # Try chaning this jmp in nop
        program = list(original_program)
        program[bug] = ("nop", original_program[bug][1])
    if original_program[bug][0] == "acc":
        # No change required, skip
        continue

    try_fix += 1
    #print "Trying fix #", try_fix
    
    # Run the program, keep track of instructions executed to identify loop
    instructions = []
    current_line = 0
    accumulator  = 0

    loop = False
    ok   = False
    while True:
        # Program execution loop
        if current_line in instructions:
            # Found line in executed instructions
            # Save current value of accumulator
            #print "Already executed, exit loop"
            p1 = accumulator
            # And exit program before we go in Loop,
            # and set flag that we did go into Loop
            loop = True
            counter = 0
            for instruction in instructions:
                counter += 1
                #print counter, instruction
            break

        if current_line == len(program):
            # We're done, exit gracefully
            ok = True
            p2 = accumulator
            break

        if current_line > len(program):
            # We've jumped to far, exit badly
            ok = False
            p2 = accumulator
            break
        
        operation = program[current_line][0]
        argument  = program[current_line][1]

        #print "Executing line:", current_line, "with operation:", operation, "and argument:", argument
        
        # Instruction executed, save line in instruction list
        instructions.append(current_line)

        old_line = current_line
        
        if operation == "acc":
            accumulator += argument
            current_line += 1

        if operation == "jmp":
            current_line += argument

        if operation == "nop":
            current_line += 1

        # Update program_flow
        #program_flow.append((old_line, operation, argument, current_line))
        

        #print "  Current value of accumulator:", accumulator, "next instruction line:", current_line

    # END of Program execution loop
    
    if ok == True:
        # This fix made us exit gracefully, stop trying
        break
# END of Bug fix loop

end = time.time()

print "Found solution in:", end - start, "seconds"
print

print "Part 1: ", p1
print "Part 2: ", p2


