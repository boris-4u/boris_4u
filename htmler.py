# Name:         htmler.py (written in Python) 
# Author:       Boris Radic  
# Date:         20.07.2025 2
# Description:  Builds html files  
#                
# Usage:        htmler.py
#
import os
import sys
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

#
# Main program
#
if len(sys.argv) != 2: sys.exit("Usage: py htmler.py | py htmler.py <Multi_FO_EU|Multi_FO_CH|Single_FO_EU>")
if (sys.argv[1] != "Multi_FO_EU" and sys.argv[1] != "Multi_FO_CH" and sys.argv[1] != "Single_FO_EU"): 
    sys.exit("Usage: py htmler.py <Multi_FO_EU|Multi_FO_CH|Single_FO_EU>")

target = sys.argv[1]

#
# Color mappings with dico vars
#
color_title_d = {"Multi_FO_EU":"#ff0000","Multi_FO_CH":"#0000ff","Single_FO_EU":"green"}
color_FO_d = {"Multi_FO_EU":"#ffcccc","Multi_FO_CH":"#ccccff","Single_FO_EU":"#ccffcc"}

#
# Building Sub_target menu
#
counter = 1
for file in os.listdir(target+"/"):
    if file.endswith('.html'):
        counter += 1

with open("Sub_"+target+".html","w") as w:
    w.write("<html><head></head><body><table bgcolor="+color_FO_d[target]+">\n")
    w.write("<tr><td align=center><font size=+2 color="+color_title_d[target]+"><b>"+target+"</b></font></td></tr>\n")
    w.write("<tr><td align=center><font color="+color_title_d[target]+">"+str(counter)+" sites</font></td></tr>\n")
    w.write("<tr><td align=center><font color="+color_title_d[target]+"></font></td></tr>\n")
    w.write("<tr><td><a href=Tokens_Compounds_"+target+".html target=data>Tokens & Compounds</a></td></tr>\n")
    w.write("<tr><td><font color="+color_title_d[target]+">VVVVVVVVVVVV</font></td></tr>\n")
    w.write("<tr><td><a href=Site_to_Tokens_"+target+".html target=data>Site to Tokens</a></td></tr>\n")
    w.write("<tr><td><a href=Token_to_Sites_"+target+".html target=data>Token to Sites</a></td></tr>\n")
    w.write("<tr><td><a href=Site_to_Compounds_"+target+".html target=data>Site to Compounds</a></td></tr>\n")
    w.write("<tr><td><a href=Compound_to_Sites_"+target+".html target=data>Compound to Sites</a></td></tr>\n")
    w.write("</table></body></html>\n")

#
# Building site_tokens_d
#
site_tokens_d = {};
i_tmp = ""
with open("tokener_results_"+target+".txt") as f:
    for i in f:
        if re.search("^===",i):
            i = i.split();
            site_tokens_d[i[3]] = ""
            i_tmp = i[3]
        else:
            site_tokens_d[i_tmp] = site_tokens_d[i_tmp] + " " + i.strip();

#
# Building sorted tokens list with target/tokens.txt
#
tokens = []
with open(target+"/tokens.txt") as r:
    [ tokens.append(i.strip().lower()) for i in r ]
tokens = sorted(set(tokens))

#
# Building sorted compounds list with target/compounds.txt
#
compounds = []
with open(target+"/compounds.txt") as r:
    [ compounds.append(i.strip().lower()) for i in r ]
compounds = sorted(set(compounds))

#
# Building "Tokens_Compounds_"+target+".html"
#
t = tt = c = cc = ""

half_left_t = len(tokens) // 2 + 1
half_left_c = len(compounds) // 2 + 1

with open("Tokens_Compounds_"+target+".html","w") as w:
    for i in range(half_left_t):
        t = t+"</li><li>"+tokens[i]
    for i in range(half_left_t,len(tokens)):
        tt = tt+"</li><li>"+tokens[i]

    for i in range(half_left_c):
        c = c+"</li><li>"+compounds[i]
    for i in range(half_left_c,len(compounds)):
        cc = cc+"</li><li>"+compounds[i]
    
    w.write("<html><head></head><body bgcolor="+color_FO_d[target]+"><table width=100% border=0>\n")
    w.write("<tr><td width=50% align=center><font size=+2 color="+color_title_d[target]+"><b>Tokens</b></font>\n")
    w.write("<td><td width=50% align=center><font size=+2 color="+color_title_d[target]+"><b>Compounds</b></font>\n")
    w.write("</td></tr></table><table width=100% border=1><tr><td width=25% valign=top>"+t+"</td>\n")
    w.write("<td width=25% valign=top>"+tt+"</td><td width=25% valign=top>"+c+"</td>\n")
    w.write("<td width=25% valign=top>"+cc+"</td></tr></table></body></html>")
    
