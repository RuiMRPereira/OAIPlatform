import os
import subprocess
import threading


def iperf():
    sub_cmd2

    with open('result_iperf.txt', 'a') as file:
        file.write(str(result_iperf))


def config_route():
    sub_cmd1


if os.path.isfile('result_iperf.txt'):
    os.remove('result_iperf.txt')

with open('result_iperf.txt', 'a') as file:
    file.write('Falhou')

threading.Thread(target=iperf).start()
threading.Thread(target=config_route).start()

