from DB_Connection import *
import csv
import json
from Tkinter import *
import tkMessageBox
from PIL import ImageTk, Image


class ui_frtb():
    def __init__(self):
        self.csvfilepath = ''

    def get_csv(self):

        root = Tk()

        root.geometry('450x325') #Define the frame
        bckgrg = ImageTk.PhotoImage(Image.open("ihs2.jpg")) #Adding the IHS Brand Logo
        panel = Label(root, image=bckgrg)
        panel.pack(side="top", fill="both", expand="no", )
        root.title("FRTB Ready For Business Checks")
        label = StringVar()
        label = "FRTB QA Utility V1.0"
        getlabel = Label(root, textvariable=label, text="FRTB QA Utility V1.0")
        getlabel.pack()
        text = Entry(root, bg='white', width=50)
        list = Listbox(root, bg='blue', fg='yellow')
        text.insert(INSERT, r"Enter Database Name (Eg. TST01MIS)", )
        text.pack()
        button = Button(root, text="MIS Status", command=lambda: self.printresult(text))
        button.pack(padx=4, pady=4, side=LEFT)
        button2 = Button(root, text="Check Batch Status", command=lambda: self.printbatch(text))
        button2.pack(padx=4, pady=4, side=LEFT)
        button3 = Button(root, text="Check File Status", command=lambda: self.printbatch(text))
        button3.pack(padx=4, pady=4, side= LEFT)

        # rl = text.get()
        # Resultlabel = Label(root, textvarible=label, text= rl )
        # Resultlabel.pack()
        root.mainloop()

    def printresult(self, text):
        root2 = Tk()
        root2.geometry('700x500')
        self.r1=text.get()
        print self.r1
        label2="FRTB asd"
        Resultlabel = Label(root2, textvariable=label2, text=self.r1)
        # Resultlabel.config(text=str(r1))
        Resultlabel.pack()
        root2.mainloop()

    def printbatch(self, text):
        root3 = Tk()
        root3.geometry('700x500')
        # self.r1=my.MIS_Job_Status()
        self.r1=text.get()
        T1 = Text(root3, height=500, width=700)
        T1.pack()
        for i in self.r1:
            T1.insert(END, str(i))
        print self.r1
        label3="FRTB asd"
        Resultlabel = Label(root3, textvariable=label3, text=self.r1)
        # Resultlabel.config(text=str(r1))
        Resultlabel.pack()
        root3.mainloop()

if __name__ == '__main__':
    my1 = ui_frtb()
    my1.get_csv()