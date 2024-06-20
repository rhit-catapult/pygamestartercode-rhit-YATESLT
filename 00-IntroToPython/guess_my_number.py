import random

print("Guess My Number")

print("I'm thinking of a number between 1 and 100")

print("Try to guess it in as few attempts as possible")

# this is a comment

# select a secret random number

#start a counter for guesses at 0

#forever loop that can break from later on

#    increment the counter by 1
#    ask the user to make a guess
#   if guess > number say to large
#    if guess < number say to small
#    if guess is spot on, end the game and say congrats
#tell the user how many guesses it took



randomNum = (int)(random.random()*100)+1
counter = 0
print(randomNum)
inp = -10

while inp != randomNum:
    inp = input("PICK A NUMBER 1-100: ")

    inp = int(inp)

    counter = counter+1
    if inp < randomNum:
        print("TOO LOW")
    elif inp > randomNum:
        print("TOO HIGH")

print("YOU GOT THE NUMBER",str(randomNum), "IN", str(counter),  "TRIES! ")
