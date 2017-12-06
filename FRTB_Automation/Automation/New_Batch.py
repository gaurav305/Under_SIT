import cx_Oracle
import logging
import datetime
import os
date_stamp = datetime.date.today()
logging.basicConfig(filename="Logs\FRTB_MIS_"+str(date_stamp)+"_Batch.log", level=logging.INFO)
log = logging.getLogger("NB")

# SELECT THE ENVIRONMENT BELOW

# Old MIS LNP Environment
database = "TST04MIS"
host_port = "ln17odcqascan03:1521"

# New LNP Environment
# database = "TST04MIS_APP.MARKIT.PARTNERS"
# host_port = "lnp6odcqascan03.markit.partners:1521"

class New_Batch ():

    def staging_file(self):
        username = 'staging_owner'
        password = 'staging_0wner1'
        print "-------------Starting Staging Process -----------------"
        con = cx_Oracle.connect(username + '/' + password + '@' + host_port+'/' + database)
        stage_cur = con.cursor()
        print " Staging_Owner: Connnection Establised: " + con.version
        ###Step 1
        staging_trans = """
        begin
           stg_file_ops.stg_file_transfer;
        end;
        """
        ###Step 2
        stage_load = """
        begin
           stg_file_ops.stg_file_stage;
        end;
        """
        Step1 = stage_cur.execute(staging_trans)
        print "Step 1 Complete - Staging File Transfer "

        Step2 = stage_cur.execute(stage_load)
        print "Step 2 Complete - Staging File Load "

        print "--------------Staging Process Complete----------------"

    def create_batch(self):
        username = 'frtb_owner'
        password = 'frtb_owner'

        con1 = cx_Oracle.connect(username + '/' + password + '@' + host_port +'/' + database)
        print "FRTB_Owner: Connnection Establised:" + con1.version
        logging.info("FRTB_Owner: Connnection Establised: " + con1.version)
        cur = con1.cursor()
        logging.info("Starting Batch Creation Process")
        print "-------------Starting Batch Creation Process -----------------"

        from_date = raw_input("Enter Businees from Date in format DD-MM-YYYY HH24:MI:SS ")
        to_date = raw_input("Enter Business to Date in format DD-MM-YYYY HH24:MI:SS ")
        logging.info("Creating Batch with Business start date from " + from_date + "to Business date" + to_date)
        create_batch = """
        DECLARE
        l_batch_no number;
        BEGIN
        l_batch_no := frtb_batch.create_batch(business_date_from_in => to_date('""" + from_date + """','DD-MM-YYYY HH24:MI:SS'),
                                             business_date_to_in   => to_date('""" + to_date + """','DD-MM-YYYY HH24:MI:SS'));
        : Batch_id := l_batch_no;
        END;
        """
        Batch_id = cur.var(cx_Oracle.STRING)
        result = cur.execute(create_batch, Batch_id=Batch_id)
        self.res = Batch_id.getvalue()
        commit = cur.execute('commit')
        print "Batch ID created : " + self.res
        logging.info("Query Executed" + create_batch)
        logging.info(" Batch Creation Complete, Batch ID created : " + str(self.res))

        frtb_steps = ['ID_FILES', 'LOAD', 'ANONYMIZE', 'MAP', 'VALIDATE', 'ENRICH', 'MATCH', 'SCORE', 'GENERATE',
                      'VALIDATION_REPORT', 'SEND_WARNING', 'CLIENT_EX_RPT']
        print "----------Starting Processing Batch : " + str(self.res) + "--------------"
        # formatter = "%r"
        for step in frtb_steps:
            print "Executing the Step: " + step
            logging.info("Starting Step: " + step + " Started at : " + str(datetime.datetime.now()))
            restart_step = ""
            ex_steps = cur.callproc('frtb_batch.process_batch', [self.res, restart_step, step])
            logging.info("Completed Step: " + step + "Completed at : " + str(datetime.datetime.now()))
            print "FRTB Step : " + step + " is Complete"

        print "------MIS Batch Processing Complete for Batch:" + str(self.res) + "--------"
        logging.info("Batch Processing for Batch:" + str(self.res))

    def send_info(self):
        username = 'staging_owner'
        password = 'staging_0wner1'
        con = cx_Oracle.connect(username + '/' + password + '@' + host_port + '/' + database)
        cur = con.cursor()
        print "---------------Getting File Infomation for TW Automation Piece-------------------------"
        # date_stamp = datetime.date.today()
        file_name = open(r'C:\Users\gaurav.saini\Desktop\frtb-test-pack\MIS_Out.txt', 'w+')
        # file_name = open(r'\\ndatstnpc145\sftp\Gaurav\MIS_' + str(date_stamp) + '_Batch_' + str(self.res) + '.txt', 'w+')
        # file_name = open('MIS_' + str(date_stamp) + '_Batch_' + str(res) + '.txt', 'w+')
        file_name.read()

        file_status = """ select distinct filename from (select * from staging_owner.stg_file_reg_status_vw where status = 'COMPLETE' order by status_timestamp desc fetch first 18 row only)
        where filename like 'FRTB_IR_00%' OR filename like 'FRTB_CR_00%' OR filename like 'FRTB_FX_00%'
        OR filename like 'FRTB_FI_00%' OR filename like 'FRTB_CM_00%' or filename like 'FRTB_EQ_00%'
            """
        get_file_name = cur.execute(file_status)
        get_file_name = get_file_name.fetchall()

        print "-----------Files created for batch : " + str(self.res) + "----------------"
        print get_file_name

        for result in get_file_name:
            result = ''.join(result)
            file_name.write(result)
            file_name.write("\n")
            logging.info("Getting Files Generated by MIS: " + result)
        print "Process Complete"
        logging.info("File Information Transfer process Complete")
        file_name.close()
        cur.close()
        con.close()

    def run_tw(self):
        try:
            print "-----------Starting TW Automation Job---------------"
            os.system(r'C:\Users\gaurav.saini\Desktop\frtb-test-pack\SftpHiveTest-App2-MISJobs.bat')
            print "Please Check TW Automation Logs for Update"
        except ValueError:
            print "Some issue found while running the TW code"

if __name__ == '__main__':

    FRTB = New_Batch()
    FRTB.staging_file()
    FRTB.create_batch()
    FRTB.staging_file()
    FRTB.send_info()
    # FRTB.run_tw()



# LNP6 TST04MIS- FRTB_OWNER	FRTB_OWNER@//lnp6odcqascan03.markit.partners:1521/TST04MIS_APP.MARKIT.PARTNERS