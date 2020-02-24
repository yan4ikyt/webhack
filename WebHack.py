import requests,re,os
import time
import sys
from os import system
from platform import platform
from time import sleep
import os

delet, dr = 'clear', '/'
if platform() == 'Windows':
    delet = 'cls'
    dr = '\\\\'

print("Welcome to camera-hack!")
print("Please select country for hack :")
print("""
1. Russian Federation
2. United States
3. Japan
4. Canada
5. New Zealand
6. Ukraine
7. Germany
8. Austria
9. Spain
10. Turkey
11. Hong Kong
12. Greece
13. Portugal
14. Singapure
15. Columbia

----Project by Yan4ik----
MODYFIED BY 0X40 (t.me/codingbots)
MODYFIED By @duckdefuck (t.me/duckdefuck)
------Version 2------                      
""")

num = int(input("country : "))
print("\\n")        
os.system(delet)

inf = [
    { "code":'RU', "to": 82 },
    { "code":'US', "to": 720 },
    { "code":'JP', "to": 232 },
    { "code":'CA', "to": 38 },
    { "code":'NZ', "to": 5 },
    { "code":'UK', "to": 2 },
    { "code":'DE', "to": 107 },
    { "code":'AT', "to": 48 },
    { "code":'ES', "to": 39 },
    { "code":'TR', "to": 54 },
    { "code":'HK', "to": 7 },
    { "code":'GR', "to": 8 },
    { "code":'PT', "to": 7 },
    { "code":'SG', "to": 7 },
    { "code":'CO', "to": 6 }
][num-1]

f = open('logs.txt', 'a')
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}

for page in range(0, inf["to"]):
    res = requests.get("https://www.insecam.org/en/bycountry/"+inf["code"]+"/?page="+str(page), headers=headers)
    
    findip = re.findall('http://\\d+.\\d+.\\d+.\\d+:\\d+', res.text)
    
    for index in range(len(findip)): 
        f.write(f'{findip[index]}' + '\n')

f.close()
print("All done! All cameras IP addresses in logs.txt")
