import tkinter as tk 
window=tk.Tk()

greeting=tk.Label(
	text="Python Rocks!",
	foreground="white",
	background="black",
	width=20,
	height=10)

greeting.pack()

button=tk.Button(
	text="Click me",
	fg="blue")

button.pack()

window.mainloop()