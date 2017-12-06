# from fabric.api import run
# from fabric.api import sudo
from fabric.api import *
# from fabric.api import env

# env.user = 'gaurav.saini'
# env.password = 'MotorolaX4153!'
# env.host = '10.23.26.139'
# env.use_ssh_config = True
env.user = 'frtb_poc_qa'
env.password = 'edmrsa@123'
env.host = ['ms01068.mserv.local']
env.port = 22
env.key_filename = r'C:\Users\gaurav.saini\PycharmProjects\FRTB_Automation\EDMSSHKEY_Export.ppk'

# env.user = 'achin.saxena'
# env.password = 'Swapswire1992@'
# env.host = 'ms00017'
# env.port = 22
# env.key_filename = 'C:\Users\gaurav.saini\PycharmProjects\FRTB_Automation\EDMSSHKey.ppk'


def vm_up(filename):
    # pass
    # run("echo test")
    run("pwd")
    run("ls")
    # print "here"
    # run("who")
    # run('LON6RTBQAAPP001.markit.partners -s')
    # run('who')
    # run("sudo su - frtbowner ")
    # # sudo("su frtbowner")
    # print "thats step 1"
    # run("ssh frtb_poc_qa@ms01068.mserv.local")
    # print "thats step 2"
    # run("cd mkit.frtb_cob.qa/incoming/TST04MIS")
    # print "thats step 3"
    # run("find" +filename)

if __name__ == '__main__':

    # rw= raw_input("Please Enter the file you need to search:")
    rw = "FRTB_DSM_CR_D170707_T0031441_PFN.csv"
    vm_up(rw)

# LON6RTBQAAPP001.markit.partners
# FRTB_DSM_CR_D170707_T0031441_PFN.csv
