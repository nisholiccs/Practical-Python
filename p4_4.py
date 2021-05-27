# Write a python program to find the IP Address of a website.
# Python Program to Get IP Address 
import socket 
hostname = socket.gethostname() 
IPAddr = socket.gethostbyname(hostname) 
print("Your Computer Name is:" + hostname) 
print("Your Computer IP Address is:" + IPAddr)
