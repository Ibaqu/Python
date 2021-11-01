# for i in range(1, 13) :
#     print ("{} squared is {}".format(i, i ** 2))


name = input("Please enter your name :")
age = int(input("How old are you {}?: ".format(name)))

print(age)

if age >= 18:
    print("You can vote {}".format(name))
else:
    print("Please come back in {} years".format(18 - age))
