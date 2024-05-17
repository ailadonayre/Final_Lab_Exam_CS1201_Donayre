import os

class Score:
    def __init__(self):
        self.data_folder = "data"
        self.scores_file = "scores.txt"
        self.scores_file_path = os.path.join(self.data_folder, self.scores_file)

    def load_scores(self):
        scores = []
        CEND = '\33[0m'
        CBLUE = '\33[34m'

        if os.path.exists(self.scores_file_path):
            with open(self.scores_file_path, "r") as file:
                for line in file:
                    scores.append(line.strip().split(', '))
            return scores
        else:
            print(CBLUE + "\t>> " + CEND + "No scores recorded yet.")
            return None

    def save_scores(self, username, scores, wins, date):
        CEND = '\33[0m'
        CBLUE = '\33[34m'

        try:
            with open(self.scores_file_path, "a") as file:
                file.write(f"{username}, {scores}, {wins}, {date}\n")
        except IOError:
            print(CBLUE + "\t>> " + CEND + "[IOError] Unable to save data.")


