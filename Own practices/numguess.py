import random

num = random.randint(1,10)

attempts = 0

while attempts < 6 :
    guess = int(input("Guess a number: "))
    attempts += 1

    if guess < num :
        print("Your guess is low")
    elif guess > num :
        print("Your guess is high")
    else :
        print("You won ")
        break

else :
    print(f"sorry you losed , my guessing number is {num}")
    