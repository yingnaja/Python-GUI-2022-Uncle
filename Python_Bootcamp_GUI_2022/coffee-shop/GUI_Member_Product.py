from ast import Lambda
from cProfile import label
from cgitb import reset, text
import code
from distutils import command
from itertools import count, product
from mailbox import MH
from msilib.schema import tables
from optparse import Values
from secrets import choice
from time import strftime
from tkinter import font
from traceback import print_tb
from turtle import stamp
from unicodedata import name
import webbrowser
from re import M, search
from tkinter import *
from tkinter import ttk, messagebox
from soupsieve import select
import wikipedia 
from distutils import command

############ DATABASE ################
from memberdb import *
from productdb import *

############ Function ################
from menufunction import *
addproduct = AddProduct()
product_icon = ProductIcon()
# View_member()

# import memberdb
# memberdb.View_member()

# import memberdb as db
# db.View_member()
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
GUI.title('Python_Bootcamp_GUI_2020')
GUI.iconbitmap('images/Coffee.ico')

W = 1200
H = 700

MW = GUI.winfo_screenwidth()
MH = GUI.winfo_screenheight()
SX = (MW/2) - (W/2)
SY = (MH/2) - (H/2)
SY = SY - 50

GUI.geometry(f'{W}x{H}+{SX:.0f}+{SY:.0f}')

################# MENUBAR ####################

menubar = Menu(GUI)
GUI.config(menu=menubar)

# file mneu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)

def ExportDatabase():
    print('Export Database to CSV')

filemenu.add_command(label='Export',command=ExportDatabase)
filemenu.add_command(label='Exit',command=GUI.quit)  # GUI.destroy  ปิดโปรแกรม

# Member Menu
membermenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Member', menu=membermenu)

#product Menu
productmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Product', menu=productmenu)

productmenu.add_command(label='Add Product', command=addproduct.command)


###########  setting ########################################################################

settingmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Setting', menu=settingmenu)

settingmenu.add_command(label='Product Icon', command=product_icon.command)















#############################################################################################



# Help Menu
import webbrowser

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
contact_url = 'https://google.com'
helpmenu.add_command(label='Contact Us',command=lambda: webbrowser.open(contact_url))

def About():
    ABGUI = Toplevel()
    ABGUI.iconbitmap('images/Coffee.ico')
    W = 300
    H = 200

    MW = GUI.winfo_screenwidth()
    MH = GUI.winfo_screenheight()
    SX = (MW/2) - (W/2)
    SY = (MH/2) - (H/2)
    

    ABGUI.geometry(f'{W}x{H}+{SX:.0f}+{SY:.0f}')
    L = Label(ABGUI, text='Program Coffee',fg='green', font=('Angsana New', 30)).pack()
    L = Label(ABGUI, text='พัฒนาโดย Ying Naja\nTelephone: 0-8975-13041',font=('Angsana New', 20)).pack()
    ABGUI.mainloop()

helpmenu.add_command(label='About Us',command=About)

##########################################################################

Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)


T3 = Frame(Tab)
T4 = Frame(Tab)


icon_tab3 = PhotoImage(file='images/Coffee-brown-icon.png')
icon_tab4 = PhotoImage(file='images/member.png')


Tab.add(T3, text='CAFE',image=icon_tab3,compound='left')
Tab.add(T4, text='Member',image=icon_tab4,compound='left')



################################ COFFEE SHOP ###############################

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

###################### Tab 4 ###################################

def ET(GUI,  text, strvar, font=('Angsana new', 20)):
    L = Label(GUI, text=text, font=('None',15)).pack()
    T = ttk.Entry(GUI, textvariable=strvar, font=font)
    return (T)

def ET2(GUI,  text, strvar, font=('Angsana new', 20)):
    L = Label(GUI, text=text, font=('None',15))
    T = ttk.Entry(GUI, textvariable=strvar, font=font)
    return (L,T)

