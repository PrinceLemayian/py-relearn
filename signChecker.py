# ask user for a number, if number is positive, say positive, if negative say negative if zero say zero

userInput = int(input("Enter a number: "))

while True:
        if userInput > 0:
            print("positive")
            userInput = int(input("Enter a number: "))
        elif userInput < 0:
            print("negative")
            userInput = int(input("Enter a number: "))
        elif userInput == 0:
            print("zero")
            userInput = int(input("Enter a number: "))