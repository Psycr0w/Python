import random
from pyparsing import ParseBaseException
import string

from logoAscii import logo
from manAscii import manlist
from words import words


def hangman():
    print(logo)

    word = random.choice(words).upper()
    wordletters = set(word)
    #alphabet = set(string.ascii_uppercase)

    used = set()

    lives = len(manlist)

    print("A word was chosen, start guessing!")

    while len(wordletters) > 0 and lives > 0:
        wordList = [letter if letter in used else "#" for letter in word]

        print(manlist[(7 - lives)], "\n")

        print('The word we are looking for is: ', '-'.join(wordList))
        print('You have ' + str(lives) + " lives, and used these letters already: " + ' '.join(used))

        userletter = input('Guess a letter: ').upper()
        if userletter not in used:
            used.add(userletter)
        else:
            print("This letter was already used.")
            continue
        if userletter not in wordletters:
            lives -= 1
            print(userletter + ' is not in our word.')
        else:
            wordletters.remove(userletter)

    if len(wordletters) == 0:
        print("You won!")
        print("The word was " + word)

    elif lives == 0:
        print("The word we were looking for was: " + word)
        print("Better Luck next time!")


if __name__ == '__main__':
    hangman()