#number guessing game.
import random

#lets user pick the range in which the computer will pick a random number from.
top_range = input("type a number: ")

#check to make sure the user has typed a number and change it from a string to digit
if top_range.isdigit():
    top_range = int(top_range)
    #check if the number typed is above 0
    if top_range <= 0:
        print('Please type a larger number next time.')
        quit()
#print this message if a number has not been inputted
else: 
    print('Please type a number next time.')
    quit()
#prints a random number between 0 and the number the user has inputted.
random_number = random.randint(0, top_range)
#count the number of times the user makes a guess
guesses = 0

#allow users to continue to type numbers until they guess the correct one.
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    #check to make sure the user has typed a number and change it from a string to digit
    if user_guess.isdigit():
        user_guess = int(user_guess)
    #print this message if a number has not been inputted
    else: 
        print('Please type a number next time.')
        continue
    #if statement to check the users guess was correct
    if user_guess == random_number:
        print("GOOD JOB!! You got it!")
        break
    #if statement to let the user know if they were above or below the right number
    elif user_guess > random_number:
        print("Your guess was too high! Try again!")
    else:
        print("Your guess was too low! Try again!")

#To let the user know how many guesses it took to get the answer
print("You got it in", guesses, "guesses. Well Done!")