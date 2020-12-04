# Day 4 - Passport validation
#

import time

start = time.time()

input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2020\\input_4.txt")

counter = 0
passport = {}
pairlist = {}

#    Passport fields
#
#    byr (Birth Year)
#    iyr (Issue Year)
#    eyr (Expiration Year)
#    hgt (Height)
#    hcl (Hair Color)
#    ecl (Eye Color)
#    pid (Passport ID)
#    cid (Country ID)
#
passportfields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

valid_passport1 = 0
valid_passport2 = 0

# Read Input lines
for line in input_file:
    #print counter, line
    if line.strip() == "":
        passport[counter] = pairlist
        # Light check in Part 1
        passport_OK1 = True
        # Stricter checking in Part 2
        passport_OK2 = True
        #print "Checking:", pairlist, "Start OK2?:", passport_OK2
        for field in passportfields:
            if (field in pairlist) == False and field <> "cid":
                # Part 1 Check. Only check if the required fields (all excluding "cid") are available
                passport_OK1 = False
                passport_OK2 = False

            if field in pairlist:            
                # Part 2 Checks
                value = pairlist[field]
                if field == "byr":
                    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
                    if int(value) < 1920 or int(value) > 2002:
                        passport_OK2 = False
                    #print "Validated: byr (Birth Year) - four digits; at least 1920 and at most 2002.", value, "OK?", passport_OK2
                if field == "iyr":
                    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
                    if int(value) < 2010 or int(value) > 2020:
                        passport_OK2 = False
                    #print "Validated: iyr (Issue Year) - four digits; at least 2010 and at most 2020.", value, "OK?", passport_OK2
                if field == "eyr":
                    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                    if int(value) < 2020 or int(value) > 2030:
                        passport_OK2 = False
                    #print "Validated: eyr (Expiration Year) - four digits; at least 2020 and at most 2030.", value, "OK?", passport_OK2
                if field == "hgt":
                    # hgt (Height) - a number followed by either cm or in:
                    # If cm, the number must be at least 150 and at most 193.
                    # If in, the number must be at least 59 and at most 76.
                    unit = value[-2:]
                    if unit in ["cm", "in"]:
                        height = int(value[:-2])
                        if unit == "cm":
                            if height < 150 or height > 193:
                                passport_OK2 = False
                        if unit == "in":
                            if height < 59 or height > 76:
                                passport_OK2 = False
                    else:
                        passport_OK2 = False
                    #print "Validated: hgt (Height)", value, "OK?", passport_OK2
                if field == "hcl":
                    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
                    if value[0] != "#":
                        passport_OK2 = False
                    else:
                        if len(value) != 7:
                            passport_OK2 = False
                        else:
                            for hexchar in value[1:]:
                                if (hexchar in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]) == False:
                                    passport_OK2 = False
                    #print "Validated: hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.", value, "OK?", passport_OK2
                if field == "ecl":
                    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                    if (value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) == False:
                        passport_OK2 = False
                    #print "Validated: ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.", value, "OK?", passport_OK2
                if field == "pid":
                    # pid (Passport ID) - a nine-digit number, including leading zeroes.
                    if len(value) != 9:
                        passport_OK2 = False
                    #print "Validated: pid (Passport ID) - a nine-digit number, including leading zeroes.", value, "OK?", passport_OK2
                #if field == "cid":
                    # cid (Country ID) - ignored, missing or not.
                    
                #print field, field in pairlist, field <> "cid", "OK?", passport_OK
        #print "OK?", passport_OK
        if passport_OK1 == True:
            valid_passport1 += 1
        if passport_OK2 == True:
            valid_passport2 += 1
        #print "Checked passport #", counter, len(pairlist), pairlist, "OK1?", passport_OK1, valid_passport1, "OK2?", passport_OK2, valid_passport2
        # print counter, pairlist
        counter += 1
        pairlist = {}
        continue
    for pair in line.split(" "):
        #print counter, pair
        key = pair.strip().split(":")[0]
        value = pair.strip().split(":")[1]
        if key != "":
            pairlist[key] = value
        key = ""
        value = ""

#print passport

end = time.time()

print "Found solution in:", end - start, "seconds"
print

print "Part 1: ", valid_passport1
print "Part 2: ", valid_passport2
