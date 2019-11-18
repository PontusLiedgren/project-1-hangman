# hangman.py
# 
# Author: Pontus Liedgren, 2019
# https://github.com/PontusLiedgren/project-1-hangman

# imports
import random

# funktioner
def read_txt_file(txt_file):
    '''function for reading txt_files'''

    with open(txt_file, encoding="utf-8") as text_file:
        hangman_words = text_file.read().split("\n")
    return hangman_words

def print_secret_word():
    '''function for guessed letters'''

    print("-"*50)
    print("Spelare: " + name)
    print("Tema: " + word_theme + "\n")
    print("Gissade bokstäver: " + str(guessed_letters))
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")

    print("")         

# hälsning
name = input("Vad heter du? ")

# regler och information
print(
    "\n\n\nHejsan, " + name + "!" + " Välkommen till hängagubbe! " 
    + "Målet med spelet är att lista ut det hemliga ordet.\n" 
    + "- Du har 12 gissningar på dig!\n" 
    + "- Om gissningarna tar slut innan du har listat ut ordet, förlorar du. \n" 
    + "- Om du har listat ut ordet innan gissningarna tar slut, vinner du. \n"
    + "- Du kan gissa på hela ordet om din gissning är lika lång som ordet. \n"
    + "- Om gissningen inte är lika långt som ordet eller bara en bokstav, då räknas gissningen som ogiltig. \n" 
    + "- Om bokstaven finns med i ordet förlorar du inga gissningar. \n"
    + "- Om bokstaven inte finns med i ordet förlorar du en gissning, samma sak om ordet du gissar på inte är rätt ord. \n"
    + "\n"
    + "PRO TIP! Gissa på enskilda bokstäver om du inte är helt säker på vilket det hemliga ordet är!"
    )

# temat på hemliga ordet
word_theme = input("\n" + "Välj tema på det hemliga ordet: A: Huvudstäder | B: Mat | C: Blandat  : ").lower()

# om temat är huvudstäder
if word_theme == "a" or word_theme == "huvudstäder":
    word_theme = "Huvudstäder"
    print("Temat är huvudstäder!")
    hangman_words = read_txt_file("words_capitals.txt")
        
# om temat är mat
elif word_theme == "b" or word_theme == "mat":
    word_theme = "Mat"
    print("Temat är mat!")
    hangman_words = read_txt_file("words_foods.txt")
        
# om temat är blandat
elif word_theme == "c" or word_theme == "blandat":
    word_theme = "Blandat"
    print("Temat är blandat!")
    hangman_words = read_txt_file("words_random.txt")

# start         
secret_word = random.choice(hangman_words)
turns = 12
guessed_letters = []
correct_letters = []
isPlaying = True
hangedman = ("_____________________" + "\n| /                |" + "\n|/              (X c X)" + "\n|                --|--" + "\n|                 / \\" + "\n| Ordet var: " + secret_word.upper()  + "\n|_______________________")
happyman = ("(OcO)\n" + "\\_|_\n" + " | |\\")

# huvudloop
while isPlaying:
    print_secret_word()

    guess = input("Gissning: ").lower()
    
    guessed_letter_count_secret_word = secret_word.count(guess)
    if len(guess) == len(secret_word):
        if guess.lower() != secret_word.lower():
            turns -= 1
            print("Fel! Du har " + str(turns) + " gissningar kvar. \n")
        elif guess.lower() == secret_word.lower():
            isPlaying = False
            print("Bra jobbat, " + name + "! Du räddade gubben.\n" + happyman)
            print("Ordet var: " + secret_word.upper())
            break
    if len(guess) != 1 or len(guess) != len(secret_word): 
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
                    print("Bra jobbat, " + name + "! Du räddade gubben.\n" + happyman)
                    print("Ordet var: " + secret_word.upper())
            else:
                turns -= 1
                print("Fel! Du har " + str(turns) + " gissningar kvar. \n")
        else: 
            print("Du har redan gissat: " + guess + " \n") 
    if turns == 0:
        isPlaying = False
        print("Oops! " + name + ", där hängdes en gubbe!")
        print(hangedman) 
