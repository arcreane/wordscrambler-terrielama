import random

#Cette fonction permet de créer une grille de mots croisés en fonction de la difficulté 
def generate_crossword_grid(difficulty):
    grid_size = determine_grid_size(difficulty)
    grid = [[' ' for _ in range(grid_size[1])] for _ in range(grid_size[0])]
    
    # Charger la liste de mots depuis un fichier (liste_francais.txt)
    words = load_words("liste_francais.txt")

    for word in words:
        place_word_in_grid(word, grid)

    return grid


# -------------------------------------------------------------------

# Cette fonction permet de déterminer la taille de la grille en fonction du niveau de difficulté
def determine_grid_size(difficulty):
    grid_sizes = {"easy": (5, 5), "medium": (8, 8), "hard": (10, 10)}
    return grid_sizes.get(difficulty.lower(), (5, 5))


# -------------------------------------------------------------------

# Cette fonction permet de charge les mots à partir d'un fichier texte 
def load_words(file_name):
    with open(file_name, 'r', encoding='utf-8') as file_words:
        words = [word.strip().upper() for word in file_words.readlines()]
        random.shuffle(words)
        return words
    
# -------------------------------------------------------------------

# Cette fonction vérifie si un mot peut être placé dans la grille  à partir d'une position (x et y)
def can_place_word(word, x, y, delta_x, delta_y, grid):
    for i in range(len(word)):
        new_x = x + i * delta_x
        new_y = y + i * delta_y

        if not (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid)):
            return False
        if grid[new_y][new_x] != " " and grid[new_y][new_x] != word[i]:
            return False
    return True


# -------------------------------------------------------------------


# Cette fonction permet placer un mot dans la grille
def place_word_in_grid(word, grid):
    # Horizontal, vertical, diagonale bas-droite, diagonale haut-droite (ne fonctionne pas)
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  

    random.shuffle(directions)

    for direction in directions:
        delta_x, delta_y = direction

        for i in range(len(word)):
            x = random.randint(0, len(grid[0]) - 1)
            y = random.randint(0, len(grid) - 1)

            if can_place_word(word, x, y, delta_x, delta_y, grid):
                for j in range(len(word)):
                    grid[y + j * delta_y][x + j * delta_x] = word[j]
                return

# -------------------------------------------------------------------


# Cette fonction affiche la grille
def display_grid(grid):
    for row in grid:
        print(' '.join(row))

# -------------------------------------------------------------------


def main():
    difficulty = input("Choisissez la difficulté (easy, medium, hard) : ")
    crossword_grid = generate_crossword_grid(difficulty)
    display_grid(crossword_grid)

if __name__ == "__main__":
    main()
