#!/usr/local/bin/python
from random import randint

class Roll:
    def d100(self):
        return randint(1,100)

    def d20(self):
        return randint(1,20)

    def d12(self):
        return randint(1,12)

    def d10(self):
        return randint(1,10)

    def d8(self):
        return randint(1,8)

    def d6(self):
        return randint(1,6)

    def d4(self):
        return randint(1,4)

    def d3(self):
        return randint(1,3)

    def d2(self):
        return randint(1,2)

    def dAttr(self):
        return randint(1,20) + randint(1,20) + randint(1,20)
        #return randint(1,6) + randint(1,6) + randint(1,6)

    def dFair(self):
        r = Roll()
        ra = [ r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr(), r.dAttr() ]
        ra.sort()
        return ra[-1:][0]

