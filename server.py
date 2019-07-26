##########################################################
#   Title   : Socket Programming Assignment 1: Web Server
#   Name    : Meir Zeevi
#   File    : ServerExtra.py
#   NYU ID  : N11290134
#   Version : 1.0.0
#   Python 3 interpreter
##########################################################

import threading
from socket import *

def set_up_connection(outputdata,connectionSocket):
   print(threading.current_thread().getName()+"\n")
   try:
      message = None
      message = connectionSocket.recv(500)
      filename = message.split()[1]

      f = open(filename[1:], 'rb')
      connectionSocket.send(b"HTTP/1.1 200 OK\r\n" + outputdata)

      for i in f:
         connectionSocket.send(i)
      connectionSocket.close()

   except IOError:
      connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n" + outputdata + b"<html>\n<body>\n<h1>404 not found!!</h1>\n</body>\n</html>\n")
      connectionSocket.close()




serverSocket = socket(AF_INET, SOCK_STREAM)


serverSocket.bind((gethostbyname(''), 6789))
serverSocket.listen(5)
i=0
while True:
    #Establish the connection

    print('Ready to serve...')
    i+=1
    connectionSocket, addr = serverSocket.accept()
    outputdata =     b"Connection: close\r\nDate: Mon, 17 Sep 2018 01:40:08 GMT\r\nServer: Apache/2.4.6 (CentOS)\r\nLast-Modified: Sun, 16 Sep 2018 05:59:02 GMT\r\nAccept-Ranges: bytes\r\nContent-Length: 81\r\nContent-Type: text/html\r\n\r\n"

    thread = threading.Thread(name="I am Thread Number: "+str(i), target=set_up_connection, args=(outputdata,connectionSocket,))
    thread.start()



