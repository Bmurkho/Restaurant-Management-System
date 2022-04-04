from tkinter import * #A module for gui
import mysql.connector
from tkinter import messagebox
root=Tk()     #for window

root.geometry("1920x1080+0+0")     #resize the window

root.resizable(0,0)           #disable the maximize button

root.title('BACKYARD STORIES')    #give a title

root.config(bg='#116562')    #change background color

conn= mysql.connector.connect(host="localhost", user= "root", passwd= "", database="bstories"  )
cursor= conn.cursor()
if conn.is_connected():
    print("successfully connected")
else:
    print("Ivalid")

topFrame=Frame(root, bd=10,relief=RAISED,bg='cyan4')     #create top frame
topFrame.pack(side=TOP)       #view top frame

labelTitle=Label(topFrame, text='Inventory', font=('arial',30,'bold'),bg='wheat1',
                 bd=9,width=62)
labelTitle.grid(row=0,column=0)


itemFrame=Frame(root,bg='cyan4',bd=10,height=20,width=62,relief=RAISED)
itemFrame.pack( anchor= CENTER)

listFrame=LabelFrame(itemFrame,text='Item',font=('arial',30,'bold'),
                 bd=5,width=62)
listFrame.pack()

#defining variables
regularpatty= StringVar()
nagaregularpatty= StringVar()
largepatty= StringVar()
nagalargepatty= StringVar()
bun= StringVar()
wings= StringVar()
fries= StringVar()
rice= StringVar()
chicken= StringVar()
coke= StringVar()
sprite= StringVar()
fanta= StringVar()
water= StringVar()

def insertRegularPatty():
    global regularpatty
    sql= "INSERT INTO Inventory (Regular_Patty) VALUES ('%d') " % (int(regularpatty.get()))
    cursor.execute(sql)
    messagebox.showinfo("Successful", "Item added Successfully!")
    quantity0.delete(0, END)
    conn.commit()


def insertLargePatty():
    global largepatty
    sql= "INSERT INTO Inventory (Large_Patty) VALUES ('%d') " % (int(largepatty.get()))
    cursor.execute(sql)
    messagebox.showinfo("Successful", "Item added Successfully!")
    quantity1.delete(0, END)
    conn.commit()

def insertBun():
    global bun
    sql= "INSERT INTO Inventory (Bun) VALUES ('%d') " % (int(bun.get()))
    cursor.execute(sql)
    messagebox.showinfo("Successful", "Item added Successfully!")
    quantity2.delete(0, END)
    conn.commit()

def insertwings():
    global wings
    sql= "INSERT INTO Inventory (Wings_Serving) VALUES ('%d') " % (int(wings.get()))
    cursor.execute(sql)
    messagebox.showinfo("Successful", "Item added Successfully!")
    quantity3.delete(0, END)
    conn.commit()

def insertfries():
    global fries
    sql= "INSERT INTO Inventory (French_Fry_Serving) VALUES ('%d') " % (int(fries.get()))
    cursor.execute(sql)
    messagebox.showinfo("Successful", "Item added Successfully!")
    quantity4.delete(0, END)
    conn.commit()

def insertrice():
    global rice
    sql= "INSERT INTO Inventory (Rice_kg) VALUES ('%d') " % (int(rice.get()))
    cursor.execute(sql)
    messagebox.showinfo("Successful", "Item added Successfully!")
    quantity5.delete(0, END)
    conn.commit()

def insertchicken():
    global chicken
    sql= "INSERT INTO Inventory (Chicken_kg) VALUES ('%d') " % (int(chicken.get()))
    cursor.execute(sql)
    messagebox.showinfo("Successful", "Item added Successfully!")
    quantity6.delete(0, END)
    conn.commit()

def insertcoke():
    global coke
    sql= "INSERT INTO Inventory (Coca_Cola) VALUES ('%d') " % (int(coke.get()))
    cursor.execute(sql)
    messagebox.showinfo("Successful", "Item added Successfully!")
    quantity7.delete(0, END)
    conn.commit()

def insertsprite():
    global sprite
    sql= "INSERT INTO Inventory (Sprite) VALUES ('%d') " % (int(sprite.get()))
    cursor.execute(sql)
    messagebox.showinfo("Successful", "Item added Successfully!")
    quantity8.delete(0, END)
    conn.commit()

def insertfanta():
    global fanta
    sql= "INSERT INTO Inventory (Fanta) VALUES ('%d') " % (int(fanta.get()))
    cursor.execute(sql)
    messagebox.showinfo("Successful", "Item added Successfully!")
    quantity9.delete(0, END)
    conn.commit()

