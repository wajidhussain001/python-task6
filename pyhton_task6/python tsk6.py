 # User Input
number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))
print(number1 + number2)

# Indentation error
try:
    print("Try block - No indentation error!")

    print(undefined_variable)
except Exception as e:
    print(f"indent caught: {e}")

# Syntax Error
try:
   print(variable_with_typo) 
except NameError as e: 
   print(f"Caught a syntaxError: {e}")

# Zero Division Error
try:
    result = 1 / 0;
except ZeroDivisionError:
    print("Division by zero error")

# Type Error
try:
  result = "2" + 2
except TypeError:
    print("Type error")

# Value Error
try:
    number = int("abc") ;
except ValueError:
    print("Value error")

# Attribute Error
try:
    # This line tries to access an attribute that doesn't exist
    result = "Hello, world!".split(",")
    print(result.upper())
except AttributeError as e:
    print(f"Caught an attribute error: {e}")