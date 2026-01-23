# ask user for number until they type exit. for each number print whether it is even or odd

userInput = ""

while True:
    userInput = input("Enter a number: ")
    if userInput.lower() == "exit":
        print("program exit successful")
        break
    elif userInput.lower() != "exit":
        userInput = int(userInput)
        if (userInput % 2) == 0:
            print("Number is even")
        elif (userInput % 2) == 1:
            print("Number is odd")