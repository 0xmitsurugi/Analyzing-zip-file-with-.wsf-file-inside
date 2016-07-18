#! /usr/bin/python

import sys

f=open(sys.argv[1],"ro")
data=f.read()
f.close()

f=open("prng_js","ro")
p=f.readlines()
f.close()

prng=[]
for i in p:
    prng.append(int(i.strip()))

out=[]
for i in range(len(data)):
    o=ord(data[i])^prng[i]
    out.append(chr(o))

out=''.join(out)

output=open(sys.argv[1]+"-xored","wb")
output.write(out)
output.close()
