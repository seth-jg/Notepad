from tkinter import *
import os

def add():
    lof = os.listdir('notes/')
    nm = f_name.get()
    if nm in lof:
        with open('notes/' + f_name.get(), 'a+') as file:
            file.write('\n')
            file.write(tx1.get())
            file.write('\n')
            file.write(tx2.get())
            file.write('\n')
            file.write(tx3.get())
            file.write('\n')
            file.write(tx4.get())
            file.write('\n')
            file.write(tx5.get())
            file.write('\n')
            file.write(tx6.get())
            file.close()
            tx1.delete(0, END)
            tx2.delete(0, END)
            tx3.delete(0, END)
            tx4.delete(0, END)
            tx5.delete(0, END)
            tx6.delete(0, END)
            success_label = Label(window, text="Success", padx=35, bg="red")
            success_label.grid(row=15, column=1, columnspan=3)
    else:
        fail_label = Label(window, text="File not recognised", padx=35, bg="red")
        fail_label.grid(row=15, column=1, columnspan=3)

def save1():
    list_of_files = os.listdir('notes')
    nm = f_name.get()
    if nm in list_of_files:
        with open('notes/'+ f_name.get(), 'w') as file:
            file.write(tx1.get())
            file.write('\n')
            file.write(tx2.get())
            file.write('\n')
            file.write(tx3.get())
            file.write('\n')
            file.write(tx4.get())
            file.write('\n')
            file.write(tx5.get())
            file.write('\n')
            file.write(tx6.get())
            file.close()
            tx1.delete(0, END)
            tx2.delete(0, END)
            tx3.delete(0, END)
            tx4.delete(0, END)
            tx5.delete(0, END)
            tx6.delete(0, END)
            success_label = Label(window, text="Success", padx=35, bg="red")
            success_label.grid(row=15, column=1, columnspan=3)
    else:
        fail_label = Label(window, text="File not recognised", padx=35, bg="red")
        fail_label.grid(row=15, column=1, columnspan=3)

def read():
    list_of_files = os.listdir('notes')
    nm = f_name.get()
    if nm in list_of_files:
        file6 = open('notes/'+ f_name.get(), 'r')
        file7 = file6.read()
        read_screen = Toplevel()
        read_screen.iconbitmap('note icon.ico')
        read_screen.geometry("350x350")
        read_screen.configure(bg='red')
        read_screen.title("Read Screen")
        Label(read_screen, bg="red").pack()
        Label(read_screen, text="Content:").pack()
        Label(read_screen, text=file7, bg="red").pack()
        Label(read_screen, bg="red")
        Button(read_screen, text="Exit", pady=4, padx=16, command=read_screen.destroy).pack()
        success_label = Label(window, text="Success", padx=35, bg="red")
        success_label.grid(row=15, column=1, columnspan=3)
    else:
        fail_label = Label(window, text="File not recognised", padx=35, bg="red")
        fail_label.grid(row=15, column=1, columnspan=3)

def yes():
    os.remove('notes/'+ f_name.get())
    success_label = Label(window, text="Successfully deleted", padx=35, bg="red")
    success_label.grid(row=15, column=1, columnspan=3)
    scr.destroy()

def no():
    fail_label = Label(window, text="File not deleted", padx=35, bg="red")
    fail_label.grid(row=15, column=1, columnspan=3)
    scr.destroy()

def delete():
    list_of_files = os.listdir('notes')
    nm = f_name.get()
    if nm in list_of_files:
        global scr
        scr = Toplevel()
        scr.iconbitmap('note icon.ico')
        scr.geometry("200x200")
        scr.configure(bg='red')
        scr.title("Delete Screen")
        Label(scr, bg='red').pack()
        Button(scr, text="Yes", command=yes, padx=60, pady=17).pack()
        Label(scr, bg='red').pack()
        Button(scr, text='No', command=no, padx=61, pady=17).pack()
    else:
        fail_label = Label(window, text="File not recognised", padx=35, bg="red")
        fail_label.grid(row=15, column=1, columnspan=3)

