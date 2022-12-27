import paramiko
import os


def band_interface():
    bands = [1, 2, 3, 5, 7, 8, 12, 20, 25, 28, 34, 38, 39, 40, 41, 50, 51, 65, 66, 70, 71, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86]
    return bands


def scs_interface():
    scs = [15, 30, 60]
    return scs


def bw_interface():
    bw = [5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]
    return bw


####################################################################################################
# Função que mostra se a banda introduzida é válida

def check_band(band):
    bands = [1, 2, 3, 5, 7, 8, 12, 20, 25, 28, 34, 38, 39, 40, 41, 50, 51, 65, 66, 70, 71, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86]
    if band in bands:
        return True
    else:
        return False
####################################################################################################
# Função que mostra o menu com as SCS disponiveis


def menu_scs(band):
    if band in [1, 2, 3, 7, 25, 38, 39, 40, 41, 50, 65, 66, 70, 74, 75, 77, 78, 79, 80, 84, 86]:
        print('SCS disponiveis: ', 15, 30, 60)
    if band in [5, 8, 12, 20, 28, 71, 81, 82, 83]:
        print('SCS disponiveis: ', 15, 30)
    if band in [34, 51, 76]:
        print('SCS disponveis: 15')
####################################################################################################
# Função que verifica se a scs introduzida é valida para a banda


def check_scs(band, scs):
    if band in [1, 2, 3, 7, 25, 38, 39, 40, 41, 50, 65, 66, 70, 74, 75, 77, 78, 79, 80, 84, 86]:
        if scs in [15, 30, 60]:
            return True
        else:
            return False
    if band in [5, 8, 12, 20, 28, 71, 81, 82, 83]:
        if scs in [15, 30]:
            return True
        else:
            return False
    if band in [34, 51, 76]:
        if scs in [15]:
            return True
        else:
            return False


####################################################################################################
# Função que mostra as larguras de banda


def menu_bandwidth(band, scs):
    if scs == 15:
        if band in [1, 2, 5, 7, 8, 20, 25, 28, 38, 65, 71, 74, 81, 82, 83, 84]:
            print('Bandwidth disponiveis: ', 5, 10, 15, 20)
        if band in [3, 80]:
            print('Bandwidth disponiveis: ', 5, 10, 15, 20, 25, 30)
        if band in [34, 51, 76]:
            print('Bandwidth disponiveis: ', 5)
        if band == 39:
            print('Bandwidth disponiveis: ', 5, 10, 15, 20, 25, 30, 40)
        if band in [66, 86]:
            print('Bandwidth disponiveis: ', 5, 10, 15, 20, 40)
        if band == 40:
            print('Bandwidth disponiveis: ', 5, 10, 15, 20, 25, 30, 40, 50)
        if band == 41:
            print('Bandwidth disponiveis: ', 10, 15, 20, 40, 50)
        if band == 50:
            print('Bandwidth disponiveis: ', 5, 10, 15, 20, 40, 50)
        if band in [77, 78]:
            print('Bandwidth disponiveis: ', 10, 15, 20, 30, 40, 50)
        if band == 79:
            print('Bandwidth disponiveis: ', 40, 50)
    if scs == 30:
        if band in [1, 2, 5, 7, 8, 20, 25, 28, 38, 65, 71, 74, 75, 81, 82, 83, 84]:
            print('Bandwidth disponiveis: ', 10, 15, 20)
        if band in [3, 80]:
            print('Bandwidth disponiveis: ', 10, 15, 20, 25, 30)
        if band == 12:
            print('Bandwidth disponiveis: ', 10, 15)
        if band == 39:
            print('Bandwidth disponiveis: ', 10, 15, 20, 25, 30, 40)
        if band == 40:
            print('Bandwidth disponiveis: ', 10, 15, 20, 25, 30, 40, 50, 60, 80, 100)
        if band == 41:
            print('Bandwidth disponiveis: ', 10, 15, 20, 40, 50, 60, 70, 80, 90, 100)
        if band == 50:
            print('Bandwidth disponiveis: ', 10, 15, 20, 40, 50, 60, 80)
        if band == 66:
            print('Bandwidth disponiveis: ', 10, 15, 20, 40)
        if band == 70:
            print('Bandwidth disponiveis: ', 10, 15, 20, 25)
        if band in [77, 78]:
            print('Bandwidth disponiveis: ', 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100)
        if band == 79:
            print('Bandwidth disponiveis: ', 40, 50, 60, 80, 100)
        if band == 86:
            print('Bandwidth disponiveis: ', 10, 15, 20, 40)
    if scs == 60:
        if band in [1, 2, 7, 25, 38, 65, 74, 75, 84]:
            print('Bandwidth disponiveis: ', 10, 15, 20)
        if band in [3, 80]:
            print('Bandwidth disponiveis: ', 10, 15, 20, 25, 30)
        if band == 39:
            print('Bandwidth disponiveis: ', 10, 15, 20, 25, 30, 40)
        if band == 40:
            print('Bandwidth disponiveis: ', 10, 15, 20, 25, 30, 40, 50, 60, 80, 100)
        if band == 41:
            print('Bandwidth disponiveis: ', 10, 15, 20, 40, 50, 60, 70, 80, 90, 100)
        if band == 50:
            print('Bandwidth disponiveis: ', 10, 15, 20, 40, 50, 60, 80)
        if band == 66:
            print('Bandwidth disponiveis: ', 10, 15, 20, 40)
        if band == 70:
            print('Bandwidth disponiveis: ', 10, 15, 20, 25)
        if band in [77, 78]:
            print('Bandwidth disponiveis: ', 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100)
        if band == 79:
            print('Bandwidth disponiveis: ', 40, 50, 60, 80, 100)
        if band == 86:
            print('Bandwidth disponiveis: ', 10, 15, 20, 40)


