import mysql.connector
from tkinter import *
from PIL import Image
from tkinter import messagebox

from tkinter import messagebox


root= Tk()
root.title("Backyard Stories")
root.geometry("1920x1080+0+0")
root.config(bg='#116562')
root.resizable(False, False)

#Database
conn= mysql.connector.connect(host="localhost", user= "root", passwd= "", database="bstories"  )
cursor= conn.cursor()
if conn.is_connected():
    print("successfully connected")
else:
    print("Ivalid")



def Inventory():
    #topFrame.destroy()
    root.destroy()

    root = Tk()  # for window

    root.geometry("1920x1080+0+0")  # resize the window

    root.resizable(0, 0)  # disable the maximize button

    root.title('BACKYARD STORIES')  # give a title

    root.config(bg='#116562')  # change background color

    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="bstories")
    cursor = conn.cursor()
    if conn.is_connected():
        print("successfully connected")
    else:
        print("Ivalid")

    topFrame = Frame(root, bd=10, relief=RAISED, bg='cyan4')  # create top frame
    topFrame.pack(side=TOP)  # view top frame

    labelTitle = Label(topFrame, text='Inventory', font=('arial', 30, 'bold'), bg='wheat1',
                       bd=9, width=62)
    labelTitle.grid(row=0, column=0)

    itemFrame = Frame(root, bg='cyan4', bd=10, height=20, width=62, relief=RAISED)
    itemFrame.pack(anchor=CENTER)

    listFrame = LabelFrame(itemFrame, text='Item', font=('arial', 30, 'bold'),
                           bd=5, width=62)
    listFrame.pack()

    # defining variables
    regularpatty = StringVar()
    nagaregularpatty = StringVar()
    largepatty = StringVar()
    nagalargepatty = StringVar()
    bun = StringVar()
    wings = StringVar()
    fries = StringVar()
    rice = StringVar()
    chicken = StringVar()
    coke = StringVar()
    sprite = StringVar()
    fanta = StringVar()
    water = StringVar()

    def insertRegularPatty():
        global regularpatty
        sql = "INSERT INTO Inventory (Regular_Patty) VALUES ('%d') " % (int(regularpatty.get()))
        cursor.execute(sql)
        messagebox.showinfo("Successful", "Item added Successfully!")
        quantity0.delete(0, END)
        conn.commit()

    def insertLargePatty():
        global largepatty
        sql = "INSERT INTO Inventory (Large_Patty) VALUES ('%d') " % (int(largepatty.get()))
        cursor.execute(sql)
        messagebox.showinfo("Successful", "Item added Successfully!")
        quantity1.delete(0, END)
        conn.commit()

    def insertBun():
        global bun
        sql = "INSERT INTO Inventory (Bun) VALUES ('%d') " % (int(bun.get()))
        cursor.execute(sql)
        messagebox.showinfo("Successful", "Item added Successfully!")
        quantity2.delete(0, END)
        conn.commit()

    def insertwings():
        global wings
        sql = "INSERT INTO Inventory (Wings_Serving) VALUES ('%d') " % (int(wings.get()))
        cursor.execute(sql)
        messagebox.showinfo("Successful", "Item added Successfully!")
        quantity3.delete(0, END)
        conn.commit()

    def insertfries():
        global fries
        sql = "INSERT INTO Inventory (French_Fry_Serving) VALUES ('%d') " % (int(fries.get()))
        cursor.execute(sql)
        messagebox.showinfo("Successful", "Item added Successfully!")
        quantity4.delete(0, END)
        conn.commit()

    def insertrice():
        global rice
        sql = "INSERT INTO Inventory (Rice_kg) VALUES ('%d') " % (int(rice.get()))
        cursor.execute(sql)
        messagebox.showinfo("Successful", "Item added Successfully!")
        quantity5.delete(0, END)
        conn.commit()

    def insertchicken():
        global chicken
        sql = "INSERT INTO Inventory (Chicken_kg) VALUES ('%d') " % (int(chicken.get()))
        cursor.execute(sql)
        messagebox.showinfo("Successful", "Item added Successfully!")
        quantity6.delete(0, END)
        conn.commit()

    def insertcoke():
        global coke
        sql = "INSERT INTO Inventory (Coca_Cola) VALUES ('%d') " % (int(coke.get()))
        cursor.execute(sql)
        messagebox.showinfo("Successful", "Item added Successfully!")
        quantity7.delete(0, END)
        conn.commit()

    def insertsprite():
        global sprite
        sql = "INSERT INTO Inventory (Sprite) VALUES ('%d') " % (int(sprite.get()))
        cursor.execute(sql)
        messagebox.showinfo("Successful", "Item added Successfully!")
        quantity8.delete(0, END)
        conn.commit()

    def insertfanta():
        global fanta
        sql = "INSERT INTO Inventory (Fanta) VALUES ('%d') " % (int(fanta.get()))
        cursor.execute(sql)
        messagebox.showinfo("Successful", "Item added Successfully!")
        quantity9.delete(0, END)
        conn.commit()

    def insertwater():
        global water
        sql = "INSERT INTO Inventory (Water) VALUES ('%d') " % (int(water.get()))
        cursor.execute(sql)
        messagebox.showinfo("Successful", "Item added Successfully!")
        quantity10.delete(0, END)
        conn.commit()

    def disable_text():
        quantity0.config(state='disabled')

    def enable_text():
        text0.config(state='normal')
        quantity0.config(state='normal')

    text0 = Label(listFrame, text='Regular Patty', font=('arial', 18, 'bold'), bd=6)
    text0.grid(row=0, column=0, padx=10)
    quantity0 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=regularpatty)
    quantity0.grid(row=0, column=1, padx=10)
    button0 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertRegularPatty)
    button0.grid(row=0, column=2, padx=10)
    button00 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button00.grid(row=0, column=3, padx=10)

    def disable_text():
        quantity1.config(state='disabled')

    def enable_text():
        text1.config(state='normal')
        quantity1.config(state='normal')

    text1 = Label(listFrame, text='Naga Regular Patty', font=('arial', 18, 'bold'), bd=6)
    text1.grid(row=1, column=0, padx=10)
    quantity1 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=nagaregularpatty)
    quantity1.grid(row=1, column=1)
    button1 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertRegularPatty)
    button1.grid(row=1, column=2)
    button01 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button01.grid(row=1, column=3)

    def disable_text():
        quantity2.config(state='disabled')

    def enable_text():
        text2.config(state='normal')
        quantity2.config(state='normal')

    text2 = Label(listFrame, text='Large Patty', font=('arial', 18, 'bold'), bd=6)
    text2.grid(row=2, column=0, padx=10)
    quantity2 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=largepatty)
    quantity2.grid(row=2, column=1)
    button2 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertLargePatty)
    button2.grid(row=2, column=2)
    button02 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button02.grid(row=2, column=3)

    def disable_text():
        quantity3.config(state='disabled')

    def enable_text():
        text3.config(state='normal')
        quantity3.config(state='normal')

    text3 = Label(listFrame, text='Large Naga Patty', font=('arial', 18, 'bold'), bd=6)
    text3.grid(row=3, column=0, padx=10)
    quantity3 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=nagalargepatty)
    quantity3.grid(row=3, column=1)
    button3 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertLargePatty)
    button3.grid(row=3, column=2)
    button03 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button03.grid(row=3, column=3)

    def disable_text():
        quantity4.config(state='disabled')

    def enable_text():
        text4.config(state='normal')
        quantity4.config(state='normal')

    text4 = Label(listFrame, text='Bun', font=('arial', 18, 'bold'), bd=6)
    text4.grid(row=4, column=0, padx=10)
    quantity4 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=bun)
    quantity4.grid(row=4, column=1)
    button4 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertBun)
    button4.grid(row=4, column=2)
    button04 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button04.grid(row=4, column=3)

    def disable_text():
        quantity5.config(state='disabled')

    def enable_text():
        text5.config(state='normal')
        quantity5.config(state='normal')

    text5 = Label(listFrame, text='Wings Serving', font=('arial', 18, 'bold'), bd=6)
    text5.grid(row=5, column=0, padx=10)
    quantity5 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=wings)
    quantity5.grid(row=5, column=1)
    button5 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertwings)
    button5.grid(row=5, column=2)
    button05 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button05.grid(row=5, column=3)

    def disable_text():
        quantity6.config(state='disabled')

    def enable_text():
        text6.config(state='normal')
        quantity6.config(state='normal')

    text6 = Label(listFrame, text='French Fry Serving', font=('arial', 18, 'bold'), bd=6)
    text6.grid(row=6, column=0, padx=10)
    quantity6 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=fries)
    quantity6.grid(row=6, column=1)
    button6 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertfries)
    button6.grid(row=6, column=2)
    button06 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button06.grid(row=6, column=3)

    def disable_text():
        quantity7.config(state='disabled')

    def enble_text():
        text7.config(state='normal')
        quantity7.config(state='normal')

    text7 = Label(listFrame, text='Rice(kg)', font=('arial', 18, 'bold'), bd=6)
    text7.grid(row=7, column=0, padx=10)
    quantity7 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=rice)
    quantity7.grid(row=7, column=1)
    button7 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertrice)
    button7.grid(row=7, column=2)
    button07 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button07.grid(row=7, column=3)

    def disable_text():
        quantity8.config(state='disabled')

    def enable_text():
        text8.config(state='normal')
        quantity8.config(state='normal')

    text8 = Label(listFrame, text='Chicken(kg)', font=('arial', 18, 'bold'), bd=6)
    text8.grid(row=8, column=0, padx=10)
    quantity8 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=chicken)
    quantity8.grid(row=8, column=1)
    button8 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertchicken)
    button8.grid(row=8, column=2)
    button07 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button07.grid(row=8, column=3)

    def disable_text():
        quantity9.config(state='disabled')

    def enable_text():
        text9.config(state='normal')
        quantity9.config(state='normal')

    text9 = Label(listFrame, text='Coke', font=('arial', 18, 'bold'), bd=6)
    text9.grid(row=9, column=0, padx=10)
    quantity9 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=coke)
    quantity9.grid(row=9, column=1)
    button9 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertcoke)
    button9.grid(row=9, column=2)
    button09 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button09.grid(row=9, column=3)

    def disable_text():
        quantity10.config(state='disabled')

    def enable_text():
        text10.config(state='normal')
        quantity10.config(state='normal')

    text10 = Label(listFrame, text='Fanta', font=('arial', 18, 'bold'), bd=6)
    text10.grid(row=10, column=0, padx=10)
    quantity10 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=fanta)
    quantity10.grid(row=10, column=1)
    button10 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertfanta)
    button10.grid(row=10, column=2)
    button010 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button010.grid(row=10, column=3)

    def disable_text():

        quantity11.config(state='disabled')

    def enable_text():
        text11.config(state='normal')
        quantity11.config(state='normal')

    text11 = Label(listFrame, text='Sprite', font=('arial', 18, 'bold'), bd=6)
    text11.grid(row=11, column=0, padx=10)
    quantity11 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=sprite)
    quantity11.grid(row=11, column=1)
    button11 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertfanta)
    button11.grid(row=11, column=2)
    button011 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button011.grid(row=11, column=3)

    def disable_text():

        quantity12.config(state='disabled')

    def enable_text():
        text12.config(state='normal')
        quantity12.config(state='normal')

    text12 = Label(listFrame, text='Water', font=('arial', 18, 'bold'), bd=6)
    text12.grid(row=12, column=0)
    quantity12 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6, textvariable=water)
    quantity12.grid(row=12, column=1)
    button12 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=insertwater)
    button12.grid(row=12, column=2)
    button012 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button012.grid(row=12, column=3)

    def disable_text():

        quantity13.config(state='disabled')

    def enable_text():
        text13.config(state='normal')
        quantity13.config(state='normal')

    text13 = Label(listFrame, text='Potato', font=('arial', 18, 'bold'), bd=6)
    text13.grid(row=13, column=0, padx=10)
    quantity13 = Entry(listFrame, font=('arial', 18, 'bold'), bd=6)
    quantity13.grid(row=13, column=1)
    button13 = Button(listFrame, text='ADD', font=('arial', 12, 'bold'), command=disable_text)
    button13.grid(row=13, column=2)
    button013 = Button(listFrame, text='Change', font=('arial', 12, 'bold'), command=enable_text)
    button013.grid(row=13, column=3)

    root.mainloop()  # to hold the window

