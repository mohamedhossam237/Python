from tkinter import *
global main_screen
global username
global password
global username_entry
global password_entry
def main_account_screen():
    
    main_screen = Tk()    
    main_screen.geometry("300x250") 
    main_screen.title("Account Login") 
 
 
    Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
 

    Button(text="Login", height="2", width="30").pack() 
    Label(text="").pack() 
 

    Button(text="Register", height="2", width="30").pack()
 
    main_screen.mainloop() 
 
    main_account_screen() 
def register():
 
    
    register_screen = Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
 
    
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
   
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    
    Label(register_screen, text="").pack()
    
    Button(register_screen, text="Register", width=10, height=1, bg="blue").pack()
 

 
 
    Button(text="Register", height="2", width="30", command=register).pack()
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
 
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
