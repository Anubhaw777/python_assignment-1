'''Program for Number Guessing Game'''

#importing module
import random

answer = random.randint(1, 100)
attempts = 5 #initializing the attempts to 5

print("Welcome to the Number Guessing Game!\nGuess a number between 1 and 100.")


while attempts > 0:
    guess = int(input(f"Attempts left ({attempts}): "))  
 
 #applying loop
    if guess == answer:
        print("🎉 Congratulations! You guessed it right!")
        break
    elif guess < answer:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1
 
 #prints the output
if attempts == 0:
    print("Game Over! The correct number was", answer)
