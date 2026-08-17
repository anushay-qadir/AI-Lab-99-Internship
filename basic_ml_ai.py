
print("Basic ML/AI Python Concepts")

# Variables and Data Types
name = "Anusha"
age = 20
score = 85.5
student = True

# Conditional Statement
if score >= 80:
    print("Grade A")
else:
    print("Grade B")

# Loop
for i in range(1, 6):
    print(i)

# Function
def average(numbers):
    return sum(numbers) / len(numbers)

print("Average:", average([20, 30, 40]))

# List Comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Dictionary Comprehension
square_dict = {x: x**2 for x in range(1, 6)}
print("Dictionary:", square_dict)

# Exception Handling
try:
    number = int("10")
    print("Number:", number)
except ValueError:
    print("Invalid value")

# File Handling
with open("data.txt", "w") as file:
    file.write("Basic ML/AI Task Completed")

# Class and Object
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student:", self.name)

student1 = Student("Anusha")
student1.display()

print("ALL CONCEPTS COMPLETED")
