#pick a secret word at random
#initalize the show word by putting * for length of word and displaying the word
#FOREVER LOOP:
#  ask the user to guess a letter
#  check th eletter (have they guessed it already)
#  check the letter (see if it is in the secret word)
#  update the show word
#  check for game over

import random

print("guess my word")

def update_show_word(newestGuess, d, s):
    result = ""
    for l in range(len(d)):
        if newestGuess == s[l]:
            result  += newestGuess
        else:
            result += d[l]

    return result

words = ["catapult","funnishment", "rose", "fisher","hulman"]

counter = 0

guessedLetters = []
showWord = ""

secretWord = words[random.randint(1,len(words))-1]
print(secretWord)

showWord = "*" * len(secretWord)
#print(showWord)



while showWord != secretWord:

    print("word so far:",showWord)
    #print(showWord)

    letter = input("GUESS A LETTER: ")
    #take a letter input

    print()
    #print a line to seperate and make it look nicer


    #check to see if the letter has already been guessed
    if letter in guessedLetters:
        print("you already guessed that")
        continue


    #check to make sure single letters were put in instead of words
    if len(letter)>1:
        print("please use single letters")
        continue

    #guess counter increase
    counter += 1

    #add the guessed letters to the array
    guessedLetters.append(letter)

    tempWord = showWord
    showWord = update_show_word(letter,showWord,secretWord)
    #update the displayed word to display the updated word with the new letters there

    #check to see if they sucsefully guessed a letter
    if tempWord != showWord:
        print("CONGRATS! The letter", letter, "appers in the word.")
    else:
        print("SORRY! this letter does not appear in the word :(")


    print("already guessed letters:",guessedLetters)


print("YOU GOT THE WORD:", secretWord, "in", counter, "tries")
#after the game has completed.
