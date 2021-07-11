# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 08:51:51 2021

@author: kathir
"""

import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self):
        self.calc_done = False
        
    def createGui(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("530x250")
        self.root.config(bg="#00BFFF")
        self.result_font = font.Font(font="Aerial",size=40,weight='bold')
        self.result_variable = tk.StringVar()
        
        self.result = tk.Entry(self.root,textvariable=self.result_variable,state="disabled",bg="#FFFFFF",bd=3)
        self.result['font'] = self.result_font
        self.result.config(disabledbackground="white")
        self.result.config(fg="#000000")
        self.result.place(x=20,y=10,width=490,height=40)
        
        self.button7 = tk.Button(self.root,text="7",font=self.result_font,command=self.button7Press,fg="#FFFFFF",bg="#000000")
        self.button7.place(x=20,y=70,width=60)
        
        self.button8 = tk.Button(self.root,text="8",font=self.result_font,command=self.button8Press,fg="#FFFFFF",bg="#000000")
        self.button8.place(x=80,y=70,width=60)
        
        self.button9 = tk.Button(self.root,text="9",font=self.result_font,command=self.button9Press,fg="#FFFFFF",bg="#000000")
        self.button9.place(x=140,y=70,width=60)

        self.buttonbspace = tk.Button(self.root,text="\u2190",font=self.result_font,command=self.buttonbsPress,fg="#FFFFFF",bg="#000000")
        self.buttonbspace.place(x=200,y=70,width=60)
        
        self.buttonbclear = tk.Button(self.root,text="C",font=self.result_font,command=self.buttonclearPress,bg="#ff0000")
        self.buttonbclear.place(x=260,y=70,width=60)
        
        self.button4 = tk.Button(self.root,text="4",font=self.result_font,command=self.button4Press,fg="#FFFFFF",bg="#000000")
        self.button4.place(x=20,y=110,width=60)

        self.button5 = tk.Button(self.root,text="5",font=self.result_font,command=self.button5Press,fg="#FFFFFF",bg="#000000")
        self.button5.place(x=80,y=110,width=60)
        
        self.button6 = tk.Button(self.root,text="6",font=self.result_font,command=self.button6Press,fg="#FFFFFF",bg="#000000")
        self.button6.place(x=140,y=110,width=60)
                
        self.buttondiv = tk.Button(self.root,text="/",font=self.result_font,command=self.buttondivPress,fg="#FFFFFF",bg="#000000")
        self.buttondiv.place(x=200,y=110,width=60)

        self.buttonsqr = tk.Button(self.root,text="𝑥\u00B2",font=self.result_font,command=self.buttonsqrPress,fg="#FFFFFF",bg="#000000")
        self.buttonsqr.place(x=260,y=110,width=60)
        
        self.button1 = tk.Button(self.root,text="1",font=self.result_font,command=self.button1Press,fg="#FFFFFF",bg="#000000")
        self.button1.place(x=20,y=150,width=60)
        
        self.button2 = tk.Button(self.root,text="2",font=self.result_font,command=self.button2Press,fg="#FFFFFF",bg="#000000")
        self.button2.place(x=80,y=150,width=60)
        
        self.button3 = tk.Button(self.root,text="3",font=self.result_font,command=self.button3Press,fg="#FFFFFF",bg="#000000")
        self.button3.place(x=140,y=150,width=60)
        
        self.buttonmul = tk.Button(self.root,text="*",font=self.result_font,command=self.buttonmulPress,fg="#FFFFFF",bg="#000000")
        self.buttonmul.place(x=200,y=150,width=60)
        
        self.buttonsqrt = tk.Button(self.root,text="\u221a",font=self.result_font,command=self.buttonsqrtPress,fg="#FFFFFF",bg="#000000")
        self.buttonsqrt.place(x=260,y=150,width=60)
        
        self.buttonplus = tk.Button(self.root,text="+",font=self.result_font,command=self.buttonplusPress,fg="#FFFFFF",bg="#000000")
        self.buttonplus.place(x=20,y=190,width=60)
        
        self.buttonzero = tk.Button(self.root,text="0",font=self.result_font,command=self.button0Press,fg="#FFFFFF",bg="#000000")
        self.buttonzero.place(x=80,y=190,width=60)
        
        self.buttonminus = tk.Button(self.root,text="-",font=self.result_font,command=self.buttonminusPress,fg="#FFFFFF",bg="#000000")
        self.buttonminus.place(x=140,y=190,width=60)
        
        self.buttondot = tk.Button(self.root,text=".",font=self.result_font,command=self.buttondotPress,fg="#FFFFFF",bg="#000000")
        self.buttondot.place(x=200,y=190,width=60) 
        
        self.buttonequal = tk.Button(self.root,text="=",font=self.result_font,command=self.buttonequalPress,fg="#FFFFFF",bg="#000000")
        self.buttonequal.place(x=260,y=190,width=60)
        
        self.archive_result_listbox = tk.Listbox(self.root,font = font.Font(family='aerial',size=12))
        self.archive_result_listbox.place(x=330,y=70 ,width=170,height=165)
        self.archive_result_scrollbar = tk.Scrollbar(self.root)
        self.archive_result_scrollbar.place(x=490,y=70,height=165)
        self.archive_result_listbox.config(yscrollcommand = self.archive_result_scrollbar.set)
        self.archive_result_scrollbar.configure(command=self.archive_result_listbox.yview)
        
        self.root.mainloop()
        
    def button1Press(self):
        if self.calc_done:
            self.result_variable.set(str())
        self.result_variable.set(self.result_variable.get()+"1")
        self.calc_done = False
    def button2Press(self):
        if self.calc_done:
            self.result_variable.set(str())
        self.result_variable.set(self.result_variable.get()+"2")
        self.calc_done = False
    def button3Press(self):
        if self.calc_done:
            self.result_variable.set(str())
        self.result_variable.set(self.result_variable.get()+"3")
        self.calc_done = False
    def button4Press(self):
        if self.calc_done:
            self.result_variable.set(str())
        self.result_variable.set(self.result_variable.get()+"4")
        self.calc_done = False
    def button5Press(self):
        if self.calc_done:
            self.result_variable.set(str())
        self.result_variable.set(self.result_variable.get()+"5")
        self.calc_done = False
    def button6Press(self):
        if self.calc_done:
            self.result_variable.set(str())
        self.result_variable.set(self.result_variable.get()+"6")
    def button7Press(self):
        if self.calc_done:
            self.result_variable.set(str())
        self.result_variable.set(self.result_variable.get()+"7")
        self.calc_done = False
    def button8Press(self):
        if self.calc_done:
            self.result_variable.set(str())
        self.result_variable.set(self.result_variable.get()+"8")
        self.calc_done = False
    def button9Press(self):
        if self.calc_done:
            self.result_variable.set(str())
        self.result_variable.set(self.result_variable.get()+"9")
        self.calc_done = False
    def buttonplusPress(self):
        self.result_variable.set(self.result_variable.get()+"+")
    def buttonminusPress(self):
        self.result_variable.set(self.result_variable.get()+"-")
    def button0Press(self):
        if self.calc_done:
            self.result_variable.set(str())
        self.result_variable.set(self.result_variable.get()+"0")
        self.calc_done = False
    def buttondivPress(self):
        self.result_variable.set(self.result_variable.get()+"/")
    def buttonmulPress(self):
        self.result_variable.set(self.result_variable.get()+"*")
    def buttondotPress(self):
        self.result_variable.set(self.result_variable.get()+".")
    def buttonclearPress(self):
        self.result_variable.set(str())
        self.archive_result_listbox.delete(0,tk.END)
    def buttonsqrPress(self):
        self.archive_result_listbox.insert(tk.END,str(self.result_variable.get()))
        self.result_variable.set(str(float(self.result_variable.get())**2))
        self.calc_done = True
        self.archive_result_listbox.insert(tk.END,str(self.result_variable.get()))
    def buttonbsPress(self):
        result = str()
        result = str(self.result_variable.get())
        self.result_variable.set(result[:-1])
    def buttonsqrtPress(self):
        self.archive_result_listbox.insert(tk.END,str(self.result_variable.get()))
        self.result_variable.set(str(float(self.result_variable.get())**0.5))
        self.calc_done = True
        self.archive_result_listbox.insert(tk.END,str(self.result_variable.get()))
    def buttonequalPress(self):
        self.archive_result_listbox.insert(tk.END,str(self.result_variable.get()))
        if self.calc_done:
            self.result_variable.set(str())
        expr = str(self.result_variable.get())
        try:
            self.result_variable.set(str(eval(expr)))
        except:
            self.result_variable.set("Invalid Expression")
        self.calc_done = True
        self.archive_result_listbox.insert(tk.END,str(self.result_variable.get()))

calc = Calculator()
calc.createGui()
