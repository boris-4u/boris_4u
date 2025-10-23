# Name:         getsites.py (written in Python) 
# Author:       Boris Radic  
# Date:         20.07.2025 
# Description:  Downloads in C:\Users\IT\DuraWealth\<target> the sites listed in 
#               C:\Users\IT\DuraWealth\<target>\<target>.txt
#
# Usage:        getsites.py <Multi_FO_EU|Multi_FO_CH|Single_FO_EU>
#
import os
import re
import sys
import ssl
import urllib
import requests

from urllib.request import urlretrieve

if len(sys.argv) != 2: sys.exit("Usage: getsites.py | getsites.py <Multi_FO_EU|Multi_FO_CH|Single_FO_EU>")
if (sys.argv[1] != "Multi_FO_EU" and sys.argv[1] != "Multi_FO_CH" and sys.argv[1] != "Single_FO_EU"): 
    sys.exit("Usage: getsites.py <Multi_FO_EU|Multi_FO_CH|Single_FO_EU>")

target = sys.argv[1]
os.chdir("C:/Users/IT/DuraWealth/"+target)

with open(target+'.txt') as textfile:  
    counter = 1
    for url in textfile:
        print("Opening ",counter,":",url)
        url = url.strip()
        url = url.rstrip("/")
        filename = url
        filename = filename.replace(".","_")
        filename = filename + ".html"
        filename = (filename.split("//"))[1]
        filename = filename.replace("/","_")
        #print("Downloading: ",counter,":",filename)
        counter += 1
        #context = ssl._create_unverified_context()
        #response = urllib.request.urlopen(url, context=context)
  
        try:
            response = requests.get(url, verify=False, headers={'User-Agent': 'Mozilla/5.0'})
        except:
            with open("download_failed.txt", "a") as w:
                w.write(url+"\n")
        else:
            with open(filename, "wb") as w:
                w.write(response.content)

sys.exit("Done")