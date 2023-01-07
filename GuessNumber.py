# guess a number
import numpy as np
import matplotlib.pyplot as plt
import random
uplimt = 4
secretNumber = random.randint(1, uplimt)
print(secretNumber)
for guessTaken in range(1, uplimt):
    print('Please input the number: ')
    guess = input()
    while True:
        try:
            guess = float(guess)
            break
        except BaseException:
            guess = input("输入错误，n只能为数字，请输入n：")
    if guess > secretNumber:
        print('You guess is too high')
    elif guess < secretNumber:
        print('You guess is too low')
    else:
        break
if guess == secretNumber:
    print(
        'Good Job! You guessed my number in ' +
        str(guessTaken) +
        ' guesses! ')
else:
    print('No! The number I was thinking was ' + str(secretNumber) + '!')
