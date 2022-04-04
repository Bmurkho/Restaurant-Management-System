from tkinter import *
from PIL import Image, ImageTk

root= Tk()
root.title("Backyard Stories")
root.iconbitmap("D:/pythonProject1/1.ico")
root.geometry("1920x1080+0+0")
root.config(bg='#116562')
root.resizable(False, False)

#image= ImageTk.PhotoImage(Image.open("2.png"))
#label1= Label(image= image)
#label1.pack()

Label(text= "Billing System", bg= "black", fg="white", font= ("Lucida Calligraphy",30, 'bold'),width= "300" ,height= "1" ).pack()

#Creating Menuz

frame= Frame(root,bg='cyan4',bd=10,height=20,width=62,relief=RAISED)
frame.place(x=10, y=70)
aframe= Frame(root,bg='cyan4',bd=10,height=20,width=62,relief=RAISED)
aframe.place(x=1100, y= 490)
bframe= Frame(root,bg='cyan4',bd=10,height=20,width=62,relief=RAISED)
bframe.place(x=1100, y= 70)
billframe= Frame(root,bg='cyan4',bd=10,relief=RAISED)
billframe.place(x=10, y= 900)

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
        a=0
    try:
        b = int(large_naga_chicken_burger.get()) * 100
    except:
        b=0
    try:
        c = int(regular_chicken_burger.get()) * 65
    except:
        c=0
    try:
        d = int(regular_naga_chicken_burger.get()) * 65
    except:
        d=0
    try:
        e = int(naga_chicken_wings.get()) * 125
    except:
        e=0
    try:
        f = int(sweet_chicken_wings.get()) * 125
    except:
        f=0
    try:
        g = int(meatbox.get()) * 140
    except:
        g=0
    try:
        h = int(ricebowl.get()) * 90
    except:
        h=0
    try:
        i = int(fries.get()) * 40
    except:
        i= 0
    try:
        j = int(coke.get()) * 20
    except:
        j=0

    try:
        k = int(sprite.get()) * 20
    except:
        k=0
    try:
        l = int(fanta.get()) * 20
    except:
        l=0
    try:
        m = int(water.get()) * 20
    except:
        m=0

    total = a+b+c+d+e+f+g+h+i+j+k+l+m
    #bill= str("%.2f"%total)+"TK."

    total_bill.set(total)




def Return():
    amountpaid= int(paid_amount.get())
    amountreturn= amountpaid-total
    return_amount.set(amountreturn)



#Appetizers

Label(frame, font=("Lucida Calligraphy",40, 'bold'), bd= 6, text= "Appetizer", fg= "black", bg= "white" ).grid(row=0, column= 0, padx=10,pady=10)
Label(frame, font=("Lucida Calligraphy",40, 'bold'),bd=6, text= "Cost", fg= "black", bg= "white" ).grid(row=0, column= 1,padx=10,pady=10)
Label(frame, font=("Lucida Calligraphy",40, 'bold'),bd=6, text= "Quantity", fg= "black", bg= "white" ).grid(row=0, column= 2,padx=10,pady=10)
#Label(frame, font=("Lucida Calligraphy",15, 'bold'), text= "Amount", fg= "black", bg= "yellow" ).grid(row=0, column= 3)

Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Large Chicken Burger", fg= "black", bg= "white" ).grid(row=1, column= 0,padx=10,pady=10)
Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "100", fg= "black", bg= "white" ).grid(row=1, column= 1,padx=10,pady=10)

Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Large Naga Chicken Burger", fg= "black", bg= "white" ).grid(row=2, column= 0,padx=10,pady=10)
Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "100", fg= "black", bg= "white" ).grid(row=2, column= 1,padx=10,pady=10)

Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Regular Chicken Burger", fg= "black", bg= "white" ).grid(row=3, column= 0,padx=10,pady=10)
Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "65", fg= "black", bg= "white" ).grid(row=3, column= 1,padx=10,pady=10)

Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Regular Naga Chicken Burger", fg= "black", bg= "white" ).grid(row=4, column= 0,padx=10,pady=10)
Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "65", fg= "black", bg= "white" ).grid(row=4, column= 1,padx=10,pady=10)

Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Naga Chicken Wings", fg= "black", bg= "white" ).grid(row=5, column= 0,padx=10,pady=10)
Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "125", fg= "black", bg= "white" ).grid(row=5, column= 1,padx=10,pady=10)

Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Sweet Chicken Wings", fg= "black", bg= "white" ).grid(row=6, column= 0,padx=10,pady=10)
Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "125", fg= "black", bg= "white" ).grid(row=6, column= 1,padx=10,pady=10)

Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "MeatBox", fg= "black", bg= "white" ).grid(row=7, column= 0,padx=10,pady=10)
Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "140", fg= "black", bg= "white" ).grid(row=7, column= 1,padx=10,pady=10)

Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Rice Bowl", fg= "black", bg= "white" ).grid(row=8, column= 0,padx=10,pady=10)
Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "90", fg= "black", bg= "white" ).grid(row=8, column= 1,padx=10,pady=10)

Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "French Fries", fg= "black", bg= "white" ).grid(row=9, column= 0,padx=10,pady=10)
Label(frame, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "40", fg= "black", bg= "white" ).grid(row=9, column= 1,padx=10,pady=10)


