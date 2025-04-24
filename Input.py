# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

# ---------------------------------------------------------------------------------------------------

# Inputs

# input()

# Calls the Input Function.

# ---------------------------------------------------------------------------------------------------

# input("What is your name?: ")

# Stores the Input from the Terminal as a string.

# ---------------------------------------------------------------------------------------------------

name = input("What is your name?: ")
# age = input("How old are you?: ")

# Stores the Input as a variable(type = string)

# age = int(age)

# Converting the variable to an integer and then adding 1.
# So the final output is, if you type in 14, 15.

age = int(input("How old are you?: "))
age = age + 1

# Too shorten the code you can make the typecasting by setting the int() infront of the input function.
# So it doesnt return as a string but as a integer.
# Works with everything else(Floats, Booleans, etc.).

print(f"Hello {name}!")
print(f"HAPPY BIRTHDAY!")
print(f"You are {age} years old!")
