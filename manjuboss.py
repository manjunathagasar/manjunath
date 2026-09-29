first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("Before swapping:")
print("First number =", first)
print("Second number =", second)

# Swapping
first, second = second, first

print("After swapping:")
print("First number =", first)
print("Second number =", second)

# Multiplication
print("Multiplication =", first * second)

# Division
if second != 0:
    print("Division =", first / second)
else:
    print("Cannot divide by zero")