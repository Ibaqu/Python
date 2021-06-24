a = 12
b = 3

print(a + b / 3 - 4 * 12)   # -35.0

# Follows BODMAS - Brackets order Mult/Div Add/Sub

# To make the precedence clearer
print(a + (b / 3) - (4 * 12))

# Parenthesis can be used to manipulate how the precedence works
print(((a+b)/3 - 4 ) * 12)


# Mult/Div and Add/Sub have equal precedence and are evaluated from left to right

print (a / (b * a) / a)