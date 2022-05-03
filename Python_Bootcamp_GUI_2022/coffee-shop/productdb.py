import sqlite3
from tabnanny import check
from idna import check_hyphen_ok

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

### สร้างตารางสินค้า status
c.execute("""CREATE TABLE IF NOT EXISTS product_status (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            status TEXT) """)

def insert_product_status(pid, status):
    check = View_product_status(pid)
    if check == None:
        with conn:
            command = 'INSERT INTO product_status VALUES (?,?,?)'
            c.execute(command,(None,pid,status))
        conn.commit()
        print('status saved')
    else:
        print('pid Exit')
        print(check)
        Update_prodcut_status(pid, status)
        
        
def View_product_status(pid):
    with conn:
        Command = 'SELECT * FROM product_status WHERE product_id = (?)'
        c.execute(Command,([pid]))  
        result = c.fetchone()
    return result


def Update_prodcut_status(pid, status):
    with conn:
        command = 'UPDATE product_status SET status = (?) WHERE ID = (?)'
        c.execute(command,([status,pid]))
    conn.commit()
    print('updated', (pid, status))   
        

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

def View_product_table_icon():
    with conn:
        Command = 'SELECT ID, productid, title FROM product'
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
    # Insert_product('CF-1001','เอสเปรสโซ่',45, r'C:\images\oxy.png')
    # View_product_table_icon()
    # View_product()
    insert_product_status(13, 'show')
    View_product_status(13)