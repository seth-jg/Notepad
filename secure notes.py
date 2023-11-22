from tkinter import *
from tkinter import filedialog
import sqlite3
import os


class ac_data_base(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def create_table(self):
        conn = sqlite3.connect("secure notes/users.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS accounts (username TEXT, password TEXT)")
        conn.commit()
        conn.close()

    def create_account(self):
        conn = sqlite3.connect("secure notes/users.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO accounts VALUES (?,?)", (self.name, self.password))
        conn.commit()
        conn.close()

    def veiw(self):
        conn = sqlite3.connect("secure notes/users.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM accounts")
        rows = cur.fetchall()
        conn.close()
        users = {}
        for row in rows:
            x = row[0]
            y = row[1]
            users[x] = y
        print(users)
    
    def change_password(self):
        conn = sqlite3.connect("secure notes/users.db")
        cur = conn.cursor()
        cur.execute("UPDATE accounts SET password=? WHERE username=?", (self.password, self.name))
        conn.commit()
        conn.close()
    
    def delete(self):
        conn= sqlite3.connect("secure notes/users.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM accounts WHERE username=?", (self.name, ))
        conn.commit()
        conn.close()


def notepad():
    note = 'c:/Windows/system32/notepad.exe'
    os.system('"%s"' % note)

def veiw_files():
    my_program = filedialog.askopenfilename()
    os.system('"%s"' % my_program)

def password_change():
    password_get = password_c.get()
    x = ac_data_base(user, password_get)
    x.change_password()
    change1.destroy()

def change_password():
    global change1
    change1 = Tk()
    change1.geometry("300x185")
    global password_c
    password_c = Entry(change1, width=30)
    password_c.pack(pady=20)
    Button(change1, text="Change Password", padx=37, pady=3, command=password_change).pack(pady=10)
    change1.mainloop()

def deletion_account():
    x = ac_data_base(user, pword)
    x.delete()
    exit()


def account_settings():
    global settings
    settings = Tk()
    settings.geometry("300x185")
    Button(settings, text="Change Password", padx=30, pady=3, command=change_password).pack(pady=20)
    Button(settings, text="Delete Account", padx=37, pady=3, command=deletion_account).pack(pady=20)
    settings.mainloop()

def home_page():
    home = Tk()
    home.geometry("600x350")
    text1 = "Welcome %s!" % user
    Label(home, text=text1, font=(9)).pack(anchor="w")
    Button(home, text="NotePad", font=(9), pady=5, padx=70, border=3, command=notepad).pack(pady=20)
    Button(home, text="Veiw Files", font=(9), pady=5, padx=63, border=3, command=veiw_files).pack(pady=20)
    Button(home, text="Account Settings", font=(9), pady=5, padx=35, border=3, command=account_settings).pack(pady=20)


    home.mainloop()


def login_account():
    conn = sqlite3.connect("secure notes/users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts")
    rows = cur.fetchall()
    conn.close()
    users = {}
    for row in rows:
        x = row[0]
        y = row[1]
        users[x] = y
    
    global user
    global pword
    user = username.get()
    pword = password.get()

    if user in users:
        if pword == users[user]:
            root.destroy()
            home_page()
        else:
            print(user)
            p_wrong = Label(root, text="password not recognised")
            p_wrong.grid(row=6, column=2, columnspan=3)
    else:
        u_wrong = Label(root, text="username not recognised")
        u_wrong.grid(row=6, column=2, columnspan=3)


def register_account():
    user = username.get()
    pword = password.get()

    create = ac_data_base(user, pword)
    create.create_table()

    conn = sqlite3.connect("secure notes/users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts")
    rows = cur.fetchall()
    conn.close()
    users = {}
    for row in rows:
        x = row[0]
        y = row[1]
        users[x] = y

    if user in users:
        u_wrong = Label(root, text="user already used")
        u_wrong.grid(row=6, column=2, columnspan=3)
    else:
        create = ac_data_base(user, pword)
        create.create_account()
        u_crt = Label(root, text="user created")
        u_crt.grid(row=6, column=2, columnspan=3)




root = Tk()
root.geometry("600x350")

title =Label(root, text="Login Page", font=(20))
title.grid(row=0, column=0, pady=10)

l1 = Label(root, text="Username: ", font=(9))
l1.grid(row=2, column=1, pady=30)
global username
username = Entry(root, font=(9))
username.grid(row=2, column=2)

l2 = Label(root, text="Password: ", font=(9))
l2.grid(row=3, column=1, pady=5)
global password
password = Entry(root, font=(9))
password.grid(row=3, column=2)



login_button = Button(root, text="Login", pady=2, padx=33, border=3, command=login_account)
login_button.grid(row=4, column=2, pady=5)

registerpage_button = Button(root, text="Register account", border=3, pady=2, padx=5, command=register_account)
registerpage_button.grid(row=5, column=2, pady=5)

root.mainloop()