def create1():
    with open('notes/' + f_name.get(), 'w') as file:
        file.write(tx1.get())
        file.write('\n')
        file.write(tx2.get())
        file.write('\n')
        file.write(tx3.get())
        file.write('\n')
        file.write(tx4.get())
        file.write('\n')
        file.write(tx5.get())
        file.write('\n')
        file.write(tx6.get())
        file.close()
        tx1.delete(0, END)
        tx2.delete(0, END)
        tx3.delete(0, END)
        tx4.delete(0, END)
        tx5.delete(0, END)
        tx6.delete(0, END)
        success_label = Label(window, text="File created", bg="red", padx=35)
        success_label.grid(row=15, column=1, columnspan=3)

def note_select():
    file_vewier = Toplevel()
    file_vewier.geometry("100x100")
    file_vewier.iconbitmap('note icon.ico')
    l1 = Label(file_vewier, text="File Names:").pack()
    list_of_files = os.listdir('notes')
    for x in list_of_files:
        r = Label(file_vewier, text=x).pack()
    global window
    window = Tk()
    window.iconbitmap('note icon.ico')
    window.geometry("350x350")
    window.configure(bg='red')
    window.title("NotePage")
    filler1 = Label(window, text="", bg="red", pady=2)
    filler1.grid(row=0)
    fn = Label(window, text="File name: ", bg="red")
    fn.grid(row=2, column=0)
    global f_name
    global nma_var
    nma_var = StringVar()
    f_name = Entry(window, width=40, textvariable=nma_var)
    f_name.grid(row=2, column=1, columnspan=4)
    filler2 = Label(window, text="", bg="red", pady=4)
    filler2.grid(row=3)
    tn = Label(window, text="Text: ", bg="red")
    tn.grid(row=4, column=0)
    
    global tx1
    global tx1_var1
    tx1_var1 = StringVar()
    tx1 = Entry(window, width= 40, textvariable=tx1_var1)
    tx1.grid(row=5, column=1, columnspan=4)
    
    global tx2
    global tx2_var2
    tx2_var2 = StringVar()
    tx2 = Entry(window, width= 40, textvariable=tx2_var2)
    tx2.grid(row=6, column=1, columnspan=4)
    
    global tx3
    global tx3_var3
    tx3_var3 = StringVar()
    tx3 = Entry(window, width= 40, textvariable=tx3_var3)
    tx3.grid(row=7, column=1, columnspan=4)
    
    global tx4
    global tx4_var4
    tx4_var4 = StringVar()
    tx4 = Entry(window, width= 40, textvariable=tx4_var4)
    tx4.grid(row=8, column=1, columnspan=4)

    global tx5
    global tx5_var5
    tx5_var5 = StringVar()
    tx5 = Entry(window, width= 40, textvariable=tx5_var5)
    tx5.grid(row=9, column=1, columnspan=4)

    global tx6
    global tx6_var6
    tx6_var6 = StringVar()
    tx6 = Entry(window, width= 40, textvariable=tx6_var6)
    tx6.grid(row=10, column=1, columnspan=4)
    
    rem = Label(window, text="File name only for Read/Delete.", bg="red", pady=2)
    rem.grid(row=11, column=0, columnspan=2)
    save_button = Button(window, text="Save", pady=4, padx=16, command=save1, anchor=E)
    save_button.grid(row=13, column=1, stick=E)
    add_button = Button(window, text="Add", pady=4, padx=18, command=add)
    add_button.grid(row=13, column=2)
    read_button = Button(window, text="Read", pady=4, padx=15, command=read)
    read_button.grid(row=13, column=3)
    close_button = Button(window, text="Close", pady=4, padx=13, command=window.destroy)
    close_button.grid(row=14, column=3)
    delete_button = Button(window, text="Delete", pady=4, padx=12, command=delete)
    delete_button.grid(row=14, column=2)
    create_button = Button(window, text="Create", pady=4, padx=11, command=create1, anchor=E)
    create_button.grid(row=14, column=1, sticky=E)
    
    window.mainloop()

