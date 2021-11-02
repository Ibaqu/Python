answer = 5

print("Please guess the number between 1 and 10 : ")
guess = int(input())


if (guess > answer) :
    print("Please guess lower")
elif (guess < answer) :
    print("Please guess higher")
else :
    print("The guess is correct")
