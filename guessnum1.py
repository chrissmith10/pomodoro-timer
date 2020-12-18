# Guess The Number

import random
import time

a = 1
b = 20
level = 1
guessesTaken = 0

print('Hello! What is your name?')
myName = input()

while True:
    number = random.randint(a, b)
    print('\nLevel', level)
    time.sleep(1)
    print(myName + ', I am thinking of a number between 1 and', b,'.')

    for guessesTaken in range(6):
        print('Take a guess.') # Four spaces in front of "print"
        while True:
            try:
                guess = input()
                guess = int(guess)
                break
            except:
                print("Error: Invalid Input. Input must be an integer.")

        if guess < number:
            print('Your guess is too low.') # Eight spaces in front of "print"

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        print('Good job, ' + myName + '! You guessed correctly in ' + guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('The number I was thinking of was ' + number + '.')
        break

    b = b + 10
    level = level + 1
