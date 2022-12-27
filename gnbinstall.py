import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect('192.168.56.102', username='rmarcelo', password='rmarcelo')

sftp = client.open_sftp()
localpath = '/home/rui_marcelo/Install_program/installgnb.sh'
remotepath = '/home/rmarcelo/installgnb.sh'
sftp.put(localpath, remotepath)
sftp.close()

ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('sudo -S chmod +x installgnb.sh;')
ssh_stdin.write('rmarcelo\n')
ssh_stdin.flush()

data = ssh_stdout.readlines()
print(data)

ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('sudo -S ./installgnb.sh;')
ssh_stdin.write('rmarcelo\n')
ssh_stdin.flush()

data = ssh_stdout.readlines()
print(data)

