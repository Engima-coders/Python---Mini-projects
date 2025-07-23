from tkinter import *
import tkinter as tk
import requests 
import json
root=tk.Tk()
root.title("CURRENCY CONVERTER")
amt_var=tk.IntVar()
f_var=tk.StringVar()
t_var=tk.StringVar()
def conv():
    a=amt_var.get()
    b=f_var.get()
    c=t_var.get()
    
    url="ENTER YOUR CURRENCY CONVERTER API KEY"#first u have to get a api key from any currency converter website 
    response=requests.get(url)
    if response.status_code==200:
        rates=response.json()
        fr=rates["data"][b]["value"]
        tr=rates["data"][c]["value"]
        if b!="USD":
            a=a/fr
        a=round(a*tr,2)
    r_amt.insert(0,str(a)) 

def clear_all():
    r_amt.delete(0,tk.END)
    t_inp.delete(0,tk.END)
    f_inp.delete(0,tk.END)
    amt_inp.delete(0,tk.END)
    
root.geometry("930x500")

heading=tk.Label( font=('Sunken',25,'bold'),text="Currency Converter",padx=2, pady=2,)
heading.grid(row=1,column=20)

amt=tk.Label( font=('Sunken',15),text="AMOUNT:")
amt.grid(row=3,column=0)

amt_inp=Entry(root,bd=5,width=20,cursor="xterm",font=50,textvariable=amt_var)
amt_inp.grid(row=3,column=1)

currency_F=tk.Label( font=('Sunken',15),text="FROM:",pady=3)
currency_F.grid(row=5,column=0)

f_inp=Entry(root,font=50,bd=5,width=20,cursor="xterm",textvariable=f_var)
f_inp.grid(row=5,column=1)

currency_T=tk.Label( font=('Sunken',15),text="TO:")
currency_T.grid(row=7,column=0)

t_inp=Entry(root,bd=5,font=50,width=20,cursor="xterm",textvariable=t_var)
t_inp.grid(row=7,column=1)

con=tk.Button(root,text="CONVERT",bg="Blue",bd=10,fg="pink",justify='right',command=conv)
con.grid(row=9,column=1)

result=tk.Label( font=('Sunken',15),text="RESULT:",padx=5,pady=5)
result.grid(row=11,column=0,sticky=W)

r_amt=Entry(root,bd=5,font=50,width=20,cursor="xterm")
r_amt.grid(row=11,column=1,sticky=E)

clear=tk.Button(root,text="CLEAR ALL",bg="Blue",bd=10,fg="pink",justify='right',command=clear_all)
clear.grid(row=13,column=1)


root.mainloop()
