#---------------------------- Fontions du menu-------------------

# Affiche le menu 
def display_menu():
    print("\nMenu:")
    print("1. Start a new game")
    print("2. Quit")


# -------------------------------------------------------------------


# Enregistre la réponse de l'utilisateur
def get_user_choice():
    return input("Choose an option (1 or 2): ")

# -------------------------------------------------------------------

# Affiche un mot quand la touche 2 est tapé
def show_goodbye_message():
    print("Goodbye!")


# -------------------------------------------------------------------

# affiche la difficulté et les la taille des grilles en fonction de celle ci
def show_difficulty_options():
    print("\nDifficulty Options:")
    print("1. Easy: 10 x 5 grid, words less than 4 letters")
    print("2. Medium: 15 x 7 grid, words between 4 and 6 letters")
    print("3. Hard: 30 x 15 grid, words between 6 and 9 letters")
    print("4. Back to main menu")



# -------------------------------------------------------------------

# Enregistre le choix de l'utilisateur
def get_difficulty_choice():
    return input("Choose a difficulty option (1, 2, 3, or 4): ")


# -------------------------------------------------------------------

# affiche un message  à l'utilisateur qu'il a fait un choix invalide dans le menu
def show_invalid_choice_message():
    print("Invalid choice. Please choose a valid option.")
