

import random
from wordlist import words
from hangmanlivesvisual import hangmanLivesVisualDict

import string

def getValidWord(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def playHangman():
    getWord = getValidWord(words)
    lettersOfWord = set(getWord)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    guessedLetters = set() # what the user has guessed 

    livesOfPlayer = 7

    # getting user input
    while len(lettersOfWord) > 0  and livesOfPlayer > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd'])
        print("You have", livesOfPlayer," lives left and you have used these letters",' '.join(guessedLetters))

        # what current word is (ie W - RD)
        wordList = [letter if letter in guessedLetters else '-' for letter in getWord]
        print('Current word: ', ' '.join(wordList))


        guessLetter = input("Guess a letter: ").upper()
        if guessLetter in alphabet - guessedLetters:
            guessedLetters.add(guessLetter)
            if guessLetter in lettersOfWord:
                lettersOfWord.remove(guessLetter)
            
            else:
                livesOfPlayer = livesOfPlayer - 1 # takes away a life if wrong letter
                print(hangmanLivesVisualDict[livesOfPlayer]) #prints the visual of lives left for every wrong guess
                print("That letter is not in the word!!")

        elif guessLetter in guessedLetters:
            print("\nYou have already guessed that character. Please try again.")

        else: 
            print("\nInvalid character. Please try again")

    # gets here when len(lettersOfWord) == 0 OR when livesOfPlayer == 0
    if livesOfPlayer == 0:
        print(hangmanLivesVisualDict[livesOfPlayer])
        print('You died, sorry. The word was',getWord)
    else:
        print('Good Job! You guessed the word', getWord, '!!')
        


playHangman()







