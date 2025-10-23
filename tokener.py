# Name:         tokener.py (written in Python) 
# Author:       Boris Radic  
# Date:         20.07.2025 
# Description:  Fetches in C:\Users\IT\DuraWealth\<target> the downloaded html files  
#                
# Usage:        tokener.py <Multi_FO_EU|Multi_FO_CH|Single_FO_EU> | tokener.py <Multi_FO_EU|Multi_FO_CH|Single_FO_EU> <html_file>  
#
#               with one argument:  sweeps all html files in C:\Users\IT\DuraWealth\sys.argv[1]                         
#               with two arguments: processes C:\Users\IT\DuraWealth\sys.argv[1]\<html_file> 
#
import os
import sys
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

#
# Function look_for_token
#
def look_for_token(file):
    buffer = []
    for line in file:
        if line.lstrip("^  *").startswith("@font-face") == True: continue
        if line.lstrip("^  *").startswith("@charset") == True: continue
        if line.find("<option value=\"silver\">") != -1: continue
        if line.find("silver: [") != -1: continue
        if line.find("{background:silver;") != -1: continue
        if line.find(",\"silver\":") != -1: continue
        if line.find("{color:silver}") != -1: continue
        if line.find("--color--gold") != -1: continue
        if line.find("-gold") != -1: continue
        if line.find("gold-line") != -1: continue
        if line.find("-gold.png") != -1: continue
        if line.find("class=\"gold") != -1: continue
        if line.find("bg-gold") != -1: continue
        if line.find("left gold panel") != -1: continue
        if line.find("gold\">") != -1: continue
        if line.find("hintergrund gold") != -1: continue
        if line.find("clip-path--diamond") != -1: continue
        if line.find(":root{--wp") != -1: continue

        line = line.strip().replace("IT","information technology").lower()
        word_tokens = word_tokenize(line)
        buffer.extend(word_tokens)

    for token in sorted(set(buffer)): is_token_in(token)

#
# Function 'is_token_in': sweeps tokens list an compares with parameter token
#
def is_token_in(token):
    for t in tokens:
        if t == token: print(token)

#
# Main program
#
if len(sys.argv) == 1 or len(sys.argv) > 3: sys.exit("Usage: tokener.py <dir> | tokener.py <dir> <client.html>")

try:
    os.chdir(sys.argv[1])
except:
    sys.exit(sys.argv[1]+": No such dir")

#
# Building tokens list with tokens.txt
#
tokens = []
with open("tokens.txt", encoding='latin-1') as textfile:
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
