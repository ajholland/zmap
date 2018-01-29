#!/bin/python
import sys
from itertools import islice
m = {}
with open(sys.argv[1]) as f:
    i = islice(f,0,None,4)
    for g in i:
        t = g.split("dest:")[1]
        n = int(t.split("|")[0])
        if n not in m:
            m[int(t.split("|")[0])] = 1
        else:
            m[int(t.split("|")[0])] += 1
for i in xrange(65536):
    if i not in m:
        print i
    i += 1
#print m
