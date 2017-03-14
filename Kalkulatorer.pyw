from tkinter import *
import tkinter as tk
from tkinter import ttk
from math import sin, degrees

# Create instance
win = tk.Tk()

# Add a title
win.title("Maskinerings kalkulatorer")
win.geometry("400x280")
#win.iconbitmap(r'Test.ico')


#Font controll
FONT1 = ("Verdana", 10)

tabControl = ttk.Notebook(win)

class Tab1(): #Skjærdata kalkulator for fresing

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

            self.result.config(state=NORMAL)
            self.result.delete(0.0, END)
            self.result.insert(0.0, spindel)
            self.result.config(state=DISABLED)

            self.result1.config(state=NORMAL)
            self.result1.delete(0.0, END)
            self.result1.insert(0.0, feed)
            self.result1.config(state=DISABLED)

        except(ValueError):
            pass




class Tab2(): #Grad av sprial kalkulator

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

            self.angle.config(state=NORMAL)
            self.angle.delete(0.0, END)
            self.angle.insert(0.0, vinkel)
            self.angle.config(state=DISABLED)

        except(ValueError):
            pass


class Tab3(): #Periferimating kalkulator

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

        Label(self.peri, text="Diameter på Fres:", font=FONT1).grid(row=2, column=0, sticky=W)
        self.Dcap = ttk.Entry(self.peri)
        self.Dcap.grid(row = 2, column = 1, sticky = W)

        Label(self.peri, text="Diameter på Hull:", font=FONT1).grid(row=3, column=0, sticky=W)
        self.Dm = ttk.Entry(self.peri)
        self.Dm.grid(row = 3, column = 1, sticky = W)

        self.radVar = IntVar()

        self.rad1 = ttk.Radiobutton(self.peri, text="MM/Min Yttre Skjærkant", variable=self.radVar, value=1, command=self.radCall)
        self.rad1.grid(column=0, row=4, sticky=W)

        self.rad2 = ttk.Radiobutton(self.peri, text="MM/Min Indre Skjærkant", variable=self.radVar, value=2, command=self.radCall)
        self.rad2.grid(column=1, row=4, sticky=W)

        self.radVar.set(1)


    def radCall(self):
        """Event handler for radiobuttons"""

        radSel = self.radVar.get()

        if   radSel == 1:
            self.calculate = ttk.Button(self.peri, text = "Kalkuler!", command = self.JUSTDOIT_INSIDE)
            self.calculate.grid(row = 5, column = 1, columnspan = 2, sticky=N, pady=10)

            Label(self.peri, text = "Periferimating Yttre Skjærkant:", font=FONT1).grid(row = 6, column = 0, sticky=N)
            self.perif = tk.Text(self.peri, width = 5, height = 1)
            self.perif.grid(row = 6, column = 1, columnspan = 2, sticky=W)

        elif radSel == 2:
            self.calculate = ttk.Button(self.peri, text = "Kalkuler!", command = self.JUSTDOIT_OUTSIDE)
            self.calculate.grid(row = 5, column = 1, columnspan = 2, sticky=N, pady=10)

            Label(self.peri, text = "Periferimating Indre Skjærkant:", font=FONT1).grid(row = 6, column = 0, sticky=N)
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

            self.perif.config(state=NORMAL)
            self.perif.delete(0.0, END)
            self.perif.insert(0.0, Vf)
            self.perif.config(state=DISABLED)

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

            self.perif.config(state=NORMAL)
            self.perif.delete(0.0, END)
            self.perif.insert(0.0, Vf)
            self.perif.config(state=DISABLED)

        except(ValueError):
            pass

