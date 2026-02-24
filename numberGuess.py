import random

def difficultyLevel():
    print("Choose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    while True:
        diffLevel = int(input("Choose a difficulty level(1, 2, 3): "))
        
    
        if diffLevel == 1:
            return 1, 20, 10
        elif diffLevel == 2:
            return 1, 50, 5
        elif diffLevel == 3:
            return 1, 100, 3
        else:
            print("Invalid choice, please select a difficulty level between 1 and 3.")
    
def gameLogic(minNumber, maxNumber, maxAttempts):
    secretNumber = random.randint(minNumber, maxNumber)
    attempts = 0
    
    print(f"Guess a number between {minNumber} and {maxNumber}")
    
    while attempts < maxAttempts:
        playerGuess = int(input("Enter your guess: "))
        
        if playerGuess < minNumber or playerGuess > maxNumber:
            print("Your guess is out of range, try again.")
            continue
        
        attempts += 1

        if playerGuess == secretNumber:
            print("Congratulations, you win the game!")
            return 
        elif playerGuess > secretNumber:
            print("Your guess is too high! Try again.")
        elif playerGuess < secretNumber:
            print("Your guess is too low! Try again.")
        else:
            print("Please enter a valid number.")
            
        print(f"Attempts remaining: {maxAttempts - attempts}")
    print(f"Game over! The correct number was {secretNumber}.")
        
def replayFunction():
    while True:
        replayInput = input("Do you want to play again(Y, N)? ").upper().strip()
        
        if replayInput == "Y":
            return True
        elif replayInput == "N":
            return False
        else:
            print("Invalid input, please enter Y or N.")
        
    

print("Welcome to the Number Guessing Game!")
    
while True:
    minNumber, maxNumber, maxAttempts = difficultyLevel()
    gameLogic(minNumber, maxNumber, maxAttempts)
        
    if replayFunction() == False:
        break
        
print("Good game! Play again soon.")