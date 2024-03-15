import random
from menu import display_menu, get_user_choice, show_goodbye_message, show_difficulty_options, get_difficulty_choice, \
    show_invalid_choice_message
from affichage import display_game_window
import sys



# Cette fonction permet de charger les lettres à partir d'un fichier
def load_letters(file_name):
    try:
        with open(file_name, 'r') as file_letters:
            letters = [letter.strip() for letter in file_letters.readlines()]
            return letters
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []
    
# -------------------------------------------------------------------

# Cette fonction ajoute un mot à une grille de mots à rechercher
def add_word(word, search_word):
    row = random.randint(0, len(search_word) - 1)
    valid_col_range = len(search_word[row]) - len(word) + 1
    if valid_col_range <= 0:
        return

    col = random.randint(0, valid_col_range)

    if col + len(word) > len(search_word[row]):
        col = len(search_word[row]) - len(word)

    for i in range(len(word)):
        search_word[row][col + i] = word[i]

def determine_grid_size(difficulty):
    grid_sizes = {"easy": (10, 5), "medium": (15, 7), "hard": (30, 15)}
    return grid_sizes[difficulty]

# ----------------------------------------------------------------------------

# Cette fonction affiche la grille de mots à rechercher dans la console
def display_word_search(word_search):
    for row in word_search:
        print(" ".join(str(cell) for cell in row).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))

# ----------------------------------------------------------------------------
        
# La fonction main exécute les différentes fonctions du fichier
def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "1":
            show_difficulty_options()
            difficulty_choice = get_difficulty_choice()

            if difficulty_choice in ["1", "2", "3"]:
                difficulty = "easy" if difficulty_choice == "1" else "medium" if difficulty_choice == "2" else "hard"
                grid_size = determine_grid_size(difficulty)
                chercherMot = [[' ' for _ in range(grid_size[1])] for _ in range(grid_size[0])]

                letters_file = "C:\\Users\\Terrie\\Desktop\\dev1\\2eme_trimestre\\python\\projet_mot_mele\\liste_francais.txt"
                letters = load_letters(letters_file)

                for i in range(grid_size[0]):
                    for j in range(grid_size[1]):
                        chercherMot[i][j] = random.choice(letters)

                words_file = "C:\\Users\\Terrie\\Desktop\\dev1\\2eme_trimestre\\python\projet_mot_mele\\mot.txt"
                words = load_letters(words_file)

                for word in words:
                    add_word(word, chercherMot)

                print(f"\nGrille pour la difficulté {difficulty} :\n")
                display_word_search(chercherMot)
                display_game_window(chercherMot, words)
                print("\n" + "=" * 30 + "\n")
            else:
                show_invalid_choice_message()

        elif choice == "2":
            show_goodbye_message()
            3

            break

        else:
            show_invalid_choice_message()

if __name__ == "__main__":
    main()