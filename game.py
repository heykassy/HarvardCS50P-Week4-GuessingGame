from random import randint

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

random_int = randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if random_int < guess:
                print("Too large!")
            elif random_int > guess:
                print("Too small!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass