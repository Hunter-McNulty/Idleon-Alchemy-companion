import tkinter
import dict
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys.MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

power_ids = []
quicc_ids = []
iq_ids = []
kazam_ids = []
for i in range(1, 26):
    power_ids.append("48px-OrangeBubble" + str(i) + ".png")
    quicc_ids.append("48px-GreenBubble" + str(i) + ".png")
    iq_ids.append("48px-PurpleBubble" + str(i)+ ".png")
    kazam_ids.append("48px-YellowBubble" + str(i) + ".png")


class Window(tkinter.Tk):
    def __init__(self):
        super().__init__()   
        self.title("Alchemy Companion")
        self.geometry("500x500")

        self.main_frame = tkinter.Frame(self, height=500, width=480).grid(column=0, row=0, sticky="ns")

        self.canvas = tkinter.Canvas(self.main_frame, width=450, height=500)
        self.canvas.grid(column=0, row=0)
        self.scrollbar = tkinter.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(column=1, row=0, sticky="ns")
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        self.canvas.bind('<Configure>', lambda e: self.canvas.config(scrollregion=self.canvas.bbox("all")))
        self.second_frame = BubbleFrame(self.canvas, "power")
        self.third_frame = BubbleFrame(self.canvas, "quicc")
        self.fourth_frame = BubbleFrame(self.canvas, "iq")
        self.fifth_frame = BubbleFrame(self.canvas, "kazam")

        self.second_frame.tkraise()


        def raise_frame(frame):
            if frame == "power":
                self.second_frame.tkraise()
            if frame == "quicc":
                self.third_frame.tkraise()
            if frame == "iq":
                self.fourth_frame.tkraise()
            if frame == "kazam":
                self.fifth_frame.tkraise()
        
        self.menubar = tkinter.Menu(self)
        self.menubar.add_command(label="Power Cauldron", command=lambda: raise_frame("power"))
        self.menubar.add_command(label="Quicc Cauldron", command=lambda: raise_frame("quicc"))
        self.menubar.add_command(label="High-IQ Cauldron", command=lambda: raise_frame("iq"))        
        self.menubar.add_command(label="Kazam Cauldron", command=lambda: raise_frame("kazam"))
        self.canvas.create_window((0,0), window=self.second_frame, anchor="nw")
        self.canvas.create_window((0,0), window=self.third_frame, anchor="nw")
        self.canvas.create_window((0,0), window=self.fourth_frame, anchor="nw")
        self.canvas.create_window((0,0), window=self.fifth_frame, anchor="nw")

        self.config(menu=self.menubar)

class BubbleFrame(tkinter.Frame):
    def __init__(self, parent, cauldron):
        tkinter.Frame.__init__(self, parent)
        self.grid(column=0, row=0)
        if cauldron == "power":
            for ids in power_ids:
                self.unit = dict.power_bubbles[power_ids.index(ids)][4]
                self.x1 = dict.power_bubbles[power_ids.index(ids)][2]
                self.x2 = dict.power_bubbles[power_ids.index(ids)][3]
                self.equation = dict.power_bubbles[power_ids.index(ids)][1]

                self.image = tkinter.PhotoImage(file=resource_path("alchemy_icons/Power_Cauldron/" + ids))
                self.label = tkinter.Label(self, image=self.image)
                self.label.grid(padx=10, pady=10, column=0, row=power_ids.index(ids))
                self.label.image = self.image

                self.customentry = CustomEntry(self, power_ids.index(ids), self.equation, self.x1, self.x2, self.unit)


        if cauldron == "quicc":
            for ids in quicc_ids:
                self.unit = dict.quicc_bubbles[quicc_ids.index(ids)][4]
                self.x1 = dict.quicc_bubbles[quicc_ids.index(ids)][2]
                self.x2 = dict.quicc_bubbles[quicc_ids.index(ids)][3]
                self.equation = dict.quicc_bubbles[quicc_ids.index(ids)][1]

                self.image = tkinter.PhotoImage(file=resource_path("alchemy_icons/Quicc_Cauldron/" + ids))
                self.label = tkinter.Label(self, image=self.image)
                self.label.grid(padx=10, pady=10 ,column=0, row=quicc_ids.index(ids))
                self.label.image = self.image

                self.customentry = CustomEntry(self, quicc_ids.index(ids), self.equation, self.x1, self.x2, self.unit)

        if cauldron == "iq":
            for ids in iq_ids:
                self.unit = dict.iq_bubbles[iq_ids.index(ids)][4]
                self.x1 = dict.iq_bubbles[iq_ids.index(ids)][2]
                self.x2 = dict.iq_bubbles[iq_ids.index(ids)][3]
                self.equation = dict.iq_bubbles[iq_ids.index(ids)][1]

                self.image = tkinter.PhotoImage(file=resource_path("alchemy_icons/High-IQ_Cauldron/" + ids))
                self.label = tkinter.Label(self, image=self.image)
                self.label.grid(padx=10, pady=10 ,column=0, row=iq_ids.index(ids))
                self.label.image = self.image

                self.customentry = CustomEntry(self, iq_ids.index(ids), self.equation, self.x1, self.x2, self.unit)
                
        if cauldron == "kazam":
            for ids in kazam_ids:
                self.unit = dict.kazam_bubbles[kazam_ids.index(ids)][4]        
                self.x1 = dict.kazam_bubbles[kazam_ids.index(ids)][2]
                self.x2 = dict.kazam_bubbles[kazam_ids.index(ids)][3]
                self.equation = dict.kazam_bubbles[kazam_ids.index(ids)][1]

                self.image = tkinter.PhotoImage(file=resource_path("alchemy_icons/Kazam_Cauldron/" + ids))
                self.label = tkinter.Label(self, image=self.image)
                self.label.grid(padx=10, pady=10 ,column=0, row=kazam_ids.index(ids))
                self.label.image = self.image

                self.customentry = CustomEntry(self, kazam_ids.index(ids), self.equation, self.x1, self.x2, self.unit)
               

class CustomEntry(tkinter.Frame):
    def __init__(self, parent, row, equation, x1, x2, unit):
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

        self.label_3 = tkinter.Label(self, text="")
        self.label_3.grid(column=5, row=0, padx=10)
        self.level_1.set(0)
        self.level_2.set(0)
        self.level_1.trace_add('write', self.callback)
        self.level_2.trace_add('write', self.callback)


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