def insertwater():
    global water
    sql= "INSERT INTO Inventory (Water) VALUES ('%d') " % (int(water.get()))
    cursor.execute(sql)
    messagebox.showinfo("Successful", "Item added Successfully!")
    quantity10.delete(0, END)
    conn.commit()


def disable_text():
    quantity0.config(state='disabled')

def enable_text():
    text0.config(state='normal')
    quantity0.config(state='normal')


text0=Label(listFrame,text='Regular Patty',font=('arial',18,'bold'),bd=6)
text0.grid(row=0,column=0,padx=10)
quantity0=Entry(listFrame,font=('arial',18,'bold'),bd=6, textvariable= regularpatty)
quantity0.grid(row=0,column=1,padx=10)
button0=Button(listFrame,text='ADD',font=('arial',12,'bold'), command= insertRegularPatty)
button0.grid(row=0,column=2,padx=10)
button00=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button00.grid(row=0,column=3,padx=10)




def disable_text():
    quantity1.config(state='disabled')

def enable_text():
    text1.config(state='normal')
    quantity1.config(state='normal')


text1=Label(listFrame,text='Naga Regular Patty',font=('arial',18,'bold'),bd=6)
text1.grid(row=1,column=0,padx=10)
quantity1=Entry(listFrame,font=('arial',18,'bold'),bd=6,textvariable= nagaregularpatty)
quantity1.grid(row=1,column=1)
button1=Button(listFrame,text='ADD',font=('arial',12,'bold'), command= insertRegularPatty)
button1.grid(row=1,column=2)
button01=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button01.grid(row=1,column=3)


def disable_text():
    quantity2.config(state='disabled')

def enable_text():
    text2.config(state='normal')
    quantity2.config(state='normal')

text2=Label(listFrame,text='Large Patty',font=('arial',18,'bold'),bd=6)
text2.grid(row=2,column=0,padx=10)
quantity2=Entry(listFrame,font=('arial',18,'bold'),bd=6, textvariable= largepatty)
quantity2.grid(row=2,column=1)
button2=Button(listFrame,text='ADD',font=('arial',12,'bold'),command=insertLargePatty)
button2.grid(row=2,column=2)
button02=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button02.grid(row=2,column=3)


def disable_text():
    quantity3.config(state='disabled')

def enable_text():
    text3.config(state='normal')
    quantity3.config(state='normal')


text3=Label(listFrame,text='Large Naga Patty',font=('arial',18,'bold'),bd=6)
text3.grid(row=3,column=0,padx=10)
quantity3=Entry(listFrame,font=('arial',18,'bold'),bd=6, textvariable= nagalargepatty)
quantity3.grid(row=3,column=1)
button3=Button(listFrame,text='ADD',font=('arial',12,'bold'),command=insertLargePatty)
button3.grid(row=3,column=2)
button03=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button03.grid(row=3,column=3)


def disable_text():
    quantity4.config(state='disabled')

def enable_text():
    text4.config(state='normal')
    quantity4.config(state='normal')


text4=Label(listFrame,text='Bun',font=('arial',18,'bold'),bd=6)
text4.grid(row=4,column=0,padx=10)
quantity4=Entry(listFrame,font=('arial',18,'bold'),bd=6, textvariable=bun)
quantity4.grid(row=4,column=1)
button4=Button(listFrame,text='ADD',font=('arial',12,'bold'),command=insertBun)
button4.grid(row=4,column=2)
button04=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button04.grid(row=4,column=3)


def disable_text():
    quantity5.config(state='disabled')

def enable_text():
    text5.config(state='normal')
    quantity5.config(state='normal')


text5=Label(listFrame,text='Wings Serving',font=('arial',18,'bold'),bd=6)
text5.grid(row=5,column=0,padx=10)
quantity5=Entry(listFrame,font=('arial',18,'bold'),bd=6, textvariable=wings)
quantity5.grid(row=5,column=1)
button5=Button(listFrame,text='ADD',font=('arial',12,'bold'),command=insertwings)
button5.grid(row=5,column=2)
button05=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button05.grid(row=5,column=3)


def disable_text():
    quantity6.config(state='disabled')

def enable_text():
    text6.config(state='normal')
    quantity6.config(state='normal')


text6=Label(listFrame,text='French Fry Serving',font=('arial',18,'bold'),bd=6)
text6.grid(row=6,column=0,padx=10)
quantity6=Entry(listFrame,font=('arial',18,'bold'),bd=6, textvariable=fries)
quantity6.grid(row=6,column=1)
button6=Button(listFrame,text='ADD',font=('arial',12,'bold'),command=insertfries)
button6.grid(row=6,column=2)
button06=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button06.grid(row=6,column=3)


