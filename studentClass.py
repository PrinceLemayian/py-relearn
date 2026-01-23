# create a class called student, the class should have attributes name and age and initialize
# Add a method to the student class that prints the student's name and age
# create at least 2 student objects and call the method for each

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"{self.name} is {self.age} years old")
        
# Examples:
student1 = Student("Lemayian", 18)
student2 = Student("Prince", 19)

student1.display()
student2.display()