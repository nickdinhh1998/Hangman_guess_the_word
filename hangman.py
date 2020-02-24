#Python game - Hangman

import random

words = 'BATMAN'
user = None
turn = None
your_word = '_ ' * len(words)
your_guess = your_word[0:len(your_word)-1]
list1 = your_guess.split()

while turn == None:
    try:
        turn = int(input('Enter the number of turn you want to guess the word:'))
        if turn < len(words):
            print('Your turn must larger or equal to word length')
            turn = None
    except ValueError:
        print('Please enter valid value')
        turn = None

while user == None:
    user = input('Enter the character you guess:').upper()
    if len(user) != 1:
        print('Please enter one character')
        user = None
    for i in range(0, len(words)):
        if words[i] == user:
            list1[i] = user
    your_guess = ''.join(list1)
    print('Your guess is: {}'.format(your_guess))
    turn -= 1
    print('You have {} chances left to guess'.format(turn))
    if turn == 0:
        if your_guess == words:
            print('You win')
        else:
            print('You fail')
        break
    else:
        user = None