import tkinter as tk
from tkinter import messagebox
import random

# Initialisation de la fenêtre
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialisation du tableau du jeu
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Symboles pour les joueurs
symbols = {1: 'X', 2: 'O'}

# Variable pour suivre le joueur actuel
joueur_actuel = 1  # Commence avec le joueur 1

# Variable pour vérifier si la partie est terminée
fin_partie = False

# Fonction appelée lorsqu'un bouton est cliqué
def case_cliquee(row, col):
    global joueur_actuel, fin_partie


    # Vérification si la case est vide et si la partie n'est pas terminée
    if board[row][col] == 0 and not fin_partie:
        board[row][col] = joueur_actuel
        buttons[row][col].config(text=symbols[joueur_actuel])

        # Vérification s'il y a un gagnant
        if verifier_victoire(joueur_actuel):
            messagebox.showinfo("Fin de partie", f"Le joueur {symbols[joueur_actuel]} a gagné !")
            fin_partie = True
        # Vérification si c'est un match nul
        elif verifier_match_nul():
            messagebox.showinfo("Fin de partie", "Match nul !")
            fin_partie = True
        # Changer de joueur
        joueur_actuel = 3 - joueur_actuel  # Alterner entre 1 et 2 pour les joueurs
        if joueur_actuel == 2 and not fin_partie:
            jouer_ia()

# Fonction pour l'IA qui joue de manière aléatoire (version basique)
def jouer_ia():
    global joueur_actuel, fin_partie
    cases_vides = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    if cases_vides:
        row, col = random.choice(cases_vides)
        board[row][col] = joueur_actuel
        buttons[row][col].config(text=symbols[joueur_actuel])

        # Vérification s'il y a un gagnant après le coup de l'IA
        if verifier_victoire(joueur_actuel):
            messagebox.showinfo("Fin de partie", f"L'IA ({symbols[joueur_actuel]}) a gagné !")
            fin_partie = True
        # Vérification si c'est un match nul après le coup de l'IA
        elif verifier_match_nul():
            messagebox.showinfo("Fin de partie", "Match nul !")
            fin_partie = True
        joueur_actuel = 3 - joueur_actuel  # Changer de joueur après le coup de l'IA

# Vérifier s'il y a un gagnant
def verifier_victoire(joueur):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == joueur or \
           board[0][i] == board[1][i] == board[2][i] == joueur:
            return True
    if board[0][0] == board[1][1] == board[2][2] == joueur or \
       board[0][2] == board[1][1] == board[2][0] == joueur:
        return True
    return False

# Vérifier s'il y a un match nul
def verifier_match_nul():
    return all(all(cell != 0 for cell in row) for row in board)

# Création des boutons pour le tableau du jeu
buttons = [[None, None, None], [None, None, None], [None, None, None]]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=('Arial', 20), width=5, height=2,
                                   command=lambda row=i, col=j: case_cliquee(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
