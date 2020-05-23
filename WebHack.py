import requests, re
import time
import sys
import os
from platform import platform

contries_info = {
    "max_pages": {
        "1": 82,                     
        "2": 720,                     
        "3": 232,                         
        "4": 38,                                  
        "5": 5,                 
        "6": 2,             
        "7": 107,                 
        "8": 48,                
        "9": 39,             
        "10": 54,
        "11": 7, 
        "12": 8,
        "13": 7,
        "14": 7, 
        "15": 6,
    },
    "codes": {
        "1": 'RU',
        "2": 'US',                    
        "3": 'JP'   ,                      
        "4": 'CA',                                 
        "5": 'NZ' ,              
        "6": 'UK',          
        "7": 'DE',            
        "8": 'AT',          
        "9": 'ES',      
        "10": 'TR',
        "11": 'HK',
        "12": 'GR',
        "13": 'PT',
        "14": 'SG',
        "15": 'CO',
    }
}

currentPlatform = platform()[:7]
if currentPlatform == 'Windows':
    delete = 'cls'
    dr = '\\'
else:
    delete = 'clear'
    dr = '/'



def find(country_index):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
    for page in range (0, contries_info["max_pages"][str(country_index)]):
        
        url = (f"https://www.insecam.org/en/bycountry/{contries_info['codes'][str(country_index)]}/?page={str(page)}")
    
        res = requests.get(url, headers=headers)
        findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                        
        for ip in findip:
            print ("\033[1;37m",ip)
            f = open('logs.txt' , 'a')
            f.write(f'{ip}' + '\n')
            f.close()

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
""")
num = int(input("country : "))

find(num)

print("Готово! Все логи были сохранены в файл logs.txt")
print("""
Subscribe to Yan4ik Channel on YouTube! 
https://youtube.com/channel/UCu6l8wKI7WGlwoD1It_vcdw
--Thanks for using this programm!--

MODIFIED BY 0X40

------Version 1.1------
""")
