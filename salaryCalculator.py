from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def calculate_pay(self):
        pass
    
    def __str__(self):
        return f"{self.name}: Employee's salary is ${self.calculate_pay():,.2f}"
    
class SalariedEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary
    
    def calculate_pay(self):
        return self.annual_salary / 12
    
class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        
    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked
    

# Challenge

employees = [
    SalariedEmployee("Askeladd", 350000),
    SalariedEmployee("Thorfinn", 280000),
    HourlyEmployee("Willibald", 35, 220),
    HourlyEmployee("Seif", 45, 160),
]

for employee in employees:
    print(employee)