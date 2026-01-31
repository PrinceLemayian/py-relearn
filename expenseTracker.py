# store expenses in a list, expense should have title and amount, allows adding expense, viewing expense, calculating total

expenses = [{"Rent": 5000}]

def add_expense():
    expense_name = input("Enter expense name: ")
    expense_amount = input("Enter expense amount: ")
    expenses.append({expense_name, expense_amount})
    
def view_expense():
    for expense in expenses:
        print(expense)

# def calculate_total:

print(view_expense())
    