import tkinter
import time 
import pynput
from tkinter import *
from pynput.keyboard import Key, Controller
#initializations

pencere = tkinter.Tk()
keyboard = Controller()

#functions
def keyboard_1():
    time.sleep(2)
    keyboard.press('1')
    keyboard.release('1')
    
def keyboard_2():
    time.sleep(2)
    keyboard.press('2')
    keyboard.release('2')
    
def keyboard_3():
    time.sleep(2)
    keyboard.press('3')
    keyboard.release('3')
    
def keyboard_4():
    time.sleep(2)
    keyboard.press('4')
    keyboard.release('4')

def keyboard_5():
    time.sleep(2)
    keyboard.press('5')
    keyboard.release('5')
    
def keyboard_6():
    time.sleep(2)
    keyboard.press('6')
    keyboard.release('6')

def keyboard_7():
    time.sleep(2)
    keyboard.press('7')
    keyboard.release('7')

def keyboard_8():
    time.sleep(2)
    keyboard.press('8')
    keyboard.release('8')

def keyboard_9():
    time.sleep(2)
    keyboard.press('9')
    keyboard.release('9')

def keyboard_0():
    time.sleep(2)
    keyboard.press('0')
    keyboard.release('0')


#a = FALSE
#title

pencere.geometry(        "300x300+475+250")#çarpılı pencere boyutu artılı ekrandaki boyutu
#pencere.resizable(width=a,height=a)
title = pencere.title("\t\tSanal Klavye")
sentence = Label(text = "\n\n\tSanal Klavyeye Hoş Geldiniz\t")

sentence.pack()
a = 1
while a:
    
    id_button1 = Button(pencere,text="1",command = keyboard_1)
    id_button1.place(relx=.05,rely=0.20,relheight=0.15,relwidth=0.30)
    #id_button1.pack()
    
    
    id_button2 = Button(pencere,text="2",command= keyboard_2)
    id_button2.place(relx=0.35,rely=0.20,relheight=0.15,relwidth=0.3)
    #id_button2.pack()
    
    id_button3 = Button(pencere,text="3",command= keyboard_3)
    id_button3.place(relx=0.65,rely=0.2,relheight=0.15,relwidth=0.3)
    #id_button3.pack(side = RIGHT)
    
    
    
    id_button4 = Button(pencere,text="4",command= keyboard_4,width = 10,height = 2)
    id_button4.place(relx=0.05,rely=0.4,relheight=0.15,relwidth=0.3)
    
    
    id_button5 = Button(pencere,text="5",command= keyboard_5,width = 10,height = 2)
    id_button5.place(relx=0.35,rely=0.4,relheight=0.15,relwidth=0.3)
    

    id_button6 = Button(pencere,text="6",command= keyboard_6,width = 10,height = 2)
    id_button6.place(relx=0.65,rely=0.4,relheight=0.15,relwidth=0.3)
    
    ##
    id_button7 = Button(pencere,text="7",command= keyboard_7,width = 10,height = 2)
    id_button7.place(relx=0.05,rely=0.6,relheight=0.15,relwidth=0.3)
   
    
    id_button8 = Button(pencere,text="8",command= keyboard_8,width = 10,height = 2)
    id_button8.place(relx=0.35,rely=0.6,relheight=0.15,relwidth=0.3)
    
    
    id_button9 = Button(pencere,text="9",command= keyboard_9,width = 10,height = 2)
    id_button9.place(relx=0.65,rely=0.6,relheight=0.15,relwidth=0.3)
    
    ##
    id_button0 = Button(pencere,text="0",command= keyboard_0,width = 10,height = 2)
    id_button0.place(relx=0.05,rely=0.8,relheight=0.15,relwidth=0.9)

    a = 0
    
    





pencere.mainloop()#pencerenin tamamlanmasını sağlıyor


    

# CODDING ------------


         
