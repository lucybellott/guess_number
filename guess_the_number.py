import random

def random_num():
    play_again = "y"
    while play_again.lower() == "y":
        comp_num = random.randrange(0, 10)
        user_num = int(input("Pick a number between 0-10!: "))
        while user_num != comp_num:
            user_num = int(input("Incorrect. Try again: "))
        play_again = input("Winner! Would you like to play again?(y or n): ")
    print("Thanks for playing!")

random_num()