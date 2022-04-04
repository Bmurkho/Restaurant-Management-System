from tkinter import *
import mysql.connector
from tkinter import messagebox
class Main:
    def __init__(self, master):
        #global root

        master.title("Backyard Stories")
        master.geometry("1920x1080+0+0")
        master.config(bg='#116562')
        master.resizable(False, False)

        # Database
        conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="bstories")
        global cursor
        cursor = conn.cursor()
        if conn.is_connected():
            print("successfully connected")
        else:
            print("Ivalid")

        # GUI
        r = IntVar()
        r.set(2)
        password = StringVar()
        username = StringVar()

        topFrame = Frame(root, bd=10, relief=RAISED, bg='slate grey', width=300, height=500)  # create top frame
        topFrame.place(relx=0.5, rely=0.5, anchor=CENTER)  # view top frame

        labelTitle = Label(topFrame, text='Backyard Stories', font=('arial', 30, 'bold'), bg='wheat1', bd=9, width=80,
                           height=1)
        labelTitle.grid(row=0, column=0)

        usernamelabel = Label(topFrame, text="Username", font=('bold', 20)).grid(row=3, column=0, pady=5)
        entry_username = Entry(topFrame, textvariable=username, font=('bold', 20)).grid(row=5, column=0, pady=5)

        passwordlabel = Label(topFrame, text="Password", font=('bold', 20)).grid(row=7, column=0, pady=5)
        entry_password = Entry(topFrame, textvariable=password, font=('bold', 20)).grid(row=9, column=0, pady=5)
        loginbutton = Button(topFrame, text="Login", font=('bold', 20), command=loginclicked).grid(row=11, column=0,
                                                                                                   pady=5)

        root.mainloop()
        def loginclicked():
            global password
            global username

            if username.get() == '' or password.get() == '':
                messagebox.showinfo("Error", "You need to put an username and password")
            elif username.get() != '' or password.get() != '':
                sql = "SELECT * FROM user Where BINARY username= '%s' AND BINARY password= '%s'" % (
                username.get(), password.get())
                cursor.execute(sql)
                if cursor.fetchone():
                    messagebox.showinfo("Successful", "Welcome!")
                    Menu()
                else:
                    messagebox.showinfo("Error", "Invalid Credentials")

        def Menu():
            topFrame.destroy()
            topFrame = Frame(root, bd=10, relief=RAISED, bg='slate grey', width=300, height=500)  # create top frame
            topFrame.place(relx=0.5, rely=0.5, anchor=CENTER)  # view top frame

            labelTitle = Label(topFrame, text='Backyard Stories', font=('arial', 30, 'bold'), bg='wheat1', bd=9,
                               width=80,
                               height=1)
            labelTitle.grid(row=0, column=0)

            billbutton = Button(topFrame, text="Generate Bill", font=('bold', 20), command=Bill).grid(row=10, column=0,
                                                                                                      padx=10, pady=5)
            inventorybutton = Button(topFrame, text="Inventory", font=('bold', 20), command=Inventory).grid(row=11,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=5)

            master.mainloop()


root = Tk()

