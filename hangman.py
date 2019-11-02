# hangman.py
# 
# Author: Pontus Liedgren, 2019
# https://github.com/PontusLiedgren/project-1-hangman

import random

# hälsning
name = input("Vad heter du? ")

# regler och information
print(
    "\n\n\nHejsan, " + name.upper() + "!" + " Välkommen till hängagubbe! " 
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
word_theme = input("\n" + "Välj tema på det hemliga ordet: A: Huvudstäder | B: Mat | C: Blandat  : ").lower()

# om temat är huvudstäder
if word_theme == "a" or word_theme == "huvudstäder":
    print("Temat är huvudstäder!")
    with open("words_capitals.txt", encoding="utf-8") as text_file:
        hangman_words = text_file.read().split("\n")
        
# om temat är mat
elif word_theme == "b" or word_theme == "mat":
    print("Temat är mat!")
    with open("words_foods.txt", encoding="utf-8") as text_file:
        hangman_words = text_file.read().split("\n")
        
# om temat är blandat
elif word_theme == "c" or word_theme == "blandat":
    print("Temat är blandat!")
    with open("words_random.txt", encoding="utf-8") as text_file:
        hangman_words = text_file.read().split("\n")

# start         
secret_word = random.choice(hangman_words)
turns = 12
guessed_letters = []
correct_letters = []
isPlaying = True

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

    guess = input("Gissa en bokstav: ").lower()
    
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
                    print("Bra jobbat " + name + "! Du räddade gubben.")
                    print("Ordet var: " + secret_word.upper())
            else:
                turns -= 1
                print("Fel! Du har " + str(turns) + " gissningar kvar. \n")
        else: 
            print("Du har redan gissat: " + guess + " \n")         
    if turns == 0:
        isPlaying = False
        print("Oops!" + name + ", där hängdes en gubbe!") 
        print("Ordet var: " + secret_word.upper()) 