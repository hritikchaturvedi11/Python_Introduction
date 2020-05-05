import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#above three lines will not effect if included or not


#Actual code for basic funcationality
url = input('enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')




numbers = re.findall('([0-9]+)', soup.get_text() )

sum = 0
num = 0
for number in numbers:
    num = int(number)
    sum = num + sum

print(f'Sum of numbers ARE: {sum}')