def save():
    with open('notes/'+ file_name.get(), 'w') as file:
        file.write(text1.get())
        file.write('\n')
        file.write(text2.get())
        file.write('\n')
        file.write(text3.get())
        file.write('\n')
        file.write(text4.get())
        file.write('\n')
        file.write(text5.get())
        file.write('\n')
        file.write(text6.get())
        file.close()
        screen4.destroy()

def create_note():
    global screen4
    screen4 = Tk()
    screen4.iconbitmap('note icon.ico')
    screen4.geometry("350x350")
    screen4.configure(bg='red')
    screen4.title("CreateNote")
    filler1 = Label(screen4, text="", bg="red", pady=2)
    filler1.grid(row=0)
    fn = Label(screen4, text="File name: ", bg="red")
    fn.grid(row=2, column=0)
    global file_name
    file_name=Entry(screen4, width=40)
    file_name.grid(row=2, column=1, columnspan=4)
    filler2 = Label(screen4, text="", bg="red", pady=4)
    filler2.grid(row=3)
    tn = Label(screen4, text="Text: ", bg="red")
    tn.grid(row=4, column=0)

    global text1
    global text_var1
    text_var1 = StringVar()
    text1 = Entry(screen4, width= 40, textvariable=text_var1)
    text1.grid(row=5, column=1, columnspan=4)

    global text2
    global text_var2
    text_var2 = StringVar()
    text2 = Entry(screen4, width= 40, textvariable=text_var2)
    text2.grid(row=6, column=1, columnspan=4)

    global text3
    global text_var3
    text_var3 = StringVar()
    text3 = Entry(screen4, width= 40, textvariable=text_var3)
    text3.grid(row=7, column=1, columnspan=4)

    global text4
    global text_var4
    text_var4 = StringVar()
    text4 = Entry(screen4, width= 40, textvariable=text_var4)
    text4.grid(row=8, column=1, columnspan=4)

    global text5
    global text_var5
    text_var5 = StringVar()
    text5 = Entry(screen4, width= 40, textvariable=text_var5)
    text5.grid(row=9, column=1, columnspan=4)

    global text6
    global text_var6
    text_var6 = StringVar()
    text6 = Entry(screen4, width= 40, textvariable=text_var6)
    text6.grid(row=10, column=1, columnspan=4)

    rem = Label(screen4, text="Use tab to change lines.", bg="red", pady=2)
    rem.grid(row=11, column=1)
    save_button = Button(screen4, text="Save", pady=4, padx=17, command=save)
    save_button.grid(row=13, column=1)
    cancel_button = Button(screen4, text="Cancel", pady=4, padx=14, anchor=E, command=screen4.destroy)
    cancel_button.grid(row=13, column=2, sticky=E)
    screen4.mainloop()

def notescreen():
    global screen3
    screen3 = Tk()
    screen3.iconbitmap('note icon.ico')
    screen3.geometry("350x350")
    screen3.configure(bg='red')
    screen3.title("MainScreen")
    l5 = Label(screen3, pady=10, text="             ", bg='red').pack()
    create = Button(screen3, text="Create Notes", padx=76, pady=20, command=create_note).pack()
    l6 = Label(screen3, pady=10, text="             ", bg='red').pack()
    veiw = Button(screen3, text="Veiw Notes", padx=80, pady=20, command=note_select).pack()
    l7 = Label(screen3, pady=5, text="             ", bg='red').pack()
    exit_b = Button(screen3, text="Exit", padx=30, pady=10, command=screen3.destroy).pack()
    screen3.mainloop()