#
# Building token_sites_d
#
token_sites_d = {};
for t in tokens:
    token_sites_d[t] = ""
    for i in site_tokens_d.keys():
        for j in site_tokens_d[i].split():
            if t == j:
                token_sites_d[t] = token_sites_d[t] + " " + i

#
# Building Site_to_Tokens_target.html with site_tokens_d
#
with open("Site_to_Tokens_"+target+".html","w") as w:
    w.write("<html><head></head><body bgcolor="+color_FO_d[target]+"><table width=100% border=1>");
    w.write("<h2 align=center>\n")
    w.write("<font color="+color_title_d[target]+">"+"Site_to_Tokens_"+target+".html".replace(".html","")+"</font></h2>")
    counter = 1
    for i in site_tokens_d.keys():
        if site_tokens_d[i]:
            w.write("<tr><td>"+str(counter)+"</td>\n")
            w.write("<td>"+i.replace("_",".").replace(".html","")+" "+str(len(site_tokens_d[i].split()))+"</td>\n") 
            w.write("<td>"+site_tokens_d[i]+"</td></tr>");
            counter += 1
    w.write("</table></body></html>");

#
# Building Tokens_to_Sites_target.html with token_sites_d
#
with open("Token_to_Sites_"+target+".html","w") as w:
    w.write("<html><head></head><body bgcolor="+color_FO_d[target]+"><table width=100% border=1>");
    w.write("<h2 align=center>\n")
    w.write("<font color="+color_title_d[target]+">"+"Token_to_Sites_"+target+".html".replace(".html","")+"</font></h2>")
    counter = 1
    for i in token_sites_d.keys():
        if token_sites_d[i]:
            w.write("<tr><td>"+str(counter)+"</td><td>"+i+" "+str(len(token_sites_d[i].split()))+"</td><td>")
            for k in token_sites_d[i].split():
                w.write("<li>"+k.replace("_",".").replace(".html","")+"</li>");
            counter += 1
            w.write("</td></tr>")
    w.write("</table></body></html>");

#
# Building site_compounds_d
#
site_compounds_d = {}
i_tmp = ""
counter = 1
with open("compounder_results_"+target+".txt") as f:
    for i in f:
        if re.search("^===",i):
            i = i.split()
            site_compounds_d[i[3]] = ""
            i_tmp = i[3]
        else:
            site_compounds_d[i_tmp] = site_compounds_d[i_tmp] + " " + i.strip()+",";

#
# Building compound_sites_d
#            
compound_sites_d = {}
for t in compounds:
    compound_sites_d[t] = ""
    for i in site_compounds_d.keys():
        for j in site_compounds_d[i].split(","):
            if str(t.strip()) == str(j.strip()):
                compound_sites_d[t] = compound_sites_d[t] + " " + i
            
#
# Building Site_to_Compounds_target.html with site_compounds_d
#
with open("Site_to_Compounds_"+target+".html","w") as w:
    w.write("<html><head></head><body bgcolor="+color_FO_d[target]+"><table width=100% border=1>");
    w.write("<h2 align=center>\n")
    w.write("<font color="+color_title_d[target]+">"+"Site_to_Compounds_"+target+".html".replace(".html","")+"</font></h2>")
    counter = 1
    for i in site_compounds_d.keys():
        if site_compounds_d[i]:
            w.write("<tr><td>"+str(counter)+"</td>\n")
            w.write("<td>"+i.replace("_",".").replace(".html","")+" "+str(len(site_compounds_d[i].split(","))-1)+"</td>\n")
            w.write("<td>"+site_compounds_d[i].rstrip(",")+"</td></tr>");
            counter += 1
    w.write("</table></body></html>");

#
# Building Compound_to_Sites_target.html with compound_sites_d
#   
with open("Compound_to_Sites_"+target+".html","w") as w:
    w.write("<html><head></head><body bgcolor="+color_FO_d[target]+"><table width=100% border=1>");
    w.write("<h2 align=center>\n")
    w.write("<font color="+color_title_d[target]+">"+"Compound_to_Sites_"+target+".html".replace(".html","")+"</font></h2>")
    counter = 1
    for i in compound_sites_d.keys():
        if compound_sites_d[i]:
            w.write("<tr><td>"+str(counter)+"</td><td>"+i+" "+str(len(compound_sites_d[i].split()))+"</td><td>")
            for c in compound_sites_d[i].split():
                w.write("<li>"+c.replace("_",".").replace(".html","")+"</li>");
            counter += 1
            w.write("</td></tr>")
    w.write("</table></body></html>");
