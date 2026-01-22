# 1) for loop - used when you know how many times you want to repeat something

# for loop to print a range of numbers
'''
for i in range(1, 11):
    print(i)
'''
    
# 2) while loop - used when you want to repeat a condition until it becomes false

'''
i = 1
while i <= 5:
    print(i)
    i += 1
'''

# 3) LOOP CONTROL STATEMENTS
# - Break (stops the loop)
for i in range(10):
    if i == 5:
        break
    print(i)