import sqlite3


#帳號信箱寫入驗證表
def verification(username,useremail):
    conn = sqlite3.connect('stock.db')
    cur = conn.cursor()
    cur.execute("select * from account")
    for rows in cur.fetchall():
        if username == rows[0]:
            cur.execute("insert into verification(username,email,verification) values({},{},true);".format(username,useremail))
            conn.commit()
            conn.close
            break
    else:
        print("此帳號不存在")

username = input("user:")
useremail = input("email:")

verification(username, useremail)

#修改密碼

def revise(password,username):
    conn = sqlite3.connect('stock.db')
    cur = conn.cursor()
    cur.execute("update account set password ={} where username = {};".format(password,username))
    conn.commit()
    conn.close()

username = input("user:")
password = input("password:")

revise(password,username)