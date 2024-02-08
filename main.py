from time import sleep
import random

play_again = 1


def get_random_word():
    words = open("wordlist.txt").read().splitlines()
    global word
    word = random.choice(words)
    word = list(word)


def play_again_check():
    try:
        global play_again
        play_again = int(
            input("Would you like to play again? Enter 1 for yes and 2 for no: ")
        )
        if play_again == 1:
            game()
        elif play_again == 2:
            print("Thanks for playing!")
            sleep(2)
            exit()
        else:
            print("Invalid input, please enter '1' or '2'.")
            play_again_check()
    except ValueError:
        print("Invalid input, please enter '1' or '2'.")
        play_again_check()


def game():
    get_random_word()
    word_length = len(word)
    correct_letters = ["_"] * word_length
    incorrect_letters = []
    tries = 6
    print(f"Welcome to hangman, your word is {word_length} letters long.")
    print("")
    print(f"You have {tries} tries to guess the word.")
    guess = input("Please guess a letter or word: ").lower()
    while tries > 0:
        if guess in word:
            for i in range(word_length):
                if guess == word[i] and len(guess) == 1:
                    correct_letters[i] = guess
            print(" ".join(correct_letters))
            print("")
            if "_" not in correct_letters:
                print("You win!")
                play_again_check()
            guess = input("Please guess a letter or word: ").lower()
        elif guess in incorrect_letters:
            print(f"You already guessed {guess}.")
            print("")
            guess = input("Please guess a letter or word: ").lower()
        else:
            print(" ".join(correct_letters))
            print("")
            incorrect_letters.append(guess)
            tries -= 1
            print(f"Wrong guess, you have {tries} tries left.")
            print("")
            guess = input("Please guess a letter or word: ").lower()
        if tries == 0:
            print("You lose!")
            print(f'The word was: {"".join(word)}')
            play_again_check()


game()
