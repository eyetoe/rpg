#!/usr/local/bin/python
from lib.roll import Roll
import time

def doit():
    r = Roll()
    booger = [ r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr() ]
    #booger = [ r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr() ]
    #booger = [ r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr() ]
    booger.sort()
    print "The List: ", booger
    print "Best Score:                          ", booger[-1:][0]

while True:
    doit()
    time.sleep(1)
