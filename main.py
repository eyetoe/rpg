#!/usr/local/bin/python
import sys
import time
import pprint
from random import randint
from pprint import pprint
################################################################################
# Setup Variables
LEVEL = 1
EXPERIENCE = 0

################################################################################
def r20():
    return randint(1,20)

################################################################################
def poop(item):
    pprint(item)
################################################################################
def level():
    a,b = 0,1000
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
################################################################################
# Dictionary to hold Stats
ATTRIBUTE = {}
ATTRIBUTE['strength']       = r20() + r20() + r20()
ATTRIBUTE['dexterity']      = r20() + r20() + r20()
ATTRIBUTE['constitution']   = r20() + r20() + r20()
ATTRIBUTE['intelligence']   = r20() + r20() + r20()
ATTRIBUTE['wisdom']         = r20() + r20() + r20()
ATTRIBUTE['charisma']       = r20() + r20() + r20()

STATISTIC = {}
STATISTIC['defence']        = (ATTRIBUTE['dexterity'] + ATTRIBUTE['constitution']) / 2
STATISTIC['attack']         = (ATTRIBUTE['dexterity'] + ATTRIBUTE['strength']) / 2
STATISTIC['perception']     = (ATTRIBUTE['intelligence'] + ATTRIBUTE['dexterity']) / 2
STATISTIC['health']         = (ATTRIBUTE['constitution'] + ATTRIBUTE['strength']) / 2

################################################################################
print '\nATTRIBUTES'
for key, value in ATTRIBUTE.iteritems():
    print(key, value)

print '\nSTATISTICS'
for key, value in STATISTIC.iteritems():
    print(key, value)

progression = level()
#total = 0
#
#for item in progression:
#    total = total + item
#    print(item)
#    print "------------: "+str(total)
#    time.sleep(.2)

total = 0
print '\nLEVEL PROGRESSION'
for each in range(1, 21):
    amt = progression.next()
    total = total + amt
    #print(each, total)
    print(each, amt)

