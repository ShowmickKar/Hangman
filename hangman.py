from word_list import words
import random
import os
from time import sleep


HANGMAN_BODY = {
    8: "--------\n|      |\n|      O\n|     \|/\n|      |\n|     /|\ \n|\n|\n--------",
    7: "--------\n|      |\n|      O\n|     \|/\n|      |\n|      |\ \n|\n|\n--------",
    6: "--------\n|      |\n|      O\n|     \|/\n|      |\n|      |  \n|\n|\n--------",
    5: "--------\n|      |\n|      O\n|     \|/\n|      |\n|         \n|\n|\n--------",
    4: "--------\n|      |\n|      O\n|     \|/\n|       \n|         \n|\n|\n--------",
    3: "--------\n|      |\n|      O\n|      |/\n|       \n|         \n|\n|\n--------",
    2: "--------\n|      |\n|      O\n|      | \n|       \n|         \n|\n|\n--------",
    1: "--------\n|      |\n|      O\n|        \n|       \n|         \n|\n|\n--------",
    0: "--------\n|      |\n|       \n|        \n|       \n|         \n|\n|\n--------",
}


def pick_random_word():
    word = random.choice(words)
    while " " in word or "-" in word or len(word) < 3:
        word = random.choice(words)
    return word


def display_current_state(string, word, life):
    sleep(1)
    os.system("clear")
    print("Welcome to Hangman!\n")
    print(HANGMAN_BODY[life])
    for ch in string:
        print(ch, end="")
    print()


def complete(string):
    for ch in string:
        if ch == "-":
            return False
    return True


def game_over_scene(won, word, player_string, life):
    display_current_state(players_string, word, life)
    sleep(2)
    os.system("clear")
    word = "".join(word)
    word.upper()
    if won > 0:
        print("\n===========\nYOU WON!!!\n===========\n")
    else:
        print("\n=============\nYOU LOST!!!!\n=============\n")
    print("===========================================\n")
    print(f"THE WORD WAS {word}\n")
    print("===========================================\n")


def search(word, ch):
    for i in range(1, len(word) - 1):
        if ch == word[i]:
            return True


run = True
while run:
    word = [i for i in pick_random_word()]
    players_string = ["-" for i in range(len(word))]
    players_string[0] = word[0]
    players_string[-1] = word[-1]

    life = 8
    while True:
        if life == 0:
            game_over_scene(0, word, players_string, 0)
            break
        if complete(players_string):
            game_over_scene(1, word, players_string, life)
            break
        display_current_state(players_string, word, life)
        user_input = input("Enter a letter: ").lower()
        if search(word, user_input):
            index = word.index(user_input)
            word[index] = word[index].upper()
            players_string[index] = user_input
        else:
            life -= 1

    play_again = input("Want to play again? (y/n): ")
    if play_again == "n":
        os.system("clear")
        break
