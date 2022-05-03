from cgitb import text
import imp
from tkinter import *
from tkinter import ttk, messagebox

########### Read CSV #################
import csv
from datetime import datetime
def writeToCSV(data):
    with open('data.csv','a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)
######################################

GUI = Tk()
GUI.title('โปรแกรมจัดการ laout')
GUI.geometry('500x500')


L1 = Label(GUI, text='จำนวนกุ้ง (กก.)',font=('Angsana New',25))
L1.pack()

v_kilo = StringVar()

E1 = ttk.Entry(GUI, textvariable=v_kilo, width=10, justify='right',font=('impact',30))
E1.pack(pady=20)

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

B1 = ttk.Button(GUI,text='คำนวณราคา',command=Calc)
B1.pack(ipadx=20,ipady=10)

E1.bind('<Return>',Calc)


GUI.mainloop()