from tkinter import *
from myFrameWindow import *



win =Tk()
desktop = Frame(win,bg="gray")
desktop.pack(fill="both", expand=True)

f1=Frame(desktop, bg="white",width=200,height=200)

f1.place(x=0,y=0)
f1.pack_propagate(False)

f1_2 = Frame(f1, bg="red")

f1_2.winfo_pointerx
f1_2.winfo_rootx

window1=myFrameWindow(f1_2,"Example")

win.geometry("900x600")
win.title("desktop test")
win.mainloop()