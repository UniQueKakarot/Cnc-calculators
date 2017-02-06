from tkinter import *
import tkinter as tk
from tkinter import ttk
from math import sin, degrees

# Create instance
win = tk.Tk()

# Add a title
win.title("Maskinerings kalkulatorer")
win.geometry("350x280")
win.iconbitmap(r'Test.ico')

#add a menu bar
#menuBar = Menu(win)
#win.config(menu = menuBar)

#fileMenu = Menu(menuBar)
#fileMenu.add_command(label="New")
#menuBar.add_cascade(label="File", menu=fileMenu)

#optionsMenu = Menu(menuBar)
#optionsMenu.add_command(label="Secret")
#menuBar.add_cascade(label="Options", menu=optionsMenu)


#aboutMenu = Menu(menuBar)
#aboutMenu.add_command(label="About")
#menuBar.add_cascade(label="About", menu=aboutMenu)

#Font controll
FONT1 = ("Verdana", 10)

tabControl = ttk.Notebook(win)

class Tab1():

    def __init__(self):

        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text='Skjærdata')
        tabControl.pack(expand=1, fill="both")

        self.cutting = ttk.LabelFrame(self.tab1, text="Skjærdata Kalkulator")
        self.cutting.pack(expand=1)#grid(row=0, column=0)

        self.cutt()


    def cutt(self):
        """Skjærdata kalkulator"""
        # empty label for formating
        Label(self.cutting).grid(row = 1, column = 0, sticky=N)

        # create label and entry for cutting meter
        Label(self.cutting, text = "Skjærhastighet:", font=FONT1).grid(row = 2, column = 0, sticky=W)

        self.cutting_meter = ttk.Entry(self.cutting)
        self.cutting_meter.grid(row = 2, column = 1, sticky=N)

        #Label(self.cutting, text = "Mm/Min").grid(row = 2, column = 2, sticky=W)

        # create label and entry for diameter on your mill
        Label(self.cutting, text = "Fres diameter:", font=FONT1).grid(row = 3, column = 0, sticky=W)

        self.dia = ttk.Entry(self.cutting)
        self.dia.grid(row = 3, column = 1, sticky=N)

        # create label and entry for number of teeth
        Label(self.cutting, text = "Antall skjær:", font=FONT1).grid(row = 4, column = 0, sticky=W)

        self.teeth = ttk.Entry(self.cutting)
        self.teeth.grid(row = 4, column = 1, sticky=N)


        # create label and entry for feed per tooth
        tk.Label(self.cutting, text = "Mating pr tann:", font=FONT1).grid(row = 5, column = 0, sticky=W)

        self.feed_tooth = ttk.Entry(self.cutting)
        self.feed_tooth.grid(row = 5, column = 1, sticky=N)

        #labels for the results
        tk.Label(self.cutting, text = "Spindelhastighet:", font=FONT1).grid(row = 7, column = 0, sticky=W)

        tk.Label(self.cutting, text = "Mating:", font=FONT1).grid(row = 8, column = 0, sticky=W)

        # creating entries for the information that i need

        # Button for doing the calc
        self.calculate = ttk.Button(self.cutting, text = "Kalkuler!", command = self.calc)
        self.calculate.grid(row = 6, column = 1, columnspan = 2, sticky=N, pady=10)

        # creating text box for displaying the result
        self.result = Text(self.cutting, width = 5, height = 1)
        self.result.grid(row = 7, column = 1, columnspan = 2, sticky=N)

        self.result1 = Text(self.cutting, width = 5, height = 1)
        self.result1.grid(row = 8, column = 1, columnspan = 2, sticky=N)

    def calc(self):

        """Doing all the maths"""

        try:
            # calculation for cutting meter
            pi = float(3.14)

            x = int(1000)

            v = self.cutting_meter.get()
            v = int(v)


            d = self.dia.get()
            d = d.replace(',' , '.')
            d = float(d)

            self.spindel_speed = (float(v) * x) / (pi * float(d))

            #calculation for feed per tooth
            f = self.feed_tooth.get()
            f = f.replace(',' , '.')
            f = float(f)

            t = self.teeth.get()
            t = int(t)

            s = self.spindel_speed
            s = int(s)

            self.feed_per_tooth = f * t * s

            spindel = self.spindel_speed
            feed = self.feed_per_tooth

            spindel = int(spindel)
            feed = int(feed)

            self.result.delete(0.0, END)
            self.result.insert(0.0, spindel)

            self.result1.delete(0.0, END)
            self.result1.insert(0.0, feed)

        except(ValueError):
            pass




