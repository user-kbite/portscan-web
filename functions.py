import socket
import array as arr

def portScan(ip):
    ports = []
    
    for i in range(1, 10001):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        connect = s.connect_ex((ip, i))
        if connect == 0:
            ports.append(i)
            #return str(i) + ' >>> OPEN'
        else:
            pass
            #print(i, '>>> CLOSED')
        #print(i)
    return ports
    print('Finish !')