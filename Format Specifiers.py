# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> =right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator

# ---------------------------------------------------------------------------------------------------

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.2f}") # says how many decimals get displayed(floating point), the number(in this case 2), says how many decimal places are being displayed
print(f"Price 2 is ${price2:10}") # 10 Means that the whole string has 10 spaces now. If the first number after the column is a 0 every space would be replaced with a 0(zero padded)
print(f"Price 3 is ${price3:<10}") # Now there are still 10 spaces but the string is left justified(same for right> left<, center^)

print(f"Price 1 is {price1:+}") # Makes positive numbers have a + in front of them.
print(f"Price 2 is {price2: }") # A space makes any positive numbers have a space in front of them
print(f"Price 3 is {price3:,}") # Separates a thousands space(e.g.: 1,000)

print(f"Price 1 is {price1:+2f}") # You can add any flags like this. No commas, spaces, no order.
print(f"Price 2 is {price2}")
print(f"Price 3 is {price3}")
