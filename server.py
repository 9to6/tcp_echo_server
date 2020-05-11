import socket
import sys

port = 10000
if len(sys.argv) > 1:
  port = int(sys.argv[1])

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('', port)
sock.bind(server_address)
sock.listen(10)

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
