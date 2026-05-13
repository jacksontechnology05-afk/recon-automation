import socket

target = input("Enter target IP: ")
port = int(input("Enter port: "))

s = socket.socket()
s.connect((target, port))

banner = s.recv(1024)

print(f"Banner: {banner.decode()}")

s.close()
