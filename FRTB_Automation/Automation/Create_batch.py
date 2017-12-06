import cx_Oracle
import csv
import logging
from Tkinter import *
import New_Jira
import tkMessageBox
from PIL import ImageTk, Image



logging.basicConfig(filename="FRTB_MIS.log", level=logging.INFO)
log = logging.getLogger("WS")

class ui_frtb():
    def __init__(self):
        self.csvfilepath = ''

    def file_status(self):
        username = 'staging_owner'
        password = 'staging_0wner1'
        database = 'TST04MIS'
        con1 = cx_Oracle.connect(username+'/'+password+'@'+'ln17odcqascan03:1521/'+database)
        # con1 = cx_Oracle.connect(username + '/' + password + '@' + 'ln17odcqascan03:1521/' + database)
        print "FRTB_Owner: Connnection Establised: " +con1.version
        cur = con1.cursor()
        staging_owner = "select file_source_instance_id as Instance_ID, filename, status, status_timestamp from staging_owner.stg_file_reg_status_vw where status_timestamp < (select sysdate from dual) and status in ('COMPLETE', 'FAILED') order by id desc fetch first 30 rows only"
        result=cur.execute(staging_owner)
        #result= cur.fetchall()
        # for row in result:
        #     print row[0], '|',row[1],'|',row[2],'|',row[3],'|', row[4],'|'
        # for row in result:
        #     result[row[0]] +=1
        with open("C:\Users\gaurav.saini\Desktop\csad.csv", "wb") as csv_file:
            writer = csv.writer(csv_file)
            for i,row in result:
                # writer.writerows([i[0] for i in result])
                writer.writerows(row[i])
        # for row in result:
        #     if result[row[0]] >= 0:
        #         writer.writerow(row)
        print "IMPORT TO CSV COMPLETE"
        print result.description
        print "------------------------------------------------------"
        cur.close()
        con1.close()

    def get_csv(self):

        logging.basicConfig(filename="FRTB_MIS.log", level=logging.INFO)
        log = logging.getLogger("WS")
        root = Tk()
        root.geometry('450x325')  # Define the frame
        bckgrg = ImageTk.PhotoImage(Image.open("ihs3.jpg"))  # Adding the IHS Brand Logo
        panel = Label(root, image=bckgrg)
        panel.pack(side="top", fill="both", expand="no", )
        panel.configure(background='white')
        root.title("FRTB Ready For Business Checks")
        label = StringVar()
        label = "FRTB QA Utility V1.0"
        getlabel = Label(root, textvariable=label, text="FRTB QA Utility V1.0")
        getlabel.configure(background='white')
        getlabel.pack()
        text = Entry(root, bg='white', width=50)
        text.insert(INSERT, r"TST04MIS", )
        text.pack()
        button = Button(root, text="MIS Status", command=lambda: self.printfrtbbatch(text))
        button.pack(padx=4, pady=4, side="bottom")
        button2 = Button(root, text="Check Batch Status", command=lambda: self.printresult(text))
        button2.pack(padx=4, pady=4, side="bottom")
        button3 = Button(root, text="Check File Status", command=lambda: self.printbatch(text))
        button3.pack(padx=4, pady=4, side="bottom")
        root.mainloop()

if __name__ == '__main__':
    my1 = ui_frtb()
    my1.get_csv()
    my1.file_status()