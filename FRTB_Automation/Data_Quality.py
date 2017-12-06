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
        root.geometry('450x325')
        bckgrg = ImageTk.PhotoImage(Image.open("ihs3.jpg"))
        panel = Label(root, image=bckgrg)
        panel.pack(side="top", fill="both", expand="no", )
        root.title("FRTB Data Quality Checker")
        label = StringVar()
        label = "FRTB QA Utility V1.0"
        getlabel = Label(root, textvariable=label, text="FRTB QA Utility V1.0")
        getlabel.pack()
        text = Entry(root, bg='white', width=50)
        # text2 = Entry(root, bg='white', width=50)
        # button = Button(root, text="Compare XML", command=self.compareNow)
        # self.compareNow()
        button = Button(root, text="Get CSV", command=lambda: self.Insert_LoadCSV(text))
        list = Listbox(root, bg='blue', fg='yellow')
        text.insert(INSERT, r"C:\Users\gaurav.saini\Desktop\Batch 10 (Final Code Drop)\FRTB_CR_0000000008_20170713051519.csv")
        text.pack()
        # text2.insert(INSERT, r"C:\Users\gaurav.saini\Desktop\DynamicFpML\DynamicFpML\DATA\T#6_176633847-timestamp.xml")
        # text2.pack()
        # button.pack(padx=4, pady=4, side="bottom")
        button.pack(padx=4, pady=4, side="bottom")
        # result = self.compareNow()
        # list.pack()
        root.mainloop()

    def Insert_LoadCSV(self, text):
        self.path1 = text.get()
        # self.path2 = text2.get()
        print "CSV:" + self.path1
        # print "Path 2" + self.path2
        reader = csv.DictReader(open(self.path1))
        print self.path1
        trades = []
        result = []
        # C:\_Project\FRTB\QA\Testing\PFN\Credits\FRTB_DSM_CR_D170221_T0031031_PFN.csv
        trade = {}
        i = 0
        for row in reader:
            # print "Printing Row:", i
            # print row
            # print len(row.keys())
            # print type(row)
            trades.append(row)
            key = row.pop('Instrument')
            # if key in result:
            #     # implement your duplicate row handling here
            #     pass
            # result[key] = row
        print len(trades)
        trades_file = open('trades.txt', 'w')
        trades_file.truncate()
        for trade in trades:
            for trade_economic in trade.keys():
                print 'Should check', trade_economic, 'for trade:', trade['Markit Electronic Conf ID']
                ##TODO validateImpl(trade_economic, trade[trade_economic])
            trades_file.write(json.dumps(trade, indent=4))
            trades_file.write('\n')
        trades_file.close()
        # print result
        return result

    def validateImpl(self, trade_economic, value):
        pass
        ## return True or False

    def check_datatype(self, result):

        for key in result:
            print type(result.get(result[key]))

        # reader = csv.reader(open(self.path1))
        # result = {}
        # for row in reader:
        #     key = row[0]
        #     if key in result:
        #         pass
        #     result[key]
        # print result


        # def LoadCSV(self):
        #
        #     reader = csv.reader(open(self.path1))
        #     result={}
        #     for row in reader:
        #         key=row[0]
        #         if key in result:


        # with open(self.path1, mode='w') as outfile:
        #     writer = csv.writer(outfile)
        # for rows in reader:
        #     k = rows[0]
        #     v = rows[1]
        #     mydict = {k:v for k, v in rows}
        # print(mydict)


if __name__ == '__main__':
    obj = ui_frtb()
    obj.get_csv()
