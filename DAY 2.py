print("\n--- Variables ---")
name = "Arjun"
age = 20
height = 5.4
student = True

print(name)
print(age)
print(height)
print(student)

print("\n--- Operations ---")
a = 10
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** b)

print("\n--- Conditionals ---")
age = 18

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")

print("\n--- Looping ---")
print("Counting with For Loop:")
for i in range(1, 6):
    print(i)

print("\n--- Function ---")
def greet(name):
    return f"Hello, {name}! Welcome to Data Science."

def add_numbers(num1, num2):
    return num1 + num2

print(greet("Intern"))
print("Sum:", add_numbers(15, 25))