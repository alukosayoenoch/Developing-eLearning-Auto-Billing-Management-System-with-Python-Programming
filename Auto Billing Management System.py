from tkinter import *
import random
import time
import datetime

root =   Tk()
frame =   Frame(root)
frame.pack()


root.title("Auto Billing Management System: Aluko Sayo Enoch")

#=============Creating Entry Widget Frame in the APP_root===================
#Create TopFrame
topframe= Frame(root, width=1350, height=100,bd=8,relief='raise')
topframe.pack(side = TOP)
#Create Leftframe
f1=Frame(root,width=900, height=650, bd=8,relief='raise')
f1.pack(side = LEFT)
#Create Right Frame
f2=Frame(root,width=440, height=650, bd=8,relief='raise')
f2.pack(side=RIGHT)
#Comments: The App_root is now divided into 3 compartment (T/L/R)
#Divide the leftframe into two compartment (T/B)
f1a=Frame(f1,width=900, height=330, bd=8,relief='raise')
f1a.pack(side=TOP)
f1b=Frame(f1,width=900, height=320, bd=8,relief='raise')
f1b.pack(side=BOTTOM)
#Divide the Top_Left_Frame into two compartment(L/R)
f1aa=Frame(f1a,width=400, height=430, bd=8,relief='raise')
f1aa.pack(side=LEFT)
f1ab=Frame(f1a,width=400, height=430, bd=8,relief='raise')
f1ab.pack(side=RIGHT)
#Divide the Bottom_Left_Frame into two compartment(L/R)
f1ba=Frame(f1b,width=450, height=330, bd=8,relief='raise')
f1ba.pack(side=LEFT)
f1bb=Frame(f1b,width=450, height=330, bd=8,relief='raise')
f1bb.pack(side=RIGHT)
#Label the topframe based on the app title
lblinfo=Label(topframe, font=('arial', 60, 'bold'), text = '   Auto Billing Management System'  , bd=10, anchor ='w')
lblinfo.grid(row=0, column=0)
###################################################################################################
#======Developing Caculating Device in the Rightmost_Frame of the APP_root===================
###################################################################################################
#===========Defining Calculator Function Operators==================================
text_Input=StringVar()
operator=''

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=''
    text_Input.set('')

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=''
#================== Creating Calculator Screen Display================================================================
txtDisplay=Entry(f2, font=('arial',20,'bold'),textvariable=text_Input, bd=40,insertwidth=6,bg='powder blue', justify='right')
txtDisplay.grid(columnspan=4)
#===========1st Row Botton Pad Function Keys==================================
btn7=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='7',bg='powder blue',command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='8',bg='powder blue',command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='9',bg='powder blue',command=lambda:btnClick(9)).grid(row=1,column=2)
Addition=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='+',bg='powder blue',command=lambda:btnClick('+')).grid(row=1,column=3)
#===========2nd Row Botton Pad Function Keys==================================
btn4=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='4',bg='powder blue',command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='5',bg='powder blue',command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='6',bg='powder blue',command=lambda:btnClick(6)).grid(row=2,column=2)
Subtraction=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='-',bg='powder blue',command=lambda:btnClick('-')).grid(row=2,column=3)
#===========3rd Row Botton Pad Function Keys==================================
btn1=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='1',bg='powder blue',command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='2',bg='powder blue',command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='3',bg='powder blue',command=lambda:btnClick(3)).grid(row=3,column=2)
Multiplication=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='*',bg='powder blue',command=lambda:btnClick('*')).grid(row=3,column=3)
#===========4th Row Botton Pad Function Keys==================================
btn0=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='0',bg='powder blue',command=lambda:btnClick(0)).grid(row=4,column=0)
clearbtn=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='C',bg='powder blue',command=btnClearDisplay).grid(row=4,column=1)
Ans=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='=',bg='powder blue',command=btnEqualsInput).grid(row=4,column=2)
Division=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='/',bg='powder blue',command=lambda:btnClick('/')).grid(row=4,column=3)
###########################################################################################
             #Creating Transaction Online Information Widget