def ET3(GUI, text, font=('Angsana new', 20)):
    v_strvar = StringVar()
    L = Label(GUI, text=text, font=('None',15)).pack()
    T = ttk.Entry(GUI, textvariable=v_strvar, font=font)
    return (L,T, v_strvar)


# v_fullName = StringVar()
# E41 = ET(T4, 'Name', v_fullName)
# E41.place(x=300, y=50)

# v_tell = StringVar()
# L, E42 = ET2(T4, 'Telephone', v_tell)
# L.place(x=550, y=120)
# E42.place(x=500,y=150)

F41 = Frame(T4)
F41.place(x=50,y=70)

v_memberCode = StringVar()
v_memberCode.set('M-1001')
v_databasecode = IntVar()  # เก็บเลขฐานข้อมูล

L = Label(T4, text='รหัสสมาชิก : NO.  ', font=('Angsana New',20)).place(x=50, y=20)
LCode = Label(T4, textvariable=v_memberCode, font=(None, 20)).place(x=150, y=20)


L, E41, v_fullname = ET3(F41, 'ชื่อ - นามสกุล')
E41.pack()

L, E42, v_tell = ET3(F41, 'เบอร์โทรศัพท์')
E42.pack()

L, E43, v_userTpye = ET3(F41, 'ประเภทสมาชิก')
E43.pack()

L, E44, v_point = ET3(F41, 'คะแนนสะสม')
E44.pack()
v_point.set('0')

def SaveMember():
    code = v_memberCode.get()
    fullname = v_fullname.get()
    tell = v_tell.get()
    userType = v_userTpye.get()
    point = v_point.get()
    print(fullname,tell,userType,point)
    # writeToCSV([code, fullname, tell, userType, point], 'member.csv')
    Insert_member(code, fullname, tell, userType, point)
    # table_member.insert('', 0, values=[code, fullname, tell, userType, point])
    UpdateTable_Member()
    ####### Set default ########
    v_fullname.set('')
    v_tell.set('')
    v_userTpye.set('general')
    v_point.set('0')


BSave = ttk.Button(F41, text='Save', command=SaveMember)
BSave.pack()


def EditMember():
    code = v_databasecode.get()  # ดึงรหัสฐานข้อมูล
    allmember[code][2] = v_fullname.get()
    allmember[code][3] = v_tell.get()
    allmember[code][4] = v_userTpye.get()
    allmember[code][5] = v_point.get()
    # UpdateCSV(list(allmember.values()), 'member.csv')
    Update_member(code, 'fullname', v_fullname.get())
    Update_member(code, 'tel', v_tell.get())
    Update_member(code, 'usertype', v_userTpye.get())
    Update_member(code, 'points', v_point.get())
    UpdateTable_Member()

    BEdit.state(['disabled'])  # ปิดปุ่มแก้ไข
    BSave.state(['!disabled'])  # เปิดปุ่ม บันทึก

    ####### Set default ########
    v_fullname.set('')
    v_tell.set('')
    v_userTpye.set('general')
    v_point.set('0')

BEdit = ttk.Button(F41, text='Edit', command=EditMember)
BEdit.pack()

def NewMember():
    UpdateTable_Member()
    BEdit.state(['disabled'])  # ปิดปุ่มแก้ไข
    BSave.state(['!disabled'])  # เปิดปุ่ม บันทึก
    ####### Set default ########
    v_fullname.set('')
    v_tell.set('')
    v_userTpye.set('general')
    v_point.set('0')

BNew = ttk.Button(F41, text='New', command=EditMember)
BNew.pack()

F42 = Frame(T4)
F42.place(x=500,y=50)

########## table ##############################################################################
header = ['ID','Code.','Name', 'Telephone','ประเภทสมาชิก', 'คะแนนสะสม']
hwidth = [50,70, 180, 100, 100, 100]

