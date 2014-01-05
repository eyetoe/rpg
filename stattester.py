#!/usr/local/bin/python
from lib.roll import Roll
import time

def doit():
    r = Roll()
    bestof = [ r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr() ]
    #bestof = [ r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr() ]
    #bestof = [ r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr() ]
    bestof.sort()
    print "The List: ", bestof
    print "Best Score:                          ", bestof[-1:][0]

while True:
    doit()
    time.sleep(1)
