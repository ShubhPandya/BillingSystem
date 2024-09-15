from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
#Functionality
def clear():
    soapEntry.delete(0, END)
    facecreamEntry.delete(0, END)
    facewashEntry.delete(0, END)
    hairsprayEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    bodylotionEntry.delete(0, END)
    riceEntry.delete(0, END)
    oilEntry.delete(0, END)
    daalEntry.delete(0, END)
    wheatEntry.delete(0, END)
    sugarEntry.delete(0, END)
    teaEntry.delete(0, END)
    maazaEntry.delete(0, END)
    pepsiEntry.delete(0, END)
    dewEntry.delete(0, END)
    spriteEntry.delete(0, END)
    cocacolaEntry.delete(0, END)
    coldcoffeeEntry.delete(0, END)

    soapEntry.insert(0,0)
    facecreamEntry.insert(0, 0)
    facewashEntry.insert(0, 0)
    hairsprayEntry.insert(0, 0)
    hairgelEntry.insert(0, 0)
    bodylotionEntry.insert(0, 0)
    riceEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    daalEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    sugarEntry.insert(0, 0)
    teaEntry.insert(0, 0)
    maazaEntry.insert(0, 0)
    pepsiEntry.insert(0, 0)
    dewEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    cocacolaEntry.insert(0, 0)
    coldcoffeeEntry.insert(0, 0)

    CosmeticTaxEntry.delete(0,END)
    GroceryTaxEntry.delete(0,END)
    ColdDrinkTaxEntry.delete(0,END)

    CosmeticAmmountEntry.delete(0,END)
    GroceryAmmountEntry.delete(0,END)
    ColdDrinkAmmountEntry.delete(0,END)

    textArea.delete(1.0,END)

    nameEntry.delete(0,END)
    phEntry.delete(0,END)
    nameEntry.insert(0,'')
    phEntry.insert(0,'')