class Tab4(): #Kalk for borring

    def __init__(self):

        self.tab4 = ttk.Frame(tabControl)
        tabControl.add(self.tab4, text='Boring')
        tabControl.pack(expand=1, fill="both")

        self.boring = ttk.LabelFrame(self.tab4, text="Skjærdatakalkulator for Boring")
        self.boring.pack(expand=1)

        self.structure()
        self.radCall()

    def structure(self):
        """Skjærdata kalkulator"""

        self.radVar = IntVar()


        self.rad1 = ttk.Radiobutton(self.boring, text="MM/Min", variable=self.radVar, value=1, command=self.radCall)
        self.rad1.grid(column=0, row=1, sticky=W)

        self.rad2 = ttk.Radiobutton(self.boring, text="MM/Omdreiing", variable=self.radVar, value=2, command=self.radCall)
        self.rad2.grid(column=1, row=1, sticky=W)


        self.radVar.set(1)



        # create label and entry for cutting meter
        Label(self.boring, text = "Skjærhastighet:", font=FONT1).grid(row = 2, column = 0, sticky=W)

        self.cutting_meter = ttk.Entry(self.boring)
        self.cutting_meter.grid(row = 2, column = 1, sticky=N)

        #Label(self.boring, text = "Mm/Min").grid(row = 2, column = 2, sticky=W)

        # create label and entry for diameter on your mill
        Label(self.boring, text = "Bor diameter:", font=FONT1).grid(row = 3, column = 0, sticky=W)

        self.dia = ttk.Entry(self.boring)
        self.dia.grid(row = 3, column = 1, sticky=N)

    def radCall(self):
        """Event handler for radiobuttons"""

        radSel = self.radVar.get()

        if   radSel == 1: #MM/Min

            # create label and entry for feed per tooth
            Label(self.boring, text = "Mating pr tann:      ", font=FONT1).grid(row = 4, column = 0, sticky=W)

            self.feed_tooth = ttk.Entry(self.boring)
            self.feed_tooth.grid(row = 4, column = 1, sticky=N)

            #labels for the results
            Label(self.boring, text = "Spindelhastighet:", font=FONT1).grid(row = 7, column = 0, sticky=W)
            Label(self.boring, text = "Mating:                   ", font=FONT1).grid(row = 8, column = 0, sticky=W)

            # Button for doing the calc
            self.calculate = ttk.Button(self.boring, text = "Kalkuler!", command = self.calc1)
            self.calculate.grid(row = 6, column = 1, columnspan = 2, sticky=N, pady=10)

            # creating text box for displaying the result
            self.result = Text(self.boring, width = 5, height = 1)
            self.result.grid(row = 7, column = 1, columnspan = 2, sticky=N)

            self.result1 = Text(self.boring, width = 5, height = 1)
            self.result1.grid(row = 8, column = 1, columnspan = 2, sticky=N)

        elif radSel == 2: #MM/Omdreiing

            Label(self.boring, text="Mating MM/Min:", font=FONT1).grid(row=4, column=0, sticky=W)

            self.feed_per_rev = ttk.Entry(self.boring)
            self.feed_per_rev.grid(row = 4, column = 1, sticky=N)

            #labels for the results
            Label(self.boring, text = "Spindelhastighet:", font=FONT1).grid(row = 7, column = 0, sticky=W)
            Label(self.boring, text = "Mating pr Omdreiing:", font=FONT1).grid(row = 8, column = 0, sticky=W)

            # Button for doing the calc
            self.calculate = ttk.Button(self.boring, text = "Kalkuler!", command = self.calc2)
            self.calculate.grid(row = 6, column = 1, columnspan = 2, sticky=N, pady=10)

            # creating text box for displaying the result
            self.result = Text(self.boring, width = 5, height = 1)
            self.result.grid(row = 7, column = 1, columnspan = 2, sticky=N)

            self.result1 = Text(self.boring, width = 5, height = 1)
            self.result1.grid(row = 8, column = 1, columnspan = 2, sticky=N)


    def calc1(self): #MM/Min
        "Doing all the maths here"

        try:


            #print("Welcome to funkytown")

            #Skjærdatakalkulering
            vc = self.cutting_meter.get() #Skjærmeter
            vc = int(vc)

            dc = self.dia.get() #Fres diameter
            dc = dc.replace(',' , '.')
            dc = float(dc)

            pi = float(3.14)

            n = (vc * 1000) / (pi * dc)
            n = int(n) #Spindelhastighet

            #Mating per tann kalkulering med mm/o
            fn = self.feed_tooth.get()
            fn = fn.replace(',' , '.')
            fn = float(fn)


            vf = fn * n
            vf = int(vf)

            self.result.config(state=NORMAL)
            self.result.delete(0.0, END)
            self.result.insert(0.0, n)
            self.result.config(state=DISABLED)

            self.result1.config(state=NORMAL)
            self.result1.delete(0.0, END)
            self.result1.insert(0.0, vf)
            self.result1.config(state=DISABLED)

        except(ValueError):
            pass



    def calc2(self): #MM/Omdreiing
        "Doing all the maths here"

        try:


            #print("Welcome to funkytown")

            #Skjærdatakalkulering
            vc = self.cutting_meter.get() #Skjærmeter
            vc = int(vc)

            dc = self.dia.get() #Fres diameter
            dc = dc.replace(',' , '.')
            dc = float(dc)

            pi = float(3.14)

            n = (vc * 1000) / (pi * dc)
            n = int(n) #Spindelhastighet

            #Mating per tann kalkulering med mm/o
            vf = float(self.feed_per_rev.get())


            fn = vf / n
            fn = float(fn)

            self.result.config(state=NORMAL)
            self.result.delete(0.0, END)
            self.result.insert(0.0, n)
            self.result.config(state=DISABLED)

            self.result1.config(state=NORMAL)
            self.result1.delete(0.0, END)
            self.result1.insert(0.0, fn)
            self.result1.config(state=DISABLED)

        except(ValueError):
            pass


