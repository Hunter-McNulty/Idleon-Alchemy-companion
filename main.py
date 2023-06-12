import tkinter
import dict
from os import path
import sys
from math import log10
import matplotlib.pyplot as plt
from numpy import linspace

def resource_path(relative_path):
    try:
        base_path = sys.MEIPASS
    except Exception:
        base_path = path.abspath(".")
    return path.join(base_path, relative_path)



class Window(tkinter.Tk):
    def __init__(self):
        super().__init__()   
        self.title("Alchemy Companion")
        self.geometry("505x500")
        

        def raise_frame(cauldron, number):
            active_frame = BubbleFrame(self, cauldron, number)
            active_frame.tkraise()

        self.menu = tkinter.Menu(self)
        
        self.pmenubar = tkinter.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Power Cauldron", menu=self.pmenubar)
        self.pmenubar.add_command(label="#1-5", command=lambda: raise_frame("Power", [1, 5]))
        self.pmenubar.add_command(label="#6-10", command=lambda: raise_frame("Power", [6, 10]))
        self.pmenubar.add_command(label="#11-15", command=lambda: raise_frame("Power", [11, 15]))
        self.pmenubar.add_command(label="#16-20", command=lambda: raise_frame("Power", [16, 20]))
        self.pmenubar.add_command(label="#21-25", command=lambda: raise_frame("Power", [21, 25]))

        self.qmenubar = tkinter.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Quicc Cauldron", menu=self.qmenubar)
        self.qmenubar.add_command(label="#1-5", command=lambda: raise_frame("Quicc", [1, 5]))
        self.qmenubar.add_command(label="#6-10", command=lambda: raise_frame("Quicc", [6, 10]))
        self.qmenubar.add_command(label="#11-15", command=lambda: raise_frame("Quicc", [11, 15]))
        self.qmenubar.add_command(label="#16-20", command=lambda: raise_frame("Quicc", [16, 20]))
        self.qmenubar.add_command(label="#21-25", command=lambda: raise_frame("Quicc", [21, 25]))

        self.imenubar = tkinter.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="High-IQ Cauldron", menu=self.imenubar)
        self.imenubar.add_command(label="#1-5", command=lambda: raise_frame("High-IQ", [1, 5]))
        self.imenubar.add_command(label="#6-10", command=lambda: raise_frame("High-IQ", [6, 10]))
        self.imenubar.add_command(label="#11-15", command=lambda: raise_frame("High-IQ", [11, 15]))
        self.imenubar.add_command(label="#16-20", command=lambda: raise_frame("High-IQ", [16, 20]))
        self.imenubar.add_command(label="#21-25", command=lambda: raise_frame("High-IQ", [21, 25]))

        self.kmenubar = tkinter.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Kazam Cauldron", menu=self.kmenubar)
        self.kmenubar.add_command(label="#1-5", command=lambda: raise_frame("Kazam", [1, 5]))
        self.kmenubar.add_command(label="#6-10", command=lambda: raise_frame("Kazam", [6, 10]))
        self.kmenubar.add_command(label="#11-15", command=lambda: raise_frame("Kazam", [11, 15]))
        self.kmenubar.add_command(label="#16-20", command=lambda: raise_frame("Kazam", [16, 20]))
        self.kmenubar.add_command(label="#21-25", command=lambda: raise_frame("Kazam", [21, 25]))

        self.config(menu=self.menu)

class BubbleFrame(tkinter.Frame):
    def __init__(self, parent, cauldron, number):
        tkinter.Frame.__init__(self, parent)
        self.grid(column=0, row=0)
        cauldronlist = dict.check(cauldron)

        for ids in range(number[0], number[1]+1):
            self.unit = cauldronlist[ids-1][4]
            self.x1 = cauldronlist[ids-1][2]
            self.x2 = cauldronlist[ids-1][3]
            self.equation = cauldronlist[ids-1][1]
            self.image = tkinter.PhotoImage(file=resource_path("alchemy_icons\\" + cauldron + "_Cauldron\\" + str(ids) + ".png"))
            self.label = tkinter.Label(self, image=self.image)
            self.label.grid(padx=10, pady=10, column=0, row=ids)
            self.label.image = self.image

            self.customentry = CustomEntry(self, ids, self.equation, self.x1, self.x2, self.unit, isdigitonly=True)


