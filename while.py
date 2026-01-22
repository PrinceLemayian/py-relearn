response = "yes"

userInput = input("Kindly type yes: ")

while userInput != response:
    print("A wrong input or no input was detected. Please type yes.")
    userInput = input("Kindly type yes: ")
else:
    print("Nice!")
