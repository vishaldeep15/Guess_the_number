# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

secret_number = 0
guess_left = 0
num_range = 0
number_of_guesses = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global num_range
    global number_of_guesses
    global guess_left
    
    guess_left = 0
    if num_range:
        secret_number = random.randrange(0,1000)
        number_of_guesses = 10
        print "New game started"
        print "Please select a number in the range of 0 to 1000"
    else:
        secret_number = random.randrange(0,100)
        number_of_guesses = 7
        print "New game started"
        print "Please select a number in the range of 0 to 100"
        
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global num_range
    num_range = 0
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global num_range
    num_range = 1
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guess_left
    global secret_number
    global num_range
    global number_of_guesses 
    guess = int(guess)
    
    guess_left += 1
    
    if guess_left == number_of_guesses + 1 :
        print "You lost the Game"
        new_game()
    else : 
        print "Number of Guess left:", number_of_guesses - guess_left +1
      
    print "Guess was", guess
   
    if secret_number > guess:
        print "Higher"
    elif secret_number < guess:
        print "Lower"
    else:
        print "Correct"
        num_range = 0
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess Game", 200, 200)

# register event handlers for control elements and start frame
guess = frame.add_input("Guess number: ", input_guess, 50)
range100 = frame.add_button("Range is [0,100)", range100, 150)
range1000 = frame.add_button("Range is [0,1000)", range1000, 150)


# call new_game 
new_game()

frame.start()
# always remember to check your completed program against the grading rubric
