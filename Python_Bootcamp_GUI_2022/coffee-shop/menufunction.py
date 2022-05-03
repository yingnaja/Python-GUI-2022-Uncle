
from argparse import FileType
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from soupsieve import select
from productdb import *


############################################################################
############################################################################

class ProductIcon:
    
    ######## ไว้ใช้ประกาศตัวแปร ###########
    def __init__(self):
        self.quantity = None   #จำนวนสินค้า
        self.table_product = None # ใส่ข้อมูลตารางโชว์สินค้า
        self.v_radio = None    # ตัวแปร ติ๊กถูก
        
        
    ########## สร้างหน้าจออีกหนึ่งหน้าจอ ##########  
    def popup(self):
        PGUI = Toplevel()    
        PGUI.geometry('500x500')
        PGUI.title('ตั้งค่า ====> โชว์ไอคอนสินค้า')
        
        ################## ตารางสินค้า ####################################################
        ########## table #############
        header = ['ID','รหัสสินค้า','ชื่อสินค้า', 'แสดงไอคอน']
        hwidth = [70,100, 150, 70]

        self.table_product = ttk.Treeview(PGUI,columns=header, show='headings',height=15)
        self.table_product.pack(pady=50)

        for hd, hw in zip(header,hwidth):
            self.table_product.heading(hd,text=hd)
            self.table_product.column(hd,width=hw)
        
        self.table_product.bind('<Double-1>', self.change_status)
        self.insert_table()
        PGUI.mainloop()
        
        
    ######## เอาข้อมูลใส่ในตาราง ###########
    def insert_table(self):
        data = View_product_table_icon()
        print(data)
        for d in data:
            row = list(d)   # แปลง tuble เป็น list
            row.append('✓')
            self.table_product.insert('','end', value=row)
        
    
    ######## คำสั่งดับเบิ้ลคลิกเพื่อแก้ไขติ๊กถูก ###################
    def change_status(self, event=None):
        select = self.table_product.selection()
        pid = self.table_product.item(select)['values'][0]
        print('##### pid ===> ',pid)
        
        
        SGUI = Toplevel()
        SGUI.geometry('200x100')
        
        ########## ตัวเลือกเช็คบ็อค ##########
        self.v_radio = StringVar()
        RB1 = ttk.Radiobutton(SGUI, text='โชว์ไอคอน', variable=self.v_radio, value='show', command= lambda x=None: insert_product_status(int(pid),'show'))
        RB2 = ttk.Radiobutton(SGUI, text='ไม่โชว์ไอคอน', variable=self.v_radio, value='noShow',command= lambda x=None: insert_product_status(int(pid),'noShow'))
        RB1.pack()
        RB2.pack()
        RB1.invoke()   # การตั้งค่า defalut ของ Radiobutton
        
        ########## ตัวเลือกดร็อปดาว ##########
        dropdown = ttk.Combobox(SGUI, values=['โชว์ไอคอน','ไม่โชว์ไอคอน'])
        dropdown.pack()
        dropdown.set('โชว์ไอคอน')   # ค่า defalut ของ dropdown
        dropdown.bind('<<ComboboxSelected>>', lambda x=None: print(dropdown.get()))
        
        
        SGUI.mainloop()
        
    
        
    ######## เอาคำสั่งที่จะใช้แสดงมาใส่ใน Function นี้ ###########   
    def command(self):
        self.popup()
        
        
        
        


############################################################################
############################################################################

class AddProduct:

    def __init__(self):
        self.v_productid = None
        self.v_title = None
        self.v_price = None
        self.v_imagepath = None


    def popup(self):
        MGUI = Toplevel()
        MGUI.geometry('500x600')
        MGUI.title('Add Product')

        self.v_productid = StringVar()
        self.v_title = StringVar()
        self.v_price = StringVar()
        self.v_imagepath = StringVar()

        L = Label(MGUI, text='เพิ่มสินค้า', font=(None, 30))
        L.pack(pady=10)

        L = Label(MGUI, text='รหัสสินค้า', font=(None, 20)).pack()
        E1 = Entry(MGUI, textvariable=self.v_productid, font=(None, 20))
        E1.pack(pady=10)

        L = Label(MGUI, text='ชื่อสินค้า', font=(None, 20)).pack()
        E2 = Entry(MGUI, textvariable=self.v_title, font=(None, 20))
        E2.pack(pady=10)

        L = Label(MGUI, text='ราคาสินค้า', font=(None, 20)).pack()
        E3 = Entry(MGUI, textvariable=self.v_price, font=(None, 20))
        E3.pack(pady=10)

        L = Label(MGUI,textvariable=self.v_imagepath).pack()

        Bselect = Button(MGUI,text='เลือกรูปสินค้า (50x50 px)', command=self.selectfile)
        Bselect.pack(pady=10)

        Bsave = Button(MGUI,text='บันทึก', command=self.saveprocut)
        Bsave.pack(pady=10,ipadx=10,ipady=20)

        MGUI.mainloop()


    def selectfile(self):
        fileTypes = (
                ('PNG', '*.png'),
                ('All files','*.*')
        )
        select = filedialog.askopenfilename(title='เลือกไฟล์ภาพ',initialdir='/',filetypes=fileTypes)
        self.v_imagepath.set(select)

    def saveprocut(self):
        v1 = self.v_productid.get()
        v2 = self.v_title.get()
        v3 = self.v_price.get()
        v4 = self.v_imagepath.get()
        Insert_product(v1,v2,v3,v4)
        self.v_productid.set('')
        self.v_title.set('')
        self.v_price.set('')
        self.v_imagepath.set('')
        View_product()


    def command(self):
        self.popup()

if __name__ == '__main__':
    test = AddProduct()
    