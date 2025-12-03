import tkinter as tk
import random

turn = random.randint(1,2)
#kreiran prozor
window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("500x500")
window.configure(background="black")
#tekst koji nam govori ko je napotezu
if turn == 1:
    label_text = tk.Label(window,text="X turn",foreground="white",bg="black",font=("Arial",20),pady=20)
else:
    label_text = tk.Label(window,text="O turn",foreground="white",bg="black",font=("Arial",20),pady=20)
label_text.pack()
#frame za tabelu
button_frame = tk.Frame(bg="black")
button_frame.pack()
#funkcije
def klik(row,column):
    global turn
    if buttons[row][column]["text"] != "":
        return
    print(f"Pritisnuto dugme: {row},{column}")
    if turn == 1:
        buttons[row][column]["text"] = "X"
        turn = 2
        label_text.config(text="O turn")
    elif turn == 2:
        buttons[row][column]["text"] = "O"
        turn = 1
        label_text.config(text="X turn")
    
    pobednik = proveri_pobednika()
    if pobednik:
        label_text.config(text=f"{pobednik} pobedjuje!")
        # blokiraj sva dugmad
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(state="disabled")

#reset funkcija
def restartGame():
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(state="normal",text="")

#funkcija za proveru pobednika
def proveri_pobednika():
    # proveri redove
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return buttons[row][0]["text"]
    
    # proveri kolone
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return buttons[0][col]["text"]

    # proveri dijagonale
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]

    return None


buttons = []
#tabela sa poljima 3x3
for row in range(3):
    buttons.append([])
    for column in range(3):
        button = tk.Button(
            button_frame,
            width=5,
            height=5,
            background="yellow",
            foreground="black",
            text="",
            command=lambda r=row, c=column: klik(r,c)

        )
        button.grid(row=row,column=column,padx=5,pady=5)
        buttons[row].append(button)
#dugmici
button_frame1 = tk.Frame(bg="black")
button_frame1.pack()
#reset dugme
reset_button = tk.Button(
    button_frame1,
    width=7,
    height=2,
    background="blue",
    fg="white",
    text="reset",
    command=restartGame
)
reset_button.grid(row=0,column=0,padx=5,pady=5)


window.mainloop()