################################################################################
#===========Defining App Transaction Operators==================================
def CostOfOrder():
    CarpetPrice=float(Carpets.get())
    BlindsPrice=float(Blinds.get())
    FabricPrice=float(Fabric.get())
    DeliveryCost=float(HomeDelivery.get())

    CarpetCost ='Naira',str('%.2f' %(CarpetPrice * 1200))
    CostofCarpets.set(CarpetCost)

    BlindsCost ='Naira',str('%.2f' %(BlindsPrice * 2000))
    CostofBlinds.set(BlindsCost)

    FabricCost ='Naira',str('%.2f' %(FabricPrice * 750))
    CostofFabric.set(FabricCost)

    Delivery ='Naira',str('%.2f' %(DeliveryCost * 500))
    CostofDelivery.set(Delivery)

    Toc ='Naira',str('%.2f' %((CarpetPrice * 1200)+(BlindsPrice * 2000)+(FabricPrice * 750)+(DeliveryCost * 500)))
    SubTotal.set(Toc)
    Tax ='Naira',str('%.2f' %(((CarpetPrice * 1200)+(BlindsPrice * 2000)+(FabricPrice * 750)+(DeliveryCost * 500))*0.05))
    PaidTax.set(Tax)
    TaxPay =(((CarpetPrice * 1200)+(BlindsPrice * 2000)+(FabricPrice * 750)+(DeliveryCost * 500))*0.05) 
    Cost= ((CarpetPrice * 1200)+(BlindsPrice * 2000)+(FabricPrice * 750)+(DeliveryCost * 500))
    CostofItems='Naira',str('%.2f' %(TaxPay + Cost))
    TotalCost.set(CostofItems)

    x=random.randint(10034,699812)
    randomRef = str(x)
    PaymentRef.set('ALUKO' + randomRef)



def PayReference():
    x=random.randint(10034,699812)
    randomRef = str(x)
    PaymentRef.set('ALUKO' + randomRef)

def iExit():
     qExit=messagebox.askyesno('Alukopy Billing System', 'Do you want to exit the systems')
     if qExit>0:
         root.destroy()
         return

def Reset():
    PaymentRef.set('')
    Carpets.set(0)
    Fabric.set(0)
    Blinds.set(0)
    HomeDelivery.set(0)
    PaidTax.set('')
    SubTotal.set('')
    TotalCost.set('')
    CostofCarpets.set('')
    CostofBlinds.set('')
    CostofFabric.set('')
    CostofDelivery.set('')
#============Declaring Entry Widget Variables====================
PaymentRef=StringVar()
Carpets=StringVar()
Fabric=StringVar()
Blinds=StringVar()
HomeDelivery=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofCarpets=StringVar()
CostofBlinds=StringVar()
CostofFabric=StringVar()
CostofDelivery=StringVar()
DateofOrder=StringVar()

Carpets.set(0)
Fabric.set(0)
Blinds.set(0)
HomeDelivery.set(0)
DateofOrder.set(time.strftime("%d/%m/%Y"))
#==========Entry Components Widget Label on Frame f1aa========================
lblRef=Label(f1aa, text="Sale Reference",font=('arial',16,'bold'),bd=16, justify='left')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1aa, textvariable=PaymentRef,font=('arial',16,'bold'),bd=10, insertwidth=2, justify='left')
txtRef.grid(row=0,column=1)

lblCarpets=Label(f1aa, text="Carpets",font=('arial',16,'bold'),bd=16, anchor='w')
lblCarpets.grid(row=1,column=0)
txtCarpets=Entry(f1aa, textvariable=Carpets,font=('arial',16,'bold'),bd=10, insertwidth=2, justify='left')
txtCarpets.grid(row=1,column=1)

lblFabric=Label(f1aa, text="Fabric",font=('arial',16,'bold'),bd=16, justify='left')
lblFabric.grid(row=2,column=0)
txtFabric=Entry(f1aa, textvariable=Fabric,font=('arial',16,'bold'),bd=10, insertwidth=2,justify='left')
txtFabric.grid(row=2,column=1)

lblBlinds=Label(f1aa, text="Blinds",font=('arial',16,'bold'),bd=16, anchor='w')
lblBlinds.grid(row=3,column=0)
txtBlinds=Entry(f1aa, textvariable=Blinds,font=('arial',16,'bold'),bd=10, insertwidth=2, justify='left')
txtBlinds.grid(row=3,column=1)

