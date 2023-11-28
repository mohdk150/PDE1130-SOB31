import random
def compare_numbers(number, user_guess):
    #Initialize counts for both of cow and bull
    cow =0
    bull=0
    for i in range(4):
        #checking the correct position of the digit
        if user_guess[i] == number[i]:
            bull+=1
        elif user_guess[i] in number:
            cow += 1
    return cow , bull       #returns counts of cow and bulls

#initial game state
playing = True  #sign to conttinue playing
number = str(random.randint(0, 9999))  # produces a random 4 digit number
guesses = 0  #counts the number of guesses by the user

#Show the game instructions
print("Let's play a game of Cowbull!")  # explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in the wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")        #input for the user's guess
    if user_guess=="exit":        #checking if the user wants to exit the game or not
        break
    cowbullcount = compare_numbers(number, user_guess)       #comparing the user's guess with the produced number
    guesses+= 1   #incrementing the guess counter

    print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:    #checking if the user guessed the digits successfly or not
        playing = False
        print("You win the game after " + str(guesses) + "! The number was " + str(number))
        break
    else:
        print("Your guess isn't quite right, try again.")
