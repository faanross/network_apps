import paramiko

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())

if __name___ == '__main__':
    import getpass
    user = input('Username: ')
    password = getpass.getpass()
    
    ip = input('Enter server IP: ') or '192.168.2.94'
    port = input('Please enter port number') or 2222
    cmd = 
