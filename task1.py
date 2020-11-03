import tkinter as tk
from tkinter import *
import math

main = tk.Tk()
main.title("MORE METH")
main.geometry("500x300")
main.resizable(0, 0)

def do():
    if entry3.get() != "" and entryH.get() != "":
        b = float(entry3.get())
        h = float(entryH.get())
        ans = (b * h) / 2
        label3["text"] = round(ans, 2)
    elif entry1.get() != "" and entry2.get() != "" and entry3.get() != "":
        a = float(entry1.get())
        b = float(entry3.get())
        c = float(entry2.get())
        s = (a + b + c) / 2
        ans = (s * (s - a) * (s - b) * (s - c))
        if ans <= 0:
            label3["text"] = "Impossible triangle!"
        else:
            ans = math.sqrt(ans)
            label3["text"] = round(ans, 2)
    else:
        label3["text"] = "Not enough numbers!"

photo = PhotoImage(file = "triangle.png")
frameX = tk.Frame(main)
label1 = tk.Label(main, image = photo)
entry1 = tk.Entry(main, width = 8)
entry2 = tk.Entry(main, width = 8)
entryH = tk.Entry(main, width = 8)
entry3 = tk.Entry(main, width = 8)
label2 = tk.Label(master = frameX, text = "Enter in as much information about the\ntriangle shown and I will calculate the area")
button = tk.Button(master = frameX, text = "Calculate!", command = do)
label3 = tk.Label(master = frameX)

label1.pack()
entry1.place(x = 140, y = 125)
entry2.place(x = 400, y = 160)
entry3.place(x = 200, y = 220)
entryH.place(x = 300, y = 150)
frameX.pack()
label2.pack(side = LEFT)
button.pack(side = LEFT)
label3.pack(side = LEFT)

main.mainloop()