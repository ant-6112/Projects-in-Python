from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.equation=Entry(master, width=40, borderwidth=5)
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.ButtonCreation()

    def ButtonCreation(self):
        but0 = self.Add_Button(0)
        but1 = self.Add_Button(1)
        but2 = self.Add_Button(2)
        but3 = self.Add_Button(3)
        but4 = self.Add_Button(4)
        but5 = self.Add_Button(5)
        but6 = self.Add_Button(6)
        but7 = self.Add_Button(7)
        but8 = self.Add_Button(8)
        but9 =  self.Add_Button(9)
        b_add = self.Add_Button('+')
        b_sub = self.Add_Button('-')
        b_mult = self.Add_Button('*')
        b_div = self.Add_Button('/')
        b_clear = self.Add_Button('C')
        b_equal = self.Add_Button('=')

        RoW_1   =  [but7,but8,but9,b_add]
        RoW_2   =  [but4,but5,but6,b_sub]
        RoW_3   =  [but1,but2,but3,b_mult]
        RoW_4   =  [b_clear,but0,b_equal,b_div]

        r=1
        for row in [RoW_1, RoW_2, RoW_3, RoW_4]:
            c=0
            for butt in row:
                butt.grid(row=r, column=c, columnspan=1)
                c+=1
            r+=1

    def Add_Button(self,val):
        return Button(self.master, text=val, width=9, command = lambda: self.Click_Button(str(val)))
    
    def Click_Button(self, val):
        current_equation=str(self.equation.get())
        if val == 'c':
            self.equation.delete(-1, END)
        elif val == '=':
            Answer_O = str(eval(current_equation))
            self.equation.delete(-1, END)
            self.equation.insert(0, Answer_O)
        else:
            self.equation.delete(0, END)
            self.equation.insert(0, current_equation+val)


if __name__=='__main__':
    Calc_Main = Tk()
    Gui = Calculator(Calc_Main)
    Calc_Main.mainloop()