import random
import sys
import emoji
from enum import Enum

def rps(name = "PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0
    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3


        player_choice = input(f"{name},please enter...\n(1 for Rock.)\n(2 for Paper.)\n(3 for scissors)\n")
        if player_choice not in ["1","2","3"]:
            print(f"{name} ,please enter 1,2, or 3")
            return play_rps
        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)
        
        print(f"{name}, you chose { str(RPS(player)).replace('RPS.','') }.")
        print(f"Computer chose {  str(RPS(computer)).replace('RPS.','') }.")

        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins +=1
                return f"🎉 {name} you win!"
            elif player == 2 and computer == 1:
                player_wins +=1
                return f"🎉 {name} you win!"
            elif player == 3 and computer == 2:
                player_wins +=1
                return f"🎉 {name} you win!"
            elif player == computer:
                return"😲 Tie game!"
            else:
                python_wins +=1
                return f"🐍 Python wins!\n sorry,{name} ..😢"
            
        game_result = decide_winner(player,computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\npython-wins: {python_wins}")
        print(f"\nPlay again,{name}?")

        while True:
            play_again = input("\nY for Yes or \nQ to Quit\n")
            if play_again.lower() not in ["y","q"]:
                continue
            else:
                break
        if play_again.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye!!! {name}👋")
            else:
                return

    return play_rps



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="provides a personalized game experience"
        )
    parser.add_argument(
            "-n","--name",metavar="name",required= True,help="The name of the person playing the game."
        )
    args = parser.parse_args()


    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
