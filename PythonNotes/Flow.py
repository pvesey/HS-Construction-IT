#This is a short introduciton to flow control

test_int = 50

if test_int > 100:
    print("The test Integer is greater than 100")
else:
    print("The test integer is less than 100")



## we also have loops.. the one below will count down from 10

increment_int = 10

while (increment_int > 0):
    print(increment_int)
    increment_int = increment_int - 1



## we can combine these two parts together to make a simple guessing game..

answer = 15


while(True):
    guess = int(input("Enter a number between 1 and 20: "))
    if (guess == answer):
        print("Yay! you have guessed correctly")
        break
    elif (guess > answer):
        print("Your guess is too high")
    else:
        print("Your guess is too low.. ")




