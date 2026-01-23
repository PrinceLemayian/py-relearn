# store username and passwd in variable, ask user to log in, allow only 3 attempts lock the system after 3 failures

userName = "lemayian"
passWord = "lema1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    usernameInput = input("Enter your username: ")
    passwordInput = input("Enter your password: ")
    
    if (usernameInput == userName) and (passwordInput == passWord):
        print("Login successful!")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            remaining = max_attempts - attempts
            print("Username or password wrong. Please try again.")
            print(f"You have {remaining} attempts remaining.")
        else:
            print("System locked! Too many failed attempts.")
    
    