string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("This" " will" " still" " works")

# Strings can be muliplied
print("Hello " * 5)
print("Hello" * (5 + 4)) # BODMAS
print("Hello " * 5 + "4") # First multiplies and then adds


print()

today = "friday"

print("day" in today)  # Is "day" in the string today --> true
print("thur" in today) # False
print("parrot" in "monke")

