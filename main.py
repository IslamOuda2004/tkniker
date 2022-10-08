from tkinter import *
import tkinter
import matplotlib.pyplot as plt
import numpy as np


top = tkinter.Tk()
top.title('Grapher')
top.configure(bg='#F0FFFF')
top.minsize(300,600)
number1label = Label(top,width=55,height=5,font='arial')
number1label.configure(bg="#C0C0C0")
number1label.pack()
fx=""

def show(value):
    global fx
    fx+=value
    number1label.config(text=fx)

def clear():
    global fx
    fx = ""
    number1label.config(text=fx)

def gogo():
    global fx
    result=""
    if fx !="":
        try:
            result=eval(fx)
        except:
            result = 'error'
            fx =''
    number1label.config(text=result)




product = Button(text='*',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('*')).place(x=290,y=120)
divide = Button(text='/',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('/')).place(x=110,y=120)
add = Button(text='+',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('+')).place(x=290,y=300)
substact = Button(text='-',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('-')).place(x=290,y=210)
one = Button(text='1',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('1')).place(x=20,y=210)
four = Button(text='4',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('4')).place(x=20,y=300)
seven = Button(text='7',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('7')).place(x=20,y=390)
two = Button(text='2',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('2')).place(x=110,y=210)
five = Button(text='5',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('5')).place(x=110,y=300)
eight = Button(text='8',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('8')).place(x=110,y=390)
three = Button(text='3',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('3')).place(x=200,y=210)
six = Button(text='6',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('6')).place(x=200,y=300)
nine = Button(text='9',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('9')).place(x=200,y=390)
go = Button(text='=',width=3,height=3,font=('arial',30,"bold"),bd=5,bg='#FF8C00',fg='#FFFFFF',command=lambda :gogo()).place(x=290,y=390)
zero = Button(text='0',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('0')).place(x=20,y=480)
dot = Button(text='.',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('.')).place(x=200,y=120)
ac = Button(text='Ac',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :clear()).place(x=20,y=120)
lbow = Button(text='(',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show('(')).place(x=110,y=480)
rbow = Button(text=')',width=3,height=1,font=('arial',30,"bold"),bd=5,bg='#87CEEB',fg='#FF0000',command=lambda :show(')')).place(x=200,y=480)

top.mainloop()



