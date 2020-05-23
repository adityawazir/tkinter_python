import tkinter as tk

def decrease():
	value=int(lbl_txt["text"])
	lbl_txt["text"]=f"{value-1}"

def increase():
	value=int(lbl_txt["text"])
	lbl_txt["text"]=f"{value+1}"	

window=tk.Tk()
window.title("Counter")

btn_dec=tk.Button(master=window,text="-",command=decrease)
lbl_txt=tk.Label(master=window,text="0")
btn_inc=tk.Button(master=window,text="+",command=increase)

btn_dec.grid(row=0,column=0)
lbl_txt.grid(row=0,column=1)
btn_inc.grid(row=0,column=2)

window.mainloop()