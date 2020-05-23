import time
import sys
import os

from utils import find

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

index = int(input("country: "))
find(index)

print("Готово! Все логи были сохранены в файл logs.txt")
print("""
Subscribe to Yan4ik Channel on YouTube! 
https://youtube.com/channel/UCu6l8wKI7WGlwoD1It_vcdw
--Thanks for using this programm!--

MODIFIED BY 0X40

------Version 1.1------
""")
