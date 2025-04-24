# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# for x in range(1, 11): # Counts to 10. Because the last number is exclusive.
#    print(x)

# for counter in reversed(range(1, 11)): # Counts down from 10.
#     print(counter)

# print("Happy New Year!")

# ---------------------------------------------------------------------------------------------------

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

# ---------------------------------------------------------------------------------------------------

# for x in range(1, 21 ):
#     if x == 13: # Doesnt print the number 13
#         continue
#     else:
#         print(x)

# ---------------------------------------------------------------------------------------------------

for x in range(1, 21):
    if x == 13: # Stops at 13
        break
    else:
        print(x)