class CustomEntry(tkinter.Frame):
    def __init__(self, parent, row, equation, x1, x2, unit, isdigitonly):
        tkinter.Frame.__init__(self, parent)
        self.unit = unit
        self.x1 = x1
        self.x2 = x2
        self.equation = equation
        self.row = row
        self.grid(column=1, row=self.row)
        self.level_1 = tkinter.IntVar()
        self.level_2 = tkinter.IntVar()

        self.label_1 = tkinter.Label(self, text="Current Level:").grid(column=1, row=0)
        self.entry_1 = tkinter.Entry(self, width=10, textvariable=self.level_1)
        self.entry_1.grid(column=2, row=0)

        self.label_2 = tkinter.Label(self, text="Desired Level:").grid(column=3, row=0)
        self.entry_2 = tkinter.Entry(self, width=10, textvariable=self.level_2)
        self.entry_2.grid(column=4, row=0)

        self.label_3 = tkinter.Label(self, text="", width=10)
        self.label_3.grid(column=5, row=0, padx=10, columnspan=3)
        self.level_1.set(1)
        self.level_2.set(1)
        self.level_1.trace_add('write', self.callback)
        self.level_2.trace_add('write', self.callback)
        if isdigitonly:
            self.level_1.trace_add('write', self.check)
            self.level_2.trace_add('write', self.check)
        
        self.graph_button = tkinter.Button(self, text="Graph me!", command=lambda: self.graph(self.level_1.get(), self.level_2.get(), self.equation, self.x1, self.x2))
        self.graph_button.grid(column=6, row=self.row)

    def graph(self, x, y, equation, x1, x2):
        x3 = linspace(x,y)
        if equation == "Add":
            y2 = Add(x3, x1, x2)
        if equation == "Decay":
            y2 = Decay(x3, x1, x2)
        if equation == "DecayMult":
            y2 = DecayMult(x3, x1, x2)
        if equation == "BigBase":
            y2 = BigBase(x3, x1, x2)
        plt.plot(x3,y2)
        plt.xlabel('Level')
        plt.ylabel('Bonus')
        plt.show()

    def removespecialcharacters(self, var):
        var = var.translate({ord(i): None for i in '+-x%'})
        var = var.replace(" ", "")
        return int(float(var))
        


#Write special claus for 0, since log10(0)+1 is undefined
#Need to add a check to disable non numbers
#Shortcut keys maybe?

    def check(self, *args):
        try:
            if log10(int(self.level_1.get())) + 1 > 5:
                num = int(self.level_1.get() / 10)
                self.level_1.set(num)
            if log10(int(self.level_2.get())) + 1 > 5:
                num = int(self.level_2.get() / 10)
                self.level_2.set(num)
        except:
            self.level_1.set(1)
            self.level_2.set(1)


    def callback(self, *args):
        try:
            if int(self.level_1.get()) / 1 and int(self.level_2.get()) / 1:
                if self.equation == "Add":
                    num = (Add(int(self.level_2.get()), self.x1, self.x2) - Add(int(self.level_1.get()), self.x1, self.x2))
                    num = format(num, '.4f')
                    self.label_3.config(text=f"+ {num} {self.unit}")
                if self.equation == "Decay":
                    num = (Decay(int(self.level_2.get()), self.x1, self.x2) - Decay(int(self.level_1.get()), self.x1, self.x2))
                    num = format(num, '.4f')
                    self.label_3.config(text=f"+ {num} {self.unit}")
                if self.equation == "DecayMult":
                    num = (DecayMult(int(self.level_2.get()), self.x1, self.x2) - DecayMult(int(self.level_1.get()), self.x1, self.x2))
                    num = format(num, '.4f')
                    self.label_3.config(text=f"+ {num} {self.unit}")
                if self.equation == "BigBase":
                    num = (BigBase(int(self.level_2.get()), self.x1, self.x2) - BigBase(int(self.level_1.get()), self.x1, self.x2))
                    num = format(num, '.4f')
                    self.label_3.config(text=f"+ {num} {self.unit}")
        except:
            self.label_3.config(text=f"+ 0 {self.unit}")


#Equations
def Decay(level, x1, x2):
    return (level * x1) / (level + x2)

def DecayMult(level, x1, x2):
    return 1 + (level * x1) / (level + x2)

def BigBase(level, x1, x2):
    return x1 + x2 * level

def Add(level, x1, x2):
    if (x2 != 0):
        return (((x1 + x2) / x2 + 0.5 * (level - 1)) / (x1 / x2)) * level * x1
    else:
        return level * x1



if __name__ == "__main__":
    window = Window()
    window.resizable(0,0)
    window.iconphoto(False, tkinter.PhotoImage(file=resource_path("logo.ico")))
    window.mainloop()