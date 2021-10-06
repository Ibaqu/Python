for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

print()
# Numbers are not required

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

print()
# We can use some extra formatting on the replacement fields to make it look better

for i in range(1, 13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()


# For left      <
# For right     >
# For center    ^
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))


print()
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))

print("Pi is approximately {0:12.50f}".format(22/7))

print("Pi is approximately {0:<72.50f}".format(22/7))
