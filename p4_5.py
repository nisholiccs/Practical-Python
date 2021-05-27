# Write a python program that reads the source code of a Web page.
import sys
import urllib.request

url="https://web.whatsapp.com/"
webpage=urllib.request.urlopen(url)
print("source code of ",url)
print(webpage.read())
