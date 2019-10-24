# hangman.py
# 
# Author: Pontus Liedgren, 2019
# https://github.com/PontusLiedgren/project-1-hangman

import random

# hälsning
name = input("Vad heter du? ")
print(50*"\n" + "Välkommen " + name + "! " + "Är du redo att spela Hängagubbe? \n")

# hemligt_ord, omgångar, listor 
hangman_words = ['gubbe', 'by', 'tyskland', 'fönster', 'nationalencyclopedi', 'dator', 'brontosaurus', 'bänkpress']
secret_word = random.choice(hangman_words)  
turns = 12
guessed_letters = []
correct_letters = []
isPlaying = True



# funktion för gissade bokstäver. 
def print_secret_word():
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")

    print("")
    print("\n")          

# huvudloop
while isPlaying:
    print_secret_word()

    guess = input("Guess a letter: ").lower()
    guessed_letter_count_secret_word = secret_word.count(guess)
    if len(guess) > 1: 
        print("Ogiltig inmatning! \n")
    if len(guess) == 1:
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            if guess in secret_word:
                print("Korrekt! Du har " + str(turns) + " gissningar kvar. \n")
                for letter in range(guessed_letter_count_secret_word):
                    correct_letters.append(guess) 
                if(len(correct_letters) == len(secret_word)):
                    isPlaying = False
                    print("Bra jobbat du räddade gubben! Ordet var: " + secret_word.upper())
            else:
                turns -= 1
                print("Fel! Du har " + str(turns) + " gissningar kvar. \n")
        else: 
            print("Du har redan gissat: " + guess + " \n")         
    if turns == 0:
        isPlaying = False
        print("Oops! Där hängdes en gubbe! Ordet var: " + secret_word.upper()) 
        
        

