class Count:
    def __init__(self, number):
        self.number = number
        
    def increase_counter(self):
        self.number += 1
    
    def decrease_counter(self):
        self.number -= 1
    
    def reset_counter(self):
        self.number = 0
        
number_1 = Count(0)
# decrease = decrease_counter()
# reset = reset_counter()

print(number_1.increase_counter())
