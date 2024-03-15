import tkinter as tk

# Affichage de la fenêtre de jeu
def display_game_window(word_search, words_to_find):
    def handle_arrow_key(event):
        nonlocal row, col

        if event.keysym == "Up" and row > 0:
            row -= 1
        elif event.keysym == "Down" and row < len(word_search) - 1:
            row += 1
        elif event.keysym == "Left" and col > 0:
            col -= 1
        elif event.keysym == "Right" and col < len(word_search[0]) - 1:
            col += 1

        # Effacer la fenêtre et réafficher la grille avec la nouvelle position
        update_grid()

# -------------------------------------------------------------------
# Aette fonction sert à vérifier si la séquence actuelle de lettres formée par l'utilisateur correspond à l'un des mots à trouver dans la grille 
    def handle_enter_key(event):
        nonlocal row, col, entered_letters

        # Vérifier si la séquence actuelle correspond à l'un des mots à trouver
        current_letter = word_search[row][col]
        entered_letters.append(current_letter)

        for word in words_to_find[:]:  # Utilisation de la copie de la liste pour itérer
            if word.startswith("".join(entered_letters)):
                if "".join(entered_letters) == word:
                    print(f"Mot trouvé : {word}")
                    entered_letters.clear()
                    words_to_find.remove(word)  # Retirer le mot trouvé de la liste
                    update_grid()  # Effacer la fenêtre et réafficher la grille
                return

# -------------------------------------------------------------------

# mise à jour visuelle de la grille dans la fenêtre de jeu
    def update_grid():
        for i in range(len(word_search)):
            for j in range(len(word_search[i])):
                if i == row and j == col:
                    if word_search[i][j]:
                        labels[i][j].config(text=word_search[i][j][0], relief="solid", borderwidth=1, bg="lightblue")
                else:
                    labels[i][j].config(text=word_search[i][j][0], relief="solid", borderwidth=1, bg="white")

        # Mettre à jour les mots restants à trouver
        words_text = ", ".join(word for word in words_to_find if word)  # Filtrer les mots vides
        words_to_find_label.config(text=words_text)

    # Initialisation de Tkinter
    window = tk.Tk()
    window.title("Mot Mêlé")

    # Création de la grille
    labels = [[None] * len(word_search[0]) for _ in range(len(word_search))]
    for i in range(len(word_search)):
        for j in range(len(word_search[i])):
            labels[i][j] = tk.Label(window, text="", width=4, height=2, relief="solid", borderwidth=1)
            labels[i][j].grid(row=i, column=j)

    # Affichage des mots à trouver à côté de la grille
    tk.Label(window, text="Mots à trouver :").grid(row=0, column=len(word_search[0]) + 2, sticky="w")
    words_text = ", ".join(word for word in words_to_find if word)  # Filtrer les mots vides
    words_to_find_label = tk.Label(window, text=words_text)
    words_to_find_label.grid(row=1, column=len(word_search[0]) + 2, sticky="w")

    # Initialisation des coordonnées de la grille
    row, col = 0, 0

    # Liste pour stocker les lettres saisies par l'utilisateur
    entered_letters = []

# ------------------les touches pour jouer-------------------------------------------------

    # Les touches fléchées
    window.bind("<Up>", handle_arrow_key)
    window.bind("<Down>", handle_arrow_key)
    window.bind("<Left>", handle_arrow_key)
    window.bind("<Right>", handle_arrow_key)

    #La touche Espace
    window.bind("<space>", handle_enter_key)

    # Fonction pour mettre à jour la grille au démarrage
    update_grid()

    # Lancement de la boucle principale Tkinter
    window.mainloop()
