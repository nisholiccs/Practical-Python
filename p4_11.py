# Write a python program to create a UDP server that sends messages to the client.
import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 1234

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
	data, addr = serverSock.recvfrom(1024)
	print ("Message: " + data.decode())
