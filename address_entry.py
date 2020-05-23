import tkinter as tk

window=tk.Tk()
window.title("Address Entry Form")

frame=tk.Frame(
		master=window,
		relief=tk.SUNKEN,
		borderwidth=3)
frame.pack()


name=["First Name:","Last Name:","Address Line 1:","Address Line 2:","City","State:","Postal Code:","Country:"]

for i in range(8):
	

	label=tk.Label(master=frame,text=name[i])
	entry=tk.Entry(master=frame)

	label.grid(row=i,column=0,sticky="e")
	entry.grid(row=i,column=1)

frm_btn=tk.Frame()
frm_btn.pack(fill=tk.X,ipadx=5,ipady=5)

btn_clr=tk.Button(master=frm_btn,text="Clear")
btn_sbm=tk.Button(master=frm_btn,text="Submit")

btn_clr.pack(side=tk.RIGHT)
btn_sbm.pack(side=tk.RIGHT)
window.mainloop()