def Menu():
    topFrame.destroy()
    topFrame = Frame(root, bd=10, relief=RAISED, bg='slate grey', width=300, height=500)  # create top frame
    topFrame.place(relx=0.5, rely=0.5, anchor=CENTER)  # view top frame

    labelTitle = Label(topFrame, text='Backyard Stories', font=('arial', 30, 'bold'), bg='wheat1', bd=9, width=80,
                       height=1)
    labelTitle.grid(row=0, column=0)

    billbutton = Button(topFrame, text="Generate Bill", font=('bold', 20), command=Bill).grid(row=10, column=0,
                                                                                                       padx=10, pady=5)
    inventorybutton = Button(topFrame, text="Inventory", font=('bold', 20), command=Inventory).grid(row=11, column=0,
                                                                                                    padx=10, pady=5)

    root.mainloop()
def Bill():
    topFrame.destroy()

    # image= ImageTk.PhotoImage(Image.open("2.png"))
    # label1= Label(image= image)
    # label1.pack()

    Label(text="Billing System", bg="black", fg="white", font=("Lucida Calligraphy", 30, 'bold'), width="300",
          height="1").pack()

    # Creating Menu
    frame = Frame(root, bg='cyan4', bd=10, height=20, width=62, relief=RAISED)
    frame.place(x=10, y=70)
    aframe = Frame(root, bg='cyan4', bd=10, height=20, width=62, relief=RAISED)
    aframe.place(x=1100, y=490)
    bframe = Frame(root, bg='cyan4', bd=10, height=20, width=62, relief=RAISED)
    bframe.place(x=1100, y=70)
    billframe = Frame(root, bg='cyan4', bd=10, relief=RAISED)
    billframe.place(x=10, y=900)

    def reset():
        large_chicken_burger.set(0)
        large_naga_chicken_burger.set(0)
        regular_chicken_burger.set(0)
        regular_naga_chicken_burger.set(0)
        ricebowl.set(0)
        meatbox.set(0)
        frenchfries.set(0)
        naga_chicken_wings.set(0)
        sweet_chicken_wings.set(0)
        coke.set(0)
        sprite.set(0)
        fanta.set(0)
        water.set(0)
        cheese.set(0)
        mayo.set(0)
        lpatty.set(0)
        rPatty.set(0)

    def Total():
        global total
        try:
            a = int(large_chicken_burger.get()) * 100
        except:
            a = 0
        try:
            b = int(large_naga_chicken_burger.get()) * 100
        except:
            b = 0
        try:
            c = int(regular_chicken_burger.get()) * 65
        except:
            c = 0
        try:
            d = int(regular_naga_chicken_burger.get()) * 65
        except:
            d = 0
        try:
            e = int(naga_chicken_wings.get()) * 125
        except:
            e = 0
        try:
            f = int(sweet_chicken_wings.get()) * 125
        except:
            f = 0
        try:
            g = int(meatbox.get()) * 140
        except:
            g = 0
        try:
            h = int(ricebowl.get()) * 90
        except:
            h = 0
        try:
            i = int(fries.get()) * 40
        except:
            i = 0
        try:
            j = int(coke.get()) * 20
        except:
            j = 0

        try:
            k = int(sprite.get()) * 20
        except:
            k = 0
        try:
            l = int(fanta.get()) * 20
        except:
            l = 0
        try:
            m = int(water.get()) * 20
        except:
            m = 0

        total = a + b + c + d + e + f + g + h + i + j + k + l + m
        # bill= str("%.2f"%total)+"TK."

        total_bill.set(total)

    def Return():
        amountpaid = int(paid_amount.get())
        amountreturn = amountpaid - total
        return_amount.set(amountreturn)

    # Appetizers

    Label(frame, font=("Lucida Calligraphy", 40, 'bold'), bd=6, text="Appetizer", fg="black", bg="white").grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=10)
    Label(frame, font=("Lucida Calligraphy", 40, 'bold'), bd=6, text="Cost", fg="black", bg="white").grid(row=0,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=10)
    Label(frame, font=("Lucida Calligraphy", 40, 'bold'), bd=6, text="Quantity", fg="black", bg="white").grid(row=0,
                                                                                                              column=2,
                                                                                                              padx=10,
                                                                                                              pady=10)
    # Label(frame, font=("Lucida Calligraphy",15, 'bold'), text= "Amount", fg= "black", bg= "yellow" ).grid(row=0, column= 3)

    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Large Chicken Burger", fg="black",
          bg="white").grid(row=1, column=0, padx=10, pady=10)
    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="100", fg="black", bg="white").grid(row=1,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Large Naga Chicken Burger", fg="black",
          bg="white").grid(row=2, column=0, padx=10, pady=10)
    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="100", fg="black", bg="white").grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Regular Chicken Burger", fg="black",
          bg="white").grid(row=3, column=0, padx=10, pady=10)
    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="65", fg="black", bg="white").grid(row=3, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)

    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Regular Naga Chicken Burger", fg="black",
          bg="white").grid(row=4, column=0, padx=10, pady=10)
    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="65", fg="black", bg="white").grid(row=4, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)

    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Naga Chicken Wings", fg="black", bg="white").grid(
        row=5, column=0, padx=10, pady=10)
    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="125", fg="black", bg="white").grid(row=5,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Sweet Chicken Wings", fg="black",
          bg="white").grid(row=6, column=0, padx=10, pady=10)
    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="125", fg="black", bg="white").grid(row=6,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="MeatBox", fg="black", bg="white").grid(row=7,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=10)
    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="140", fg="black", bg="white").grid(row=7,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Rice Bowl", fg="black", bg="white").grid(row=8,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=10)
    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="90", fg="black", bg="white").grid(row=8, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)

    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="French Fries", fg="black", bg="white").grid(row=9,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10)
    Label(frame, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="40", fg="black", bg="white").grid(row=9, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)

    Label(bframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Beverages", fg="black", bg="white").grid(row=0,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10)
    Label(bframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Cost", fg="black", bg="white").grid(row=0,
                                                                                                           column=1,
                                                                                                           padx=10,
                                                                                                           pady=10)
    Label(bframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Quantity", fg="black", bg="white").grid(row=0,
                                                                                                               column=2,
                                                                                                               padx=10,
                                                                                                               pady=10)
    # Label(bframe, font=("Lucida Calligraphy",15, 'bold'), text= "Amount", fg= "black", bg= "yellow" ).grid(row=0, column= 3)

    Label(bframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Coca Cola", fg="black", bg="white").grid(row=1,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10)
    Label(bframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="20", fg="black", bg="white").grid(row=1,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

    Label(bframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Sprite", fg="black", bg="white").grid(row=2,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=10)
    Label(bframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="20", fg="black", bg="white").grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

    Label(bframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Fanta", fg="black", bg="white").grid(row=3,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=10)
    Label(bframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="20", fg="black", bg="white").grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

    Label(bframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Water", fg="black", bg="white").grid(row=4,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=10)
    Label(bframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="15", fg="black", bg="white").grid(row=4,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

    # ADD-Ons
    Label(aframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Add-ons", fg="black", bg="white").grid(row=0,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=10)
    Label(aframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Cost", fg="black", bg="white").grid(row=0,
                                                                                                           column=1,
                                                                                                           padx=10,
                                                                                                           pady=10)
    Label(aframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Quantity", fg="black", bg="white").grid(row=0,
                                                                                                               column=2,
                                                                                                               padx=10,
                                                                                                               pady=10)
    # Label(aframe, font=("Lucida Calligraphy",15, 'bold'), text= "Amount", fg= "black", bg= "yellow" ).grid(row=0, column= 3)

    Label(aframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Cheese", fg="black", bg="white").grid(row=1,
                                                                                                             column=0,
                                                                                                             padx=10)
    Label(aframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Mayonnaise", fg="black", bg="white").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10)
    Label(aframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="10", fg="black", bg="white").grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

    Label(aframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Large Patty", fg="black", bg="white").grid(row=3,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10)
    Label(aframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="50", fg="black", bg="white").grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

    Label(aframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Regular Patty", fg="black", bg="white").grid(
        row=4, column=0, padx=10, pady=10)
    Label(aframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="35", fg="black", bg="white").grid(row=4,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

    # Bill

    Label(billframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Total bill", fg="black", bg="white").grid(
        row=0,
        column=0, padx=45, pady=10)
    Label(billframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Amount Paid", fg="black", bg="white").grid(
        row=0,
        column=3, padx=45, pady=10)
    # Label(billframe, font=("Lucida Calligraphy", 25, 'bold'),bd=6 ,text="Return", fg="black", bg="white").grid(row=2,column=0,padx=10, pady=10)
    Button(billframe, font=("Lucida Calligraphy", 25, 'bold'), bd=6, text="Return", command=Return, fg="black",
           bg="pink").grid(row=0,
                           column=6, padx=45, pady=10)
    # entry Field
    large_chicken_burger = StringVar()
    large_naga_chicken_burger = StringVar()
    regular_chicken_burger = StringVar()
    regular_naga_chicken_burger = StringVar()
    naga_chicken_wings = StringVar()
    sweet_chicken_wings = StringVar()
    ricebowl = StringVar()
    meatbox = StringVar()
    frenchfries = StringVar()
    large_chicken_burger_amount = StringVar()
    large_naga_chicken_burger_amount = StringVar()
    regular_chicken_burger_amount = StringVar()
    regular_naga_chicken_burger_amount = StringVar()
    chicken_wings_amount = StringVar()
    ricebowl_amount = StringVar()
    meatbox_amount = StringVar()
    frenchfries_amount = StringVar()
    coke = StringVar()
    coke_amount = StringVar()
    sprite = StringVar()
    sprite_amount = StringVar()
    fanta = StringVar()
    fanta_amount = StringVar()
    water = StringVar()
    water_amount = StringVar()
    cheese = StringVar()
    mayo = StringVar()
    lpatty = StringVar()
    rPatty = StringVar()
    cheese_amount = StringVar()
    mayo_amount = StringVar()
    lpatty_amount = StringVar()
    rpatty_amount = StringVar()
    total_bill = IntVar()
    paid_amount = IntVar()
    return_amount = IntVar()

    lburger = Entry(frame, font=('arial', 25, 'bold'), textvariable=large_chicken_burger, bd=6, width=8,
                    bg='yellow').grid(row=1, column=2, padx=10, pady=10)
    lnburger = Entry(frame, font=('arial', 25, 'bold'), textvariable=large_naga_chicken_burger, bd=6, width=8,
                     bg='yellow').grid(row=2, column=2, padx=10, pady=10)
    rburger = Entry(frame, font=('arial', 25, 'bold'), textvariable=regular_chicken_burger, bd=6, width=8,
                    bg='yellow').grid(row=3, column=2, padx=10, pady=10)
    rnburger = Entry(frame, font=('arial', 25, 'bold'), textvariable=regular_naga_chicken_burger, bd=6, width=8,
                     bg='yellow').grid(row=4, column=2, padx=10, pady=10)
    nwongs = Entry(frame, font=('arial', 25, 'bold'), textvariable=naga_chicken_wings, bd=6, width=8, bg='yellow').grid(
        row=5, column=2, padx=10, pady=10)
    swings = Entry(frame, font=('arial', 25, 'bold'), textvariable=sweet_chicken_wings, bd=6, width=8,
                   bg='yellow').grid(row=6, column=2, padx=10, pady=10)
    mbox = Entry(frame, font=('arial', 25, 'bold'), textvariable=meatbox, bd=6, width=8, bg='yellow').grid(row=7,
                                                                                                           column=2,
                                                                                                           padx=10,
                                                                                                           pady=10)
    rbowl = Entry(frame, font=('arial', 25, 'bold'), textvariable=ricebowl, bd=6, width=8, bg='yellow').grid(row=8,
                                                                                                             column=2,
                                                                                                             padx=10,
                                                                                                             pady=10)
    fries = Entry(frame, font=('arial', 25, 'bold'), textvariable=frenchfries, bd=6, width=8, bg='yellow').grid(row=9,
                                                                                                                column=2,
                                                                                                                padx=10,
                                                                                                                pady=10)

    bcoke = Entry(bframe, font=('arial', 25, 'bold'), textvariable=coke, bd=6, width=8, bg='yellow').grid(row=1,
                                                                                                          column=2,
                                                                                                          padx=120,
                                                                                                          pady=10)
    bsprite = Entry(bframe, font=('arial', 25, 'bold'), textvariable=sprite, bd=6, width=8, bg='yellow').grid(row=2,
                                                                                                              column=2,
                                                                                                              padx=120,
                                                                                                              pady=10)
    bfanta = Entry(bframe, font=('arial', 25, 'bold'), textvariable=fanta, bd=6, width=8, bg='yellow').grid(row=3,
                                                                                                            column=2,
                                                                                                            padx=120,
                                                                                                            pady=10)
    bwater = Entry(bframe, font=('arial', 25, 'bold'), textvariable=water, bd=6, width=8, bg='yellow').grid(row=4,
                                                                                                            column=2,
                                                                                                            padx=120,
                                                                                                            pady=10)

    acheese = Entry(aframe, font=('arial', 25, 'bold'), textvariable=cheese, bd=6, width=8, bg='yellow').grid(row=1,
                                                                                                              column=2,
                                                                                                              padx=80,
                                                                                                              pady=10)
    amayo = Entry(aframe, font=('arial', 25, 'bold'), textvariable=mayo, bd=6, width=8, bg='yellow').grid(row=2,
                                                                                                          column=2,
                                                                                                          padx=80,
                                                                                                          pady=10)
    alpatty = Entry(aframe, font=('arial', 25, 'bold'), textvariable=lpatty, bd=6, width=8, bg='yellow').grid(row=3,
                                                                                                              column=2,
                                                                                                              padx=80,
                                                                                                              pady=10)
    arpatty = Entry(aframe, font=('arial', 25, 'bold'), textvariable=rPatty, bd=6, width=8, bg='yellow').grid(row=4,
                                                                                                              column=2,
                                                                                                              padx=80,
                                                                                                              pady=10)

    billamount = Entry(billframe, font=('arial', 25, 'bold'), textvariable=total_bill, bd=6, width=8, bg='yellow').grid(
        row=0, column=1, columnspan=2, padx=10, pady=10)
    paidamount = Entry(billframe, font=('arial', 25, 'bold'), textvariable=paid_amount, bd=6, width=8,
                       bg='yellow').grid(row=0, column=4, columnspan=2, padx=10, pady=10)
    returnamount = Entry(billframe, font=('arial', 25, 'bold'), textvariable=return_amount, bd=6, width=8,
                         bg='yellow').grid(row=0, column=7, columnspan=2, padx=10, pady=10)

    # Buttons
    resetbutton = Button(billframe, font=('arial', 25, 'bold'), bd=6, width=8, bg='yellow', text="Reset",
                         command=reset).grid(row=0, column=9, columnspan=2, padx=10, pady=10)
    totalbutton = Button(billframe, font=('arial', 25, 'bold'), bd=6, width=8, bg='yellow', text="Total",
                         command=Total).grid(row=0, column=11, columnspan=2, padx=10, pady=10)

    root.mainloop()

    button_quit = Button(root, text="Exit", command=root.quit)
    button_quit.pack()

    root.mainloop()

def loginclicked():
    global password
    global username
    
    if username.get()=='' or password.get()=='':
        messagebox.showinfo("Error", "You need to put an username and password")
    elif username.get()!='' or password.get()!='':
        sql= "SELECT * FROM user Where BINARY username= '%s' AND BINARY password= '%s'" %(username.get(),password.get())
        cursor.execute(sql)
        if cursor.fetchone():
            messagebox.showinfo("Successful", "Welcome!")
            Menu()
        else:
            messagebox.showinfo("Error", "Invalid Credentials")


#GUI
r= IntVar()
r.set(2)
password= StringVar()
username= StringVar()

topFrame=Frame(root, bd=10,relief=RAISED,bg='slate grey',width= 300,height=500)     #create top frame
topFrame.place(relx=0.5, rely=0.5, anchor=CENTER)      #view top frame

labelTitle=Label(topFrame, text='Backyard Stories', font=('arial',30,'bold'),bg='wheat1',bd=9,width=80, height =1)
labelTitle.grid(row= 0, column=0)

usernamelabel= Label(topFrame, text= "Username",font=('bold', 20) ).grid(row= 3 ,column= 0,pady= 5)
entry_username= Entry(topFrame, textvariable= username,font=('bold', 20) ).grid(row= 5 ,column= 0, pady=5)

passwordlabel= Label(topFrame, text= "Password",font=('bold', 20) ).grid(row= 7 ,column= 0, pady=5)
entry_password= Entry(topFrame, textvariable= password,font=('bold', 20) ).grid(row= 9 ,column= 0, pady=5)
loginbutton= Button(topFrame, text= "Login",font=('bold', 20) , command= loginclicked).grid(row= 11 ,column= 0, pady=5)



root.mainloop()