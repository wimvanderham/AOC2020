input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2020\\input_1.txt")

expense_list = []
item = 0
a = 0
b = 0
c = 0

# Read Input lines in list
for line in input_file:
    item += 1
    expense = int(line)
    expense_list.append(expense)

findExpense1 = 0
findExpense2 = 0

for a in range(item):
    for b in range(a + 1, item):
        if expense_list[a] + expense_list[b] == 2020:
            print expense_list[a], expense_list[b]
            findExpense1 = expense_list[a] * expense_list[b]
        for c in range(b + 1, item):
            if expense_list[a] + expense_list[b] + expense_list[c] == 2020:
                print expense_list[a], expense_list[b], expense_list[c]
                findExpense2 = expense_list[a] * expense_list[b] * expense_list[c]
        
print "Part 1: ", findExpense1
print "Part 2: ", findExpense2

