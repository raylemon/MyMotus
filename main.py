import random
import tkinter as tk
from time import strftime, gmtime
from tkinter import messagebox

# ======================================== CONSTANTES ==================================================================
BT_FONT = ("Calibri", "14")
LBL_FONT = ("Cambria", "16")

TIMER = 181

WHITE = "white"
RED = "firebrick"
YELLOW = "goldenrod"
BLUE = "powderblue"
GREEN = "forestgreen"


# ========================================== FONCTIONS =================================================================
def do_verif():
    pass  # TODO à faire plus tard !
    # Récupérer le contenu de l’entry
    attempt = sv_entry.get().upper()
    sv_entry.set("")

    # Vérifier la taille du mot
    if len(attempt) != 6:
        messagebox.showerror("Mot Incorrect", f"Votre mot est trop {'court' if len(attempt) < 6 else 'long'} !")
    elif attempt not in words:  # vérification si dans le dictionnaire
        messagebox.showerror("Mot Incorrect", "Votre mot n’est pas dans le dictionnaire !")
    else:
        occur = []
        word = sv_word.get()
        tip = sv_tip.get()
        # Boucle de comparaison des lettres
        for i in range(6):  # Vérifier la position de chaque lettre
            letter = attempt[i]
            occur.append(letter)
            if letter == word[i]:  # Vérifier si la lettre est à la bonne place
                tip = tip[:i] + letter + tip[i + 1:]  # Insertion de lettre dans le mot
                sv_tip.set(tip)
                draw_colors(i, GREEN)  # On dessine la couleur
            elif letter in word and occur.count(letter) <= word.count(letter):  # and letter != word[i]:
                draw_colors(i, YELLOW)

            draw_text(i, letter)  # Dessiner le texte
        end_game()  # Vérifier si on a gagné


def draw_colors(pos_x: int, color: str):
    pos_y = iv_tries.get()  # position sur l’axe Y
    canvas.create_rectangle(pos_x * 50, pos_y * 50, (pos_x + 1) * 50, (pos_y + 1) * 50, fill=color, tag="color")


def draw_text(pos_x: int, text: str):
    pos_y = iv_tries.get()
    canvas.create_text((25 + pos_x * 50, pos_y * 50 + 25), text=text, tag="text")


def end_game():
    pass


def pick_a_word() -> str:
    return random.choice(list(words)).upper()


def load_words() -> set:
    with open("res/6-letters.txt", "rt", encoding="utf-8") as file:
        lines = file.readlines()

        # Version simple
        # w = set()
        # for lin in lines:
        #     w.add(lin.strip())
        # return w

        # Version moins simple
        # w = set()
        # w.add(_.strip() for _ in lines)
        # return w

        # Uber version méga rapide
        return set(map(lambda x: x.strip(), lines))


def do_reset():
    bottom_frame.pack_forget()
    canvas.delete("text", "color")
    iv_timer.set(TIMER)
    word = pick_a_word()
    sv_word.set(word)
    tip = word[0] + "     "
    sv_tip.set(tip)
    iv_tries.set(0)
    for i in range(6):
        letter = tip[i]
        draw_text(i, letter)
    clock()


def clock():
    time = iv_timer.get() - 1
    sv_time.set(strftime("%M:%S", gmtime(time)))
    iv_timer.set(time)

    if time > 0:
        sv_job.set(lbl_time.after(1000, clock))
    else:
        bottom_frame.pack(side=tk.TOP, padx=2, pady=2, expand=tk.YES, fill=tk.BOTH)
        pass  # TODO on a encore des trucs à faire ici


# ===================================== VARIABLES - CRÉATION DES WIDGETS ===============================================

root = tk.Tk()  # création du node racine // démarre la console TCL

sv_entry = tk.StringVar()
sv_time = tk.StringVar()
sv_word = tk.StringVar()  # le mot à deviner
sv_tip = tk.StringVar()  # l’affichage du mot dans le canvas
sv_message = tk.StringVar()
iv_timer = tk.IntVar(value=TIMER)
sv_job = tk.StringVar()
iv_tries = tk.IntVar()

top_frame = tk.Frame(root, relief=tk.GROOVE, borderwidth=2)
entry = tk.Entry(top_frame, textvariable=sv_entry)
bt_validate = tk.Button(top_frame, text="Valider", command=do_verif, font=BT_FONT)
lbl_time = tk.Label(top_frame, textvariable=sv_time, font=LBL_FONT, fg=GREEN)
center_frame = tk.Frame(root, borderwidth=2, relief=tk.GROOVE)
canvas = tk.Canvas(center_frame, width=300, height=500, bg=WHITE)

for line in range(10):
    for column in range(6):
        canvas.create_rectangle(column * 50, line * 50, (column + 1) * 50, (line + 1) * 50, fill=BLUE, tag="grid")

#for i in range(6):
#    canvas.create_text((25 + i * 50, 25), text=sv_tip.get()[i], tag="text")

bottom_frame = tk.Frame(root, borderwidth=2, relief=tk.GROOVE)
lbl_message = tk.Label(bottom_frame, textvariable=sv_message, font=LBL_FONT)
button_bar = tk.Frame(bottom_frame)
bt_continue = tk.Button(button_bar, text="Continuer", command=do_reset, font=BT_FONT, bg=GREEN)  # TODO affect command
bt_quit = tk.Button(button_bar, text="Quitter", command=root.quit, font=BT_FONT, bg=RED, fg=WHITE)

# ==================================== PLACEMENT DES WIDGETS ===========================================================

top_frame.pack(side=tk.TOP, padx=10, pady=10, expand=tk.YES, fill=tk.BOTH)
entry.pack(padx=2, pady=2, expand=tk.YES, fill=tk.X)
bt_validate.pack(padx=2, pady=2)
lbl_time.pack()
center_frame.pack()
canvas.pack()

lbl_message.pack(side=tk.TOP, padx=2, pady=2)
button_bar.pack(side=tk.TOP, padx=2, pady=2, expand=tk.YES, fill=tk.X)
bt_continue.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X, padx=2, pady=2)
bt_quit.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=2, pady=2)

# =================================== CONFIGURATION ====================================================================

root.title("Motus")
root.bind("<Return>", lambda event: do_verif())
# root.geometry("300x300")
icon = tk.PhotoImage(file="res/ball.png")  # Chargement de l’image dans tkinter
root.iconphoto(False, icon)

# =================================== PROGRAMME PRINCIPAL ==============================================================
if __name__ == '__main__':
    words = load_words()
    do_reset()
    root.mainloop()
