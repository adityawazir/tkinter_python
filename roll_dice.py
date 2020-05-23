import tkinter as tk
import random

def roll():
	lbl["text"]=f"{random.randint(1,6)}"

window=tk.Tk()

btn_roll=tk.Button(master=window,text="Roll",command=roll)
lbl=tk.Label(master=window,text="-")

btn_roll.pack()
lbl.pack()

window.mainloop()