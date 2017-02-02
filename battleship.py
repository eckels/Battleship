from random import randint

ocean = []

for x in range(10):
   ocean.append(["0"] * 10)

print("Time to play Battleship!")

playerships = []
for x in range(10):
   playerships.append(["-"] * 10)

enemyships = []
for x in range(10):
   enemyships.append(["-"] * 10)

def threeship():
   row = randint(0, 7)
   column = randint(0, 7)
   if playerships[row][column] == "-":
       playerships[row][column] = "X"
       rando = randint(0,1)
       if rando == 0:
           if playerships[row + 2][column] == "-" and row + 2 <= 9:
                if playerships[row + 1][column] == "-" and row + 1 <= 9:
                    playerships[row + 1][column] = "X"
                    playerships[row + 2][column] = "X"
       if rando == 1:
           if playerships[row][column + 2] == "-" and column + 2 <= 9:
                if playerships[row][column + 1] == "-" and column + 1 <= 9:
                    playerships[row][column + 2] = "X"
                    playerships[row][column + 1] = "X"
   else:
        threeship()

def threeship2():
   row = randint(0, 7)
   column = randint(0, 7)
   if enemyships[row][column] == "-":
       enemyships[row][column] = "X"
       rando = randint(0,1)
       if rando == 0:
           if enemyships[row + 2][column] == "-" and row + 2 <= 9:
                if enemyships[row + 1][column] == "-" and row + 1 <= 9:
                    enemyships[row + 1][column] = "X"
                    enemyships[row + 2][column] = "X"
       if rando == 1:
           if enemyships[row][column + 2] == "-" and column + 2 <= 9:
                if enemyships[row][column + 1] == "-" and column + 1 <= 9:
                    enemyships[row][column + 2] = "X"
                    enemyships[row][column + 1] = "X"
   else:
        threeship2()

def fourship():
   row = randint(0, 6)
   column = randint(0, 6)
   if playerships[row][column] == "-" and playerships[row + 1][column] == "-" and playerships[row + 2][column] == "-" and playerships[row + 3][column] == "-":
        if playerships[row][column + 1] == "-" and playerships[row][column + 2] == "-" and playerships[row][column + 3] == "-":
           playerships[row][column] = "X"
           rando = randint(0,1)
           if rando == 0:
               if playerships[row + 2][column] == "-" and row + 2 <= 9:
                    if playerships[row + 1][column] == "-" and row + 1 <= 9:
                        if playerships[row + 3][column] == "-" and row + 3 <= 9:
                            playerships[row + 3][column] = "X"
                            playerships[row + 2][column] = "X"
                            playerships[row + 1][column] = "X"
           if rando == 1:
               if playerships[row][column + 2] == "-" and column + 2 <= 9:
                    if playerships[row][column + 1] == "-" and column + 1 <= 9:
                        if playerships[row][column + 3] == "-" and column + 3 <= 9:
                            playerships[row][column + 3] = "X"
                            playerships[row][column + 2] = "X"
                            playerships[row][column + 1] = "X"
        else:
            fourship()
   else:
        fourship()

def fourship2():
   row = randint(0, 6)
   column = randint(0, 6)
   if enemyships[row][column] == "-" and enemyships[row + 1][column] == "-" and enemyships[row + 2][column] == "-" and enemyships[row + 3][column] == "-":
        if enemyships[row][column + 1] == "-" and enemyships[row][column + 2] == "-" and enemyships[row][column + 3] == "-":
           enemyships[row][column] = "X"
           rando = randint(0,1)
           if rando == 0:
               if enemyships[row + 2][column] == "-" and row + 2 <= 9:
                    if enemyships[row + 1][column] == "-" and row + 1 <= 9:
                        if enemyships[row + 3][column] == "-" and row + 3 <= 9:
                            enemyships[row + 3][column] = "X"
                            enemyships[row + 2][column] = "X"
                            enemyships[row + 1][column] = "X"
           if rando == 1:
               if enemyships[row][column + 2] == "-" and column + 2 <= 9:
                    if enemyships[row][column + 1] == "-" and column + 1 <= 9:
                        if enemyships[row][column + 3] == "-" and column + 3 <= 9:
                            enemyships[row][column + 3] = "X"
                            enemyships[row][column + 2] = "X"
                            enemyships[row][column + 1] = "X"
        else:
            fourship2()
   else:
        fourship2()

