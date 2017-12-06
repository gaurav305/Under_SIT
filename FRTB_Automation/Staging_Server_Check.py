import os
import subprocess

class tw_run:

    def run_bat(self):
        subp = subprocess.call(r'C:\Users\gaurav.saini\Desktop\frtb-test-pack\SftpHiveTest-App2-MISJobs.bat', shell=True)
        subp.communicate()
        print "Process complete"


    def run_tw(self):
        try:
            print "-----------Starting TW Automation Job---------------"
            os.system(r'C:\Users\gaurav.saini\Desktop\frtb-test-pack\SftpHiveTest-App2-MISJobs.bat')
            print "Please Check TW Automation Logs for Update"
        except ValueError:
            print "Some issue found while running the TW code"

if __name__ == '__main__':

    my = tw_run()
    my.run_bat()