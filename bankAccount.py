# create a bank acc clsss, balance starts at 0, deposit and withdrawak methods, prevent overdraft

class Account:
    def __init__(self):
        self.balance = 0
        
    def deposit(self, deposit_amount):
        if amount <= 0:
            print("Kindly input a valid amount.")
            return  
        elif amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: {self.balance}")
            
    def withdraw(self, withdraw_amount):
        if amount > self.balance:
            print("Insufficient funds for withdrawal. Please top up.")
         
        else:
            self.balance = self.balance - withdraw_amount
            print(f"Withdrawal successful. New balance: {self.balance}")
            
            
          
    def check_balance(self):
        print(f"Your balance is: {self.balance}")
        
account = Account()    

while True: 
    
    print("1. Deposit funds\n2. Withdraw funds \n3. Check Balance")
    user_input = int(input("Select an action(1,2,3): \n"))
    
    if user_input == 1:
        amount = int(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif user_input == 2:
        amount = int(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif user_input == 3:
        account.check_balance()