table_member = ttk.Treeview(F42,columns=header, show='headings',height=20)
table_member.pack()

for hd, hw in zip(header,hwidth):
    table_member.heading(hd,text=hd)
    table_member.column(hd,width=hw)


#### Update CSV
def UpdateCSV(data, filename='data.csv'):
    with open(filename,'w', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerows(data)



###### Delete ข้อมูลในตารางที่เลือก
def DeleteMember(event=None):
    choice = messagebox.askyesno('Delete', 'คุณต้องการลบข้อมูลนี้หรือไม่ ?')
    print(choice)
    if choice == True:
        select = table_member.selection()  # เลือก item
        if len(select) != 0:
            data = table_member.item(select)['values']
            print(data)
            del allmember[data[0]]
            # UpdateCSV(list(allmember.values()), 'member.csv')
            Delete_member(data[0])
            UpdateTable_Member()
        else:
            messagebox.showwarning('ไม่ได้เลือกรายการ','กรุณาเลือกรายการก่อนลบข้อมูล')
    else:
        pass

table_member.bind('<Delete>', DeleteMember)

##### Update ข้อมูลสมาชิก
def UpdateMemberInfo(event=None):
    select = table_member.selection()  # เลือก item
    if len(select) != 0:
        code = table_member.item(select)['values'][0]
        v_databasecode.set(code)
        print(allmember[code])
        memberinfo = allmember[code]

        v_memberCode.set(memberinfo[1])
        v_fullname.set(memberinfo[2])
        v_tell.set(memberinfo[3])
        v_userTpye.set(memberinfo[4])
        v_point.set(memberinfo[5])

        BEdit.state(['!disabled'])  # เปิดปุ่มแก้ไข
        BSave.state(['disabled'])  # ปิดปุ่ม บันทึก
    else:
        messagebox.showwarning('ไม่ได้เลือกรายการ','กรุณาเลือกรายการก่อนแก้ไขข้อมูล')


table_member.bind('<Double-1>', UpdateMemberInfo)


# ######## Update Table_MEMBER
last_member = ''
allmember = {}

def UpdateTable_Member():  #### แก้ไขเป็น database
    global last_member
    # with open('member.csv',newline='',encoding='utf-8') as file:
    # fr = csv.reader(file)
    fr = View_member()
    table_member.delete(*table_member.get_children()) # เคลียข้อมูล
    for row in fr:
        table_member.insert('',0,value=row)
        code = row[0]
        allmember[code] = list(row)  # convert tuple to list

    print('Last Row : ', row)
    last_member = row[1]  #  select member
    next_member = int(last_member.split('-')[1]) +1
    v_memberCode.set(f'M-{next_member}')
    print(allmember)


####### Pop Up Menu ##########

member_rcmenu = Menu(GUI,tearoff=0)
table_member.bind('<Button-3>', lambda event: member_rcmenu.post(event.x_root,event.y_root))
member_rcmenu.add_command(label='Delete', command=DeleteMember)
member_rcmenu.add_command(label='Update', command=UpdateMemberInfo)

def SearchName():
    select = table_member.selection()
    name = table_member.item(select)['values'][1]
    print(name)
    url = f'https://www.google.com/search?q={name}'
    webbrowser.open(url)

def SearchBBC():
    select = table_member.selection()
    name = table_member.item(select)['values'][1]
    print(name)
    url = f'https://www.bbc.co.uk/search?q={name}'
    webbrowser.open(url)

member_rcmenu.add_command(label='Search Name', command=SearchName)
member_rcmenu.add_command(label='Search BBC', command=SearchBBC)



BEdit.state(['disabled'])
try:
    UpdateTable_Member()
except:
    print('กรุณากรอกข้อมูลอย่างน้อย 1 รายการ')


# import os

# file = os.listdir()
# print(file)

# if 'memberdb.sqlite3' in file:
#     print('OK')
#     UpdateTable_Member()

GUI.mainloop()