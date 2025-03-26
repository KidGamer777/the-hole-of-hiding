"""Create a basic game selector and player. 

The selection screen should display this:

Select a game!
1. Roulette
2. Math Quiz
3. The Waiting Game
4. Quit

After this it should take an input for the number corresponding to the game. Be sure to error check that the number is indeed between 1 and 4.

If not, please output Invalid selection. Please pick a valid game number. and ask again.

The Selections should use functions to run the particular game. If you code the entire game within the if condition, it'll be points off.



roulette:

At the beginning seed the random number generator with the seed 10 with random.seed(10) This is for grading purposes.

Afterwards, generate a random number between 1 and 10. Prompt the player to guess by asking 

Guess a number between 1 and 10: 
If the guess right, print You Win! Otherwise print Wrong! Guess again! before prompting them for another input with the same message as above.
mathQuiz:
As before, seed the random number generator with the seed 10. Now generate 2 random numbers and ask the user
What is {firstNumber} + {secondNumber}? 
If they guess right, once again print You Win! and if they guess wrong print Wrong! Guess again! before repeating the same prompt as above. 
theWaitingGame:
Wait 5 seconds, then print You Win! then return.
Upon completion of any game, the game selection should repeat to prompt the user to select another game. This should only end if the user inputs 4 as their game selection in order to quit.
"""

# Importing the required libraries
import random
import time 
import math 

# Defining the Roulette function
def roulette():
    random.seed(10)
    target = random.randint(1, 10)
    while True:
        guess_roulette = int(input("Guess a number between 1 and 10: "))
        if guess_roulette == target:
            print("You Win!")
            break
        else:
            print("Wrong! Guess again.")

# Defining the Math Quiz function
def mathQuiz():
    random.seed(10)
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    added = num_1 + num_2
    while True:
        guess_math = int(input(f"What is {num_1} + {num_2}? "))
        if guess_math == added:
            print("You Win!") 
            break
        else:
            print("Wrong! Guess again.")   

# Defining The Waiting Game function
def theWaitingGame():
    time.sleep(5)
    print("You Win!")

# Calling the game selection menu, error checking 
while True:
    game = input("Select a game! \n 1. Roulette \n 2. Math Quiz \n 3. The Waiting Game \n 4. Quit \n")
    if game == "1":
        roulette()
    elif game == "2":
        mathQuiz()
    elif game == "3":
       theWaitingGame()
    elif game == "4":
        break 
    else:
        print("Invalid selection. Please pick a valid game number.")  