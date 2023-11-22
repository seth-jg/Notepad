from tkinter import *

def save_file():
    fname = name.get()
    fcontent = content.get(1.0, END)
    file = open("C:/Users/sethg/Desktop/Notes/" + fname + ".txt", "w")
    file.write(fcontent)
    file.close()

root = Tk()
root.geometry("300x500")
root.config(background="pink")
global name
global content
Label(root, text="File name:", bg="pink").pack(anchor="w")
name = Entry(root, width=40)
name.pack(pady=10)
Label(root, text="Content:", bg="pink").pack(anchor="w")
content = Text(root, width=30, height=20, )
content.pack(pady=10)
Button(root, text="Save", width=33, height=3, borderwidth=2, command=lambda: save_file()).pack(pady=4)

root.mainloop()