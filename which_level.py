#!/usr/local/bin/python
from lib.roll import *
from lib.level_progression import *

print '\nDisplay Level Progession:'
level_progression = level_progression()
print level_progression

r = Roll()

exp_level = r.d100()
level = 1
print "Experience               : ", exp_level

for key, value in level_progression.iteritems():
    if exp_level >= value:
        level = key     

print "Level                    : ", level
