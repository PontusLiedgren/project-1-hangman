# hangman.py
# 
# Author: Pontus Liedgren, 2019
# https://github.com/PontusLiedgren/project-1-hangman

import random

# hälsning
name = input("Vad heter du? ")
print("Välkommen " + name + "! " + "Är du redo att spela Hängagubbe? ")

# ordlista, omgångar 
hangman_words = ['gubbe', 'by', 'tyskland', 'fönster', 'nationalencyclopedi', 'dator', 'brontosaurus', 'bänkpress']
secret_word = random.choice(hangman_words)  
turns = 12
guessed_letters = []

isPlaying = True

# funktion för gissade bokstäver. 
def print_secret_word():
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")

    print("")          

# huvudloop
while isPlaying:
    print_secret_word()

    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)

    if guess in secret_word:
        print("Korrekt! Du har " + str(turns) + " kvar")
    else:
        turns -= 1
        print("Fel! Du har " + str(turns) + " kvar")
    if turns == 0:
        isPlaying = False
        print("Du förlorade! Ordet var: " + secret_word)
    for letter in secret_word: 
        if letter in guessed_letters:

# För nästa gång: kolla om bokstäverna i secret_word finns i guessed_letters om alla finns isPlaying = False         
        


