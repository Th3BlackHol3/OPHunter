#!/bin/python3

from socket import *
import time
startTime = time.time()

print('''

  ██████╗ ██████╗ ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
 ██╔═══██╗██╔══██╗██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
 ██║   ██║██████╔╝███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
 ██║   ██║██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
 ╚██████╔╝██║     ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
  ╚═════╝ ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                     
Developed by Th3 BlackHol3
https://twitter.com/Th3BlackHol3_

''')


if __name__ == '__main__':
   target = input('Enter the Target IP: ')
   t_IP = gethostbyname(target)
   print ('Firing Gamma-Rays on Target: ', t_IP)
   
   print ('Be Patient! Gamma-Rays will Hit 65535 Ports!')
   
   for i in range(1, 65535):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()
print('Time taken:', time.time() - startTime)
