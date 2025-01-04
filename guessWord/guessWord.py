import random as r

def returnUniqueChars(w):
    n = []
    for c in w:
        if c not in n:
            n.append(c)
    return n

# :D

def checkChar(guessedChars, word, triedChars):
    try:
        c = input("Guess the character: ")
        if len(c) > 1:
            raise
    except:
        print("Invalid input. You have to enter one character!")
        return checkChar(guessedChars, word, triedChars)
    else:
        if c in triedChars:
            print(f"{c} character already tried. Try different one!")
            return checkChar(guessedChars, word, triedChars)
        triedChars.append(c)
        if c in guessedChars:
            print("")
        for ca in word:
            if c == ca:
                guessedChars.append(c)
            if ca in guessedChars:
                print(ca)
            else:
                print("-")
        unique = returnUniqueChars(word)
        uniqueGuessed = returnUniqueChars(guessedChars)
        if len(unique) == len(uniqueGuessed):
            print(f"You guessed the word: {word} ")
            return True
        return False

def cycle():
    guessed = False
    guessedChars = []
    triedChars = []
    randomWord = r.choice(words)

    print("Guess the characters:")
    for c in randomWord:
        print("-")

    numberOfTries = round(len(randomWord) + (len(randomWord) / 2))
    while guessed == False:
        numberOfTries -= 1
        if numberOfTries < 1:
            print("You lost. To many tries!")
            print(f"Correct word was: {randomWord}")
            guessed = True
            break
        print(f"You have {numberOfTries} tries left!")
        guessed = checkChar(guessedChars, randomWord, triedChars)
    

words = [
    # Animals
    "elephant", "dolphin", "kangaroo", "penguin", "giraffe",

    # Colors
    "crimson", "turquoise", "emerald", "amber", "indigo",

    # Countries
    "germany", "australia", "brazil", "turkey", "canada",

    # Fruits
    "pineapple", "blueberry", "strawberry", "watermelon", "papaya",

    # Objects
    "umbrella", "backpack", "telescope", "keyboard", "headphones",

    # Adjectives
    "beautiful", "curious", "daring", "frightened", "grateful",

    # Space
    "galaxy", "nebula", "comet", "planet", "asteroid",

    # Sports
    "football", "cricket", "badminton", "volleyball", "baseball",

    # Programming
    "python", "algorithm", "function", "variable", "compiler"
]
again = False


name = input("What is your name: ")
print(f"Good luck!  {name}")

cycle()
while again == False:
    playAgain = input("Play again? Type y if yes or n if no: \n")
    if playAgain == 'y':
        cycle()
    elif playAgain == 'n':
        again = True
    else:
        print("Wrong input")




