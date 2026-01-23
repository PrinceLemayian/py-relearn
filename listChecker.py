# ask user to enter 5 numbers, store them in a list, print list, total, average

numbers = []
inputs = 0
max_inputs = 5

for i in range(5):
    user_input = int(input(f"Enter number {inputs + 1}: "))
    numbers.append(user_input)
    inputs += 1

totals = 0

for number in numbers:
    totals = totals + number
 
average = totals/5
   
print(numbers)
print(totals)
print(average)



