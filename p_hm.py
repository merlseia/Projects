word_list = ["Monkey", "Cat", "Chicken", "Horse", "Shark", "Snake"]

import random

selected_word = random.choice(word_list).lower()

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

guessed_letters = []

while True:
    guessed_word = display_word(selected_word, guessed_letters)
    print("Güncel durum: ", guessed_word)


    if guessed_word == selected_word:
        print("Tebrikler! Kazandınız.")
        break

    guess = input("Bir harf tahmin edin: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Geçersiz giriş. Lütfen bir harf girin.")
        continue

    if guess in guessed_letters:
        print("Bu harfi zaten tahmin ettiniz.")
        continue

    guessed_letters.append(guess)

    if guess not in selected_word:
        print("Tahmininiz yanlış.")