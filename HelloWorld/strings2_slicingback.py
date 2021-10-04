letters = "abcdefghijklmnopqrstuvwxyz"

# With negative step, it defaults to the end of the string
# So it goes backwards
backwards = letters[25:0:-1]

print(backwards)

print(letters[4::-1]) #edcba
print(letters[16:13:-1])

# Python idioms
print(letters[::-1])
print(letters[-4:])
print(letters[-1:]) # Last item
print(letters[:1])  # First item. Without errors if empty
print(letters[0])   # First item, but with an error if empty
