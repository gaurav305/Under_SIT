import paramiko


def check_file():
    # user = 'gaurav.saini'
    # password = 'MotorolaX4153!'
    # host = '10.23.26.139'

    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('10.23.26.139', 'gaurav.saini', password='MotorolaX4153!')
    stdin, stdout, stderr = \
        ssh.exec_command("who")
    type(stdin)

if __name__ == '__main__':

    check_file()