import time
from random_word import RandomWords





name = input("What is your name? ")

print("Hello, " + name, "Time to play hangman!")

time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# Return a single random word
r = RandomWords()
word = r.get_random_word()


guesses = ''
turns = 10
misses = ''

while turns > 0:
    failed = 0
    print("Misses so far: " + misses)
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_", end=' ')
            failed += 1
    if failed == 0:
        print("Congratulations! You won!")
        break

    guess = input("Please, guess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        misses +=guess
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Lose")
    else:
        print("Great Guess!")
