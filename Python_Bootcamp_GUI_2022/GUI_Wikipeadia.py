from cgitb import reset, text
from distutils import command
from itertools import count, product
from msilib.schema import tables
from optparse import Values
from time import strftime
from tkinter import font
from turtle import stamp
from unicodedata import name
import webbrowser
from re import M, search
from tkinter import *
from tkinter import ttk, messagebox
import wikipedia 
from distutils import command

########### Read CSV #################
import csv
from datetime import datetime
from unittest import result
def writeToCSV(data, filename='data.csv'):
    with open(filename,'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)
######################################

GUI = Tk()
GUI.title('โปรแกรมจัดการ laout')
GUI.geometry('1200x700')

Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

icon_tab1 = PhotoImage(file='images/shrimp-icon.png')
icon_tab2 = PhotoImage(file='images/Search-icon.png')
icon_tab3 = PhotoImage(file='images/Coffee-brown-icon.png')

Tab.add(T1, text='กุ้ง', image=icon_tab1,compound='left')
Tab.add(T2, text='Wikipedia', image=icon_tab2,compound='left')
Tab.add(T3, text='CAFE',image=icon_tab3,compound='left')

########### Tab 1 ขายกุ้ง #################
L1 = Label(T1, text='จำนวนกุ้ง (กก.)',font=('Angsana New',25))
L1.pack()

v_kilo = StringVar()

E1 = ttk.Entry(T1, textvariable=v_kilo, width=10, justify='right',font=('impact',30))
E1.pack(pady=20)
E1.focus()

def Calc(event=None):
    print('### Please wait')
    kilo = float(v_kilo.get())
    print('### จำนวนกิโล ',kilo)
    calc_result = kilo * 299
    date = datetime.now()
    year = date.year + 543
    stamp = date.strftime(f'{year}-%m-%d  %H:%M:%S')
    data = [stamp, 'กุ้ง' , f'{calc_result:,.2f}']
    writeToCSV(data)
    messagebox.showinfo('รวมราคาทั้งหมด',f'ลูกค้าต้องจ่ายทั้งหมด: {calc_result:,.2f} บาท (กก.ละ 299 บาท)')

B1 = Button(T1,text='คำนวณราคา',command=Calc)
B1.pack(ipadx=20,ipady=10)

E1.bind('<Return>',Calc)
############################################

################ Tab 2 Wiki ################

Font1 = ('Angsana New',25)
Font2 = ('Angsana New',16)

L2 = Label(T2,text='ค้นหาข้อมูล Wikipedia',font=Font1)
L2.pack()

v_search = StringVar()

E2 = ttk.Entry(T2, textvariable=v_search,font=Font1)
E2.pack(pady=10)

wikipedia.set_lang('th')

v_link = StringVar()

def Search(event=None):
    try:
        search = v_search.get()
        # text = wikipedia.summary(search)
        text = wikipedia.page(search)
        v_result.set(text.content[:1000])
        print('LINK ===> ', text.url)
        v_link.set(text.url)
    except:
        v_result.set('------ไม่มีข้อมูล---------')


B2 = Button(T2, text='Search',image=icon_tab2,compound='left',command=Search)
B2.pack(ipadx=10,ipady=10)

def readMore():
    webbrowser.open(v_link.get())


B3 = Button(T2, text='Readmore......',command=readMore)
B3.pack()

v_result = StringVar()
v_result.set('----------- Result----------')
result = Label(T2, textvariable=v_result,font=Font2,wraplength= 500)
result.pack(pady=15)

E2.bind('<Return>',Search)

############################################

################ Tab 3 CAFE ################

Bfont = ttk.Style()
Bfont.configure('TButton',font=('Angsana New',18))

CF1 = Frame(T3)
CF1.place(x=50,y=50)

###### ROW 0

allmenu = {}
product = {'latte':{'name':'ลาเต้','price':30},
            'cappuccino':{'name':'คาปูชิโน','price':35},
            'espresso':{'name':'เอสเปรสโซ่','price':40},
            'greentea':{'name':'ชาเขียว','price':45},
            'icetea':{'name':'ชาเย็น','price':50},
            'hottea':{'name':'ชาร้อน','price':65}},

def UpdateTable():
    table.delete(*table.get_children())  # เคลียข้อมูล
    for i,m in enumerate(allmenu.values(), start=1):
        table.insert('','end',values=[ i, m[0], m[1], m[2], m[3] ])

    

def AddMenu(name = 'latte'):
    # table.insert('','end', values=[1,'ลาเต้',1,30,50])
    # allmenu['latte'] = [1,'ลาเต้',1,30,50]
    # print(allmenu)
    # name = 'latte'
    if name not in allmenu:
        allmenu[name] = [product[name]['name'],product[name]['price'],1,product[name]['price']]
        
    else:
        quan = allmenu[name][2] + 1
        total = quan * product[name]['price']
        allmenu[name] = [product[name]['name'],product[name]['price'], quan, total]
    
    print(allmenu)
    # sum
    count = sum([m[3] for m in allmenu.values()])
    v_total.set(f'{count:,.2f}')
    UpdateTable()
    

# def Menu1():
#     AddMenu('latte')
#     UpdateTable()

# def Menu2():
#     AddMenu('cappuccino')
#     UpdateTable()

# def Menu3():
#     AddMenu('espresso')
#     UpdateTable()

B = ttk.Button(CF1,text='ลาเต้',image=icon_tab3,compound='top',command=lambda m = 'latte' : AddMenu(m))
B.grid(row=0, column=0,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='คาปูชิโน',image=icon_tab3,compound='top',command=lambda m = 'cappuccino' : AddMenu(m))
B.grid(row=0, column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='เอสเปรสโซ่',image=icon_tab3,compound='top',command=lambda m = 'espresso' : AddMenu(m))
B.grid(row=0, column=2,ipadx=20,ipady=10)

B = ttk.Button(CF1,text='ชาเขียว',image=icon_tab3,compound='top',command=lambda m = 'greentea' : AddMenu(m))
B.grid(row=1, column=0,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='ชาเย็น',image=icon_tab3,compound='top',command=lambda m = 'icetea' : AddMenu(m))
B.grid(row=1, column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='โกโก้',image=icon_tab3,compound='top',command=lambda m = 'hottea' : AddMenu(m))
B.grid(row=1, column=2,ipadx=20,ipady=10)

CF2 = Frame(T3)
CF2.place(x=500,y=50)

header = ['No.','title', 'price','quantity', 'total']
hwidth = [50, 200, 100, 100, 100]

table = ttk.Treeview(CF2,columns=header, show='headings',height=20)
table.pack()

# for hd in header:
#     table.heading(hd,text=hd)

for hd, hw in zip(header,hwidth):
    table.heading(hd,text=hd)
    table.column(hd,width=hw)


v_total = StringVar()
v_total.set(0.0)

Label(T3, text='Total : ', font=(None,30)).place(x=500, y=480)

LF = Frame(T3, width=200)
LF.place(x=650, y=480)
L = Label(LF, textvariable=v_total, font=(None,30),fg='green')
L.pack()

Label(T3, text=' บาท', font=(None,30)).place(x=800, y=480)

def Reset():
    global allmenu
    table.delete(*table.get_children())
    allmenu = {}
    v_total.set(0.0)
    trstamp = datetime.now().strftime('%y%m%d%H%M%S')
    v_transaction.set(trstamp)

B = ttk.Button(T3, text='Reset',command=Reset)
B.place(x=500,y=550)

# Transaction ID
v_transaction = StringVar()
trstamp = datetime.now().strftime('%y%m%d%H%M%S')
v_transaction.set(trstamp)
LTR = Label(T3, textvariable=v_transaction,font=(None,10)).place(x=960, y=25)


# Save Button
FB = Frame(T3)
FB.place(x=600, y=550)

def AddTransaction():
    #writeToCSV('transaction.csv')
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction = v_transaction.get()
    print(transaction,stamp, allmenu.values())
    for m in allmenu.values():
        m.insert(0,transaction)
        m.insert(1,stamp)
        writeToCSV(m, 'transaction.csv')
    Reset()


B = ttk.Button(FB, text='Save',command=AddTransaction)
B.pack()

################# History New Windows ###########################

def HistoryWindow(event):
    HIS = Toplevel()  # คล้าย  GUI = Tk()
    HIS.title('ข้อมูลการสั่งซื้อ')
    HIS.geometry('750x550')

    L = Label(HIS, text='ประวัติการสั่งซื้อ',font=(None, 15)).pack(pady=20)

    header = ['TS-ID','Datetime','title', 'price','quantity', 'total']
    hwidth = [100, 150, 150, 80, 80, 80, 100]

    table_history = ttk.Treeview(HIS,columns=header, show='headings',height=20)
    table_history.pack()

    for hd, hw in zip(header,hwidth):
        table_history.heading(hd,text=hd)
        table_history.column(hd,width=hw)

    # Update from CSV
    with open('transaction.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        for row in fr:
            table_history.insert('',0,value=row)

    HIS.mainloop()

GUI.bind('<F1>', HistoryWindow)




GUI.mainloop()