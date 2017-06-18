# coding: cp865

from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import math


#win = Tk()
#win.geometry("600x480")


global PI
global STèL
PI = math.pi
STèL = 7.85 #g/kubikkcm

FONT1 = ("Calibri", 11)
FONT2 = ("Calibri", 11, "bold", "underline")

uiUtboring1 = []
uiUtboring2 = []

uiGjennomgÜendehull1 = []
uiGjennomgÜendehull2 = []

uiFirkant = []
uiRundt = []

class Vekt():
    
    def __init__(self, master, tab):
        
        self.master = master
        self.tab = tab

        self.tab6 = ttk.Frame(self.tab)
        
        self.tab.add(self.tab6, text='Vekt ')
        self.tab.configure(takefocus=0)
        self.tab.pack(expand=1, fill="both")       
        
        self.vekt = ttk.LabelFrame(self.tab6, text="Vekt og Vektfordeling")
        self.vekt.grid(row=1, column=0, sticky=S, padx=60, pady=20)
        
        self.hovedkropp()
        self.RadEvent()


    def hovedkropp(self):
        """Hoveddelen av fanen kommer her"""
        
        self.radVar = IntVar()
    
        self.arb1 = ttk.Radiobutton(self.vekt, text="Rund arbeidsbit", variable=self.radVar, value=1, command=self.RadEvent, takefocus=0)
        self.arb1.grid(row=1, column=0, sticky=W, pady=1)
    
        self.arb2 = ttk.Radiobutton(self.vekt, text="Firkantet arbeidsbit", variable=self.radVar, value=2, command=self.RadEvent, takefocus=0)
        self.arb2.grid(row=1, column=1, sticky=W, pady=1)
        
        self.radVar.set(1)
        
    def RadEvent(self):
        """HÜndtering av hva Radioknappene skal gjõre"""
        
        radSel = self.radVar.get()
        
        if radSel == 1: #Layouten for rund arbeidsbit kommer under her

            self.lbl1 = Label(self.vekt, text="Diameter:", font=FONT1)
            self.lbl1.grid(row=3, column=0, sticky=W)
            self.lbl2 = Label(self.vekt, text="Lengde i MM:", font=FONT1)
            self.lbl2.grid(row=4, column=0, sticky=W)
            self.lbl3 = Label(self.vekt)
            self.lbl3.grid(row=5, column=0, sticky=W)            
            
            self.dia = ttk.Entry(self.vekt)
            self.dia.grid(row=3, column=1, sticky=N)
            self.length = ttk.Entry(self.vekt)
            self.length.grid(row=4, column=1, sticky=N)
            
            self.checkVar = IntVar()
            self.checkVar2 = IntVar()
            
            self.kalk()
            self.uiDelete()
            
            self.check = Checkbutton(self.vekt, text="Utborring?", var=self.checkVar, command=self.checkEvent2, takefocus=0)
            self.check.grid(row=2, column=0, sticky=W, pady=10)
            self.check2 = Checkbutton(self.vekt, text="GjennomgÜende hull?", var=self.checkVar2, command=self.checkEvent, takefocus=0)
            self.check2.grid(row=2, column=1, sticky=W, pady=10)
            
            uiFirkant.append(self.lbl1)
            uiFirkant.append(self.lbl2)
            uiFirkant.append(self.lbl3)
            uiFirkant.append(self.dia)
            uiFirkant.append(self.length)
            uiFirkant.append(self.check)
            uiFirkant.append(self.check2)
            


        elif radSel == 2: #Layouten for firkantet arbeidsbit kommer under her

            self.lbl4 = Label(self.vekt, text="Lengde:", font=FONT1)
            self.lbl4.grid(row=2, column=0, pady=1, sticky=W)
            self.lbl5 = Label(self.vekt, text="Bredde:", font=FONT1)
            self.lbl5.grid(row=3, column=0, pady=1, sticky=W)
            self.lbl6 = Label(self.vekt, text="Hõyde:", font=FONT1)
            self.lbl6.grid(row=4, column=0, sticky=W)
            self.lbl7 = Label(self.vekt)
            self.lbl7.grid(row=5, column=0, sticky=W)
            
            self.lengde = ttk.Entry(self.vekt)
            self.lengde.grid(row=2, column=1, sticky=N)
            self.bredde = ttk.Entry(self.vekt)
            self.bredde.grid(row=3, column=1, sticky=N)
            self.hõyde = ttk.Entry(self.vekt)
            self.hõyde.grid(row=4, column=1, sticky=N)
            
            self.butt1 = Button(self.vekt, text="Kalkuler!", command=self.kubeKalk)
            self.butt1.grid(row=5, column=1, sticky=N, pady=10)
            
            self.lbl8 = Label(self.vekt)
            self.lbl8.grid(row=6, column=0, columnspan=2, sticky=W)
            #self.lbl9 = Label(self.vekt)
            #self.lbl9.grid(row=7, column=0, columnspan=2, sticky=W)
            
            uiRundt.append(self.lbl4)
            uiRundt.append(self.lbl5)
            uiRundt.append(self.lbl6)
            uiRundt.append(self.lbl7)
            uiRundt.append(self.lengde)
            uiRundt.append(self.bredde)
            uiRundt.append(self.hõyde)
            uiRundt.append(self.butt1)
            uiRundt.append(self.lbl8)
            
            self.uiDelete()
            
     
    def kubeKalk(self):
        
        try:
            lengde = self.lengde.get()
            lengde = lengde.replace(',' , '.')
            lengde = float(lengde)
            
            bredde = self.bredde.get()
            bredde = bredde.replace(',' , '.')
            bredde = float(bredde)
            
            hõyde = self.hõyde.get()
            hõyde = hõyde.replace(',' , '.')
            hõyde = float(hõyde)
            
            volum = lengde * bredde * hõyde
            volum = volum / 1000
            
            vekt1 = volum * STèL
            vekt1 = vekt1 / 1000
            vekt1 = int(vekt1)
            
            vekt1 = str(vekt1)
        except(ValueError, ZeroDivisionError):
            pass
        
        
        self.lbl8.configure(text="Vekten er: " + vekt1 + "kg", font=FONT2)
        #self.lbl9.configure(text="Vektsentret er i senter av arbeidsbiten", font=FONT2)
         
         
     
     
     
     
            
    def checkEvent(self):
        """HÜndterer hva som skjer nÜr du velger GjennomgÜende hull boksen her"""
        
        checkSel2 = self.checkVar2.get()

        if checkSel2 == 1:
            
            self.lbl20 = Label(self.vekt, text="GjennomgÜende Hull:", font=FONT2)
            self.lbl20.grid(row=10, column=0, sticky=W, pady=5)
            self.lbl21 = Label(self.vekt, text="Diameter:", font=FONT1)
            self.lbl21.grid(row=11, column=0, sticky=W)           
            
            self.dia2 = ttk.Entry(self.vekt)
            self.dia2.grid(row=11, column=1, sticky=N)
            
            uiGjennomgÜendehull2.append(self.lbl20)
            uiGjennomgÜendehull2.append(self.lbl21)
            uiGjennomgÜendehull2.append(self.dia2)
            
            uiFirkant.append(self.lbl20)
            uiFirkant.append(self.lbl21)
            uiFirkant.append(self.dia2)
            
            self.kalk()
            self.uiDelete()
            
            
        else: #checkSel2 == 0:

            self.kalk()
            self.uiDelete()
            
            
    def checkEvent2(self):
        """HÜndterer hva som skjer nÜr du velger Utborrings boksen her"""
        
        checkSel = self.checkVar.get()

        if checkSel == 1:
            
            self.lbl33 = Label(self.vekt)
            self.lbl33.grid(row=20, column=0, sticky=W)
            self.lbl30 = Label(self.vekt, text="Utborring:", font=FONT2)
            self.lbl30.grid(row=21, column=0, sticky=W, pady=5)
            self.lbl31 = Label(self.vekt, text="Diameter pÜ Utborring:", font=FONT1)
            self.lbl31.grid(row=22, column=0, sticky=W, pady=1)
            self.lbl32 = Label(self.vekt, text="Lengde pÜ utborring:", font=FONT1)
            self.lbl32.grid(row=23, column=0, sticky=W)
            
            self.dia3 = ttk.Entry(self.vekt)
            self.dia3.grid(row=22, column=1, sticky=N, pady=1)
            self.lengde1 = ttk.Entry(self.vekt)
            self.lengde1.grid(row=23, column=1, sticky=N)
            
            uiUtboring2.append(self.lbl30)
            uiUtboring2.append(self.lbl31)
            uiUtboring2.append(self.lbl32)
            uiUtboring2.append(self.lbl33)
            uiUtboring2.append(self.dia3)
            uiUtboring2.append(self.lengde1)
            
            uiFirkant.append(self.lbl30)
            uiFirkant.append(self.lbl31)
            uiFirkant.append(self.lbl32)
            uiFirkant.append(self.lbl33)
            uiFirkant.append(self.dia3)
            uiFirkant.append(self.lengde1)
            
            self.kalk()
            self.uiDelete()
            

        else: #checkSel == 0:
            
            self.kalk()
            self.uiDelete()
            
            
    def kalk(self):
        
        checkSel = self.checkVar.get()
        checkSel1 = self.checkVar2.get()
        #checkSel2 = self.radVar.get()
        
        if checkSel == 0 and checkSel1 == 0: #Ren stang

            self.butt = Button(self.vekt, text="Kalkuler!", command=self.Vekt_Stang)
            self.butt.grid(row=6, column=1, sticky=N, pady=10)
            self.lbl40 = Label(self.vekt)
            self.lbl40.grid(row=7, column=0, columnspan=2, sticky=W)
            self.lbl41 = Label(self.vekt)
            self.lbl41.grid(row=8, column=0, columnspan=2, sticky=W)
            
            uiUtboring1.append(self.lbl40)
            uiUtboring1.append(self.lbl41)
            uiUtboring1.append(self.butt)
            
            uiGjennomgÜendehull1.append(self.lbl40)
            uiGjennomgÜendehull1.append(self.lbl41)
            uiGjennomgÜendehull1.append(self.butt)
            
            uiFirkant.append(self.butt)
            uiFirkant.append(self.lbl40)
            uiFirkant.append(self.lbl41)
            

            
        elif checkSel == 1 and checkSel1 == 0: #Utboring         
            self.butt = Button(self.vekt, text="Kalkuler!", command=self.Vekt_Stang_Utbor)
            self.butt.grid(row=24, column=1, sticky=N, pady=10)
            self.lbl50 = Label(self.vekt)
            self.lbl50.grid(row=25, column=0, columnspan=2, sticky=W)
            self.lbl51 = Label(self.vekt)
            self.lbl51.grid(row=26, column=0, columnspan=2, sticky=W)
            
            uiUtboring2.append(self.lbl50)
            uiUtboring2.append(self.lbl51)
            uiUtboring2.append(self.butt)
            
            uiGjennomgÜendehull1.append(self.lbl50)
            uiGjennomgÜendehull1.append(self.lbl51)
            uiGjennomgÜendehull1.append(self.butt)
            
            uiFirkant.append(self.butt)
            uiFirkant.append(self.lbl50)
            uiFirkant.append(self.lbl51)
            

            
        elif checkSel == 0 and checkSel1 == 1: #GjennomgÜende hull
            self.butt = Button(self.vekt, text="Kalkuler!", command=self.Vekt_Stang_Gjenhull)
            self.butt.grid(row=12, column=1, sticky=N, pady=10)
            self.lbl42 = Label(self.vekt)
            self.lbl42.grid(row=13, column=0, columnspan=2, sticky=W)
            self.lbl43 = Label(self.vekt)
            self.lbl43.grid(row=14, column=0, columnspan=2, sticky=W)
            
            uiUtboring1.append(self.lbl42)
            uiUtboring1.append(self.lbl43)
            uiUtboring1.append(self.butt)
            
            
            uiGjennomgÜendehull2.append(self.lbl42)
            uiGjennomgÜendehull2.append(self.lbl43)
            uiGjennomgÜendehull2.append(self.butt)
            
            uiFirkant.append(self.butt)
            uiFirkant.append(self.lbl42)
            uiFirkant.append(self.lbl43)
            

            
        else: #GjennomgÜende hull og utborring
            self.butt = Button(self.vekt, text="Kalkuler!", command=self.Vekt_Stang_Utbor_og_Gjenhull)
            self.butt.grid(row=24, column=1, sticky=N, pady=10)
            self.lbl60 = Label(self.vekt)
            self.lbl60.grid(row=27, column=0, columnspan=2, sticky=W)
            self.lbl61 = Label(self.vekt)
            self.lbl61.grid(row=28, column=0, columnspan=2, sticky=W)
            
            uiUtboring2.append(self.lbl60)
            uiUtboring2.append(self.lbl61)
            uiUtboring2.append(self.butt)
            
            uiGjennomgÜendehull2.append(self.lbl60)
            uiGjennomgÜendehull2.append(self.lbl61)
            uiGjennomgÜendehull2.append(self.butt)
            
            uiFirkant.append(self.butt)
            uiFirkant.append(self.lbl60)
            uiFirkant.append(self.lbl61)
                      
            
            
    def Vekt_Stang(self):
        """Beregninger av vekt av ei ren stang kommer her"""
        try:
            r = self.dia.get()
            r = r.replace(',' , '.')
            r = float(r)
            r = r / 2
            r = r**2
            
            h = self.length.get()
            h = h.replace(',' , '.')
            h = float(h)
            
            l = h / 2
            l = int(l)
            
            l = str(l)
            
            
            v = PI * r * h
            v = v / 1000
            
            vekt = STèL * v
            vekt = vekt / 1000
            vekt = int(vekt)
            
            vekt = str(vekt)
        except(ValueError, ZeroDivisionError):
            pass
        
        self.lbl40.configure(text="Biten veier: " + vekt + "kg", font=FONT2)
        self.lbl41.configure(text="Vektsentrum er: " + l + "mm fra en av sidene", font=FONT2)
        
    def Vekt_Stang_Gjenhull(self):
        """Beregninger av vekt for stang med gjennomgÜende hull"""
        try:
            r = self.dia.get()
            r = r.replace(',' , '.')
            r = float(r)
            r = r / 2
            r = r**2
            
            r2 = self.dia2.get()
            r2 = r2.replace(',' , '.')
            r2 = float(r2)
            r2 = r2 / 2
            r2 = r2**2
            
            h = self.length.get()
            h = h.replace(',' , '.')
            h = float(h)
        
            l = h / 2
            l = int(l)
        
            l = str(l)
            
            v1 = PI * r * h
            
            v2 = PI * r2 * h
            
            v1 = v1 / 1000
            
            v2 = v2 / 1000
            
            vekt1 = STèL * v1
            vekt1 = vekt1 / 1000
            vekt1 = int(vekt1)
            
            vekt2 = STèL * v2
            vekt2 = vekt2 / 1000
            vekt2 = int(vekt2)
            
            slutt_vekt = vekt1 - vekt2
            slutt_vekt = str(slutt_vekt)
        except(ValueError, ZeroDivisionError):
            pass
        
        
        self.lbl42.configure(text="Biten veier: " + slutt_vekt + "kg", font=FONT2)
        self.lbl43.configure(text="Vektsentrum er: " + l + "mm fra en av sidene", font=FONT2)
        
    def Vekt_Stang_Utbor(self):
        """Beregning av vekt for stang med utborring kommer her"""
        try:
            #Ren stang
            r = self.dia.get()
            r = r.replace(',' , '.')
            r = float(r)
            r = r / 2
            r = r**2
            
            
            
            #Lengde pÜ ren stang
            h = self.length.get()
            h = h.replace(',' , '.')
            h = float(h)
            
            
            
            #Utborring
            r3 = self.dia3.get()
            r3 = r3.replace(',' , '.')
            r3 = float(r3)
            r3 = r3 / 2
            r3 = r3**2
            
            
            
            #Lengde pÜ utborring
            h1 = self.lengde1.get()
            h1 = h1.replace(',' , '.')
            h1 = float(h1)
            
            
            
            #Volum av ren stang i kubikk millimeter
            v1 = PI * r * h
            
            #Omregning til Kubikk Centimeter
            v1 = v1 / 1000
            
            #Omregning til kilo
            vekt1 = STèL * v1
            vekt1 = vekt1 / 1000
            
            #Volum av utborring i kubikk millimeter
            v3 = PI * r3 * h1
            
            #Omregning til kubikk centimeter
            v3 = v3 / 1000
            
            #Omregining til kilo
            vekt3 = STèL * v3
            vekt3 = vekt3 / 1000
            
            #Totalvekt med gjennomgÜende hull trekt ifra
            tot_vekt = vekt1 - vekt3   
            
            #Beregninger angÜende vektsenter pÜ bit med utborring kommer her
            
            D = h / h1
            
            Ve = vekt1 / D
            
            Vk = Ve - vekt3
            
            Vs = vekt1 - Ve
            
            x = (Vk + Vs) / (2 * Vs)
            
            a = x * (h - h1)
            
            
            tot_vekt = int(tot_vekt)
            tot_vekt = str(tot_vekt)
            
            a = int(a)
            a = str(a)
        except(ValueError, ZeroDivisionError):
            pass
        
        self.lbl50.configure(text="Total vekt: " + tot_vekt + "kg", font=FONT2)
        self.lbl51.configure(text="Vektsenter er : " + a + " mm fra uborret side", font=FONT2)
            
    def Vekt_Stang_Utbor_og_Gjenhull(self):
        """Beregning av vekt for stang med utborring og gjennomgÜende hull kommer her"""

        try:      
            #Ren stang
            r = self.dia.get()
            r = r.replace(',' , '.')
            r = float(r)
            r = r / 2
            r = r**2           
            
            #Lengde pÜ ren stang
            h = self.length.get()
            h = h.replace(',' , '.')
            h = float(h)
            
            #GjennomgÜende Hull
            r2 = self.dia2.get()
            r2 = r2.replace(',' , '.')
            r2 = float(r2)
            r2 = r2 / 2
            r2 = r2**2
            
            #Utborring
            r3 = self.dia3.get()
            r3 = r3.replace(',' , '.')
            r3 = float(r3)
            r3 = r3 / 2
            r3 = r3**2
            
            #Lengde pÜ utborring
            h1 = self.lengde1.get()
            h1 = h1.replace(',' , '.')
            h1 = float(h1)
            
            #Volum av ren stang i kubikk millimeter
            v1 = PI * r * h
            
            #Omregning til Kubikk Centimeter
            v1 = v1 / 1000
            
            #Omregning til kilo
            vekt1 = STèL * v1
            vekt1 = vekt1 / 1000
            
            #Volum av gjennomgÜende hull i kubikk millimeter
            v2 = PI * r2 * h
            
            #Omregning til kubikk Centimeter
            v2 = v2 / 1000           
            
            #Omregning til kilo
            vekt2 = STèL * v2
            vekt2 = vekt2 / 1000
            
            #Volum av utborring i kubikk millimeter
            v3 = PI * r3 * h1
            
            #Omregning til kubikk centimeter
            v3 = v3 / 1000
            
            #Omregining til kilo
            vekt3 = STèL * v3
            vekt3 = vekt3 / 1000
            
            #Totalvekt med gjennomgÜende hull trekt ifra
            tot_uten_utbor = vekt1 - vekt2
            tot_vekt = vekt1 - vekt2 - vekt3
            
            
            #Beregninger angÜende vektsenter pÜ bit med utborring kommer her
            
            D = h / h1
            
            Ve = tot_uten_utbor / D
            
            Vk = Ve - vekt3
            
            Vs = tot_uten_utbor - Ve
            
            x = (Vk + Vs) / (2 * Vs)
            
            a = x * (h - h1)
            
            
            tot_vekt = int(tot_vekt)
            tot_vekt = str(tot_vekt)
            
            a = int(a)
            a = str(a)
        except(ValueError, ZeroDivisionError):
            pass
        
        
        try:
            self.lbl60.configure(text="Total vekt: " + tot_vekt + "kg", font=FONT2)
            self.lbl61.configure(text="Vektsenter er : " + a + " mm fra uborret side", font=FONT2)
        except(TypeError):
            pass
        
        
    def uiDelete(self):
        radSel = self.radVar.get()
        checkSel = self.checkVar.get()
        checkSel1 = self.checkVar2.get()
        
        ####################################################################
        # Sletter alle UI element som ikke har noe med utborringen Ü gjõre #
        ####################################################################
            
        if checkSel == 1:
            for i in uiUtboring1:
                i.destroy()
        else:
            for i in uiUtboring2:
                i.destroy()
                    
        #######################################################################
        # Sletter alle UI element som ikke har med gjennomgÜende hull Ü gjõre #
        #######################################################################
        
        if checkSel1 == 1:
            for i in uiGjennomgÜendehull1:
                i.destroy()
                    
        else:
            for i in uiGjennomgÜendehull2:
                i.destroy()
                
        ####################################################################################
        # Sletter alle UI element som ikke har med firkantet emne eller rundt emne Ü gjõre #
        ####################################################################################
        
        if radSel == 2:
            for i in uiFirkant:
                i.destroy()
                
        else:
            for i in uiRundt:
                i.destroy()

            
    


#vekt = Vekt(win)
#win.mainloop()
