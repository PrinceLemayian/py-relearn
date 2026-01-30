number = 1

def increase_number():
    global number
    number += 1
    
def decrease_number():
    global number
    number -= 1
    
def reset_number():
    global number
    number = 0
    
while True:
    user_choice = int(input("Choose an option(1, 2, 3): "))
    print("1. Increase a number: ")
    print("2. Decrease number: ")
    print("3. Reset number: ")
    
    if (user_choice == 1):
        increase_number()
        print(f"The new number is: {number}")
    elif (user_choice == 2):
        decrease_number()
        print(f"The new number is: {number}")
    elif (user_choice == 3):
        reset_number()
        print(f"The new number is: {number}")
    else:
        print("Invalid input! Please try again.")