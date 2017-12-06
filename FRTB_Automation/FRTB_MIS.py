import cx_Oracle
import csv
import logging
from Tkinter import *
import New_Jira
import datetime
from PIL import ImageTk, Image

logging.basicConfig(filename="Logs\FRTB_MIS.log", level=logging.INFO)
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
        with open("Reports_File\Report_File.csv", "wb") as csv_file:
            writer = csv.writer(csv_file)
            for row in result:
                # writer.writerows([i[0] for i in result])
                writer.writerows(row)
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
        # rl = text.get()
        # Resultlabel = Label(root, textvarible=label, text= rl )
        # Resultlabel.pack()
        root.mainloop()

    def printresult(self, text):
        logging.basicConfig(filename="FRTB_JS.log", level=logging.INFO)
        log = logging.getLogger("WS")
        logging.info("Info gathering started")
        root2 = Tk()
        root2.geometry('700x500')
        username = 'frtb_owner'
        password = 'frtb_owner'
        self.database= text.get()
        con1 = cx_Oracle.connect(username + '/' + password + '@' + 'ln17odcqascan03:1521/' + self.database)
        # con1 = cx_Oracle.connect(username + '/' + password + '@' + 'ln17odcqascan03:1521/' + database)
        print "FRTB_Owner: Connnection Establised: " + con1.version
        cur = con1.cursor()
        staging_owner = 'select Batch_ID, status, run_type, created_ts ' \
                        'from frtb_batches where created_ts <= (select sysdate from dual) order by batch_id desc'
        result = cur.execute(staging_owner)
        textbox = Text(root2)
        textbox.pack(fill=BOTH, expand=1)
        field_names = [i[0] for i in cur.description]

        textbox.insert(END, field_names)

        headers = []

        for i in result:
            # str(i).strftime('%y-%m-%d-%h-%m-%s')
            i = ''.join(str(i))         # To get the result in format
            headers.append(i)           # To Store headers for the query
            textbox.insert(END,"\n" +str(i))
            # print "i am here"
        label2 = "FRTB asd"
        batch_number = Entry(root2, bg='white', width=50)
        batch_number.insert(INSERT, r"Enter Batch - ID", )
        batch_number.pack(side = "bottom")
        Resultlabel = Label(root2, textvariable=label2, text=result)
        bdbutton = Button(root2, text="Check Batch Details", command=lambda: self.batch_details(batch_number))
        bdbutton.pack(padx=4, pady=4, side="bottom", )
        logging.info("Results fetched")
        Resultlabel.pack()
        root2.mainloop()

    def batch_details(self, batch_number):
        root4 = Tk()
        root4.geometry('700x500')
        self.batch_id = batch_number.get()
        username = 'frtb_owner'
        password = 'frtb_owner'
        con1 = cx_Oracle.connect(username + '/' + password + '@' + 'ln17odcqascan03:1521/' + self.database)
        cur = con1.cursor()
        batch_d = 'select * from frtb_batch_steps where batch_id ='+self.batch_id+'order by step_no asc'
        result = cur.execute(batch_d)
        textbox = Text(root4)
        textbox.pack(fill=BOTH, expand=1)
        field_names = [i[0] for i in cur.description]
        textbox.insert(END, field_names)
        for i in result:
            str=repr(i)
            textbox.insert(END, "\n" + str)
            # print "i am here"
        root4.mainloop()

    def printfrtbbatch(self, text):
        root2 = Tk()
        root2.geometry('700x500')
        username = 'staging_owner'
        password = 'staging_0wner1'
        self.database= text.get()
        con1 = cx_Oracle.connect(username + '/' + password + '@' + 'ln17odcqascan03:1521/' + self.database)
        # con1 = cx_Oracle.connect(username + '/' + password + '@' + 'ln17odcqascan03:1521/' + database)
        print "FRTB_Owner: Connnection Establised: " + con1.version
        cur = con1.cursor()
        staging_owner = "select distinct job_name,log_date,status, errors from all_scheduler_job_run_details " \
                        "where job_name  in ('STG_FILE_TRANSFER','STG_FILE_STAGE','FRTB_BATCH_JOB') " \
                        "and log_date >= (select sysdate from dual)" \
                        "order by log_date desc" \
                        # "select audit_log_key, log_start_DTTM, session_user from audit_log where session_user like 'STAGING_OWNER' order by audit_log_key desc offset 20 ROWS fetch next 20 rows only"
        result = cur.execute(staging_owner)
        label = StringVar()
        getlabel = Label(root2, textvariable=label, text="FRTB File Delivery Status")
        getlabel.configure(background='white')
        getlabel.pack()
        textbox = Text(root2)
        textbox.pack(fill=BOTH, expand=1)
        field_names = [i[0] for i in cur.description]
        textbox.insert(END, field_names)
        for i in result:
            textbox.insert(END,"\n" +str(i))
        label2 = "FRTB asd"
        Resultlabel = Label(root2, textvariable=label2, text=result)
        Summary = Entry(root2, bg='white', width=50)
        Summary.insert(INSERT, r"Enter Batch - ID", )
        Summary.pack(side="bottom")
        Resultlabel = Label(root2, textvariable=label2, text=result)
        server_url = 'https://jira.markit.com'
        username = "gaurav.saini"
        password = "MotorolaX4153!"
        jirabutton = Button(root2, text="Log a issue", command=lambda: New_Jira.createTask(server_url,username, password, 'FRTB', Summary.get()))
        jirabutton.pack(padx=4, pady=4, side="bottom", )
        # issue_code = issue["key"]
        # issue_url = "%s/browse/%s" % (server_url, issue_code)

        # Resultlabel.config(text=str(r1))

        cur.close()
        con1.close()
        Resultlabel.pack()
        root2.mainloop()


    def printbatch(self, text):
        root3 = Tk()
        root3.geometry('1180x600')
        username = 'staging_owner'
        password = 'staging_0wner1'
        self.database = text.get()
        con1 = cx_Oracle.connect(username + '/' + password + '@' + 'ln17odcqascan03:1521/' + self.database)
        # con1 = cx_Oracle.connect(username + '/' + password + '@' + 'ln17odcqascan03:1521/' + database)
        print "FRTB_Owner: Connnection Establised: " + con1.version
        cur = con1.cursor()
        staging_owner = "select file_source_instance_id as Instance_ID, filename, status, status_timestamp " \
                        "from staging_owner.stg_file_reg_status_vw where status_timestamp < (select sysdate from dual) " \
                        "and status in ('COMPLETE', 'FAILED') and target_ssh_credentials != 'liq_rep_qa@ms01068' order by id desc fetch first 30 rows only"
        result = cur.execute(staging_owner)
        # result= cur.fetchall()
        # for row in result:
        #     print row[0], '|', row[1], '|', row[2], '|', row[3], '|', row[4], '|'
        Textbox = Text(root3)
        Textbox.pack(fill=BOTH, expand=1)
        label = StringVar()
        getlabel = Label(root3, textvariable=label, text="FRTB File Delivery Status")
        getlabel.configure(background='white')
        getlabel.pack()
        field_names = [i[0] for i in cur.description]
        Textbox.insert(END, field_names)
        print "Loop1 ended"
        for i in result:
            Textbox.insert(END, "\n" +str(i))
        label3 = "FRTB asd"
        Resultlabel = Label(root3, textvariable=label3, text=result)
        # Resultlabel.config(text=str(r1))
        Resultlabel.pack()
        root3.mainloop()
if __name__ == '__main__':
    my1 = ui_frtb()
    my1.get_csv()
    my1.file_status()