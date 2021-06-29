from tkinter import *
from tkinter import messagebox
import mysql.connector


Login = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1", database="Hospitals",
                               auth_plugin="mysql_native_password")

mycursor = Login.cursor()
xy = mycursor.execute("Select * from Login")

obj = {}
for i in mycursor:
    rcv = {i[0]: i[1]}
    keys = rcv.keys()
    entries = rcv.values()

    for key in keys:
        for entry in entries:
            obj[key] = entry

print(obj)


def register():
    global Login
    sql = "INSERT INTO Login VALUES(%s, %s)"
    val = (userentry.get(), entrypass.get())
    mycursor.execute(sql, val)
    Login.commit()
    print(mycursor.rowcount, "record installed")
    import pdb;pdb.set_trace()
    mycursor.execute("Select * from Login")
    for i in mycursor:
        print(i)



user_pass = obj


def clear_entry():
    userentry.delete(0, 'end')
    entrypass.delete(0, 'end')





def user_pass_search(username, _password, _dict):
    if username in _dict:
        if _password == _dict[username]:
            return 1
        else:
            return 0
    else:
        return -1


def verify():
    user = userentry.get()
    password = entrypass.get()

    x = int(user_pass_search(user, password, user_pass))
    print(" ")
    if x == 1:
        root.destroy()

    elif x == 0:
        messagebox.showinfo("Alert", "Incorrect password ")
        userentry.delete(0, 'end')
        entrypass.delete(0, 'end')
    elif x == -1:
        messagebox.showinfo("Alert", "Username Doesn't Exist")
        userentry.delete(0, 'end')
        entrypass.delete(0, 'end')


root = Tk()
root.title("Password and username Verification")
root.geometry("500x400")
root.config(bg='black')

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)



lbluser = Label(frame, text="Enter your Username")
lbluser.grid(row=1, column=1)

userentry = Entry(frame, )
userentry.grid(row=1, column=2, pady=5)

lblpass = Label(frame, text="Enter your Password")
lblpass.grid(row=2, column=1)

entrypass = Entry(frame, )
entrypass.grid(row=2, column=2, pady=5)

reset_btn = Button(frame, text='clear', bg='#8dc63f', command=clear_entry)
reset_btn.grid(row=6, column=2, pady=8)

exit_btn = Button(frame, text='Exit', bg='#8dc63f', command=lambda: root.destroy())
exit_btn.grid(row=5, column=2, pady=5)

cal_btn = Button(frame, text='Log in', bg='#8dc63f', command=verify)
cal_btn.grid(row=5, column=1, pady=5)

reg_btn = Button(frame, text='Register', bg='#8dc63f', command=register)
reg_btn.grid(row=6, column=1, pady=5)

root.mainloop()
