from utils.user_manager import UserManager
    
def main():
    user_manager = UserManager()

    while True:
        try:
            CEND = '\33[0m'
            CBOLD = '\33[1m'
            CITALIC   = '\33[3m'
            CYELLOW = '\33[33m'
            CBLUE = '\33[34m'

            print("_" * 100, "\n")
            print(("Welcome to " + CBLUE + CBOLD + "DICE GAME!" + CEND).center(100))
            print(CYELLOW + """
                            █▀▄ █ █▀▀ █▀▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀
                            █▄▀ █ █▄▄ ██▄   █▄█ █▀█ █░▀░█ ██▄ \n""" + CEND)
            print("1. Register")
            print("2. Sign in")
            print("3. Exit")

            choice = int(input(CYELLOW + "\n> " + CEND + "Kindly enter the number of your choice: "))

            if choice == 1:
                user_manager.register()
            elif choice == 2:
                user_manager.sign_in()
            elif choice == 3:
                print(CITALIC + "\nExiting the program..." + CEND)
                exit()
            else:
                print(CBLUE + "\t>> " + CEND + "Invalid input. Please try again.")
                continue
        except ValueError as e:
            print(CBLUE + "\t>> " + CEND + "[ValueError]", e)

if __name__ == "__main__":
    main()