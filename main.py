from tkinter import *
import sqlite3
import string
import random



def register_menu():
    global register_window
    register_window = Toplevel(mainMenu)
    register_window.title("Register")
    register_window.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(register_window, text="Please enter details below", bg="blue").pack()
    Label(register_window, text="").pack()

    username_label = Label(register_window,text="Username * ")
    username_label.pack()

    username_entry = Entry(register_window, textvariable=username)
    username_entry.pack()

    password_label = Label(register_window, text="Password * ")
    password_label.pack()

    password_entry = Entry(register_window, textvariable=password, show='*')
    password_entry.pack()

    Label(register_window, text="").pack()

    Button(register_window, text="Register", width=10, height=1, bg="blue", command=register_user).pack()

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str

def register_user():
    connection = sqlite3.connect("locker.db")
    cursor = connection.cursor()

    AccountNum = id_generator(10)
    username_record = username.get()
   # print(username_record)
    password_record = password.get()
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    #print(password_record)
    cursor.execute("Insert INTO tablePW(AccountNum, Username, Password) VALUES(?, ?, ?)", (AccountNum, username_record, password_record))
    connection.commit()
    cursor.close()
    Label(register_window, text="Registration Succes", fg="green", font=("calibri", 11)).pack()

def login_menu():
    global login_window
    login_window = Toplevel(mainMenu)
    login_window.title("Login")
    login_window.geometry("300x250")
    Label(login_window,text="Please enter your details below to login.").pack()
    Label(login_window,text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_window, text="Username * ").pack()
    username_login_entry = Entry(login_window, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_window, text="").pack()
    Label(login_window, text="Password * ").pack()
    password_login_entry = Entry(login_window, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_window, text="").pack()
    Button(login_window, text="Login", width=10, height=1, command=login_verify).pack()

def login_verify():
  global username1
  global password1
  print("Working...")
  connection1 = sqlite3.connect("locker.db")
  cursor1 = connection1.cursor()

  username1 = username_verify.get()
  password1 = password_verify.get()

  username_login_entry.delete(0, END)
  password_login_entry.delete(0, END)

  query = """select Password from tablePW where Username = ?"""
  cursor1.execute(query, (username1,))
  verifyPW = cursor1.fetchall()
  sum(map(len, verifyPW))

  if sum(map(len, verifyPW)) > 0:

      verifyPW = convertTuple(verifyPW[0])

      if verifyPW == password1:
          login_succes_box()
      elif verifyPW is not password1:
          login_failure_box()
  else:
      credential_failure_box()

def login_failure_box():
    global login_failure_box
    login_failure_box = Toplevel(login_window)
    login_failure_box.title("Username not found")
    login_failure_box.geometry("175x125")
    Label(login_failure_box, text="Username not found").pack()
    Button(login_failure_box, text="OK", command=delete_login_failure_box).pack()

def credential_failure_box():
    global credential_failure_box
    credential_failure_box = Toplevel(login_window)
    credential_failure_box.title("Failed Login")
    credential_failure_box.geometry("175x125")
    Label(credential_failure_box, text="Login failed").pack()
    Button(credential_failure_box, text="OK", command=delete_credential_failure_box).pack()


def login_succes_box():
    global login_succes_box
    login_succes_box = Toplevel(login_window)
    login_succes_box.title("Succesful Login")
    login_succes_box.geometry("175x125")
    Label(login_succes_box, text="Login Success").pack()
    Button(login_succes_box, text="OK", command=delete_login_succes_box).pack()

def username_portal():
    global username_portal_box
    username_portal_box = Toplevel(mainMenu)
    username_portal_box.title("Welcome")
    username_portal_box.geometry("300x250")
    Label(username_portal_box, text=f"Welcome {username1}").pack()
    Label(username_portal_box, text="").pack()

    connection2 = sqlite3.connect("locker.db")
    cursor2 = connection2.cursor()

    query = """select AccountNum from tablePW where Username = ?"""
    cursor2.execute(query, (username1,))
    account_num = cursor2.fetchall()
    account_num =  convertTuple(account_num[0])

    Label(username_portal_box, text=f"Account Number: {account_num}").pack()
    Label(username_portal_box, text="").pack()


def delete_login_succes_box():
    login_succes_box.destroy()
    login_window.destroy()
    username_portal()

def delete_login_failure_box():
    login_failure_box.destroy()

def delete_credential_failure_box():
    credential_failure_box.destroy()

def main_menu():
    global mainMenu
    mainMenu = Tk()
    mainMenu.geometry("300x250")


    mainMenu.title("Login Page")

    Label(text="Login or Register a new account", bg="DarkGray", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    Button(text="Login", height="2", width="30", command=login_menu).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register_menu).pack()


    mainMenu.mainloop()
main_menu()