class Tab2():

    def __init__(self):

        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text='Spiral')
        tabControl.pack(expand=1, fill="both")

        self.spiral = ttk.LabelFrame(self.tab2, text="Spiral Kalkulator")
        self.spiral.pack(expand=1)#grid(row=0, column=0)

        self.SPIRAL()

    def SPIRAL(self):
        """Spiral Kalkulator"""
        # empty label for formating
        Label(self.spiral).grid(row = 1, column = 0, sticky=N, pady=10)

        Label(self.spiral, text = "Diameter på Fres:", font=FONT1).grid(row = 2, column = 0, sticky=N)
        self.dia_mill = ttk.Entry(self.spiral)
        self.dia_mill.grid(row = 2, column = 1, sticky = W)

        Label(self.spiral, text = "Diameter på hull:", font=FONT1).grid(row = 3, column = 0, sticky=N)
        self.dia_hole = ttk.Entry(self.spiral)
        self.dia_hole.grid(row = 3, column = 1, sticky = W)

        Label(self.spiral, text = "Step/Pitch:", font=FONT1).grid(row = 4, column = 0, sticky=N)
        self.step_pitch = ttk.Entry(self.spiral)
        self.step_pitch.grid(row = 4, column = 1, sticky = W)

        self.calculate = ttk.Button(self.spiral, text = "Kalkuler!", command = self.DOIT)
        self.calculate.grid(row = 5, column = 1, columnspan = 2, sticky=N, pady=20)

        Label(self.spiral, text = "Vinkel:", font=FONT1).grid(row = 6, column = 0, sticky=N)
        self.angle = tk.Text(self.spiral, width = 5, height = 1)
        self.angle.grid(row = 6, column = 1, columnspan = 2, sticky=W)

    def DOIT(self):
        """Calculate the angle of your spiral"""

        try:

            dia_fres = self.dia_mill.get()
            dia_fres = dia_fres.replace(',' , '.')
            dia_fres = float(dia_fres)

            dia_hull = self.dia_hole.get()
            dia_hull = dia_hull.replace(',' , '.')
            dia_hull = float(dia_hull)

            z_step = self.step_pitch.get()
            z_step = z_step.replace(',' , '.')
            z_step = float(z_step)

            omkrets = (dia_hull - dia_fres) * 3.14

            #print(omkrets)

            vinkel = (sin(1.57079633) * z_step) / omkrets

            #print(vinkel)

            vinkel = degrees(vinkel)

            #print(vinkel)

            self.angle.delete(0.0, END)
            self.angle.insert(0.0, vinkel)

        except(ValueError):
            pass


class Tab3():

    def __init__(self):

        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text='Periferi')
        tabControl.pack(expand=1, fill="both")

        self.peri = ttk.LabelFrame(self.tab3, text="Periferi Mating Kalkulator")
        self.peri.pack(expand=1)

        self.PERIFERI()
        self.radCall()

    def PERIFERI(self):

        Label(self.peri, text="Mating:", font=FONT1).grid(row=1, column=0, sticky=W)
        self.Vfm = ttk.Entry(self.peri)
        self.Vfm.grid(row = 1, column = 1, sticky = W)

        Label(self.peri, text="Diameter på Hull:", font=FONT1).grid(row=2, column=0, sticky=W)
        self.Dm = ttk.Entry(self.peri)
        self.Dm.grid(row = 2, column = 1, sticky = W)

        Label(self.peri, text="Diameter på Fres:", font=FONT1).grid(row=3, column=0, sticky=W)
        self.Dcap = ttk.Entry(self.peri)
        self.Dcap.grid(row = 3, column = 1, sticky = W)

        self.radVar = IntVar()

        self.rad1 = ttk.Radiobutton(self.peri, text="Innvendig", variable=self.radVar, value=1, command=self.radCall)
        self.rad1.grid(column=0, row=4, sticky=W)

        self.rad2 = ttk.Radiobutton(self.peri, text="Utvendig", variable=self.radVar, value=2, command=self.radCall)
        self.rad2.grid(column=1, row=4, sticky=W)


    def radCall(self):
        """Event handler for radiobuttons"""

        radSel = self.radVar.get()

        if   radSel == 1:
            self.calculate = ttk.Button(self.peri, text = "Kalkuler!", command = self.JUSTDOIT_INSIDE)
            self.calculate.grid(row = 5, column = 1, columnspan = 2, sticky=N, pady=10)

            Label(self.peri, text = "Periferimating Innvendig:", font=FONT1).grid(row = 6, column = 0, sticky=N)
            self.perif = tk.Text(self.peri, width = 5, height = 1)
            self.perif.grid(row = 6, column = 1, columnspan = 2, sticky=W)

        elif radSel == 2:
            self.calculate = ttk.Button(self.peri, text = "Kalkuler!", command = self.JUSTDOIT_OUTSIDE)
            self.calculate.grid(row = 5, column = 1, columnspan = 2, sticky=N, pady=10)

            Label(self.peri, text = "Periferimating Utvendig:", font=FONT1).grid(row = 6, column = 0, sticky=N)
            self.perif = tk.Text(self.peri, width = 5, height = 1)
            self.perif.grid(row = 6, column = 1, columnspan = 2, sticky=W)



    def JUSTDOIT_INSIDE(self):
        """Calculations for periferi feed inside circular ramping"""

        try:

            Vfm = self.Vfm.get()
            Vfm = int(Vfm)

            Dm = self.Dm.get()
            Dm = Dm.replace(',' , '.')
            Dm = float(Dm)

            Dcap = self.Dcap.get()
            Dcap = Dcap.replace(',' , '.')
            Dcap = float(Dcap)

            Vf = (Vfm * (Dm + Dcap)) / Dm
            Vf = int(Vf)

            self.perif.delete(0.0, END)
            self.perif.insert(0.0, Vf)

        except(ValueError):
            pass



    def JUSTDOIT_OUTSIDE(self):
        """Calculations for periferi feed outside circular ramping"""

        try:

            Vfm = self.Vfm.get()
            Vfm = int(Vfm)

            Dm = self.Dm.get()
            Dm = Dm.replace(',' , '.')
            Dm = float(Dm)

            Dcap = self.Dcap.get()
            Dcap = Dcap.replace(',' , '.')
            Dcap = float(Dcap)

            Vf = (Vfm * (Dm - Dcap)) / Dm
            Vf = int(Vf)

            self.perif.delete(0.0, END)
            self.perif.insert(0.0, Vf)

        except(ValueError):
            pass





#main

test = Tab1()
test2 = Tab2()
test3 = Tab3()


win.mainloop()