####################################################################################################
# Função que verifica se a bandwidth existe


def check_bandwidth(band, scs, bw):
    if scs == 15:
        if band in [1, 2, 5, 7, 8, 20, 25, 28, 38, 65, 71, 74, 81, 82, 83, 84]:
            if bw in [5, 10, 15, 20]:
                return True
            else:
                return False
        if band in [3, 80]:
            if bw in [5, 10, 15, 20, 25, 30]:
                return True
            else:
                return False
        if band in [34, 51, 76]:
            if bw == 5:
                return True
            else:
                return False
        if band == 39:
            if bw in [5, 10, 15, 20, 25, 30, 40]:
                return True
            else:
                return False
        if band in [66, 86]:
            if bw in [5, 10, 15, 20, 40]:
                return True
            else:
                return False
        if band == 40:
            if bw in [5, 10, 15, 20, 25, 30, 40, 50]:
                return True
            else:
                return False
        if band == 41:
            if bw in [10, 15, 20, 40, 50]:
                return True
            else:
                return False
        if band == 50:
            if bw in [5, 10, 15, 20, 40, 50]:
                return True
            else:
                return False
        if band in [77, 78]:
            if bw in [10, 15, 20, 30, 40, 50]:
                return True
            else:
                return False
        if band == 79:
            if bw in [40, 50]:
                return True
            else:
                return False
    if scs == 30:
        if band in [1, 2, 5, 7, 8, 20, 25, 28, 38, 65, 71, 74, 75, 81, 82, 83, 84]:
            if bw in [10, 15, 20]:
                return True
            else:
                return False
        if band in [3, 80]:
            if bw in [10, 15, 20, 25, 30]:
                return True
            else:
                return False
        if band == 12:
            if bw in [10, 15]:
                return True
            else:
                return False
        if band == 39:
            if bw in [10, 15, 20, 25, 30, 40]:
                return True
            else:
                return False
        if band == 40:
            if bw in [10, 15, 20, 25, 30, 40, 50, 60, 80, 100]:
                return True
            else:
                return False
        if band == 41:
            if bw in [10, 15, 20, 40, 50, 60, 70, 80, 90, 100]:
                return True
            else:
                return False
        if band == 50:
            if bw in [10, 15, 20, 40, 50, 60, 80]:
                return True
            else:
                return False
        if band == 66:
            if bw in [10, 15, 20, 40]:
                return True
            else:
                return False
        if band == 70:
            if bw in [10, 15, 20, 25]:
                return True
            else:
                return False
        if band in [77, 78]:
            if bw in [10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
                return True
            else:
                return False
        if band == 79:
            if bw in [40, 50, 60, 80, 100]:
                return True
            else:
                return False
        if band == 86:
            if bw in [10, 15, 20, 40]:
                return True
            else:
                return False
    if scs == 60:
        if band in [1, 2, 7, 25, 38, 65, 74, 75, 84]:
            if bw in [10, 15, 20]:
                return True
            else:
                return False
        if band in [3, 80]:
            if bw in [10, 15, 20, 25, 30]:
                return True
            else:
                return False
        if band == 39:
            if bw in [10, 15, 20, 25, 30, 40]:
                return True
            else:
                return False
        if band == 40:
            if bw in [10, 15, 20, 25, 30, 40, 50, 60, 80, 100]:
                return True
            else:
                return False
        if band == 41:
            if bw in [10, 15, 20, 40, 50, 60, 70, 80, 90, 100]:
                return True
            else:
                return False
        if band == 50:
            if bw in [10, 15, 20, 40, 50, 60, 80]:
                return True
            else:
                return False
        if band == 66:
            if bw in [10, 15, 20, 40]:
                return True
            else:
                return False
        if band == 70:
            if bw in [10, 15, 20, 25]:
                return True
            else:
                return False
        if band in [77, 78]:
            if bw in [10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
                return True
            else:
                return False
        if band == 79:
            if bw in [40, 50, 60, 80, 100]:
                return True
            else:
                return False
        if band == 86:
            if bw in [10, 15, 20, 40]:
                return True
            else:
                return False

def clear():
    if os.path.isfile('dest1.docx'):
        os.remove('dest1.docx')
    if os.path.isfile('result.txt'):
        os.remove('result.txt')
    if os.path.isfile('result_ping.txt'):
        os.remove('result_ping.txt')
    if os.path.isfile('logs_teste1.txt'):
        os.remove('logs_teste1.txt')
    if os.path.isfile('logs_teste2.txt'):
        os.remove('logs_teste2.txt')
    if os.path.isfile('logs_RAN.txt'):
        os.remove('logs_RAN.txt')
    if os.path.isfile('logs_gNB.txt'):
        os.remove('logs_gNB.txt')
    if os.path.isfile('logs_UE.txt'):
        os.remove('logs_UE.txt')
    if os.path.isfile('check_ip.txt'):
        os.remove('check_ip.txt')
    if os.path.isfile('ip_do_teste.txt'):
        os.remove('ip_do_teste.txt')
    if os.path.isfile('result_iperf.txt'):
        os.remove('result_iperf.txt')