def twoship():
   row = randint(0, 8)
   column = randint(0, 8)
   if playerships[row][column] == "-" and playerships[row + 1][column] == "-":
        if playerships[row][column + 1] == "-":
           playerships[row][column] = "X"
           rando = randint(0,1)
           if rando == 0:
                if playerships[row + 1][column] == "-" and row + 1 <= 9:
                    playerships[row + 1][column] = "X"
           if rando == 1:
                if playerships[row][column + 1] == "-" and column + 1 <= 9:
                    playerships[row][column + 1] = "X"
        else:
            twoship()
   else:
        twoship()

def twoship2():
   row = randint(0, 8)
   column = randint(0, 8)
   if enemyships[row][column] == "-" and enemyships[row + 1][column] == "-":
        if enemyships[row][column + 1] == "-":
           enemyships[row][column] = "X"
           rando = randint(0,1)
           if rando == 0:
                if enemyships[row + 1][column] == "-" and row + 1 <= 9:
                    enemyships[row + 1][column] = "X"
           if rando == 1:
                if enemyships[row][column + 1] == "-" and column + 1 <= 9:
                    enemyships[row][column + 1] = "X"
        else:
            twoship2()
   else:
        twoship2()

threeship()
fourship()
twoship()
threeship2()
fourship2()
twoship2()

def printboard(board):
    for row in board:
        print(" ".join(row))

print("\nHere are your ships: \n")
printboard(playerships)

print("\nFor the enemy oceans board, the misses will be displayed with a '-' while hits will be marked with a 'X' and unguessed spaced will be marked with 'O'\n")
print("For your board, your ships will be marked with an 'X' and your enemies hits will be marked with a '#' while the misses will be marked with a '+' and open spots will be shown with a '-'\n")

print("\nHere is the enemy ocean, now we will start! \n")
printboard(ocean)

playerscore = []
enemyscore = []

def guess():
    print("Your turn to guess! \n")
    guessrow = int(input("Coordinate Row: "))
    guessrow = guessrow - 1
    guesscolumn = int(input("Coordinate Column: "))
    guesscolumn = guesscolumn - 1
    if enemyships[guessrow][guesscolumn] == "X" and ocean[guessrow][guesscolumn] == "0":
        print("\nYou hit an enemy ship!")
        ocean[guessrow][guesscolumn] = "X"
        playerscore.append(1)
    elif enemyships[guessrow][guesscolumn] == "-":
        print("\nYou missed!")
        ocean[guessrow][guesscolumn] = "-"
    elif ocean[guessrow][guesscolumn] == "X":
        print("\nYou missed again!")

def computerguess():
    guessrow = randint(0,9)
    guesscolumn = randint(0,9)
    if playerships[guessrow][guesscolumn] == "X":
        playerships[guessrow][guesscolumn] = "#"
        enemyscore.append(1)
        print("\nEnemy hit your ship!")
    elif playerships[guessrow][guesscolumn] == "-":
        playerships[guessrow][guesscolumn] = "+"
        print("\nEnemy missed!")
    else:
        computerguess()

turns = 0
while turns <= 200:
    if len(playerscore) == 9:
        youwin = input("\nYou won the game!")
        break
    if len(enemyscore) == 9:
        youlose = input("\nYou lost the game")
        break
    guess()
    computerguess()
    print("\nEnd of Turn, here is your ocean:")
    printboard(playerships)
    print("\nHere is the enemy ocean:")
    printboard(ocean)