def ds1():
    user1 = username_verify.get()
    pass1 = password_verify.get()
    user_text.delete(0, END)
    password_text.delete(0, END)
    list_of_files = os.listdir('accounts')
    if user1 in list_of_files:
        file = open('accounts/'+ user1,'r')
        verify = file.readline()
        if pass1 in verify:
            screen1.destroy()
            notescreen()
        else:
            n_work = Label(screen1, text="Password incorrect!", bg="red")
            n_work.grid(columnspan=5, column=1, row=6)
    else:
        u_work = Label(screen1, text="User incorrect!", bg="red")
        u_work.grid(columnspan=5, column=1, row=6)

def login():
    global screen1
    global user_text
    global password_text
    screen1 = Tk()
    screen1.iconbitmap('note icon.ico')
    screen1.geometry("350x350")
    screen1.configure(bg='red')
    screen1.title("LogIn")
    l1 = Label(screen1, pady=10, text="             ", bg='red')
    l1.grid(row=0, column=0)
    l2 = Label(screen1, text="Username:   ", bg="red")
    l2.grid(row=1, column=1)
    global username_verify
    username_verify = StringVar()
    user_text = Entry(screen1, width=30, textvariable=username_verify)
    user_text.grid(row=1, column=2)

    l4 = Label(screen1, pady=10, text="             ", bg='red')
    l4.grid(row=2, column=0)
    l3 = Label(screen1, text="Password:   ", bg="red")
    l3.grid(row=3, column=1)
    global password_verify
    password_verify = StringVar()
    password_text = Entry(screen1, width=30, textvariable=password_verify)
    password_text.grid(row=3, column=2)

    l4 = Label(screen1, pady=10, text="             ", bg='red')
    l4.grid(row=4, column=0)
    log = Button(screen1, text="Login", padx=60, pady=10, command=ds1)
    log.grid(columnspan=5, column=1, row=5)

    screen1.mainloop()


def ds2():
    file = open('accounts/'+ user_text.get(), "w")
    file.write(password_text.get())
    file.close()
    screen2.destroy()
    login()

def register():
    root.destroy()
    global screen2
    global user_text
    global password_text
    screen2 = Tk()
    screen2.iconbitmap('note icon.ico')
    screen2.geometry("350x350")
    screen2.configure(bg='red')
    screen2.title("Create Account")
    l1 = Label(screen2, pady=10, text="             ", bg='red')
    l1.grid(row=0, column=0)
    l2 = Label(screen2, text="Username:   ", bg="red")
    l2.grid(row=1, column=1)

    username_verify = StringVar()
    user_text = Entry(screen2, width=30, textvariable=username_verify)
    user_text.grid(row=1, column=2)

    l4 = Label(screen2, pady=10, text="             ", bg='red')
    l4.grid(row=2, column=0)
    l3 = Label(screen2, text="Password:   ", bg="red")
    l3.grid(row=3, column=1)

    password_verify = StringVar()
    password_text = Entry(screen2, width=30, textvariable=password_verify)
    password_text.grid(row=3, column=2)

    l4 = Label(screen2, pady=10, text="             ", bg='red')
    l4.grid(row=4, column=0)
    log = Button(screen2, text="Register", padx=60, pady=10, command=ds2)
    log.grid(columnspan=5, column=1, row=5)


def ds3():
    root.destroy()
    login()

def mainscreen():
    global root
    root = Tk()
    root.iconbitmap('note icon.ico')
    root.geometry("350x350")
    root.configure(bg='red')
    root.title("StartUp")

    l1 = Label(root, pady=10, bg='red').pack()
    b1 = Button(root, padx=100, pady=20, text="Login", command=ds3)
    b1.pack()
    l2 = Label(root, pady=3, bg='red').pack()
    b2 = Button(root, padx=94, pady=20, text="Register", command=register)
    b2.pack()
    root.mainloop()

mainscreen()

if __name__ == '__main__':
    mainscreen()