import socket
import sys
import time

def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )


families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

t0 = time.perf_counter()
# Create a TCP/IP socket
#sock = socket.create_connection(('test-NLB-AC01-fc2a3ed6a807441e.elb.us-east-1.amazonaws.com', 10000))
#sock = socket.create_connection(('test-NLB-AC01-2697fb3930d68527.elb.us-east-1.amazonaws.com', 10000))
#sock = socket.create_connection(('10.25.212.134', 10000))
sock = socket.create_connection(('localhost', 2701))

print ('Family  :', families[sock.family])
print ('Type    :', types[sock.type])
print ('Protocol:', protocols[sock.proto])

try:
    while(True):
      time.sleep(2)
      # Send data
      print(sys.argv[1])
      message = 'echo {}'.format(sys.argv[1])
      print('sending "{}"'.format(message))
      sock.sendall(message.encode())
      print('sended')

      amount_received = 0
      amount_expected = len(message)

      while amount_received < amount_expected:
          data = sock.recv(16)
          amount_received += len(data)
          print('received "{}"'.format(data.decode('utf-8')))

except KeyboardInterrupt:
        print('Interrupted')

finally:
    print('closing socket')
    sock.close()
    print("Time elapsed: ", time.perf_counter() - t0) # CPU seconds elapsed (floating point)
