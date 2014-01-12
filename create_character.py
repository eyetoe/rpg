#!/usr/local/bin/python
# Run directly
# Create Character metrics and display them
import math
from lib.roll import Roll
################################################################################
# Setup Variables
LEVEL = float(1)
EXPERIENCE = 0
################################################################################
# Setup Objects
r = Roll()
################################################################################
# ATTRIBUTES:  The base metrics for the character.  These factors should be
# important enough to impact all the more specific metrics.  
ATTRIBUTE = {}
#ATTRIBUTE['strength']       = r.dAttr()
ATTRIBUTE['strength']       = r.dFair()
#ATTRIBUTE['dexterity']      = r.dAttr()
ATTRIBUTE['dexterity']      = r.dFair()
#ATTRIBUTE['constitution']   = r.dAttr()
ATTRIBUTE['constitution']   = r.dFair()
#ATTRIBUTE['intelligence']   = r.dAttr()
ATTRIBUTE['intelligence']   = r.dFair()

# STATISTICS: These metrics are derived using only ATTRIBUTES and LEVEL and
# represent features that are related to all t
STAT = {}
STAT['sd']     = (ATTRIBUTE['strength'] + ATTRIBUTE['dexterity']) /2
STAT['sc']     = (ATTRIBUTE['strength'] + ATTRIBUTE['constitution']) /2
STAT['si']     = (ATTRIBUTE['strength'] + ATTRIBUTE['intelligence']) /2
STAT['dc']     = (ATTRIBUTE['dexterity'] + ATTRIBUTE['constitution']) /2
STAT['di']     = (ATTRIBUTE['dexterity'] + ATTRIBUTE['intelligence']) /2
STAT['ci']     = (ATTRIBUTE['constitution'] + ATTRIBUTE['intelligence']) /2

STATISTIC = {}
STATISTIC['defence']    = STAT['dc']
STATISTIC['attack']     = STAT['sd']
STATISTIC['health']     = STAT['sc']

SKILL = {}
SKILL['perception']         = STAT['di'] + LEVEL
SKILL['arcana']             = ATTRIBUTE['intelligence'] + LEVEL
SKILL['athletics']          = STAT['sd'] + LEVEL

ABILITY = {}
ABILITY['stealth']          = math.ceil(SKILL['perception'] * LEVEL / 3)
ABILITY['fireball']         = math.ceil(SKILL['arcana'] * LEVEL / 3)
ABILITY['melee']            = math.ceil(((STATISTIC['attack'] + ATTRIBUTE['strength'])/2) * LEVEL / 3)
ABILITY['ranged']           = math.ceil(((STATISTIC['attack'] + ATTRIBUTE['dexterity'])/2) * LEVEL / 3)

################################################################################

print '\nLEVEL: ', LEVEL
print '\nEXPERIENCE: ', EXPERIENCE

print '\nATTRIBUTES'
for key, value in ATTRIBUTE.iteritems():
    print(key, value)

print '\nSTAT'
for key, value in STAT.iteritems():
    print(key, value)

print '\nSTATISTICS'
for key, value in STATISTIC.iteritems():
    print(key, value)

print '\nSKILL'
for key, value in SKILL.iteritems():
    print(key, value)

print '\nABILITY'
for key, value in ABILITY.iteritems():
    print(key, value)
