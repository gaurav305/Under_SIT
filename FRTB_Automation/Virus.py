# class virus():
#
#     def __init__(self):
#         pass
#
#     def get_input(self):
#         test = raw_input("Enter Test Number:")
#         row, column = raw_input("Enter Row and Column with space: \n ").split()
#         r,c= raw_input("Enter file location in format (r,c):").split(',')
#         print "User Input " \
#               "\n Test: "+ test+\
#               "\n Row/Column:" +str(row)+ "/" +str(column)+\
#               "\n file location:" "("+str(r)+","+str(c)+")"
#         return test, row, r,c
#
#
#     def find_time(self):
#         pass
#
# if __name__ == '__main__':
#
#     mygi= virus()
#     mygi.get_input()
#     mygi.find_time()
#
# import json
#
# FI_Header = [['CFI Code'], ['Instrument'], ['Instrument Sub-type'], ['Contributor Trade Ref ID'],
#              ['Contributor Trade Ref ID old'], ['Markit Electronic Conf ID'], ['Transaction Type'],
#              ['Transaction Sub-Type'], ['Contributor Identifier'], ['Counterparty Identifier'], ['Counterparty Type'],
#              ['Trade Date'], ['Start Date'], ['End Date'], ['Direction'], ['Notional / Units'], ['Notional Currency'],
#              ['Forward Starting'], ['Transaction Fee'], ['Fee CCY'], ['Fee Direction'],
#              ['Post Trade Event Transaction Date & Time'], ['Post Trade Event Affected Notional / Units'],
#              ['First Exercise Date'], ['Expiry Date'], ['Option Type'], ['Option Style'], ['Exercise Style'],
#              ['Option Exercise Frequency'], ['Strike'], ['Strike2'], ['Strike3'], ['Strike4'], ['Premium'],
#              ['Premium CCY'], ['Digital'], ['Barrier Type'], ['Barrier 1'], ['Barrier 2'], ['Averaging Start Date'],
#              ['Averaging Frequency'], ['Settlement Type'], ['Jurisdiction'], ['Settlement Currency'],
#              ['Jurisdiction 2'], ['Settlement Currency 2'], ['Clearing House Name'], ['Internal'],
#              ['Bond/Loan ID Type'], ['Bond/Loan ID Value'], ['Fixed Rate'], ['Equity ID Type'],
#              ['Equity ID'], ['Payment Type'], ['Issuer Name'], ['Secured / Covered Bonds'], ['Score'],
#              ['FRTB Transaction ID'], ['FRTB Trade ID'], ['Data Source'], ['Validation Codes'],
#              ['Source File Line Number'], ['Source File Name']]
#
# with open('C:\Users\gaurav.saini\PycharmProjects\FRTB_Automation\Data_Qty\JSON\FI.json', 'wb') as outfile:
#     json.dump(FI_Header, outfile)

#
# from Tkinter import *
# from ttk import *
#     # from tkinter import *
#     # from tkinter.ttk import *
#
#
# class App(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.CreateUI()
#         self.LoadTable()
#         self.grid(sticky = (N,S,W,E))
#         parent.grid_rowconfigure(0, weight = 1)
#         parent.grid_columnconfigure(0, weight = 1)
#
#     def CreateUI(self):
#         tv = Treeview(self)
#         tv['columns'] = ('starttime', 'endtime', 'status')
#         tv.heading("#0", text='Sources', anchor='w')
#         tv.column("#0", anchor="w")
#         tv.heading('starttime', text='Start Time')
#         tv.column('starttime', anchor='center', width=100)
#         tv.heading('endtime', text='End Time')
#         tv.column('endtime', anchor='center', width=100)
#         tv.heading('status', text='Status')
#         tv.column('status', anchor='center', width=100)
#         tv.grid(sticky = (N,S,W,E))
#         self.treeview = tv
#         self.grid_rowconfigure(0, weight = 1)
#         self.grid_columnconfigure(0, weight = 1)
#
#     def LoadTable(self):
#         self.treeview.insert('', 'end', text="First", values=('10:00',
#                              '10:10', 'Ok'))
#
# def main():
#     root = Tk()
#     App(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()
#
#


#
# import Tkinter
# window = Tkinter.Tk()
# frame = Tkinter.Frame(window)
# frame.pack()
#
# entries = {} # this 'entries'is what you might want to specify a custom class to manage
#              # for now,a dictionary will do
#
# for j in range(10):
#     for i in range(10):
#         e = Tkinter.Entry(f)
#         e.grid(column=i,row=j, borderwidth=0)
#         es[i,j] = e


