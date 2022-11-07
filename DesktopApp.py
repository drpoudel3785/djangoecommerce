from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
# add widgets here

window.title('Hello Python')
btn=Button(window, text="This is Button widget", fg='blue', bg='magenta')
btn.place(x=90, y=100)
window.title('Hello Python')



lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)

txtfld=Entry(window, text="This is Entry Widget", bg='black',fg='white', bd=5)
txtfld.place(x=60, y=75)

v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="male", variable=v0,value=1)
r2=Radiobutton(window, text="female", variable=v0,value=2)
r1.place(x=100,y=120)
r2.place(x=180, y=120)


v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "Cricket", variable = v1)
C2 = Checkbutton(window, text = "Tennis", variable = v2)
C1.place(x=100, y=140)
C2.place(x=180, y=140)

data=("one", "two", "three", "four")
cb=Combobox(window, values=data)
cb.place(x=60, y=150)

lb=Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=100, y=170)




#window.geometry("widthxheight+XPOS+YPOS")
window.geometry("300x600+10+20")

#Signature: Button(window, attributes)
"""
You can set the following important properties to customize a button:
•	text : caption of the button
•	bg : background colour
•	fg : foreground colour
•	font : font name and size
•	image : to be displayed instead of text
•	command : function to be called when clicked
"""
window.mainloop()


