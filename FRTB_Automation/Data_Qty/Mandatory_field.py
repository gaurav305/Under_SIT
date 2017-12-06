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
        button = Button(root, text="Get CSV", command=lambda: self.Mandatory_Check_CR(text))
        list = Listbox(root, bg='blue', fg='yellow')
        text.insert(INSERT, r"C:\Users\gaurav.saini\Desktop\Batch 10 (Final Code Drop)\FRTB_CR_0000000008_20170713051519.csv")
        text.pack()
        button.pack(padx=4, pady=4, side="bottom")
        root.mainloop()

    def Mandatory_Check_CR(self, text):
        self.path1 = text.get()
        # self.path2 = text2.get()
        print "CSV:" + self.path1

        CR_Header = ["CFI Code","Instrument", "Instrument Sub-type", "Contributor Trade Ref ID", "Contributor Trade Ref ID old",
                  "Markit Electronic Conf ID","Transaction Type", "Transaction Sub-Type","Contributor Identifier",
                  "Counterparty Identifier","Counterparty Type", "Trade Date","Start Date", "End Date","Direction",
                  "Notional / Units", "Notional Currency", "Forward Starting","Transaction Fee", "Fee CCY", "Fee Direction",
                  "Post Trade Event Transaction Date & Time", "Post Trade Event Affected Notional / Units", "First Exercise Date",
                  "Expiry Date" , "Option Type", "Option Style", "Exercise Style", "Option Exercise Frequency", "Strike","Strike2",
                  "Strike3", "Strike4","Premium", "Premium CCY", "Digital","Barrier Type","Barrier 1", "Barrier 2" , "Averaging Start Date",
                  "Averaging Frequency", "Settlement Type", "Jurisdiction", "Settlement Currency", "Jurisdiction 2","Settlement Currency 2",
                  "Clearing House Name", "Internal", "Reference Type","Reference Obligation","Reference Entity Name","Reference Entity",
                  "Master Document Transaction Type", "Fixed Rate","Index","Index Fixing Tenor", "Initial Payment Amount", "Initial Payment Amount CCY",
                  "Spread","Attachment Point","Exhaustion Point","Restructuring", "Contractual Definition", "Score", "FRTB Transaction ID",
                  "FRTB Trade ID","Data Source", "Validation Codes","Source File Line Number","Source File Name" ]

        fileH = open(self.path1)
        reader= csv.DictReader(fileH, CR_Header)
        print "----------- Checking cds  - corporate -------------------"

        mandatoryForCDS = ["Instrument","Contributor Trade Ref ID", "Trade Date", "Start Date", "End Date", "Direction",
                           "Notional / Units", "Notional Currency", "Forward Starting", "Internal","Reference Obligation",
                           "Restructuring"]

        mandatoryforcdsindex = ["Instrument", "Contributor Trade Ref ID", "Trade Date", "Start Date", "End Date",
                                "Direction", "Notional / Units", "Notional Currency", "Forward Starting",
                                "Reference Entity"]

        mcdsswaptionindices = ["Instrument", "Contributor Trade Ref ID", "Trade Date", "Start Date", "End Date",
                                "Direction", "Notional / Units", "Notional Currency", "Forward Starting","Expiry Date" ,
                                "Option Type", "Exercise Style", "Option Exercise Frequency", "Strike",
                                "Reference Entity"]

        mcdsswaptionsingle = ["Instrument", "Contributor Trade Ref ID", "Trade Date", "Start Date", "End Date",
                               "Direction", "Notional / Units", "Notional Currency", "Forward Starting", "Expiry Date",
                               "Option Type", "Exercise Style", "Option Exercise Frequency", "Strike",
                               "Reference Obligation"]

        for row in reader:
            if row["Instrument"] == 'cds'and row["Instrument Sub-type"] == 'corporate' \
                    or row["Instrument Sub-type"] == 'abs' or row["Instrument Sub-type"] == 'loans' \
                    or row["Instrument Sub-type"] == 'muni' or row["Instrument Sub-type"] == 'sovereign'\
                    or row["Instrument Sub-type"] == 'other' :
                for attr in mandatoryForCDS:
                    if row[attr] == '':
                        print attr, "Mandatory Value Missing CDS:"+row["Instrument Sub-type"]+ " for ID: ", row['Markit Electronic Conf ID'], " !!!!"

        print "--------------------Checks Complete--------------------------\n"

        fileH.seek(0)
        reader = csv.DictReader(fileH, CR_Header)

        print "------------------ Checking CDSIndex ------------------------\n"
        for i in reader:
            # print " xyz", reader
            if i["Instrument"] == 'cdsIndex' and i["Instrument Sub-type"] == 'cdx'\
                or i["Instrument Sub-type"] == 'lcdx' or i["Instrument Sub-type"] == 'mcdx'\
                or i["Instrument Sub-type"] == 'iTraxx' or 'abx' or 'ios' or 'mbx' or 'po' or 'primeX' or 'trx'\
                or 'sp' or 'cmbx' or 'other':
                # print "ABC I m herer"
                for attr in mandatoryforcdsindex:
                    if i[attr] == '':
                        print attr, "Mandatory Value Missing CDSINDEX:"+i["Instrument Sub-type"] +" for ID: ", i['Markit Electronic Conf ID'], " !!!!"

        print "--------------------Checks Complete--------------------------\n"

        fileH.seek(0)
        reader = csv.DictReader(fileH, CR_Header)

        print "------------------ Checking CDSSwaption: Indices------------------------\n"

        for j in reader:

            if j["Instrument"] == 'cdsSwaption' and j["Instrument Sub-type"] == 'indices':
                for attr in mcdsswaptionindices:
                    if j[attr] == '':
                        print attr, "Mandatory Value Missing cdsSwaption" +j["Instrument Sub-type"] +" for ID: ", j['Markit Electronic Conf ID'], " !!!!"

        print "--------------------Checks Complete--------------------------\n"

        fileH.seek(0)
        reader = csv.DictReader(fileH, CR_Header)

        print "------------------ Checking CDSSwaption: singleName------------------------\n"

        for k in reader:
            if k["Instrument"] == 'cdsSwaption' and k["Instrument Sub-type"] == 'singleName':
                for attr in mcdsswaptionsingle:
                    if k[attr] == '':
                        print attr, "Mandatory Value Missing cdsSwaption" + k["Instrument Sub-type"] + " for ID: ", k['Markit Electronic Conf ID'], "!!!!"

        print "--------------------Checks Complete--------------------------\n"


    def Mandotory_FI(self, text):

        self.path_FI = text.get()

        FI_Header = [['CFI Code'], ['Instrument'], ['Instrument Sub-type'], ['Contributor Trade Ref ID'],
                     ['Contributor Trade Ref ID old'], ['Markit Electronic Conf ID'], ['Transaction Type'],
                     ['Transaction Sub-Type'], ['Contributor Identifier'], ['Counterparty Identifier'], ['Counterparty Type'],
                     ['Trade Date'], ['Start Date'], ['End Date'], ['Direction'], ['Notional / Units'], ['Notional Currency'],
                     ['Forward Starting'], ['Transaction Fee'], ['Fee CCY'], ['Fee Direction'],
                     ['Post Trade Event Transaction Date & Time'], ['Post Trade Event Affected Notional / Units'],
                     ['First Exercise Date'], ['Expiry Date'], ['Option Type'], ['Option Style'], ['Exercise Style'],
                     ['Option Exercise Frequency'], ['Strike'], ['Strike2'], ['Strike3'], ['Strike4'], ['Premium'],
                     ['Premium CCY'], ['Digital'], ['Barrier Type'], ['Barrier 1'], ['Barrier 2'], ['Averaging Start Date'],
                     ['Averaging Frequency'], ['Settlement Type'], ['Jurisdiction'], ['Settlement Currency'],
                     ['Jurisdiction 2'], ['Settlement Currency 2'], ['Clearing House Name'], ['Internal'],
                     ['Bond/Loan ID Type'], ['Bond/Loan ID Value'], ['Fixed Rate'], ['Equity ID Type'],
                     ['Equity ID'], ['Payment Type'], ['Issuer Name'], ['Secured / Covered Bonds'],  ['Score'],
                     ['FRTB Transaction ID'], ['FRTB Trade ID'], ['Data Source'], ['Validation Codes'],
                     ['Source File Line Number'], ['Source File Name']]

        # Fixed Income Header Definations
        File_FI = open(self.path_FI)
        reader_FI = csv.DictReader(File_FI, FI_Header)

        mandatorybond = [['Instrument'], ['Contributor Trade Ref ID'],['Transaction Type'],['Contributor Identifier'],
                         ['Counterparty Identifier'], ['Trade Date'], ['Start Date'], ['End Date'], ['Direction'],
                         ['Notional / Units'], ['Notional Currency'], ['Post Trade Event Transaction Date & Time'],
                         ['Post Trade Event Affected Notional / Units'], ['Bond/Loan ID Type'], ['Bond/Loan ID Value'],
                         ['Fixed Rate'], ['Secured / Covered Bonds']]

        mandatoryloan = [['Instrument'], ['Contributor Trade Ref ID'],['Transaction Type'],['Contributor Identifier'],['Counterparty Identifier'],
                        ['Trade Date'], ['Start Date'], ['End Date'], ['Direction'], ['Notional / Units'], ['Notional Currency'],
                        ['Post Trade Event Transaction Date & Time'], ['Post Trade Event Affected Notional / Units'],
                        ['Bond/Loan ID Type'], ['Bond/Loan ID Value'], ['Fixed Rate']]

        mandatorycertificate = [['Instrument'], ['Contributor Trade Ref ID'],['Transaction Type'],['Contributor Identifier'],['Counterparty Identifier']
                        ['Trade Date'], ['Start Date'], ['End Date'], ['Direction'], ['Notional / Units'], ['Notional Currency'],
                        ['Post Trade Event Transaction Date & Time'], ['Post Trade Event Affected Notional / Units'],
                        ['Bond/Loan ID Type'], ['Bond/Loan ID Value'], ['Fixed Rate']]

        mandatoryembedded = [['Instrument'], ['Instrument Sub-type'], ['Contributor Trade Ref ID'],['Transaction Type'],
                             ['Contributor Identifier'],['Counterparty Identifier'], ['Trade Date'], ['Start Date'],
                             ['End Date'], ['Direction'], ['Notional / Units'], ['Notional Currency'],
                             ['Post Trade Event Transaction Date & Time'], ['Post Trade Event Affected Notional / Units'],
                             ['First Exercise Date'], ['Expiry Date'], ['Exercise Style'],['Option Exercise Frequency'],
                             ['Strike'], ['Bond/Loan ID Type'], ['Bond/Loan ID Value'], ['Equity ID Type'],
                             ['Equity ID'], ['Issuer Name']]

        mandatoryembedded_warrant = [['Instrument'], ['Instrument Sub-type'], ['Contributor Trade Ref ID'],
                                     ['Transaction Type'],['Contributor Identifier'],['Counterparty Identifier'],
                                     ['Trade Date'], ['Start Date'], ['End Date'], ['Direction'], ['Notional / Units'],
                                     ['Notional Currency'], ['Post Trade Event Transaction Date & Time'],
                                     ['Post Trade Event Affected Notional / Units'], ['First Exercise Date'],
                                     ['Expiry Date'], ['Option Exercise Frequency'], ['Strike'], ['Bond/Loan ID Type'],
                                     ['Bond/Loan ID Value'], ['Equity ID Type'], ['Equity ID'], ['Issuer Name']]

        mandatoryrepo = [['Instrument'], ['Contributor Trade Ref ID'],['Transaction Type'],['Contributor Identifier'],
                ['Counterparty Identifier'], ['Trade Date'], ['Start Date'], ['End Date'], ['Direction'],
                ['Notional / Units'], ['Notional Currency'], ['Post Trade Event Transaction Date & Time'],
                ['Post Trade Event Affected Notional / Units'], ['Bond/Loan ID Type'], ['Bond/Loan ID Value'],
                ['Fixed Rate']]

        mandatorybondoption = [['Instrument'], ['Instrument Sub-type'], ['Contributor Trade Ref ID'],['Transaction Type'],
                               ['Contributor Identifier'],['Counterparty Identifier'], ['Trade Date'], ['Direction'],
                               ['Notional / Units'], ['Notional Currency'], ['Post Trade Event Transaction Date & Time'],
                               ['Post Trade Event Affected Notional / Units'], ['First Exercise Date'], ['Expiry Date'],
                               ['Option Type'], ['Exercise Style'],['Option Exercise Frequency'], ['Strike'],
                               ['Bond/Loan ID Type'], ['Bond/Loan ID Value']]

        bondFwd_future = [['Instrument'], ['Instrument Sub-type'], ['Contributor Trade Ref ID'],['Transaction Type'],
                          ['Contributor Identifier'],['Counterparty Identifier'], ['Trade Date'], ['Direction'],
                          ['Notional / Units'], ['Notional Currency'], ['Post Trade Event Transaction Date & Time'],
                          ['Post Trade Event Affected Notional / Units'], ['First Exercise Date'], ['Expiry Date'],
                          ['Option Type'], ['Exercise Style'],['Option Exercise Frequency'], ['Strike'],
                          ['Bond/Loan ID Type'], ['Bond/Loan ID Value']]


        bondFwd_forward = [['Instrument'], ['Instrument Sub-type'], ['Contributor Trade Ref ID'],['Transaction Type'],
                          ['Contributor Identifier'],['Counterparty Identifier'], ['Trade Date'], ['Direction'],
                          ['Notional / Units'], ['Notional Currency'], ['Post Trade Event Transaction Date & Time'],
                          ['Post Trade Event Affected Notional / Units'], ['First Exercise Date'], ['Expiry Date'],
                          ['Option Type'], ['Exercise Style'],['Option Exercise Frequency'], ['Strike'],
                          ['Bond/Loan ID Type'], ['Bond/Loan ID Value'], ['Fixed Rate']]

        inflationLinkedBond = []






    # Foriegn Exchange Header Defination

    def Get_Header(self):
        Path = raw_input("Enter the FilePath\n")
        F_Reader = csv.reader(open(Path))
        FI_Header = []
        # C:\Users\gaurav.saini\Documents\FI_Fields.csv
        for row in F_Reader:
            FI_Header.append(row)

        print FI_Header

        return FI_Header

if __name__ == '__main__':
    obj = ui_frtb()
    obj.get_csv()
    # obj.Get_Header()