def send_email():
    def send():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),receiverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)

    if textArea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.title('Send Email')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1,text='Sender',font=('Arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0)

        senderlabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderlabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordlabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        passwordlabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        receiverFrame = LabelFrame(root1, text='Receiver', font=('Arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        receiverFrame.grid(row=1, column=0, padx=40, pady=20)

        receiverlabel = Label(receiverFrame, text="Email Address", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        receiverlabel.grid(row=0, column=0, padx=10, pady=8)

        receiverEntry = Entry(receiverFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        receiverEntry.grid(row=0, column=1, padx=10, pady=8)

        messagelabel = Label(receiverFrame, text="Message", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        messagelabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea=Text(receiverFrame,font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textArea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t\t','\t').replace('\t\t','\t'))

        sendButton=Button(root1,text='Send',font=('arial',16,'bold'),width=15)
        sendButton.grid(row=2,column=0,pady=20)

        root1.mainloop()
def print_bill():
    if textArea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textArea.get(1.0,END))
        os.startfile(file,'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billNumEntry.get():
            f=open(f'bills/{i}','r')
            textArea.delete(1.0,END)
            for data in f:
                textArea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm','Do You want to save the bill?')
    if result:
        bill_content = textArea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number {billnumber} is saved successfully')
        billnumber = random.randint(500,1000)
billnumber = random.randint(500,1000)
def bill_area():
        if  nameEntry.get()=='' or phEntry.get()=='':
            messagebox.showerror('Error','Customer details are required')
        elif CosmeticAmmountEntry.get()=='' and GroceryAmmountEntry.get()=='' and ColdDrinkAmmountEntry.get()=='':
            messagebox.showerror('Error','No Products are selected')
        elif CosmeticAmmountEntry.get()=='0 Rs' and GroceryAmmountEntry.get()=='0 Rs' and ColdDrinkAmmountEntry.get()=='0 Rs':
            messagebox.showerror('Error', 'No Products are selected')
            textArea.delete(1.0,END)
        else:
            textArea.delete(1.0, END)
            textArea.insert(END, '\t\t\t**Welcome Customer**\n')
            textArea.insert(END, f'\nBill Number: {billnumber}')
            textArea.insert(END, f'\nCustomer Name: {nameEntry.get()}')
            textArea.insert(END, f'\nPhone Number: {phEntry.get()}')
            textArea.insert(END, '\n======================================================================')
            textArea.insert(END, '\nProducts\t\tQuantity\t\t\t\tPrice\t\tAmount')
            textArea.insert(END, '\n======================================================================')
            if soapEntry.get()!='0':
                textArea.insert(END,f'Bath Soap\t\t{soapEntry.get()}\t\t\t\t{20}\t\t{soapAmmount}')
            if facecreamEntry.get()!='0':
                textArea.insert(END,f'\nFace Cream\t\t{facecreamEntry.get()}\t\t\t\t{80}\t\t{faceCreamAmmount}')
            if facewashEntry.get()!='0':
                textArea.insert(END,f'\nFace Wash\t\t{facewashEntry.get()}\t\t\t\t{150}\t\t{facewashAmmount}')
            if hairsprayEntry.get()!='0':
                textArea.insert(END,f'\nHair Spray\t\t{hairsprayEntry.get()}\t\t\t\t{300}\t\t{hairsprayAmmount}')
            if hairgelEntry.get()!='0':
                textArea.insert(END,f'\nHair Gel\t\t{hairgelEntry.get()}\t\t\t\t{120}\t\t{hairgelAmmount}')
            if bodylotionEntry.get()!='0':
                textArea.insert(END,f'\nBody Lotion\t\t{bodylotionEntry.get()}\t\t\t\t{180}\t\t{bodylotionAmmount}')
            if riceEntry.get()!='0':
                textArea.insert(END,f'\nRice\t\t{riceEntry.get()}\t\t\t\t{100}\t\t{RiceAmmount}')
            if oilEntry.get()!='0':
                textArea.insert(END,f'\nOil\t\t{oilEntry.get()}\t\t\t\t{100}\t\t{OilAmmount}')
            if daalEntry.get()!='0':
                textArea.insert(END,f'\nDaal\t\t{daalEntry.get()}\t\t\t\t{40}\t\t{DaalAmmount}')
            if wheatEntry.get()!='0':
                textArea.insert(END,f'\nWheat\t\t{wheatEntry.get()}\t\t\t\t{150}\t\t{WheatAmmount}')
            if sugarEntry.get()!='0':
                textArea.insert(END,f'\nSugar\t\t{sugarEntry.get()}\t\t\t\t{80}\t\t{SugarAmmount}')
            if teaEntry.get()!='0':
                textArea.insert(END,f'\nTea\t\t{teaEntry.get()}\t\t\t\t{200}\t\t{TeaAmmount}')
            if maazaEntry.get()!='0':
                textArea.insert(END,f'\nMaaza\t\t{maazaEntry.get()}\t\t\t\t{20}\t\t{MaazaAmmount}')
            if pepsiEntry.get()!='0':
                textArea.insert(END,f'\nPepsi\t\t{pepsiEntry.get()}\t\t\t\t{45}\t\t{PepsiAmmount}')
            if dewEntry.get()!='0':
                textArea.insert(END,f'\nDew\t\t{dewEntry.get()}\t\t\t\t{45}\t\t{DewAmmount}')
            if spriteEntry.get()!='0':
                textArea.insert(END,f'\nSprite\t\t{spriteEntry.get()}\t\t\t\t{40}\t\t{SpriteAmmount}')
            if cocacolaEntry.get()!='0':
                textArea.insert(END,f'\nCoca Cola\t\t{cocacolaEntry.get()}\t\t\t\t{40}\t\t{CocaColaAmmount}')
            if coldcoffeeEntry.get()!='0':
                textArea.insert(END,f'\nCold Coffee\t\t{coldcoffeeEntry.get()}\t\t\t\t{60}\t\t{ColdCoffeeAmmount}')
            textArea.insert(END, '\n----------------------------------------------------------------------')
            if CosmeticTaxEntry.get()!='0.0Rs':
                textArea.insert(END,f'\nCosmetic Tax\t\t{CosmeticTaxEntry.get()}')
            if GroceryTaxEntry.get()!='0.0Rs':
                textArea.insert(END,f'\nGrocery Tax\t\t{GroceryTaxEntry.get()}')
            if ColdDrinkTaxEntry.get()!='0.0Rs':
                textArea.insert(END,f'\nCold Drink Tax\t\t{ColdDrinkTaxEntry.get()}')
            textArea.insert(END,f'\n\nTotal Bill\t\t{totalBill}')
            save_bill()

def total():
    global soapAmmount,faceCreamAmmount,facewashAmmount,hairsprayAmmount,hairgelAmmount,bodylotionAmmount
    soapAmmount = int(soapEntry.get())*20
    faceCreamAmmount = int(facecreamEntry.get())*80
    facewashAmmount = int(facewashEntry.get())*150
    hairsprayAmmount = int(hairsprayEntry.get())*300
    hairgelAmmount = int(hairgelEntry.get())*120
    bodylotionAmmount = int(bodylotionEntry.get())*180

    totalCosmetic=soapAmmount+faceCreamAmmount+facewashAmmount+hairsprayAmmount+hairgelAmmount+bodylotionAmmount
    CosmeticAmmountEntry.delete(0,END)
    CosmeticAmmountEntry.insert(0,f'{totalCosmetic} Rs')
    CosmeticTax=totalCosmetic*0.04
    CosmeticTaxEntry.delete(0,END)
    CosmeticTaxEntry.insert(0,str(CosmeticTax)+'Rs')


    global RiceAmmount,OilAmmount,DaalAmmount,WheatAmmount,SugarAmmount,TeaAmmount
    RiceAmmount = int(riceEntry.get()) * 100
    OilAmmount = int(oilEntry.get()) * 100
    DaalAmmount = int(daalEntry.get()) * 40
    WheatAmmount = int(wheatEntry.get()) * 150
    SugarAmmount = int(sugarEntry.get()) * 80
    TeaAmmount = int(teaEntry.get()) * 200

    totalGrocery=RiceAmmount+OilAmmount+DaalAmmount+WheatAmmount+SugarAmmount+TeaAmmount
    GroceryAmmountEntry.delete(0, END)
    GroceryAmmountEntry.insert(0,f'{totalGrocery} Rs')
    GroceryTax = totalGrocery * 0.1
    GroceryTaxEntry.delete(0, END)
    GroceryTaxEntry.insert(0, str(GroceryTax) + 'Rs')


    global MaazaAmmount,PepsiAmmount,DewAmmount,SpriteAmmount,CocaColaAmmount,ColdCoffeeAmmount
    MaazaAmmount = int(maazaEntry.get()) * 20
    PepsiAmmount = int(pepsiEntry.get()) * 45
    DewAmmount = int(dewEntry.get()) * 45
    SpriteAmmount = int(spriteEntry.get()) * 40
    CocaColaAmmount = int(cocacolaEntry.get()) * 40
    ColdCoffeeAmmount = int(coldcoffeeEntry.get()) * 60

    totalDrinks = MaazaAmmount+PepsiAmmount+DewAmmount+SpriteAmmount+CocaColaAmmount+ColdCoffeeAmmount
    ColdDrinkAmmountEntry.delete(0, END)
    ColdDrinkAmmountEntry.insert(0, f'{totalDrinks} Rs')
    ColdDrinkTax = totalDrinks * 0.02
    ColdDrinkTaxEntry.delete(0, END)
    ColdDrinkTaxEntry.insert(0, str(ColdDrinkTax) + 'Rs')

    global totalBill
    totalBill = totalCosmetic + totalGrocery + totalDrinks + CosmeticTax + GroceryTax + ColdDrinkTax


#GUI
root = Tk()
root.title('Billing System')
root.geometry('1530x850')
headinglabel=Label(root,text='Bill',font=('times new roman',30,'bold'),bg='grey20',fg='white',bd=12,relief=GROOVE)
headinglabel.pack(fill=X )#pady=10

custdetail=LabelFrame(root,text='Customer Details',font=('times new roman',20,'bold'),bg='grey20',fg='white',bd=8,relief=GROOVE)
custdetail.pack(fill=X)
nameLabel=Label(custdetail,text='Name:',font=('times new roman',15,'bold'),fg='white',bg='grey20')
nameLabel.grid(row=0,column=0,padx=10)
nameEntry=Entry(custdetail,font=('arial',15),bd=7)
nameEntry.grid(row=0,column=1,padx=15,pady=4)
phLabel=Label(custdetail,text='Phone Number:',font=('times new roman',15,'bold'),fg='white',bg='grey20')
phLabel.grid(row=0,column=2,padx=10)
phEntry=Entry(custdetail,font=('arial',15),bd=7)
phEntry.grid(row=0,column=3,padx=15,pady=4)
billNum=Label(custdetail,text='Bill Number:',font=('times new roman',15,'bold'),fg='white',bg='grey20')
billNum.grid(row=0,column=4,padx=10)
billNumEntry=Entry(custdetail,font=('arial',15),bd=7)
billNumEntry.grid(row=0,column=5,padx=15,pady=4)

searchButton=Button(custdetail,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=8,padx=110,pady=8)


prodFrame=Frame(root)
prodFrame.pack()

cosmeticsFrame=LabelFrame(prodFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='white',bg='grey20',bd=8,relief=GROOVE)
cosmeticsFrame.grid(row=0,column=0)

soapLabel=Label(cosmeticsFrame,text='Bath Soap:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
soapLabel.grid(row=0,column=0,sticky='w',padx=19,pady=12)
soapEntry=Entry(cosmeticsFrame,font=('arial',15),bd=7,width=10)
soapEntry.grid(row=0,column=1,padx=19,pady=12)
soapEntry.insert(0,0)
facecreamlabel=Label(cosmeticsFrame,text='Face Cream:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
facecreamlabel.grid(row=1,column=0,sticky='w',padx=19,pady=12)
facecreamEntry=Entry(cosmeticsFrame,font=('arial',15),bd=7,width=10)
facecreamEntry.grid(row=1,column=1,padx=19,pady=12)
facecreamEntry.insert(0,0)
facewashlabel=Label(cosmeticsFrame,text='Face Wash:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
facewashlabel.grid(row=2,column=0,sticky='w',padx=19,pady=12)
facewashEntry=Entry(cosmeticsFrame,font=('arial',15),bd=7,width=10)
facewashEntry.grid(row=2,column=1,padx=19,pady=12)
facewashEntry.insert(0,0)
hairspraylabel=Label(cosmeticsFrame,text='Hair Spray:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
hairspraylabel.grid(row=3,column=0,sticky='w',padx=19,pady=12)
hairsprayEntry=Entry(cosmeticsFrame,font=('arial',15),bd=7,width=10)
hairsprayEntry.grid(row=3,column=1,padx=19,pady=12)
hairsprayEntry.insert(0,0)
hairgellabel=Label(cosmeticsFrame,text='Hair Gel:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
hairgellabel.grid(row=4,column=0,sticky='w',padx=19,pady=12)
hairgelEntry=Entry(cosmeticsFrame,font=('arial',15),bd=7,width=10)
hairgelEntry.grid(row=4,column=1,padx=19,pady=12)
hairgelEntry.insert(0,0)
bodylotionlabel=Label(cosmeticsFrame,text='Body Lotion:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
bodylotionlabel.grid(row=5,column=0,sticky='w',padx=19,pady=12)
bodylotionEntry=Entry(cosmeticsFrame,font=('arial',15),bd=7,width=10)
bodylotionEntry.grid(row=5,column=1,padx=19,pady=12)
bodylotionEntry.insert(0,0)


GroceryFrame=LabelFrame(prodFrame,text='Grocery',font=('times new roman',15,'bold'),fg='white',bg='grey20',bd=8,relief=GROOVE)
GroceryFrame.grid(row=0,column=1)

riceLabel=Label(GroceryFrame,text='Rice:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
riceLabel.grid(row=0,column=0,sticky='w',padx=19,pady=12)
riceEntry=Entry(GroceryFrame,font=('arial',15),bd=7,width=10)
riceEntry.grid(row=0,column=1,padx=19,pady=12)
riceEntry.insert(0,0)
oillabel=Label(GroceryFrame,text='Oil:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
oillabel.grid(row=1,column=0,sticky='w',padx=19,pady=12)
oilEntry=Entry(GroceryFrame,font=('arial',15),bd=7,width=10)
oilEntry.grid(row=1,column=1,padx=19,pady=12)
oilEntry.insert(0,0)
daallabel=Label(GroceryFrame,text='Daal:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
daallabel.grid(row=2,column=0,sticky='w',padx=19,pady=12)
daalEntry=Entry(GroceryFrame,font=('arial',15),bd=7,width=10)
daalEntry.grid(row=2,column=1,padx=19,pady=12)
daalEntry.insert(0,0)
wheatlabel=Label(GroceryFrame,text='Wheat:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
wheatlabel.grid(row=3,column=0,sticky='w',padx=19,pady=12)
wheatEntry=Entry(GroceryFrame,font=('arial',15),bd=7,width=10)
wheatEntry.grid(row=3,column=1,padx=19,pady=12)
wheatEntry.insert(0,0)
sugarlabel=Label(GroceryFrame,text='Sugar:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
sugarlabel.grid(row=4,column=0,sticky='w',padx=19,pady=12)
sugarEntry=Entry(GroceryFrame,font=('arial',15),bd=7,width=10)
sugarEntry.grid(row=4,column=1,padx=19,pady=12)
sugarEntry.insert(0,0)
tealabel=Label(GroceryFrame,text='Tea:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
tealabel.grid(row=5,column=0,sticky='w',padx=19,pady=12)
teaEntry=Entry(GroceryFrame,font=('arial',15),bd=7,width=10)
teaEntry.grid(row=5,column=1,padx=19,pady=12)
teaEntry.insert(0,0)


ColdDrinkFrame=LabelFrame(prodFrame,text='ColdDrink',font=('times new roman',15,'bold'),fg='white',bg='grey20',bd=8,relief=GROOVE)
ColdDrinkFrame.grid(row=0,column=2)

maazaLabel=Label(ColdDrinkFrame,text='Maaza:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
maazaLabel.grid(row=0,column=0,sticky='w',padx=15,pady=12)
maazaEntry=Entry(ColdDrinkFrame,font=('arial',15),bd=7,width=10)
maazaEntry.grid(row=0,column=1,padx=15,pady=12)
maazaEntry.insert(0,0)
pepsilabel=Label(ColdDrinkFrame,text='Pepsi:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
pepsilabel.grid(row=1,column=0,sticky='w',padx=15,pady=12)
pepsiEntry=Entry(ColdDrinkFrame,font=('arial',15),bd=7,width=10)
pepsiEntry.grid(row=1,column=1,padx=15,pady=12)
pepsiEntry.insert(0,0)
dewlabel=Label(ColdDrinkFrame,text='Dew:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
dewlabel.grid(row=2,column=0,sticky='w',padx=15,pady=12)
dewEntry=Entry(ColdDrinkFrame,font=('arial',15),bd=7,width=10)
dewEntry.grid(row=2,column=1,padx=15,pady=12)
dewEntry.insert(0,0)
spritelabel=Label(ColdDrinkFrame,text='Sprite:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
spritelabel.grid(row=3,column=0,sticky='w',padx=15,pady=12)
spriteEntry=Entry(ColdDrinkFrame,font=('arial',15),bd=7,width=10)
spriteEntry.grid(row=3,column=1,padx=15,pady=12)
spriteEntry.insert(0,0)
cocacolalabel=Label(ColdDrinkFrame,text='Coca-Cola:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
cocacolalabel.grid(row=4,column=0,sticky='w',padx=15,pady=12)
cocacolaEntry=Entry(ColdDrinkFrame,font=('arial',15),bd=7,width=10)
cocacolaEntry.grid(row=4,column=1,padx=15,pady=12)
cocacolaEntry.insert(0,0)
coldcoffeeEntry=Label(ColdDrinkFrame,text='Cold Coffee:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
coldcoffeeEntry.grid(row=5,column=0,sticky='w',padx=15,pady=12)
coldcoffeeEntry=Entry(ColdDrinkFrame,font=('arial',15),bd=7,width=10)
coldcoffeeEntry.grid(row=5,column=1,padx=15,pady=12)
coldcoffeeEntry.insert(0,0)


billframe=Frame(prodFrame,bd=7,relief=GROOVE)
billframe.grid(row=0,column=3,padx=4)
billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scroll=Scrollbar(billframe,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
textArea=Text(billframe,height=21,width=70,yscrollcommand=scroll.set)
textArea.pack()
scroll.config(command=textArea.yview)

Bill=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='white',bg='grey20',bd=8,relief=GROOVE)
Bill.pack()

CosmeticAmmount=Label(Bill,text='Cosmetic Price:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
CosmeticAmmount.grid(row=0,column=0,sticky='w',padx=20,pady=10)
CosmeticAmmountEntry=Entry(Bill,font=('arial',15),bd=7,width=10)
CosmeticAmmountEntry.grid(row=0,column=1,padx=20,pady=10)
GroceryAmmount=Label(Bill,text='Grocery Price:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
GroceryAmmount.grid(row=1,column=0,sticky='w',padx=20,pady=10)
GroceryAmmountEntry=Entry(Bill,font=('arial',15),bd=7,width=10)
GroceryAmmountEntry.grid(row=1,column=1,padx=20,pady=10)
ColdDrinkAmmount=Label(Bill,text='ColdDrink Price:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
ColdDrinkAmmount.grid(row=2,column=0,sticky='w',padx=20,pady=10)
ColdDrinkAmmountEntry=Entry(Bill,font=('arial',15),bd=7,width=10)
ColdDrinkAmmountEntry.grid(row=2,column=1,padx=20,pady=10)
CosmeticTax=Label(Bill,text='Cosmetic Tax:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
CosmeticTax.grid(row=0,column=2,sticky='w',padx=20,pady=10)
CosmeticTaxEntry=Entry(Bill,font=('arial',15),bd=7,width=10)
CosmeticTaxEntry.grid(row=0,column=3,padx=20,pady=10)
GroceryTax=Label(Bill,text='Grocery Tax:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
GroceryTax.grid(row=1,column=2,sticky='w',padx=20,pady=10)
GroceryTaxEntry=Entry(Bill,font=('arial',15),bd=7,width=10)
GroceryTaxEntry.grid(row=1,column=3,padx=20,pady=10)
ColdDrinkTax=Label(Bill,text=' ColdDrink Tax:',font=('times new roman',15,'bold'),fg='white',bg='grey20',)
ColdDrinkTax.grid(row=2,column=2,sticky='w',padx=20,pady=10)
ColdDrinkTaxEntry=Entry(Bill,font=('arial',15),bd=7,width=10)
ColdDrinkTaxEntry.grid(row=2,column=3,padx=20,pady=10)

buttonFrame=Frame(Bill,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3,padx=20)

totalbutton=Button(buttonFrame,text='Total',font=('arial',15,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=20,command=total)
totalbutton.grid(row=0,column=0,padx=20,pady=20)

billbutton=Button(buttonFrame,text='Bill',font=('arial',15,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=20,command=bill_area)
billbutton.grid(row=0,column=1,padx=20,pady=20)

emailbutton=Button(buttonFrame,text='E-Mail',font=('arial',15,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=20,command=send_email)
emailbutton.grid(row=0,column=2,padx=20,pady=20)

printbutton=Button(buttonFrame,text='Print',font=('arial',15,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=20,command=print_bill)
printbutton.grid(row=0,column=3,padx=20,pady=20)

clearbutton=Button(buttonFrame,text='Clear',font=('arial',15,'bold'),bg='grey20',fg='white',bd=5,width=8,pady=20,command=clear)
clearbutton.grid(row=0,column=4,padx=20,pady=20)

root.mainloop()