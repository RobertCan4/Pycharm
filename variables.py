# Variable = A continer for a value(string, integer, float, boolean).
#            A variable behaves as if it was the value it contains.

# ---------------------------------------------------------------------------------------------------

print("Strings:")
# Strings
# A series of characters that can includ numbers but will be treated as characters.
first_name = "Lennard"
food = "pizza"
email = "Lennard@fake.com"

# print(first_name)
# Prints the name of the Variable(No Quotes!).

print(f'Hello {first_name}!')
print(f'You like {food}!')
print(f'Your email is: {email}')

# f = Format
# Prints the variable in the curly braces.

# ---------------------------------------------------------------------------------------------------

print("Integers:")
# Integers
# Is a whole number.

age = 14
quantity = 3
num_of_students = 30

# No Quotes else it would be a string.
# No commas else it would be a float(see later).

print(f"You are {age} years  old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {num_of_students} students!")

# Needs an f string again.

# ---------------------------------------------------------------------------------------------------

print("Floats:")
# Float
# Is a number that contains a decimal portion

price = 10.99
gpa = 3.2
distance = 5.5

# No Quotes else it would be a string.

print(f"The price is ${price}!")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} kilometers!")

# ---------------------------------------------------------------------------------------------------

print("Booleans:")
# Boolean
# Is either true or false

is_student = True
for_sale = True

# Only Options: True/False

print(f"Are you a student?: {is_student}")
print(f"That Item is for sale: {for_sale}")
