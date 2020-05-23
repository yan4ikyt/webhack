import requests
import re

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