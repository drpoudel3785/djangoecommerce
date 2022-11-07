from tkinter import *

def  checkLogin():
    user = txtflduser.get()
    password = txtfldpassword.get()
    t3.delete(0, 'end')
    if user=="admin" and password=="admin123":
         t3.insert(END, "Success")
    else:
        t3.insert(END, "Login Failed")

window = Tk()
window.title('Login')

lbl = Label(window, text = "Username: ", fg ='Black',font=("Arial",16))
lbl.place(x=50,y=20)

txtflduser = Entry(window, text ="",bg='white',fg='black',font=("Arial",14))
txtflduser.place(x=50,y=50)

lbl = Label(window, text = "Password: ", fg ='Black',font=("Arial",16))
lbl.place(x=50,y=90)

txtfldpassword = Entry(window, text = "", bg='white',fg='black',font=("Arial",14))
txtfldpassword.place(x=50,y=120)

btn = Button(window, text = "LOGIN",fg='white',bg='blue', command=checkLogin)
btn.place(x=130, y=200)

lbl3=Label(window, text='Result')
t3=Entry(window)
lbl3.place(x=130, y=240)
t3.place(x=200, y=240)
window.geometry("300x400+10+20")
window.mainloop()



