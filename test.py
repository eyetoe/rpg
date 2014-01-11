#!/usr/bin/env python
#from roll import Roll
from lib.roll import *
#from level_progression import level_progression
from lib.level_progression import *

print '\nTest Die Rolls:'
r = Roll()
print "d20:     ", r.d20()
print "dAttr:   ", r.dAttr()
print "dAttr:   ", r.dAttr()
print "dAttr:   ", r.dAttr()
print "d2:      ", r.d2()
print "d4:      ", r.d4()
print "d6:      ", r.d6()
print "d8:      ", r.d8()
print "d10:     ", r.d10()
print "d12:     ", r.d12()
print "d100:    ", r.d100()
#print Roll().d20() # works..weird

print '\nDisplay Level Progession:'
level_progression = level_progression()
print level_progression
