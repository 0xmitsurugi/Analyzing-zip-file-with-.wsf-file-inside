#! /usr/bin/python

import sys,zipfile,re

def read_zip(filepath):
    zfile = zipfile.ZipFile(filepath)
    zipname=zfile.namelist()
    if len(zipname) == 1 and zipname[0].endswith(".wsf"):
        print "[+] Ok zip contains one file ending in .wsf"
        wsf_data=zfile.read(zipname[0])
        return wsf_data
    else:
        print "[ ] Doesn't look like good, more than one file in zip,"
        print "    or not ending with .wsf"

def extract_stage2(data):
    var_sum=""
    data=data.split("\n")
    for line in data:
        while line.startswith(" "):
            line=line[1:]
        #if line.startswith("<"):
        #    print "[ ] skipping tag"
        if (re.search("\+",line)>0) and (re.search(";",line)<0):
               var_sum=var_sum+line
        if (re.search(";",line)>0) and (re.search("^'\w+'",line)>0):
            var_sum=eval(var_sum+line.split(";")[0]+' ')
        if line.startswith("var "):
            if len(line) > 250:
                print "[+] Assigning a long var, seems good"
                #Extracting the part after the '=' and without the final ;
                var = line.split("=")
                var_sum=(('='.join(var[1:]))[:-1])
                var_sum=eval(var_sum)
        if (line.find("reverse") > 0):
            print "[+] We have to reverse the string"
            var_sum=var_sum[::-1]
            #print line
        if (line.find("split") > 0):
            split_char = line.split("\"")[-2:-1][0].decode('string-escape')
            #print split_char
            if len(split_char) == 0:
                #print "    No char to split with, doing nothing"
                True
            else:
                print "[+] Splitting and joining string with char %s" % split_char
                var_sum=''.join(var_sum.split(split_char))
    return var_sum        

def parse_line(line):
    var_name="None"
    var_value="None"
    #print line
    if line.startswith("var ") and re.search("\"",line):
        #print line
        var_name=line.split("=")[0].split(" ")[1]
        var_value=eval((line.split("=")[1]).split(";")[0])
    if line.startswith("function"):
        items=line.split(";")
        for item in items:
            if item.startswith("var "):
                var_name=item.split("=")[0].split(" ")[1]
                var_value=eval(item.split("=")[1])
    return var_name,var_value

def extract_URL(data):
    data=data.split("\n")
    i=0
    #The first occurence of WScript is the end of var declarations
    for line in data:
        i+=1
        if line.find("WScript")>0:
            break 
    data=data[0:i]
    #Filling up a big dict with all vars
    dict_var={}
    for all_vars in data:
        var_name,var_value=parse_line(all_vars)
        dict_var[var_name]=var_value
    #print dict_var
    #searching for a table of URL
    URLs=""
    for line in data:
        if re.search("^var.*\[(.*,){1,5}.*\]",line):
            URLs=line.split("[")[1].split("]")[0].split(",")
    #printing URLS
    if len(URLs)<2:
        print "[ ] Unable to find URL table in data."
        print "    Exiting cowardly"
        exit(1)
    URL_tab=[]
    for U in URLs:
        output=""
        U=U.split("+")
        for a in U:
            a=a.strip()
            if dict_var.has_key(a):
                output=output+dict_var[a]
            elif re.search("\w+\(\w+\)",a):
                k=a.split("(")[1].split(")")[0]
                output=output+dict_var[k]
            else:
                k=a.split(";")[0].split(" ")[2]
                output=output+dict_var[k]
        URL_tab.append(output)          
                
    return URL_tab

### MAIN
#At first, extract the zipped file
print "Extracting zip"
wsf_data=read_zip(sys.argv[1])
#Then, we add all vars, split, reverse and join data to get an obfuscated js
print "Get obfusctated js"
obfus_js = extract_stage2(wsf_data)
#Then, we try to extract relevant data
#print obfus_js
print "Parsing obfuscated and getting URLs"
URLS = extract_URL(obfus_js)
print "[+] printing download URLs"
for U in URLS:
    print "    " + U
