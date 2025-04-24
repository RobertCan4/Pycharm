# if = Do some code only IF some condition is true
#      Else do something else
#      Basic form of decision making

# age = int(input("Enter your age: "))

# if age >= 18:
#    print("You are now signed up!")
# else:
#    print("You must be 18+ to sign up.")

# ---------------------------------------------------------------------------------------------------

# If statements

# In this case it checks if the variable age is greater than or equal to 18 and then prints the Output "You are now signed up".
# If the age is true it will execute the code beneath it.
# If its not greater than 18 the if statement would be false.
# It skips over the code beneath the if statement.

# ---------------------------------------------------------------------------------------------------

# Else Statements

# If the if statement is false it will run the code beneath the else statement.

# ---------------------------------------------------------------------------------------------------

# Elseif statements

# Shortend to elif
# It goes through the whole if statement 1 by 1.
# You can add as many elseif statements as you want.

# if age >= 100:
#     print("You are too old to sign up!")
# elif age >= 18:
#     print("You are now signed up!")
# elif age < 0:
#     print("You haven't been born!")
# else:
#     print("You must be 18+ to sign up.")


# You need to pay attention to the order of the if statements if something is true

# ---------------------------------------------------------------------------------------------------

# Example

# response = input("Would you like food (Y/N): ")

# if response == "Y":
#     print("Have some food!")
# else:
#     print("No food for you!")



# To check if something is equal to use 2 =.(Comparison operator)

# ---------------------------------------------------------------------------------------------------

# Example 2

# name = input("Enter your name: ")

# if name == "":
#     print("You did not type in your name!")
# else:
#     print(f"Hello {name}!")

# ---------------------------------------------------------------------------------------------------

# Booleans with if statements
# With Booleans it is either true or false and executes the code depending on the state of the boolean.

online = False

if online:
    print("The user is online!")
else:
    print("The user is offline!")