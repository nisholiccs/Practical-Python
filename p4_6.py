# Write a python program that reads the source code of a Web page.
import urllib.request, urllib.error, urllib.parse

url="https://www.youtube.com/"

response = urllib.request.urlopen(url)
webContent = response.read()

f = open('youtube.html', 'wb')
f.write(webContent)
f.close
print("\n\tFile Downloaded")
