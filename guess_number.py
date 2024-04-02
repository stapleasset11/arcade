import sys
import random
from enum import Enum

def GG(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    def play_GG():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins
        class GG(Enum):
            ONE = 1
            TWO = 2
            THREE = 3


        print(" ")
        guess =  input(f"\n{name},please guess a number...\n1 2 or 3: ")


        if guess not in ["1", "2", "3"]:
            print(f"\n{name}, please enter 1, 2, or 3.")
            return play_GG()

        player_guess = int(guess)
        computer= random.choice("123")
        computer_guess = int(computer)

        print("")
        print(f"\n{name},you chose {str(GG(player_guess)).replace('GG.', '').title()}.")
        print(f"\ncomputer chose {str(GG(computer_guess)).replace('GG.', '').title()}.")
        print("")
        

        def decide_winner(player_guess, computer_guess):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            if player_guess == computer_guess:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                computer_wins += 1
                return f"🐍 computer wins!,\nSorry, {name}..😢"

        game_result = decide_winner(player_guess, computer_guess)
        print(game_result)

        nonlocal game_count
        game_count += 1
        win_percentage = int((player_wins/game_count)*100)
        print(f"\nGame count: {str(game_count)}")
        print(f"\n{name}'s wins: {str(player_wins)}")
        print(f"\nPython wins: {str(computer_wins)}")
        print(f"\nwin percentage: {str(win_percentage)} %")
        print("\nPlay again?")
        
        
        while True:
            playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

            if playagain.lower() not in [ "y","q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_GG()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye!!! {name}👋")
            else:
                return
    
    return play_GG

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    guessing_game = GG(args.name)
    guessing_game()


