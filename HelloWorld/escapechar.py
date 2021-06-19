splitstring = "This string has been \n split over \n serveral lines"
print(splitstring)


tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)


print('The pet shop owener said "No, no, \'e\'s uh, ... he\'s resting".')

print(""" No need to escape if 'there are three quotes """)


# You can use triple quotes to split the string over serveral lines

anotherSplitString = """ This is a really \
long split string \
but it seems to work somehow"""

print(anotherSplitString)


# When dealing with paths, they can be escaped with double backslash or `r` before the string
print("C:\\Users\\aquib\\notes.txt")
print(r"C:\Users\aquib\notes.txt")