# hangman.py
# 
# Author: Pontus Liedgren, 2019
# https://github.com/PontusLiedgren/project-1-hangman

import random

# hälsning
name = input("Vad heter du? ")
# print("\n" + "Välkommen " + name + "! " + "Är du redo att spela Hängagubbe? \n")

# hemligt_ord, omgångar, listor 
hangman_words = ['gubbe', 'by', 'tyskland', 'fönster', 'nationalencyclopedi', 'dator', 'brontosaurus', 'bänkpress']
words_capitals = ['',]
secret_word = random.choice(hangman_words)  
turns = 12
guessed_letters = []
correct_letters = []
isPlaying = True

# regler
print(
    "Hejsan, " + name + "!" + " Välkommen till hängagubbe! " 
    + "Målet med spelet är att lista ut det hemliga ordet.\n" 
    + "- Du har 12 gissningar på dig!\n" 
    + "- Om gissningarna tar slut innan du har listat ut ordet, förlorar du! \n" 
    + "- Om du har listat ut ordet innan gissningarna tar slut, vinner du! \n"
    + "- Du kan bara gissa en bokstav i taget! \n" 
    + "- Om bokstaven finns med i ordet förlorar du inga gissningar! \n"
    + "- Om bokstaven inte finns med i ordet förlorar du en gissning! \n"
    + "- Du kan inte gissa på flera bokstäver samtidigt!"
    )

# temat på hemliga ordet


# funktion för gissade bokstäver. 
def print_secret_word():
    print("-----------------------------------------------------------------------")
    print("Spelare: " + name.upper() + "\n")
    print("Gissade bokstäver: " + str(guessed_letters))
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
                    print("Bra jobbat, du räddade gubben!")
                    print("Ordet var: " + secret_word.upper())
            else:
                turns -= 1
                print("Fel! Du har " + str(turns) + " gissningar kvar. \n")
        else: 
            print("Du har redan gissat: " + guess + " \n")         
    if turns == 0:
        isPlaying = False
        print("Oops! Där hängdes en gubbe!") 
        print("Ordet var: " + secret_word.upper()) 