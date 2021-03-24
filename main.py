import tkinter as tk
from time import strftime, gmtime

BT_FONT = ("Calibri", "14")
LBL_FONT = ("Cambria", "16")
TIMER = 11

WHITE = "white"
RED = "firebrick"
YELLOW = "goldenrod"
BLUE = "powderblue"
GREEN = "forestgreen"


root = tk.Tk()  # création du node racine // démarre la console TCL
sv_entry = tk.StringVar()
sv_time = tk.StringVar()
sv_word = tk.StringVar(value="MAISON") # le mot à deviner
sv_tip = tk.StringVar(value="M     ")  # l’affichage du mot dans le canvas
sv_message = tk.StringVar(value="Message dynamique")
iv_timer = tk.IntVar(value=TIMER)
sv_job = tk.StringVar()

def do_verif():
    pass  # TODO à faire plus tard !


def clock():
    time = iv_timer.get() -1
    sv_time.set(strftime("%M:%S",gmtime(time)))
    iv_timer.set(time)

    if time > 0:
        sv_job.set(lbl_time.after(1000,clock))
    else:
        draw_bottom() # TODO on a encore des trucs à faire ici


def draw_bottom():
    bottom_frame = tk.Frame(root,borderwidth=2,relief=tk.GROOVE)
    bottom_frame.pack(side=tk.TOP,padx=2,pady=2,expand=tk.YES,fill=tk.BOTH)

    lbl_message = tk.Label(bottom_frame,textvariable=sv_message,font=LBL_FONT)
    lbl_message.pack(side=tk.TOP,padx=2,pady=2)

    button_bar = tk.Frame(bottom_frame)
    button_bar.pack(side=tk.TOP,padx=2,pady=2,expand=tk.YES,fill=tk.X)

    bt_continue = tk.Button(button_bar,text="Continuer",command=None,font=BT_FONT,bg=GREEN) #TODO affect command
    bt_continue.pack(side=tk.LEFT, expand=tk.YES,fill=tk.X,padx=2,pady=2)

    bt_quit = tk.Button(button_bar,text="Quitter",command=root.quit,font=BT_FONT,bg=RED,fg=WHITE)
    bt_quit.pack(side=tk.RIGHT, expand=tk.YES,fill=tk.X,padx=2,pady=2)


top_frame = tk.Frame(root,relief=tk.GROOVE,borderwidth=2)
top_frame.pack(side=tk.TOP,padx=10,pady=10, expand=tk.YES,fill=tk.BOTH)

entry = tk.Entry(top_frame,textvariable=sv_entry)
entry.pack(padx=2,pady=2,expand=tk.YES,fill=tk.X)

bt_validate = tk.Button(top_frame,text="Valider",command=do_verif,font=BT_FONT)
bt_validate.pack(padx=2,pady=2)

lbl_time = tk.Label(top_frame,textvariable=sv_time,font=LBL_FONT,fg=GREEN)
lbl_time.pack()

center_frame = tk.Frame(root, borderwidth=2,relief=tk.GROOVE)
center_frame.pack()

canvas = tk.Canvas(center_frame,width=300,height=500,bg=WHITE)

for line in range(10):
    for column in range(6):
        canvas.create_rectangle(column*50,line*50,(column+1)*50,(line+1)*50,fill=BLUE)

for i in range(6):
    canvas.create_text((25+i*50, 25),text=sv_tip.get()[i])
canvas.pack()
clock()

root.title("Motus")
# root.geometry("300x300")
icon = tk.PhotoImage(file="res/ball.png")  # Chargement de l’image dans tkinter
root.iconphoto(False, icon)

if __name__ == '__main__':
    root.mainloop()
