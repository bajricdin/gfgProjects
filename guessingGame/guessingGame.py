import random as r

randomNumber = r.randint(0,101)
guessed = False
print(randomNumber)
def checkNumber(randomnNumber, userNumber):
    if randomnNumber == int(userNumber):
        return True
    else:
        return userNumber

def getUserNumber():
    n = input("Guess the number: ")
    return n

while guessed == False:
    checked = checkNumber(randomNumber, getUserNumber())
    print(checked)
    if checked == True:
        print(f"You guessed the number! Number was {randomNumber} ")
        guessed = True
    else:
        checkedNum = int(checked)
        if randomNumber > checkedNum:
            print("Guessing number is bigger than your number. Try again.")
        else:
            print("Guessing number is smaller than your number. Try again.")


