import random
import socket
import time

host = '127.0.0.1'
port = '-1'

while(True):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port = str(random.randint(1000, 2000))
    try:
        print 'Try ' + port
        s.bind((host, int(port)))
        break
    except Exception as e:
        print e
        continue
print port
s.listen(5)

while True:
    tcpsock, addr = s.accept()
    tcpsock.send('KanColle Mac')
    if tcpsock.recv(4096) == 'KanColle Mac':
        print 'Accepted connection'
        break
f = open('raw.txt', 'w')
buf = ''
while True:
    tmp = tcpsock.recv(4096)
    lst = tmp.split('\n')
    buf = buf + lst[0]
    if(len(lst) != 1):
        if('svdata' in buf):
            f.write(buf + '\n')
        buf = ''
    for i in range(1, len(lst) - 1):
        if('svdata' in lst[i]):
            f.write(lst[i] + '\n')
    if(len(lst) != 1):
        buf = lst[len(lst) - 1]
    f.flush()
f.close()
s.close()