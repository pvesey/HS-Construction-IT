# ConditionsAndLoops.py
from random import randint


print('********************************')
print('****  NUMBER GUESSING GAME  ****')
print('********************************')

answer = randint(1,100)
# print(answer)
number_tries = 0
user_guess = 0

print('Guess a number between 1 and 100:')


while (answer != user_guess):
    user_guess = int(input('Enter your guess: '))
    number_tries += 1   # shorthand way to increment a variable
    if (user_guess == answer):
        print('Well done! You got it in ' +  str(number_tries) + ' tries')
    elif (user_guess > answer):
        print('Your guess is too high, try again')
    else:
        print('Your guess is too low, try again')
