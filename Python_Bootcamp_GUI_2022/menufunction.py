
from argparse import FileType
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from productdb import *

class AddMember:

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
        L.pack()

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
    test = AddMember()