def disable_text():
    quantity7.config(state='disabled')

def enble_text():
    text7.config(state='normal')
    quantity7.config(state='normal')


text7=Label(listFrame,text='Rice(kg)',font=('arial',18,'bold'),bd=6)
text7.grid(row=7,column=0,padx=10)
quantity7=Entry(listFrame,font=('arial',18,'bold'),bd=6, textvariable=rice)
quantity7.grid(row=7,column=1)
button7=Button(listFrame,text='ADD',font=('arial',12,'bold'),command=insertrice)
button7.grid(row=7,column=2)
button07=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button07.grid(row=7,column=3)


def disable_text():
    quantity8.config(state='disabled')

def enable_text():
    text8.config(state='normal')
    quantity8.config(state='normal')


text8=Label(listFrame,text='Chicken(kg)',font=('arial',18,'bold'),bd=6)
text8.grid(row=8,column=0,padx=10)
quantity8=Entry(listFrame,font=('arial',18,'bold'),bd=6, textvariable=chicken)
quantity8.grid(row=8,column=1)
button8=Button(listFrame,text='ADD',font=('arial',12,'bold'),command=insertchicken)
button8.grid(row=8,column=2)
button07=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button07.grid(row=8,column=3)


def disable_text():
    quantity9.config(state='disabled')

def enable_text():
    text9.config(state='normal')
    quantity9.config(state='normal')


text9=Label(listFrame,text='Coke',font=('arial',18,'bold'),bd=6)
text9.grid(row=9,column=0,padx=10)
quantity9=Entry(listFrame,font=('arial',18,'bold'),bd=6, textvariable=coke)
quantity9.grid(row=9,column=1)
button9=Button(listFrame,text='ADD',font=('arial',12,'bold'),command=insertcoke)
button9.grid(row=9,column=2)
button09=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button09.grid(row=9,column=3)


def disable_text():
    quantity10.config(state='disabled')

def enable_text():
    text10.config(state='normal')
    quantity10.config(state='normal')


text10=Label(listFrame,text='Fanta',font=('arial',18,'bold'),bd=6)
text10.grid(row=10,column=0,padx=10)
quantity10=Entry(listFrame,font=('arial',18,'bold'),bd=6, textvariable=fanta)
quantity10.grid(row=10,column=1)
button10=Button(listFrame,text='ADD',font=('arial',12,'bold'),command=insertfanta)
button10.grid(row=10,column=2)
button010=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button010.grid(row=10,column=3)



def disable_text():

    quantity11.config(state='disabled')

def enable_text():
    text11.config(state='normal')
    quantity11.config(state='normal')


text11=Label(listFrame,text='Sprite',font=('arial',18,'bold'),bd=6)
text11.grid(row=11,column=0,padx=10)
quantity11=Entry(listFrame,font=('arial',18,'bold'),bd=6, textvariable=sprite)
quantity11.grid(row=11,column=1)
button11=Button(listFrame,text='ADD',font=('arial',12,'bold'),command=insertfanta)
button11.grid(row=11,column=2)
button011=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button011.grid(row=11,column=3)


def disable_text():

    quantity12.config(state='disabled')

def enable_text():
    text12.config(state='normal')
    quantity12.config(state='normal')


text12=Label(listFrame,text='Water',font=('arial',18,'bold'),bd=6)
text12.grid(row=12,column=0)
quantity12=Entry(listFrame,font=('arial',18,'bold'),bd=6, textvariable=water)
quantity12.grid(row=12,column=1)
button12=Button(listFrame,text='ADD',font=('arial',12,'bold'),command=insertwater)
button12.grid(row=12,column=2)
button012=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button012.grid(row=12,column=3)


def disable_text():

    quantity13.config(state='disabled')

def enable_text():
    text13.config(state='normal')
    quantity13.config(state='normal')


text13=Label(listFrame,text='Potato',font=('arial',18,'bold'),bd=6)
text13.grid(row=13,column=0,padx=10)
quantity13=Entry(listFrame,font=('arial',18,'bold'),bd=6)
quantity13.grid(row=13,column=1)
button13=Button(listFrame,text='ADD',font=('arial',12,'bold'),command=disable_text)
button13.grid(row=13,column=2)
button013=Button(listFrame,text='Change',font=('arial',12,'bold'),command=enable_text)
button013.grid(row=13,column=3)


root.mainloop()     #to hold the window
