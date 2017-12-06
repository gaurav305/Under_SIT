import cx_Oracle
import logging
import datetime
import pyexcel as pe
import csv

date_stamp = datetime.date.today()
logging.basicConfig(filename="Logs\FRTB_Count_"+str(date_stamp)+"_.log", level=logging.INFO)
log = logging.getLogger("FRTB")
date_stamp = datetime.date.today()

# SELECT THE ENVIRONMENT BELOW

# Old MIS LNP Environment
database = "TST04MIS"
host_port = "ln17odcqascan03:1521"

# New LNP Environment
# database = "TST04MIS_APP.MARKIT.PARTNERS"
# host_port = "lnp6odcqascan03.markit.partners:1521"


class counter():

    def get_distinct_data(self):
        username = 'frtb_owner'
        password = 'frtb_owner'

        con1 = cx_Oracle.connect(username + '/' + password + '@' + host_port+'/' + database)
        print "FRTB_Owner: Connection Establised:" + con1.version
        logging.info("FRTB_Owner: Connection Establised: " + con1.version)
        batch_id = raw_input("Enter The Batch ID:\n")
        cur = con1.cursor()
        sql1 = """
        select distinct asset_class_id from frtb_normalised where batch_id = """ +batch_id+"""
        """
        sql2 = """
        select distinct contributor_identifier from frtb_normalised where batch_id = """ +batch_id+"""
                        
        """

        sql4 = """
        
        select count(*) as Total_Count from frtb_normalised where batch_id = """ +batch_id+"""
        
        """

        self.csvfile = "Reports\Analysis_Report_Batch_"+ batch_id +"_" + str(date_stamp) + ".csv"
        file = open(self.csvfile, 'wb')
        output = csv.writer(file, dialect='excel')

        Report_Header = ["Execution and Count Analysis for Batch ID: " + str(batch_id) + "", ""]
        output.writerow(Report_Header)

        asset = []
        client = []

        asset_header = ["Asset Classes in this batch", ""]
        output.writerow(asset_header)
        get_asset = cur.execute(sql1)
        logging.info(" Executing the query : " +str(sql1))
        for i in get_asset:
            output.writerow(i)
            i = ''.join(i)
            asset.append(i)
            print i
        logging.info(" Execution Compelete for sql1")

        client_header = ["Clients in the Batch"]
        output.writerow(client_header)
        get_client = cur.execute(sql2)
        logging.info(" Executing the query : " + str(sql2))
        for j in get_client:
            output.writerow(j)
            j = ''.join(j)
            # if j== '':
            #     j = str('null')
            #     return j
            client.append(j)
            print j
        print client
        logging.info(" Execution Compelete for sql1")

        Total_header = [" Total Count in the Batch",""]
        output.writerow(Total_header)
        counter = cur.execute(sql4)
        logging.info(" Execution Total count query")
        for counts in counter:
            output.writerow(counts)
            print counts
            logging.info(" Total count in the batch : "+str(counts)+"")

        for name in client:
            sql3 = """
            select 
            asset_class_id,
            contributor_identifier,
            instrument_type,
            instrument_sub_type,
            notional_ccy_code,
            count(*) as Total_Count,
            validation_codes,
            count(validation_codes) as Error_Transactions
            from frtb_normalised where batch_id = """+batch_id+""" 
            and contributor_identifier = '"""+name+"""'
            group by 
            asset_class_id, 
            instrument_type, 
            instrument_sub_type, 
            contributor_identifier,
            notional_ccy_code,
            validation_codes
            """
            analyse_header = ["Analyzing Data for :" + name + "", ""]
            print analyse_header
            output.writerow(analyse_header)
            get_count = cur.execute(sql3)
            logging.info(" Executing the query : " + str(sql2))
            logging.info("Analyzing Data for :" + name)
            logging.info("Writing data to CSV")
            field_names = [i[0] for i in cur.description]
            print field_names
            output.writerow(field_names)
            res = []
            for row in get_count:
                print (("{:<10}"*len(row)).format(*row))
                output.writerow(row)
                res.append(row)
            print res
        cur.close()
        con1.close()
        file.close()

if __name__ == '__main__':
    FRTB_Count = counter()
    FRTB_Count.get_distinct_data()
    # FRTB_Count.save_as_excel()