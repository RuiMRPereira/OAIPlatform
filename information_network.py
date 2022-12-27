import re
import os
import subprocess
import time
import paramiko
from getpass import getpass


def core_information():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('192.168.81.225', username='epc', password='test4g')

    cmd = 'netstat -ie | grep -B1 "192.168.81.214" | head -n1 | awk '+'\''+'{print $1}'+'\''+';'
    print(cmd)

    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(cmd)
    ssh_stdin.flush()

    #time.sleep(0.1)

    ##data = ssh_stdout.readlines()
    ##data = str(data)
    #print(data)
    #print(data[2:len(data)-5])
    ##interfacecore = data[2:len(data)-5]
    #print(interfacecore)

    ##cmd = 'nmcli device show '+interfacecore+' | grep IP4.DNS > dns.txt'
    #print(cmd)
    ##ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(cmd)

    #time.sleep(0.01)

    ##data = ssh_stdout.readlines()
    ##data = str(data)

    ##sftp = client.open_sftp()
    ##localpath = '/home/rui_marcelo/Install_program/dns.txt'
    ##remotepath = '/home/epc/dns.txt'
    ##sftp.get(remotepath, localpath)
    ##sftp.close()

    ##if os.path.isfile('dns.txt'):
    ##    with open('dns.txt', 'r') as file:
    ##        dns_data = file.read()
    ##file.close()

    #print(str(dns_data[40:53]))
    #print(str(dns_data[94:len(dns_data)]))

    ##dns1 = str(dns_data[40:53])
    ##dns2 = str(dns_data[94:len(dns_data)])

    #print(dns1)
    #print(dns2)

    ##if os.path.isfile('docker-compose-basic-nrf_templete_fast.yaml'):
    ##    with open('docker-compose-basic-nrf_templete_fast.yaml', 'r') as file:
    ##        docker_compose = file.read()
    ##file.close()

    ##dns1 = '            - DEFAULT_DNS_IPV4_ADDRESS='+dns1
    ##docker_compose = docker_compose.replace('            - DEFAULT_DNS_IPV4_ADDRESS=', dns1)

    ##dns2 = '            - DEFAULT_DNS_SEC_IPV4_ADDRESS=' + dns2
    ##docker_compose = docker_compose.replace('            - DEFAULT_DNS_SEC_IPV4_ADDRESS=', dns2)

    ##with open('docker-compose-basic-nrf.yaml', 'w') as file:
    ##    file.write(docker_compose)


def nic_information(ip, user, password): # Nic livres
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(ip, username=user, password=password)

    sftp = client.open_sftp()
    localpath = '/home/rui_marcelo/Install_program/interfaces.sh'
    remotepath = '/home/' + user + '/interfaces.sh'
    sftp.put(localpath, remotepath)
    sftp.close()

    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('sudo -S chmod +x interfaces.sh;')
    ssh_stdin.write(password + '\n')
    ssh_stdin.flush()

    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('./interfaces.sh')
    ssh_stdin.flush()

    sftp = client.open_sftp()
    localpath = '/home/rui_marcelo/Install_program/ocupadas.txt'
    remotepath = '/home/' + user + '/ocupadas.txt'
    sftp.get(remotepath, localpath)
    sftp.close()

    if os.path.isfile('ocupadas.txt'):
        with open('ocupadas.txt', 'r') as file:
            ocupadas = file.read()
    file.close()

    sftp = client.open_sftp()
    localpath = '/home/rui_marcelo/Install_program/todas.txt'
    remotepath = '/home/' + user + '/todas.txt'
    sftp.get(remotepath, localpath)
    sftp.close()

    livres = []

    todas = open('todas.txt', 'r')
    lines = todas.readlines()
    for line in lines:
        if not line in ocupadas:
            line = str(line)
            livres.append(line[0:len(line) - 1])

    if len(livres) == 0:
        print('Sem NIC livres')
    else:
        print(livres[len(livres) - 1])
        #nic_livres = livres
        #livres.pop()
    return livres


def config_nic():
    cmd = 'sudo -S ifconfig '+livres[len(livres)-1]+' 192.168.69.69 netmask 255.255.255.0;'
    print(cmd)

    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(cmd)
    ssh_stdin.write('rmarcelo\n')
    ssh_stdin.flush()

    livres.pop()

#core_information()

# quero que o 16 seja core e 15 seja gNB

password = getpass()
nic_core = nic_information(ipcore, usercore, passcore)
config_nic()

