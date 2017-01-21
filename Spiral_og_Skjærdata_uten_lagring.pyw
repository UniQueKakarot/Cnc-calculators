
from tkinter import *
import tkinter as tk   # python3
from tkinter import ttk
from math import sin, degrees


TITLE_FONT = ("Verdana", 14)

GLOBAL_Yolo = 0

class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, Application):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#Placeholder page for now
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Skjærdata og Spiralkalkulator", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = ttk.Button(self, text="Spiral Kalkulator",
                            command=lambda: controller.show_frame("PageOne"))
        button3 = ttk.Button(self, text="Skjærdata Kalkulator",
                            command=lambda: controller.show_frame("Application"))
        button1.pack()
        button3.pack()

#Placeholder page for now
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.ramp_vinkel()
        label = tk.Label(self, text="Spiral Kalkulator")
        label.grid(row = 0, column = 0, sticky = N, pady = 10)
        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row = 8, column = 1, sticky = W, pady = 10)

    def ramp_vinkel(self):
        """Defines the window for holding the ramp angle calc"""

        Label(self).grid(row = 1, column = 1, padx = 80)

        Label(self, text = "Diameter på Fres:").grid(row = 2, column = 0, sticky=N)
        self.dia_mill = ttk.Entry(self)
        self.dia_mill.grid(row = 2, column = 1, sticky = W)

        Label(self, text = "Diameter på hull:").grid(row = 3, column = 0, sticky=N)
        self.dia_hole = ttk.Entry(self)
        self.dia_hole.grid(row = 3, column = 1, sticky = W)

        Label(self, text = "Step/Pitch:").grid(row = 4, column = 0, sticky=N)
        self.step_pitch = ttk.Entry(self)
        self.step_pitch.grid(row = 4, column = 1, sticky = W)

        self.calculate = ttk.Button(self, text = "Kalkuler!", command = self.DOIT)
        self.calculate.grid(row = 5, column = 1, columnspan = 2, sticky=N, pady=10)

        Label(self, text = "Vinkel:").grid(row = 6, column = 0, sticky=N)
        self.angle = tk.Text(self, width = 5, height = 1)
        self.angle.grid(row = 6, column = 1, columnspan = 2, sticky=W)


    def DOIT(self):
        """Calculate the angle of your spiral"""

        dia_fres = self.dia_mill.get()
        dia_fres = int(dia_fres)

        dia_hull = self.dia_hole.get()
        dia_hull = int(dia_hull)

        z_step = self.step_pitch.get()
        z_step = z_step.replace(',' , '.')
        z_step = float(z_step)

        omkrets = (dia_hull - dia_fres) * 3.14

        print(omkrets)

        vinkel = (sin(1.57079633) * z_step) / omkrets

        print(vinkel)

        vinkel = degrees(vinkel)

        print(vinkel)

        self.angle.delete(0.0, END)
        self.angle.insert(0.0, [vinkel])




#Cutting data calculator frame
class Application(tk.Frame):
    """GUI Application for the cuttingspeed calculator"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid()
        self.create_widget()

        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=9, column=1, sticky=N, pady=10)

    def create_widget(self):
        """Creates widgets for the calculator"""
        # create description label
        tk.Label(self, text = "Skjærdata Kalkulator").grid(row = 0, column = 1, sticky=N)

        # empty label for formating
        tk.Label(self).grid(row = 1, column = 0, sticky=N)

        # create label and entry for cutting meter
        tk.Label(self, text = "Skjærhastighet:").grid(row = 2, column = 0, sticky=N)

        self.cutting_meter = ttk.Entry(self)
        self.cutting_meter.grid(row = 2, column = 1, sticky=W)

        # create label and entry for diameter on your mill
        tk.Label(self, text = "Fres diameter:").grid(row = 3, column = 0, sticky=N)

        self.dia = ttk.Entry(self)
        self.dia.grid(row = 3, column = 1, sticky=W)

        # create label and entry for number of teeth
        tk.Label(self, text = "Antall skjær:").grid(row = 4, column = 0, sticky=N)

        self.teeth = ttk.Entry(self)
        self.teeth.grid(row = 4, column = 1, sticky=W)


        # create label and entry for feed per tooth
        tk.Label(self, text = "Mating pr tann:").grid(row = 5, column = 0, sticky=N)

        self.feed_tooth = ttk.Entry(self)
        self.feed_tooth.grid(row = 5, column = 1, sticky=W)

        #labels for the results
        tk.Label(self, text = "Spindelhastighet:").grid(row = 7, column = 0, sticky=N)

        tk.Label(self, text = "Mating:").grid(row = 8, column = 0, sticky=N)

        # creating entries for the information that i need

        # Button for doing the calc
        self.calculate = ttk.Button(self, text = "Kalkuler!", command = self.calculate)
        self.calculate.grid(row = 6, column = 1, columnspan = 2, sticky=N, pady=10)

        # creating text box for displaying the result
        self.result = tk.Text(self, width = 5, height = 1)
        self.result.grid(row = 7, column = 1, columnspan = 2, sticky=W)

        self.result1 = tk.Text(self, width = 5, height = 1)
        self.result1.grid(row = 8, column = 1, columnspan = 2, sticky=W)


    def calculate(self):
        """Doing all the maths"""

        GLOBAL_Yolo = 1

        # calculation for cutting meter
        pi = float(3.14)
        x = int(1000)
        v = self.cutting_meter.get()
        d = self.dia.get()
        v = int(v)
        d = int(d)
        self.spindel_speed = (float(v) * x) / (pi * float(d))

        #calculation for feed per tooth
        f = self.feed_tooth.get()
        rem_comma = f.replace(',' , '.')
        my_f = float(rem_comma)
        t = self.teeth.get()
        t = int(t)
        s = self.spindel_speed
        s = int(s)
        self.feed_per_tooth = my_f * t * s

        spindel = self.spindel_speed
        feed = self.feed_per_tooth

        spindel = int(spindel)
        feed = int(feed)

        self.result.delete(0.0, END)
        self.result.insert(0.0, [spindel])

        self.result1.delete(0.0, END)
        self.result1.insert(0.0, [feed])


# main
#root = Tk()

#root.geometry("275x225")
#root.resizable(width=False, height=False)

app = SampleApp()
app.title("Skjærdata Kalkulator")
app.resizable(width=False, height=False)




app.mainloop()
