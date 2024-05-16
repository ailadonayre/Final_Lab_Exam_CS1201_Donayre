import os
from utils.user import User
from utils.dice_game import DiceGame

class UserManager(User):
    def __init__(self, current_user = None):
        super().__init__("", "", 0, 0)
        self.current_user = current_user

    def validate_username(self):
        CEND = '\33[0m'
        CBLUE = '\33[34m'
        
        if len(self.username) >= 4:
            return True
        else:
            print(CBLUE + "\t>> " + CEND + "Your username must have at least four (4) characters. Please try again.")
            return False

    def validate_password(self):
        CEND = '\33[0m'
        CBLUE = '\33[34m'

        if len(self.password) >= 8:
            return True
        else:
            print(CBLUE + "\t>> " + CEND + "Your password must have at least eight (8) characters. Please try again.")
            return False

    def register(self):
        user_list = self.load_users()
        CEND = '\33[0m'
        CITALIC   = '\33[3m'
        CYELLOW = '\33[33m'
        CBLUE = '\33[34m'

        print("_" * 100, "\n")
        print((CYELLOW + "Register" + CEND + " an account.").center(100))

        while True:
            self.username = input(CYELLOW + "\n> " + CEND + "Enter your username " + CITALIC + "(leave blank to exit program):" + CEND + " ")

            if not self.username:
                print(CBLUE + "\t>> " + CEND + "User registration was cancelled.")
                return

            if any(username == self.username for username, password, score, wins in user_list):
                print(CBLUE + "\t>> " + CEND + "Username already exists. Please try again.")
                continue

            if not self.validate_username():
                continue

            self.password = input(CYELLOW + "> " + CEND + "Enter your password " + CITALIC + "(leave blank to exit program):" + CEND + " ")
            if not self.validate_password():
                continue

            else:
                self.new_user = User(self.username, self.password, 0, 0)
                user_list.append((self.username, self.password, 0, 0))
                self.save_users(user_list)
                print(CBLUE + "\t>> " + CEND + "You have registered successfully!")
                return

    def sign_in(self):
        user_list = self.load_users()
        CEND = '\33[0m'
        CITALIC   = '\33[3m'
        CYELLOW = '\33[33m'
        CBLUE = '\33[34m'

        print("_" * 100, "\n")
        print((CYELLOW + "Sign in" + CEND + " to your account.").center(100))

        while True:
            self.username = input(CYELLOW + "\n> " + CEND + "Enter your username " + CITALIC + "(leave blank to exit program):" + CEND + " ")

            if not self.username:
                print(CBLUE + "\t>> " + CEND + "Sign in cancelled.")
                return

            matching_users = [user for user in user_list if user[0] == self.username]

            if not matching_users:
                print(CBLUE + "\t>> " + CEND + "User not found in list. Kindly register first.")
                self.register()
                return

            self.password = input(CYELLOW + "> " + CEND + "Enter your password " + CITALIC + "(leave blank to exit program):" + CEND + " ")

            matching_user = next((user for user in matching_users if user[1] == self.password), None)

            if not matching_user:
                print(CBLUE + "\t>> " + CEND + "Your password is incorrect. Please try again.")
                continue
            else:
                print(CBLUE + "\t>> " + CEND + "You have signed in successfully.")
                self.current_user = User(*matching_user)
                DiceGame.menu(self)
                break