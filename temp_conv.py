import tkinter as tk

def convert():
	df=int(ent_temp.get())
	lbl_res["text"]=str(((df-32)*5)/9)

window=tk.Tk()
window.title("Temperature Converter")

ent_temp = tk.Entry(master=window)
lbl_res = tk.Label(master=window,text="-")
btn_conv=tk.Button(master=window,text="\N{RIGHTWARDS BLACK ARROW}",command=convert)
lbl_df=tk.Label(master=window,text="\N{DEGREE FAHRENHEIT}") 
lbl_dc=tk.Label(master=window,text="\N{DEGREE CELSIUS}")

ent_temp.grid(row=0,column=0,padx=5,pady=5)
lbl_df.grid(row=0,column=1,padx=5,pady=5)
btn_conv.grid(row=0,column=2,padx=5,pady=5)
lbl_res.grid(row=0,column=3,padx=5,pady=5)
lbl_dc.grid(row=0,column=4,padx=5,pady=5)

window.mainloop()