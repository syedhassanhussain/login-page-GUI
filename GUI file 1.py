import tkinter
from tkinter import *
from PIL import ImageTk, Image

root = Tk() #yahan tak aik normal GUI create hojati hai
title = root.title("hassan login page")

root.minsize(800,400)
root.configure(background="sky blue")
img = Image.open('D:\Downloads\logo-design-49597.png')
resized_img = img.resize((90,70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image=img)
img_label.pack(pady = (10,5))
text_label = Label(root,text='(Bayerische Motoren Werke Aktiengesellschaft)',fg='red',bg='sky blue')
text_label.pack()
text_label.configure(font=('verdana',24))
#Email section:
email_label = Label(root,text='Enter Your Email address',fg='black',bg='sky blue')
email_label.pack(pady = (20,5))
email_label.configure(font=('verdana',15))
email_input = Entry(root,width=50,bg='light blue')
email_input.pack(ipady=6,pady=(1,15))
#password section:
password_label = Label(root,text='Enter Your Password',fg='black',bg='sky blue')
password_label.pack(pady = (20,5))
password_label.configure(font=('verdana',15))
password_input = Entry(root,width=50,bg='light blue')
password_input.pack(ipady=6,pady=(1,15))
#login button section:
login_button = Button(root,text='LOGIN HERE',bg='light green',fg='black',width=10,height=1)
login_button.pack(pady=(10,20))
login_button.config(font=('verdana',20))
root.mainloop()

