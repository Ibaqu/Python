
#         01234567890123
parrot = "Norwegian Blue"

# Upto BUT NOT INCLUDING
print(parrot[0:6])      # Norweg

print(parrot[3:5])      # we        - Middle values

print(parrot[:9])       # Norwegian - Start value not required

print(parrot[10:14])    # Blue
print(parrot[10:])      # Blue      - End values arent required

print(parrot[:6] + parrot[6:])

print(parrot[:])

# Negative values
print()
print(parrot[-4:-2])    # Index -4 upto but not including -2
print(parrot[-4:12])    # Same thing except 12 index


# Step values
print();

# Starts from index 0 -> 6 but in steps of two
print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw


number = "9,222;222 222.222:221"

# Step through string, and print commas only
# Dont include index 0
print(number[1::4]);


# Useful application
separators = number[1::4]

values = "".join(char if char not in separators else " " for char in number).split();
print([int(val) for val in values])