lblHomeDelivery=Label(f1aa, text="Home Delivery",font=('arial',16,'bold'),bd=16, anchor='w')
lblHomeDelivery.grid(row=4,column=0)
txtHomeDelivery=Entry(f1aa, textvariable=HomeDelivery,font=('arial',16,'bold'),bd=10, insertwidth=2, justify='left')
txtHomeDelivery.grid(row=4,column=1)
#==========Entry Components Widget Label on Frame f1ab========================
lblDateofOrder=Label(f1ab, text="Order Date",font=('arial',16,'bold'),bd=16, justify='left')
lblDateofOrder.grid(row=0,column=0)
txtDateofOrder=Entry(f1ab, textvariable=DateofOrder,font=('arial',16,'bold'),bd=10, insertwidth=2, justify='left')
txtDateofOrder.grid(row=0,column=1)

lblCostofCarpets=Label(f1ab, text="Cost of Carpets",font=('arial',16,'bold'),bd=16, anchor='w')
lblCostofCarpets.grid(row=1,column=0)
txtCostofCarpets=Entry(f1ab, textvariable=CostofCarpets,font=('arial',16,'bold'),bd=10, insertwidth=2, justify='left')
txtCostofCarpets.grid(row=1,column=1)

lblCostofFabric=Label(f1ab, text="Cost of Fabric",font=('arial',16,'bold'),bd=16, justify='left')
lblCostofFabric.grid(row=2,column=0)
txtCostofFabric=Entry(f1ab, textvariable=CostofFabric,font=('arial',16,'bold'),bd=10, insertwidth=2,justify='left')
txtCostofFabric.grid(row=2,column=1)

lblCostofBlinds=Label(f1ab, text="Cost of Blinds",font=('arial',16,'bold'),bd=16, anchor='w')
lblCostofBlinds.grid(row=3,column=0)
txtCostofBlinds=Entry(f1ab, textvariable=CostofBlinds,font=('arial',16,'bold'),bd=10, insertwidth=2, justify='left')
txtCostofBlinds.grid(row=3,column=1)

lblCostofDelivery=Label(f1ab, text='Cost of Delivery',font=('arial',16,'bold'),bd=16, anchor='w')
lblCostofDelivery.grid(row=4,column=0)
txtCostofDelivery=Entry(f1ab, textvariable=CostofDelivery,font=('arial',16,'bold'),bd=10, insertwidth=2, justify='left')
txtCostofDelivery.grid(row=4,column=1)
#==========Entry Components Widget Label on Frame f1ba========================
lblPaidTax=Label(f1ba, text="Paid Tax",font=('arial',16,'bold'),bd=16, justify='left')
lblPaidTax.grid(row=2,column=0)
txtPaidTax=Entry(f1ba, textvariable=PaidTax,font=('arial',16,'bold'),bd=16, insertwidth=2, justify='left')
txtPaidTax.grid(row=2,column=1)

lblSubTotal=Label(f1ba, text="Sub Total",font=('arial',16,'bold'),bd=16,justify='left' )
lblSubTotal.grid(row=3,column=0)
txtSubTotal=Entry(f1ba, textvariable=SubTotal,font=('arial',16,'bold'),bd=16, insertwidth=2, justify='left')
txtSubTotal.grid(row=3,column=1)

lblTotalCost=Label(f1ba, text="Total Cost",font=('arial',16,'bold'),bd=16, justify='left')
lblTotalCost.grid(row=4,column=0)
txtTotalCost=Entry(f1ba, textvariable=TotalCost,font=('arial',16,'bold'),bd=16, insertwidth=2,justify='left')
txtTotalCost.grid(row=4,column=1)
#====================Order Buttons===========================================
btnTotal=Button(f1bb, text='Total Cost', padx=16,pady=16,bd=8,fg='black',
                 font=('arial',16,'bold'), width=15,command=CostOfOrder).grid(row=0,column=0)

btnReset=Button(f1bb, text='Reset', padx=16,pady=16,bd=8,fg='black',
                 font=('arial',16,'bold'), width=15, command=Reset).grid(row=0,column=1)

btnRefer=Button(f1bb, text='Sales Reference', padx=16,pady=16,bd=8,fg='black',
                 font=('arial',16,'bold'), width=15,command=PayReference).grid(row=1,column=0)

btnExit=Button(f1bb, text='Exit System', padx=16,pady=16,bd=8,fg='black',
                 font=('arial',16,'bold'), width=15,command=iExit).grid(row=1,column=1)











root.mainloop()
  
