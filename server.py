import socket
from Login import LoginLogic

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    User = clientsocket.recv(8)
    User = User.decode("utf-8")
    print(User)
    Pass = clientsocket.recv(8)
    Pass = Pass.decode("utf-8")
    print(Pass)
    
    LogLogic = LoginLogic(User,Pass)
    if LogLogic == 1:
        print("Login Successful")
        clientsocket.send(bytes("1","utf-8"))
    else:
        print("Login Unsuccessful")
        clientsocket.send(bytes("0","utf-8"))
   
    
    
    
    
    
