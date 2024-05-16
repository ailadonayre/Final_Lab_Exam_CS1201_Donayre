import random
import os
from utils.user_manager import *
from utils.score import *
from datetime import datetime

class DiceGame():
    def __init__(self, current_user):
        self.current_user = current_user
        self.current_user.score = int(self.current_user.score)
        self.current_user.wins = int(self.current_user.wins)

    def play_game(self):
        CEND = '\33[0m'
        CBOLD = '\33[1m'
        CITALIC   = '\33[3m'
        CYELLOW = '\33[33m'
        CBLUE = '\33[34m'

        print("_" * 100, "\n")
        print((CYELLOW + "Roll the Dice!" + CEND).center(100), "\n")
        print(CITALIC + "Starting a new game..." + CEND)

        while True:
            user_points = 0
            CPU_points = 0

            for i in range(3):
                print(CITALIC + "\nRolling the dice..." + CEND)
                user_dice = random.randint(1, 6)
                CPU_dice = random.randint(1, 6)

                print(CBOLD + f"{self.current_user.username} " + CEND + f"rolled: {user_dice}")
                print(CBOLD + "CPU " + CEND + f"rolled: {CPU_dice}")

                if user_dice > CPU_dice:
                    print(CBLUE + f"{self.current_user.username} " + CEND + "wins this round!")
                    user_points += 1
                elif user_dice < CPU_dice:
                    print(CBLUE + "CPU " + CEND + "wins this round!")
                    CPU_points += 1
                else:
                    print(CBLUE + "It's a tie! " + CEND + CITALIC + "Rolling again..." + CEND)
                    while user_dice == CPU_dice:
                        user_dice = random.randint(1, 6)
                        CPU_dice = random.randint(1, 6)
                        print(CITALIC + "\nRolling the dice again..." + CEND)

                        print(CBOLD + f"{self.current_user.username} " + CEND + f"rolled: {user_dice}")
                        print(CBOLD + "CPU " + CEND + f"rolled: {CPU_dice}")

                        if user_dice > CPU_dice:
                            print(CBLUE + f"{self.current_user.username} " + CEND + "wins this round!")
                            user_points += 1
                        elif user_dice < CPU_dice:
                            print(CBLUE + "CPU " + CEND + "wins this round!")
                            CPU_points += 1

            self.current_user.score += user_points

            if user_points > CPU_points:
                self.current_user.score += 3
                self.current_user.wins += 1
                print(CBOLD + "\nCongratulations, " + CEND + CBOLD + CYELLOW + f"{self.current_user.username}! " + CEND + "You won this stage!")
                print(CBOLD + CBLUE + "\t>> " + CEND + CBOLD + f"Score: " + CEND + CYELLOW + f"{self.current_user.score}" + CEND)
                print(CBOLD + CBLUE + "\t>> " + CEND + CBOLD + f"Wins: " + CEND + CYELLOW + f"{self.current_user.wins}" + CEND)

                user_scores = Score()
                score_date = datetime.now().strftime("%Y-%m-%d")

                user_scores.save_scores(self.current_user.username, self.current_user.score, self.current_user.wins, score_date)

                try:
                    choice = int(input(CYELLOW + "\n> " + CEND + "Would you like to " + CBLUE + "(1) " + CEND + "continue to the next stage or " + CBLUE + "(0) " + CEND + "go back to the menu? "))
                    if choice == 1:
                        continue
                    if choice == 0:
                        print(CITALIC + "Going back to the menu..."+ CEND)
                        DiceGame.menu(self)
                        break
                    else:
                        print(CBLUE + "\t>> " + CEND + "Invalid input. " + CITALIC + "Exiting the game..." + CEND)
                        DiceGame.menu(self)
                        break
                except ValueError as e:
                    print(CBLUE + "\t>> " + CEND + "[ValueError]", e)

            elif user_points < CPU_points:
                print(CBOLD + "\nGame over, " + CEND + CBOLD + CYELLOW + f"{self.current_user.username}. " + CEND + "You did not win any stages. Better luck next time!")
                print(CBOLD + CBLUE + "\t>> " + CEND + CBOLD + f"Score: " + CEND + CYELLOW + f"{self.current_user.score}" + CEND)
                print(CBOLD + CBLUE + "\t>> " + CEND + CBOLD + f"Wins: " + CEND + CYELLOW + f"{self.current_user.wins}" + CEND)

                user_scores = Score()
                score_date = datetime.now().strftime("%Y-%m-%d")

                user_scores.save_scores(self.current_user.username, self.current_user.score, self.current_user.wins, score_date)

                while True:
                    self.current_user.score = 0

                    choice = input(CYELLOW + "\n> " + CEND + "Would you like to " + CBLUE + "(A) " + CEND + "start a new game or " + CBLUE + "(B) " + CEND + "go back to the menu? ").upper()
                    try:
                        if choice == 'A':
                            DiceGame.play_game(self)
                            break
                        elif choice == 'B':
                            DiceGame.menu(self)
                            break
                        else:
                            print(CBLUE + "\t>> " + CEND + "Invalid input. Please try again.")
                            continue
                    except ValueError as e:
                        print(CBLUE + "\t>> " + CEND + "[ValueError]", e)

    def show_top_scores(self):
        user_scores = Score()
        ranking = user_scores.load_scores()

        CEND = '\33[0m'
        CBOLD = '\33[1m'
        CYELLOW = '\33[33m'
        CBLUE = '\33[34m'

        if ranking:
            ranking.sort(key=lambda x: int(x[1]), reverse=True)
            print("_" * 100, "\n")
            print((CYELLOW + "Top 10 Highest Dice Rolls" + CEND).center(100), "\n")

            for i, (username, score, wins, score_date) in enumerate(ranking[:10], 1):
                print(f"{i}. " + CBOLD + CBLUE + f"{username} " + CEND + f"(Score: {str(score)}, Wins: {str(wins)}, Date: {score_date})")

        while True:
            choice = input(CYELLOW + "\n> " + CEND + "Would you like to go back to the menu? " + CBLUE + "(Y/N) "+ CEND).upper()
            try:
                if choice == 'Y':
                    DiceGame.menu(self)
                    break
                elif choice == 'N':
                    DiceGame.show_top_scores(self)
                    break
                else:
                    print(CBLUE + "\t>> " + CEND + "Invalid input. Please try again.")
                    continue
            except ValueError as e:
                print(CBLUE + "\t>> " + CEND + "[ValueError]", e)

    def log_out(self):
        import main

        self.current_user = None
        main.main()

    def menu(self):  
        CEND = '\33[0m'
        CYELLOW = '\33[33m'
        CBLUE = '\33[34m'

        print("_" * 100, "\n")
        print(("Welcome back, " + CYELLOW + f"{self.current_user.username}!" + CEND).center(100))
        print("\n1. Start Game")
        print("2. Show Top Scores")
        print("3. Sign Out")

        while True:
            try:
                choice = int(input(CYELLOW + "\n> " + CEND + "Kindly enter your choice: "))
                if choice == 1:
                    DiceGame.play_game(self)
                    break
                elif choice == 2:
                    DiceGame.show_top_scores(self)
                    break
                elif choice == 3:
                    DiceGame.log_out(self)
                    break
                else:
                    print(CBLUE + "\t>> " + CEND + "Invalid input. Please try again.")
            except ValueError as e:
                print(CBLUE + "\t>> " + CEND + "[ValueError]", e)