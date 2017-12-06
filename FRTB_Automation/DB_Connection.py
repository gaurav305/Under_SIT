import cx_Oracle
import csv
import sys

class MIS_Status():

    def file_status(self):
        username = 'staging_owner'
        password = 'staging_0wner1'
        database = 'TST04MIS'
        con1 = cx_Oracle.connect(username+'/'+password+'@'+'ln17odcqascan03:1521/'+database)
        # con1 = cx_Oracle.connect(username + '/' + password + '@' + 'ln17odcqascan03:1521/' + database)
        print "FRTB_Owner: Connnection Establised: " +con1.version
        cur = con1.cursor()
        staging_owner = 'select file_source_instance_id, filename, status, status_timestamp, source_dir, target_dir from staging_owner.stg_file_reg_status_vw order by id desc fetch first 30 rows only'
        result=cur.execute(staging_owner)
        #result= cur.fetchall()
        field_names = [i[0] for i in cur.description]
        print field_names
        for row in result:
            print field_names
            print row[0], '|',row[1],'|',row[2],'|',row[3],'|', row[4],'|'
        # for row in result:
        #     result[row[0]] +=1
        with open("C:\Users\gaurav.saini\Desktop\csad.csv", "wb") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows([i[0] for i in result.description])
            writer.writerows(result)
        # for row in result:
        #     if result[row[0]] >= 0:
        #         writer.writerow(row)
        print "IMPORT TO CSV COMPLETE"
        print result.description
        # num_fields = len(cur.description)
        # field_names = [i[0] for i in cur.description]
        print field_names
        print "------------------------------------------------------"
        cur.close()
        con1.close()

    def Batch_Status(self):
        username = 'frtb_owner'
        password = 'frtb_owner'
        database = 'TST04MIS'
        con2= cx_Oracle.connect(username + '/' + password + '@' + 'ln17odcqascan03:1521/' + database)
        batch_result = 'select * frtb_batches order by desc'
        batch_status = 'select * from frtb_batch_steps order by batch_id'
        cur2=con2.cursor()
        bresult = cur2.execute(batch_status)
        columns = cur2.description
        # fields = map(lambda x: x[0], cur2.description)
        bresult=cur2.execute(batch_status)
        # bresult = [dict(zip(fields, row)) for row in cursor.fetchall()]
        for row in bresult:
             print row[0],"|", row[1],"|", row[2],"|", row[3],"|", row[4],"|", row[5],"|\n",
        print "------------------------------------------------------"

        cur2.close()
        con2.close()

    def MIS_Job_Status(self):
        username = 'frtb_owner'
        password = 'frtb_owner'
        database = 'TST04MIS'
        con3 = cx_Oracle.connect(username + '/' + password + '@' + 'ln17odcqascan03:1521/' + database)
        batch_status = "select audit_log_key, log_start_DTTM, session_user from audit_log where session_user like 'STAGING_OWNER' order by audit_log_key desc offset 20 ROWS fetch next 20 rows only"
        cur3 = con3.cursor()
        cur3.execute(batch_status)
        Job = list(cur3.fetchall())
        for i,row in enumerate(cur3.fetchall()):
            Job.append(row[i])

        print "I am here"
        print Job

        field_names = [i[0] for i in cur3.description]
        # print field_names
        # for row in mresult:
        #     print row[0],"|", row[1],"|", row[2],"|","|\n",
        print "------------------------------------------------------"
        cur3.close()
        con3.close()

if __name__ == '__main__':
    my = MIS_Status()
    my.file_status()
    my.Batch_Status()
    my.MIS_Job_Status()