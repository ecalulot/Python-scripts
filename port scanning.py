#!/usr/bin/python
import socket
import subprocess
import sys
from datetime import datetime


#Ask for IP
#translate a host name to IPv4 address format
hostname=socket.gethostbyname(input('Please enter IP Address: \n: '))



#record time started
timein=datetime.now()
print('-'*100)
portamount=int(input('Scan ports (1-X).  \nEnter X: '))
print('-'*100)

try:
    for port in range(1,portamount):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=sock.connect_ex((hostname,port))
        if result == 0:
            print('Port{}:   Open'.format(port))
            sock.close()
        else:
            print('Port{}:   Closed'.format(port))
            sock.close()
except KeyboardInterrupt:
    Print('You stopped the scan. \n')
    sys.exit()

#Get IP Address Info Error
except socket.gaierror:
    print('Host can not be resolved \n')
    sys.exit()
                  
except socket.error:
    print('Host can not be connected to. \n')
    sys.exit()

timeout=datetime.now()
                  
timeamount=timeout-timein

print(timeamount)
