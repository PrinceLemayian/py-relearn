def calculate_compound_interest(principal, rate, years, frequency):
    percentRate = rate / 100
    amount = principal * (1 + (percentRate / frequency))**(frequency*years)
    totalInterest = amount - principal
    
    return amount, totalInterest


print("Welcome to the python compound interest calculator.")
while True:
    userPrincipal = float(input("Enter your principal amount: "))
    userRate = float(input("Enter the annual interest rate: "))
    userYear = float(input("Enter the number of years: "))
    userFrequency = int(input("Enter the number of times compounded per year: "))
    
    amount, totalInterest = calculate_compound_interest(userPrincipal, userRate, userYear, userFrequency)
    
    print(f"\nThe final amount is {amount:.2f}, and the total interest is {totalInterest:.2f}")

    