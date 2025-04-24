# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition  (not False, not True)

# ---------------------------------------------------------------------------------------------------

# Or
# With or you can check more than one condition, if at least one of those conditions is true then the entire statement is true

# Example

# temp = 20
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print("Thw outdoor event is cancelled.")
# else:
#     print("The outdoor event is still scheduled.")

# if at least one of these (if temp > 35 or temp < 0 or is_raining:) conditions is true, the entire statement is true.

# ---------------------------------------------------------------------------------------------------

# And
# You can link 2 conditions together, where both of them must be true for the entire statement to be True

# temp = 25
# is_sunny = True

# if temp >= 28 and is_sunny:
#     print("It is HOT outside")
#     print("It is SUNNY")
# the temp is not True.

# temp = 20
# is_sunny = True

# if temp >= 28 and is_sunny:
#     print("It is HOT outside")
#     print("It is SUNNY")
# elif temp <= 0 and is_sunny:
#     print("It is COLD outside.")
#     print("It is SUNNY")
# elif 28 > temp > 0 and is_sunny:
#     print("It is WARM outside")
#     print("It is SUNNY")

# Now both are True

# ---------------------------------------------------------------------------------------------------

# Not
# Inverts the condition, to see if something is not False or not True

temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside.")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside.")
    print("It is CLOUDY")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY")


# Not does the opposite of what your looking for.
# Inverts the condition, if its True its now False, if its False its now True











