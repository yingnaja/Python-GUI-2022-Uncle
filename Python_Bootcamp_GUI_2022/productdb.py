import sqlite3

from setuptools import Command

conn = sqlite3.connect('produtdb.sqlite3')
c = conn.cursor()

# สร้างตารางจัดเก็บ
c.execute("""CREATE TABLE IF NOT EXISTS product (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            productid TEXT,
            title TEXT,
            price TEXT,
            image TEXT ) """)


def Insert_product(productid, title,price,imgae):
    with conn:
        Command = 'INSERT INTO product VALUES (?,?,?,?,?)'   # SQL
        c.execute(Command,(None,productid, title,price,imgae))  
    conn.commit()   # save database
    print('Saved')


def View_product():
    with conn:
        Command = 'SELECT * FROM product'
        c.execute(Command)  
        result = c.fetchall()
    print(result)
    return result


def View_product_single(productid):
    with conn:
        Command = 'SELECT * FROM product WHERE productid = (?)'
        c.execute(Command,([productid]))  
        result = c.fetchone()
    print(result)
    return result

# เช็คว่าตอนนี้ไฟล์ที่กำลังรันนี้อยู่ในไฟล์จริงหรือไม่
if __name__ == '__main__':
    Insert_product('CF-1001','เอสเปรสโซ่',45, r'C:\images\oxy.png')
    View_product()
