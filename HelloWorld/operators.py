a = 12
b = 3

print(a + b)    # Addition 15
print(a - b)    # Subtraction 9
print(a * b)    # Multiplication 36
print(a / b)    # Division 4.0
print(a // b)   # Integer division 4 , rounded down towards minus infinity
print(a % b)    # 0 modulo, the remainder after integer division


print()

# For loop
# Range can take only integers
# So a//b will work since it evals to int, but not a/b since it evals to float
for i in range(1, a//b):
    print(i)