import tkinter as tk

root = tk.Tk()  # création du node racine // démarre la console TCL
sv_entry = tk.StringVar()
sv_time = tk.StringVar(value="2:30")
sv_word = tk.StringVar(value="MAISON") # le mot à deviner
sv_tip = tk.StringVar(value="PAUSE!")  # l’affichage du mot dans le canvas

def do_verif():
    pass  # TODO à faire plus tard !


top_frame = tk.Frame(root,relief=tk.GROOVE,borderwidth=2)
top_frame.pack()

entry = tk.Entry(top_frame,textvariable=sv_entry)
entry.pack()

bt_validate = tk.Button(top_frame,text="Valider",command=do_verif)
bt_validate.pack()

lbl_time = tk.Label(top_frame,textvariable=sv_time)
lbl_time.pack()

center_frame = tk.Frame(root, borderwidth=2,relief=tk.GROOVE)
center_frame.pack()

canvas = tk.Canvas(center_frame,width=300,height=500)

for line in range(10):
    for column in range(6):
        canvas.create_rectangle(column*50,line*50,(column+1)*50,(line+1)*50)

for i in range(6):
    canvas.create_text((25+i*50, 25),text=sv_tip.get()[i])
canvas.pack()

root.title("Motus")
# root.geometry("300x300")
icon = tk.PhotoImage(file="res/ball.png")  # Chargement de l’image dans tkinter
root.iconphoto(False, icon)

if __name__ == '__main__':
    root.mainloop()
