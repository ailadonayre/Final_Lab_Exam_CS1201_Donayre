import os

class User:
    def __init__(self, username, password, score, wins):
        self.username = username
        self.password = password
        self.score = int(score)
        self.wins = int(wins)

        self.data_folder = "data"
        self.users_file = "users.txt"
        self.users_file_path = os.path.join(self.data_folder, self.users_file)

    def load_users(self):
        users = []

        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
            return users

        if os.path.exists(self.users_file_path):
            with open(self.users_file_path, "r") as file:
                for line in file:
                    username, password, score, wins = line.strip().split(', ')
                    users.append((username, password, int(score), int(wins)))
        return users

    def save_users(self, users):
        CEND = '\33[0m'
        CBLUE = '\33[34m'

        try:
            with open(self.users_file_path, "w") as file:
                for username, password, score, wins in users:
                    file.write(f"{username}, {password}, {score}, {wins}\n")
        except IOError:
            print(CBLUE + "\t>> " + CEND + "[IOError] Unable to save username and password.")