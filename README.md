# HarvardCS50P-Week4-GuessingGame

CS50P's Introduction to Programming with Python
Week 4, Problem Set 4

Project specifications:

"Guessing Game
I’m thinking of a number between 1 and 100…

What is it?
In a file called game.py, implement a program that:

Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and , inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.

How to Test
Here’s how to test your code manually:

Run your program with python game.py. Type cat at a prompt that says Level: and press Enter. Your program should reprompt you:
Level:   
Run your program with python game.py. Type -1 at a prompt that says Level: and press Enter. Your program should reprompt you:
Level:   
Run your program with python game.py. Type 10 at a prompt that says Level: and press Enter. Your program should now be ready to accept guesses:
Guess:   
Run your program with python game.py. Type 10 at a prompt that says Level: and press Enter. Then type cat. Your program should reprompt you:
Guess:   
Run your program with python game.py. Type 10 at a prompt that says Level: and press Enter. Then type -1. Your program should reprompt you:
Guess:   
Run your program with python game.py. Type 1 at a prompt that says Level: and press Enter. Then type 1. Your program should output:
Just right!  
There’s only one possible number the answer could be!

Run your program with python game.py. Type 10 at a prompt that says Level: and press Enter. Then type 100. Your program should output:
Too large!  
Looks like you’re guessing outside the range you specified.

Run your program with python game.py. Type 10000 at a prompt that says Level: and press Enter. Then type 1. Your program should output:
Too small!  
Most likely, anyways: you might get lucky and see Just right!. But it would certainly be odd for you to see Just right! every time. And certainly you shouldn’t see Too large!.
"
