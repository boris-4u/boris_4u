# Name:         compounder.py (written in Python) 
# Author:       Boris Radic  
# Date:         20.07.2025 
# Description:  Fetches in C:\Users\IT\DuraWealth\<target> the downloaded html files  
#                
# Usage:        compounder.py <Multi_FO_EU|Multi_FO_CH|Single_FO_EU> | compounder.py <Multi_FO_EU|Multi_FO_CH|Single_FO_EU> <html_file>  
#
#               with one argument:  sweeps all html files in C:\Users\IT\DuraWealth\sys.argv[1]                         
#               with two arguments: processes C:\Users\IT\DuraWealth\sys.argv[1]\<html_file> 
#
import os
import sys
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, line_tokenize

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

#
# Function look_for_token
#
def look_for_token(file):
    buffer = []
    for lines in file:
        for line in line_tokenize(lines.strip().lower()):                 
            for token in tokens:
                if re.findall(" "+token+" ",line) != []:
                    buffer.append(token)
    [ print(result) for result in sorted(set(buffer)) ]

#
# Main program
#
if len(sys.argv) == 1 or len(sys.argv) > 3: sys.exit("Usage: py compounder.py <dir> | py compounder.py <dir> <client.html>")

try:
    os.chdir(sys.argv[1])
except:
    sys.exit(sys.argv[1]+": No such dir")

#
# Building tokens list with tokens.txt
#
tokens = []
with open("compounds.txt", encoding='latin-1') as textfile:
    [ tokens.append(token.strip().lower()) for token in textfile ]

if len(sys.argv) == 3:
    try:
        with open(sys.argv[2], encoding='latin-1') as htmlfile:
            print("===> ",sys.argv[1])
            look_for_token(htmlfile)
    except:
        sys.exit(sys.argv[2]+": No such html file in "+sys.argv[1])
    sys.exit("Done")

#
# Browsing all C:\Users\IT\DuraWealth\sys.argv[1]\*.html files
#
counter = 1
for file in os.listdir("./"):
    if file.endswith('.html'):
        with open(file, encoding='latin-1') as htmlfile:  
            print("===> ",counter,":",file)
            counter += 1
            look_for_token(htmlfile)
          
sys.exit("Done")