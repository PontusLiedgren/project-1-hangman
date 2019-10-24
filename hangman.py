import random

#Hälsning
name = input("Vad heter du? ")
print("Välkommen " + name + "! " + "Är du redo att spela Hänga Gubben? ")

#Ordlista, omgångar 
hangman_words = ['gubbe', 'by', 'tyskland', 'fönster', 'nationalencyclopedi', 'dator', 'brontosaurus', 'bänkpress']
secret_word = random.choice(hangman_words)  
turns = 2*len(secret_word)
guessed_letters = []

#funktion
for user_guess in secret_word:
    print("_ " *(len(secret_word)))
    guess = input("Guess a letter: ").lower()
    if guess not in secret_word:
        turns -= 1
        print("Wrong! You have " + str(turns) + " guesses left.")
    elif guess in secret_word:
        print("Correct! You have " + str(turns) + " guesses left.")
        print(guess in secret_word)
    for guess in guessed_letters:
        print("Ops, du har redan sagt den bokstaven!")
        guessed_letters.append(guess)


if turns == 0:
    print("You lose")
else:
    print()




