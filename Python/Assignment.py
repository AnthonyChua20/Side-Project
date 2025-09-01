import random
noOfGames = 3
wins = 0
losses = 0
ties = 0

while noOfGames >= 1:
    element = str(input("Choose an element Fire,Water,Grass:")).upper()
    if element =="FIRE":
        element = 0
    elif element == "WATER":
        element = 1
    elif element == "GRASS":
        element = 2

    ourGuess = random.randint(0,2)

    match element:
        case 0 if ourGuess == 0:
            print("It's a tie")
            ties +=1
        case 0 if ourGuess == 1:
            print("You lose")
            losses +=1
        case 0 if ourGuess ==2:
            print("You win")
            wins +=1
        case 1 if ourGuess == 0:
            print("You win")
            wins +=1
        case 1 if ourGuess == 1:
            print("it's a tie")
            ties +=1
        case 1 if ourGuess == 2:
            print("You lose")
            losses +=1
        case 2 if ourGuess == 0:
            print("You lose")
            losses +=1
        case 2 if ourGuess == 1:
            print("You win")
            wins +=1
        case 2 if ourGuess == 2:
            print("It's a tie") 
            ties +=1
        case _: 
            print("Invalid input")
            print("YOU LOSE")   
            losses +=1  
    noOfGames -= 1
if noOfGames == 0:
    print("You have",wins,"wins",losses,"losses and",ties,"ties")
    if wins > losses or wins > ties:
        print("You are the overall winner")
    elif losses > wins or losses > ties:
        print("You lose!")
    elif wins == losses:
        print("It's a tie!")
    print("Game Over")
    exit()
