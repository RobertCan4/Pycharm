# indexing = accessing elements of a sequence using [] (indexing operators)
#           [start : end : step]

# ---------------------------------------------------------------------------------------------------

# Example

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# When printing this it will output the character that is in that position(starts with 0).

# ---------------------------------------------------------------------------------------------------

credit_number = "1234-5678-9012-3456"


# print(credit_number[0 : 4])
# print(credit_number[5:9])
# print(credit_number[5:])
#print(credit_number[-1])
# print(credit_number[::2])


# Now we have the first 4 digits.
# If you want to list everything in a string from a certain character on you only need to type [5:], this lists every character from the 5. on.
# When using negative numbers it goes from the back, example [-1] prints 6.
# print(credit_number[::2]) prints every second number. Can also be every 3rd and so on.

# ---------------------------------------------------------------------------------------------------

# Example

last_digits = credit_number[-4:]

print(f"XXXX-XXXX-XXXX-{last_digits}")

# ---------------------------------------------------------------------------------------------------

credit_number = credit_number[::-1]
print(credit_number)

# To reverse a string do this.