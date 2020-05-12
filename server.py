import socket
import sys

port = 10000
if len(sys.argv) > 1:
  port = int(sys.argv[1])

addr = ("0.0.0.0", port)  # all interfaces, port 8080
if socket.has_dualstack_ipv6():
    sock = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
else:
    sock = socket.create_server(addr)
sock.listen(10)

#HOST = None               # Symbolic name meaning all available interfaces
#s = None
#for res in socket.getaddrinfo(HOST, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
#    af, socktype, proto, canonname, sa = res
#    try:
#        s = socket.socket(af, socktype, proto)
#    except OSError as msg:
#        s = None
#        continue
#    try:
#        s.bind(sa)
#        s.listen(10)
#    except OSError as msg:
#        s.close()
#        s = None
#        continue
#    break
#
#sock = s

while True:
  print('waiting for a connection')
  connection, client_address = sock.accept()
  try:
    #print('client connected: {}'.format(client_address))
    while True:
      data = connection.recv(16)
      if len(data) > 0:
        print('received "{}"'.format(data.decode('utf-8')))
        if data:
          connection.sendall(data)
        else:
          break
  finally:
    connection.close()