class Tab5(): #Ra kalkulator

    def __init__(self):

        self.tab5 = ttk.Frame(tabControl)
        tabControl.add(self.tab5, text='RA')
        tabControl.pack(expand=1, fill="both")

        self.surface = ttk.LabelFrame(self.tab5, text="RA Kalkulator")
        self.surface.pack(expand=1)#grid(row=0, column=0)

        self.structure()

    def structure(self):

        Label(self.surface, text="MM/Omdreiing:", font=FONT1).grid(row=0, column=0, sticky=W)

        self.feed_revolt = ttk.Entry(self.surface)
        self.feed_revolt.grid(row=0, column=1, sticky=N)

        self.nose = StringVar(win)

        self.choices = [ '', '0.2', '0.4', '0.8', '1.2', '1.6', '2.4' ]

        self.nose.set('0.2') #Standard verdi

        Label(self.surface, text="Velg Neseradius:", font=FONT1).grid(row=1, column=0, sticky=W)

        self.popupMenu = ttk.OptionMenu(self.surface, self.nose, *self.choices)
        self.popupMenu.grid(row=1, column=1, sticky=N)

        self.calculate = ttk.Button(self.surface, text = "Kalkuler!", command = self.calculations)
        self.calculate.grid(row = 3, column = 1, columnspan = 2, sticky=N, pady=10)

        Label(self.surface, text="Kalkulert RA:", font=FONT1).grid(row=5, column=0, sticky=W)

        self.result = Text(self.surface, width = 5, height = 1)
        self.result.grid(row = 5, column = 1, columnspan = 2, sticky=N)

        #self.nose.trace('w', self.change_dropdown)

    def calculations(self):
        "Maths and stuffs"

        try:


            x = self.feed_revolt.get()
            x = x.replace(',' , '.')
            x = float(x)

            r = self.nose.get()
            r = float(r)

            ra = ((x**2) / (r*24)) * 1000

            self.result.config(state=NORMAL)
            self.result.delete(0.0, END)
            self.result.insert(0.0, ra)
            self.result.config(state=DISABLED)

            #print(ra)

        except(ValueError):
            pass



#main

skjærdata = Tab1()
spiral_kalk = Tab2()
periferi_kalk = Tab3()
boring_kalk = Tab4()
ra_kalk = Tab5()

win.mainloop()
