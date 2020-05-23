import tkinter as tk

window=tk.Tk()

ent = tk.Entry(
	width=40,
	fg="black",
	bg="white")

ent.insert(0,"What is your name?")

ent.pack()

window.mainloop()