age = "24"
print("My age is " + str(age) + " years") # For normal cases

# Using replacement fields with format
print("My age is {0} years".format(age));


# Other uses of format for multiple replacement fields
print("There are {0} days in {1}, {2}, {3}, {4}, {5}"
      .format(31, "Jan", "Mar", "May", "July", "Aug"))


print("Jan : {2}, Feb : {0}, Mar : {2}, Apr : {1}"
      .format(28, 30, 31))

print(
    """
    Jan     : {2}
    Feb     : {0}
    Mar     : {2}
    Apr     : {1}
    May     : {2}
    June    : {1}
    July    : {2}
    Aug     : {2}
    Sept    : {1}
    Oct     : {2}
    Nov     : {1}
    Dec     : {2}
    """.format(28, 30, 31));

