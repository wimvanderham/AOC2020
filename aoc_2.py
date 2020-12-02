import time

start = time.time()

input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2020\\input_2.txt")

passwords = 0
password_ok1 = 0
password_ok2 = 0

min_char = 0
max_char = 0
char = ""
password = ""

min_max_range = ""

count_char = 0

# Read Input lines in list and check validity
for line in input_file:
    min_max_range = line.split(" ")[0]
    
    min_char = int(min_max_range.split("-")[0])
    max_char = int(min_max_range.split("-")[1])
    char = line.split(" ")[1][0]
    password = line.split(" ")[2]

    passwords += 1
    
    # Check validity: Part 1
    count_char = 0
    for check_char in password:
        if check_char == char:
            count_char += 1
    if count_char >= min_char and count_char <= max_char:
        password_ok1 += 1

    # Check validity: Part 2
    if password[min_char - 1] == char and password[max_char - 1] != char:
        password_ok2 += 1
    if password[min_char - 1] != char and password[max_char - 1] == char:
        password_ok2 += 1
    #print line, min_char, max_char, char, password, password_ok, password_ok2


end = time.time()

print "Found solution in:", end - start, "seconds"
print "Checked:", passwords, "total passwords"
print

print "Part 1: ", password_ok1
print "Part 2: ", password_ok2

