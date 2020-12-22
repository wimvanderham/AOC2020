# Day 22 - Playing cards with a crab
#

import collections

import time

start = time.time()

counter = 0
filename = "C:\\Users\\Wim\\Documents\\AOC\\2020\\input_22.txt"
input_file = open(filename)

# Solutions
p1 = 0
p2 = 0

# Global Variables
Deck1 = collections.deque()
Deck2 = collections.deque()
player = 0

# Functions
def playGame(Deck1, Deck2, GameNr):
    previous1 = []
    previous2 = []
    
    playround = 0
    score     = 0

    infiniteLoop = False
    
    #if GameNr > 0:
    #    print "=== Game", GameNr, "==="
    #print "Player 1's deck:", Deck1
    #print "Player 2's deck:", Deck2
    
    while len(Deck1) > 0 and len(Deck2) > 0:
        playround += 1
        #print
        #print "-- Round", playround,
        #if GameNr > 0:
        #    print "(Game", str(GameNr) + ")",
        #print "--"
        #print "Player 1's deck:", printDeque(Deck1)
        #print "Player 2's deck:", printDeque(Deck2)

        if (Deck1 in previous1) or (Deck2 in previous2):
            # Been there, done that
            #print "Deck1:", Deck1, "in previous1:", previous1, "?", (Deck1 in previous1)
            #print "Deck2:", Deck2, "in previous2:", previous2, "?", (Deck2 in previous2)
            #print "Been there, done that, Player 1 wins"
            infiniteLoop = True
            break
        else:
            # First time, save it for later
            previous1.append(collections.deque(Deck1))
            previous2.append(collections.deque(Deck2))
            
        card1 = Deck1.popleft()
        card2 = Deck2.popleft()

        #print "Player 1 plays:", card1
        #print "Player 2 plays:", card2

        # Check for Sub game
        if GameNr > 0 and len(Deck1) >= card1 and len(Deck2) >= card2:
            # Play sub-game (only for Part 2)
            #print "Playing a sub-game to determine the winner..."
            #print
            newDeck1 = collections.deque()
            newDeck2 = collections.deque()
            while len(newDeck1) < card1:
                newDeck1.append(Deck1[len(newDeck1)])
            while len(newDeck2) < card2:
                newDeck2.append(Deck2[len(newDeck2)])
            WinnerP1, score = playGame(newDeck1, newDeck2, GameNr + 1)
            #print "The winner of game", GameNr, "is player",
            #if WinnerP1:
            #    print "1!"
            #else:
            #    print "2!"
        else:
            WinnerP1 = (card1 > card2)
        if WinnerP1:
            # Player 1 wins round
            #if GameNr == 0:
            #    print "Player 1 wins the round!"
            #else:
            #    print "Player 1 wins round", playround, "of game", str(GameNr) + "!"
            Deck1.append(card1)
            Deck1.append(card2)
        else:
            # Player 2 wins round
            #if GameNr == 0:
            #    print "Player 2 wins the round!"
            #else:
            #    print "Player 2 wins round", playround, "of game", str(GameNr) + "!"
            Deck2.append(card2)
            Deck2.append(card1)
        #sec = input('Let us wait for user input. Let me know how many seconds to sleep now.\n')

    if GameNr <= 1:
        #print "== Post-game results =="
        #print "Player 1's deck:", printDeque(Deck1)
        #print "Player 2's deck:", printDeque(Deck2)

        if len(Deck1) > 0 or infiniteLoop:
            # Player 1 has won
            for card in range(len(Deck1)):
                card1 = Deck1.pop()
                #print card1, "*", (card + 1)
                score += (card + 1) * card1
        elif len(Deck2) > 0:
            # Player 2 has won
            for card in range(len(Deck2)):
                card2 = Deck2.pop()
                print card2, "*", (card + 1)
                score += (card + 1) * card2
        else:
            # No winner?
            assert False

    return (len(Deck1) > len(Deck2) or infiniteLoop), score

def printDeque(dequein):
    dequeString = ""
    for element in range(len(dequein)):
        if dequeString <> "":
            dequeString += ", "
        dequeString += str(dequein[element])
    return dequeString

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
    if counter == num_lines:
        EOF = True

    #print counter, line

    if line.startswith("Player"):
        player = int(line.split(" ")[1].strip(":"))
        #print "New player:", player
        continue
    if line == "":
        continue
    
    if player == 1:
        Deck1.append(int(line))
    elif player == 2:
        Deck2.append(int(line))
    else:
        print "Unkown player:", player
        assert False
                     
    
# END of # Read input lines

    
# Part 1:
#print "Player 1's deck:", Deck1
#print "Player 2's deck:", Deck2
print "Part 1"
p1 = 0

WinnerP1, p1 = playGame(collections.deque(Deck1), collections.deque(Deck2), 0)
if WinnerP1 == True:
    print "Player 1 won"
else:
    print "Player 2 won"
    
end = time.time()

print "Found solution to Part 1 in:", end - start, "seconds"

# Part 2: 
print "Part 2"
p2 = 0

WinnerP1, p2 = playGame(collections.deque(Deck1), collections.deque(Deck2), 1)
if WinnerP1 == True:
    print "Player 1 won"
else:
    print "Player 2 won"

end = time.time()

print "Found solution to Part 2 in:", end - start, "seconds"
print

print "Part 1: ", p1
print "Part 2: ", p2
