import requests,re,os
import time
import sys
from os import system
from platform import platform
from time import sleep
import os
puk = platform()

if "Windows" in puk:
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'

os.system(delet)
time.sleep(1)

print("loading modules...")
time.sleep(1)
os.system(delet)

print("""
█───█
█───█
█─█─█
█████
─█─█
""")
time.sleep(0.1)
os.system(delet)
print("""
█───█──███
█───█──█
█─█─█──███
█████──█
─█─█───███
""")
time.sleep(0.1)
os.system(delet)
print("""
█───█──███──████
█───█──█────█──██
█─█─█──███──████
█████──█────█──██
─█─█───███──████
""")
time.sleep(0.1)
os.system(delet)
print("""
█───█──███──████───█──█
█───█──█────█──██──█──█
█─█─█──███──████───████
█████──█────█──██──█──█
─█─█───███──████───█──█
""")
time.sleep(0.1)
os.system(delet)
print("""
█───█──███──████───█──█──████
█───█──█────█──██──█──█──█──█
█─█─█──███──████───████──████
█████──█────█──██──█──█──█──█
─█─█───███──████───█──█──█──█
""")
time.sleep(0.1)
os.system(delet)
print("""
█───█──███──████───█──█──████──████
█───█──█────█──██──█──█──█──█──█──█
█─█─█──███──████───████──████──█
█████──█────█──██──█──█──█──█──█──█
─█─█───███──████───█──█──█──█──████
""")
time.sleep(0.1)
os.system(delet)
print("""
█───█──███──████───█──█──████──████──█──█
█───█──█────█──██──█──█──█──█──█──█──█─█
█─█─█──███──████───████──████──█─────██
█████──█────█──██──█──█──█──█──█──█──█─█
─█─█───███──████───█──█──█──█──████──█──█
""")
time.sleep(0.3)
os.system(delet)
print("""
████
█──██
████
█──██
████
""")
time.sleep(0.1)
os.system(delet)
print("""
████───██─██
█──██───███
████─────█
█──██────█
████─────█
─────────█
""")
time.sleep(0.1)
os.system(delet)
print("""
████───██─██──────██─██
█──██───███────────███
████─────█──────────█
█──██────█──────────█
████─────█──────────█
─────────█──────────█
""")
time.sleep(0.1)
os.system(delet)
print("""
████───██─██──────██─██
█──██───███────────███
████─────█──────────█
█──██────█──────────█
████─────█──────────█
─────────█──────────█
""")
time.sleep(0.1)
os.system(delet)
print("""
████───██─██
█──██───███
████─────█
█──██────█
████─────█
─────────█

██─██──████──█──█
─███───█──█──██─█
──█────████──█─██
──█────█──█──█──█
──█────█──█──█──█
──█
""")
time.sleep(0.1)
os.system(delet)
print("""
████───██─██
█──██───███
████─────█
█──██────█
████─────█
─────────█

██─██──████──█──█──█──█
─███───█──█──██─█──█──█
──█────████──█─██──████
──█────█──█──█──█─────█
──█────█──█──█──█─────█
──█
""")
time.sleep(0.1)
os.system(delet)
print("""
████───██─██
█──██───███
████─────█
█──██────█
████─────█
─────────█

██─██──████──█──█──█──█──███
─███───█──█──██─█──█──█───█
──█────████──█─██──████───█
──█────█──█──█──█─────█───█
──█────█──█──█──█─────█──███
──█
""")
time.sleep(0.1)
os.system(delet)
print("""
████───██─██
█──██───███
████─────█
█──██────█
████─────█
─────────█

██─██──████──█──█──█──█──███──█──█
─███───█──█──██─█──█──█───█───█─█
──█────████──█─██──████───█───██
──█────█──█──█──█─────█───█───█─█
──█────█──█──█──█─────█──███──█──█
──█
""")
time.sleep(1)
os.system(delet)
print('------Version 1.2------\n')
time.sleep(2)
os.system(delet)
print("""
Subscribe to Yan4ik Channel on YouTube! 
https://youtube.com/channel/UCu6l8wKI7WGlwoD1It_vcdw

------Version 1.2------
""")
time.sleep(2)
os.system(delet)
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
Subscribe to Yan4ik Channel on YouTube! 
https://youtube.com/channel/UCu6l8wKI7WGlwoD1It_vcdw
------Version 1.2------                      
""")

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
countries = ["RU", "US", "JP", "CA", "NZ", "UK", "DE", "AT", "ES", "TR", "HK", "GR", "PT", "SG", "CO"]
country_ranges = [82, 720, 232, 38, 5, 2, 107, 48, 39, 54, 7, 8, 7, 7, 6]

def scan(chosen_num: int):
    os.system(delet)
    url = f"https://www.insecam.org/en/bycountry/{countries[chosen_num - 1]}/?page="
    page_range_max = country_ranges[chosen_num - 1]
    
    for i in range(0, page_range_max):
        res = requests.get(url+str(i), headers=headers)
        findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
        count = 0
        ips = []
        for ii in findip:
            hasil = findip[count]
            print ("\033[1;37m",hasil)
            ips.append(hasil)
            count += 1
        f = open("logs.txt", "a")
        for j in ips:
            f.write(j + "\n")
        f.close()
    


num = int(input("country : "))

scan(num)

print("Готово! Все логи были сохранены в файл logs.txt")
print("""
Subscribe to Yan4ik Channel on YouTube! 
https://youtube.com/channel/UCu6l8wKI7WGlwoD1It_vcdw
--Thanks for using this programm!--

MODYFIED BY 0X40

------Version 1.1------
""")
