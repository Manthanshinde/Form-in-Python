import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("600x600")

frame = tk.Frame(win, bg="khaki", width=500, height=500)
frame.pack(pady=50)
frame.pack_propagate(0)

tittle = tk.Label(frame, text="Employess Data Form", fg="Red", bg="khaki", font=("serif", 18))
tittle.pack(pady=50)

# Lables
lable1 = tk.Label(frame, text="Employee Name:-", bg="khaki", fg="Brown", font=13)
lable1.pack(side="left")
lable1.place(x="25", y="110")

lable2 = tk.Label(frame, text="Employee Id:-", bg="khaki", fg="Brown", font=13)
lable2.pack(side="left")
lable2.place(x="25", y="150")

lable3 = tk.Label(frame, text="Employee Contact no:-", bg="khaki", fg="Brown", font=13)
lable3.pack(side="left")
lable3.place(x="25", y="190")

lable4 = tk.Label(frame, text="Employee Address:-", bg="khaki", fg="Brown", font=13)
lable4.pack(side="left")
lable4.place(x="25", y="230")

lable6 = tk.Label(frame, text="Employee Gender:-", bg="khaki", fg="Brown", font=13)
lable6.pack(side="left")
lable6.place(x="25", y="270")

lable5 = tk.Label(frame, text="Emp location choose:-", bg="khaki", fg="Brown", font=13)
lable5.pack(side="left")
lable5.place(x="25", y="310")

lable5 = tk.Label(frame, text="Emp Joining Month:-", bg="khaki", fg="Brown", font=13)
lable5.pack(side="left")
lable5.place(x="25", y="350")


# enteries
entry = tk.Entry(frame, width=43, bg="cyan", fg="black")
entry.pack(side="right")
entry.place(x="195", y="112")

entry1 = tk.Entry(frame, width=43, bg="cyan", fg="black")
entry1.pack(side="right")
entry1.place(x="195", y="152")

entry2 = tk.Entry(frame, width=43, bg="cyan", fg="black")
entry2.pack(side="right")
entry2.place(x="195", y="192")

entry3 = tk.Entry(frame, width=43, bg="cyan", fg="black")
entry3.pack(side="right")
entry3.place(x="195", y="232")

# radiobutton
radiobutton=tk.Radiobutton(frame, text="Male", font=8,bg="cyan",fg="black")
radiobutton.pack()
radiobutton.place(x=195,y=270)
radiobutton1=tk.Radiobutton(frame, text="Female", font=8,bg="cyan",fg="black")
radiobutton1.pack()
radiobutton1.place(x=258,y=270)
radiobutton2=tk.Radiobutton(frame, text="Others", font=8,bg="cyan",fg="black")
radiobutton2.pack()
radiobutton2.place(x=340,y=270)

# Checkbutton
c1 = tk.Checkbutton(frame, text="Navi-mumbai", bg="cyan", font=8)
c1.pack(side="left")
c1.place(x=195, y=310)
c2 = tk.Checkbutton(frame, text="Andheri", bg="cyan", font=8)
c2.pack(side="left")
c2.place(x=250, y=310)
c3 = tk.Checkbutton(frame, text="Airoli", bg="cyan", font=8)
c3.pack(side="left")
c3.place(x=330, y=310)
c4 = tk.Checkbutton(frame, text="Thane", bg="cyan", font=8)
c4.pack(side="left")
c4.place(x=395, y=310)

# Combobox
n = tk.StringVar()
monthchoose = ttk.Combobox(win, width=43, textvariable=n, background="cyan")
# dropdown list

monthchoose['values'] = (' January',
                         ' February',
                         ' March',
                         ' April',
                         ' May',
                         ' June',
                         ' July',
                         ' August',
                         ' September',
                         ' October',
                         ' November',
                         ' December',)
# monthchoose.grid(column=9,row=5)
# monthchoose.current()
monthchoose.pack(side="right")
monthchoose.place(x=240,y=400)


# Buttons
reset=tk.Button(frame, text="Reset", fg="white", bg="Cyan", bd=5 , width=10, font=12)
reset.pack()
reset.place(x=110, y=420)

submit=tk.Button(frame, text="submit", fg="white", bg="Cyan", bd=5, width=10, font=12)
submit.pack()
submit.place(x=250, y=420)


win.mainloop()
