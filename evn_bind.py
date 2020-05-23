import tkinter as tk

window=tk.Tk()

ent_t= tk.Entry()
btn_click= tk.Button(text="click me!")

ent_t.pack()
btn_click.pack()

def handle_click(event):
	ent_t.insert(0,"click!")

btn_click.bind("<Button-1>",handle_click)

window.mainloop()