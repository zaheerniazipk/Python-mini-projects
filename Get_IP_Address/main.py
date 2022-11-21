##############################
# Get IP Address
###############################
import socket

hostname = socket.gethostname()

IP_Address = socket.gethostbyname(hostname)

print("IP Address: " + IP_Address)
