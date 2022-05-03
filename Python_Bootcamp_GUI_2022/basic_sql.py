from ast import Del
import sqlite3

from setuptools import Command

conn = sqlite3.connect('basicdb.sqlite3')
c = conn.cursor()

# สร้างตารางจัดเก็บ
c.execute("""CREATE TABLE IF NOT EXISTS member (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            membercode TEXT,
            fullname TEXT,
            tel TEXT,
            usertype TEXT,
            points INTEGER ) """)


def Insert_member(membercode, fullname,tel,usertype,points):
    with conn:
        Command = 'INSERT INTO member VALUES (?,?,?,?,?,?)'   # SQL
        c.execute(Command,(None,membercode, fullname,tel,usertype,points))  
    conn.commit()   # save database
    print('Saved')


def View_member():
    with conn:
        Command = 'SELECT * FROM member'
        c.execute(Command)  
        result = c.fetchall()
    print(result)
    return result


def Update_member(ID, field,newvalue):
    #update
    with conn:
        Command = 'UPDATE member SET {} = (?) WHERE ID=(?)'.format(field)
        c.execute(Command,([newvalue,ID]))
    conn.commit()
    print('updated')


def Delete_member(ID):
    with conn:
        command = 'DELETE FROM member WHERE ID=(?)'
        c.execute(command,([ID]))
    conn.commit()
    print('Deleted')


# res = View_member()
# print(res[1])
#Update_member(2,'fullname','sinya pong')
Delete_member(1)
View_member()


#Insert_member('MB-1002','pang naja','01024646450','normal',1000)