Label(bframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Beverages", fg= "black", bg= "white" ).grid(row=0, column= 0,padx=10,pady=10)
Label(bframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Cost", fg= "black", bg= "white" ).grid(row=0, column= 1,padx=10,pady=10)
Label(bframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Quantity", fg= "black", bg= "white" ).grid(row=0, column= 2,padx=10,pady=10)
#Label(bframe, font=("Lucida Calligraphy",15, 'bold'), text= "Amount", fg= "black", bg= "yellow" ).grid(row=0, column= 3)

Label(bframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Coca Cola", fg= "black", bg= "white" ).grid(row=1, column= 0,padx=10,pady=10)
Label(bframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "20", fg= "black", bg= "white" ).grid(row=1, column= 1,padx=10,pady=10)

Label(bframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Sprite", fg= "black", bg= "white" ).grid(row=2, column= 0,padx=10,pady=10)
Label(bframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "20", fg= "black", bg= "white" ).grid(row=2, column= 1,padx=10,pady=10)

Label(bframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Fanta", fg= "black", bg= "white" ).grid(row=3, column= 0,padx=10,pady=10)
Label(bframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "20", fg= "black", bg= "white" ).grid(row=3, column= 1,padx=10,pady=10)

Label(bframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Water", fg= "black", bg= "white" ).grid(row=4, column= 0,padx=10,pady=10)
Label(bframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "15", fg= "black", bg= "white" ).grid(row=4, column= 1,padx=10,pady=10)

#ADD-Ons
Label(aframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Add-ons", fg= "black", bg= "white" ).grid(row=0, column= 0,padx=10,pady=10)
Label(aframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Cost", fg= "black", bg= "white" ).grid(row=0, column= 1,padx=10,pady=10)
Label(aframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Quantity", fg= "black", bg= "white" ).grid(row=0, column= 2,padx=10,pady=10)
#Label(aframe, font=("Lucida Calligraphy",15, 'bold'), text= "Amount", fg= "black", bg= "yellow" ).grid(row=0, column= 3)

Label(aframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Cheese", fg= "black", bg= "white" ).grid(row=1, column= 0,padx=10)
Label(aframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Mayonnaise", fg= "black", bg= "white" ).grid(row=2, column= 0,padx=10,pady=10)
Label(aframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "10", fg= "black", bg= "white" ).grid(row=2, column= 1,padx=10,pady=10)

Label(aframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Large Patty", fg= "black", bg= "white" ).grid(row=3, column= 0,padx=10,pady=10)
Label(aframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "50", fg= "black", bg= "white" ).grid(row=3, column= 1,padx=10,pady=10)

Label(aframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "Regular Patty", fg= "black", bg= "white" ).grid(row=4, column= 0,padx=10,pady=10)
Label(aframe, font=("Lucida Calligraphy",25, 'bold'),bd=6, text= "35", fg= "black", bg= "white" ).grid(row=4, column= 1,padx=10,pady=10)


#Bill

Label(billframe, font=("Lucida Calligraphy", 25, 'bold'),bd=6, text="Total bill", fg="black", bg="white").grid(row=0,
                                                                                                         column=0,padx=45, pady=10)
Label(billframe, font=("Lucida Calligraphy", 25, 'bold'),bd=6 ,text="Amount Paid", fg="black", bg="white").grid(row=0,
                                                                                                            column=3,padx=45,pady=10)
#Label(billframe, font=("Lucida Calligraphy", 25, 'bold'),bd=6 ,text="Return", fg="black", bg="white").grid(row=2,column=0,padx=10, pady=10)
Button(billframe, font=("Lucida Calligraphy", 25, 'bold'),bd=6 ,text="Return",command=Return, fg="black", bg="pink").grid(row=0,
                                                                                                       column=6,padx=45, pady=10)
#entry Field
large_chicken_burger= StringVar()
large_naga_chicken_burger= StringVar()
regular_chicken_burger= StringVar()
regular_naga_chicken_burger= StringVar()
naga_chicken_wings= StringVar()
sweet_chicken_wings= StringVar()
ricebowl= StringVar()
meatbox= StringVar()
frenchfries= StringVar()
large_chicken_burger_amount= StringVar()
large_naga_chicken_burger_amount= StringVar()
regular_chicken_burger_amount= StringVar()
regular_naga_chicken_burger_amount= StringVar()
chicken_wings_amount= StringVar()
ricebowl_amount= StringVar()
meatbox_amount= StringVar()
frenchfries_amount= StringVar()
coke= StringVar()
coke_amount= StringVar()
sprite= StringVar()
sprite_amount= StringVar()
fanta= StringVar()
fanta_amount= StringVar()
water= StringVar()
water_amount= StringVar()
cheese= StringVar()
mayo= StringVar()
lpatty= StringVar()
rPatty= StringVar()
cheese_amount= StringVar()
mayo_amount= StringVar()
lpatty_amount= StringVar()
rpatty_amount= StringVar()
total_bill= IntVar()
paid_amount= IntVar()
return_amount= IntVar()


lburger= Entry(frame, font=('arial', 25, 'bold'), textvariable= large_chicken_burger, bd=6, width=8, bg= 'yellow').grid(row=1, column=2,padx=10, pady=10)
lnburger= Entry(frame, font=('arial', 25, 'bold'), textvariable= large_naga_chicken_burger, bd=6, width=8, bg= 'yellow').grid(row=2, column=2,padx=10, pady=10)
rburger= Entry(frame, font=('arial', 25, 'bold'), textvariable= regular_chicken_burger, bd=6, width=8, bg= 'yellow').grid(row=3, column=2,padx=10, pady=10)
rnburger= Entry(frame, font=('arial', 25, 'bold'), textvariable= regular_naga_chicken_burger, bd=6, width=8, bg= 'yellow').grid(row=4, column=2,padx=10, pady=10)
nwongs= Entry(frame, font=('arial', 25, 'bold'), textvariable= naga_chicken_wings, bd=6, width=8, bg= 'yellow').grid(row=5, column=2,padx=10, pady=10)
swings= Entry(frame, font=('arial', 25, 'bold'), textvariable= sweet_chicken_wings, bd=6, width=8, bg= 'yellow').grid(row=6, column=2,padx=10, pady=10)
mbox= Entry(frame, font=('arial', 25, 'bold'),textvariable= meatbox, bd=6, width=8, bg= 'yellow').grid(row=7, column=2,padx=10, pady=10)
rbowl= Entry(frame, font=('arial', 25, 'bold'), textvariable= ricebowl, bd=6, width=8, bg= 'yellow').grid(row=8, column=2,padx=10, pady=10)
fries= Entry(frame, font=('arial', 25, 'bold'), textvariable= frenchfries, bd=6, width=8, bg= 'yellow').grid(row=9, column=2,padx=10, pady=10)

bcoke= Entry(bframe, font=('arial', 25, 'bold'), textvariable= coke, bd=6, width=8, bg= 'yellow').grid(row=1, column=2,padx=120, pady=10)
bsprite= Entry(bframe, font=('arial', 25, 'bold'), textvariable= sprite, bd=6, width=8, bg= 'yellow').grid(row=2, column=2,padx=120, pady=10)
bfanta= Entry(bframe, font=('arial', 25, 'bold'), textvariable= fanta, bd=6, width=8, bg= 'yellow').grid(row=3, column=2,padx=120, pady=10)
bwater= Entry(bframe, font=('arial', 25, 'bold'), textvariable= water, bd=6, width=8, bg= 'yellow').grid(row=4, column=2,padx=120, pady=10)

acheese= Entry(aframe, font=('arial', 25, 'bold'), textvariable= cheese, bd=6, width=8, bg= 'yellow').grid(row=1, column=2,padx=80, pady=10)
amayo= Entry(aframe, font=('arial', 25, 'bold'), textvariable= mayo, bd=6, width=8, bg= 'yellow').grid(row=2, column=2,padx=80, pady=10)
alpatty= Entry(aframe, font=('arial', 25, 'bold'), textvariable= lpatty, bd=6, width=8, bg= 'yellow').grid(row=3, column=2,padx=80, pady=10)
arpatty= Entry(aframe, font=('arial', 25, 'bold'), textvariable= rPatty, bd=6, width=8, bg= 'yellow').grid(row=4, column=2,padx=80, pady=10)


billamount= Entry(billframe, font=('arial', 25, 'bold'), textvariable= total_bill, bd=6, width=8, bg= 'yellow').grid(row=0, column=1, columnspan=2,padx=10,pady=10)
paidamount= Entry(billframe, font=('arial', 25, 'bold'), textvariable= paid_amount, bd=6, width=8, bg= 'yellow' ).grid(row=0, column=4, columnspan=2,padx=10,pady=10)
returnamount= Entry(billframe, font=('arial', 25, 'bold'), textvariable= return_amount, bd=6, width=8, bg= 'yellow').grid(row=0, column=7, columnspan=2,padx=10,pady=10)


#Buttons
resetbutton= Button(billframe, font=('arial', 25, 'bold'),  bd=6, width=8, bg= 'yellow', text= "Reset" ,command= reset).grid(row=0, column=9, columnspan=2,padx=10,pady=10)
totalbutton= Button(billframe, font=('arial', 25, 'bold'),  bd=6, width=8, bg= 'yellow', text= "Total" ,command= Total).grid(row=0, column=11, columnspan=2,padx=10,pady=10)


root.mainloop()
