#!/usr/bin/env python
from lib.roll import Roll
from lib.level_progression import get_level
import time

def skill_test(skill_exp, skill_level):
    r = Roll()
    attempt = r.d20()
    print "Your skill exp and level: ", skill_exp, skill_level
    print "You rolled: ", attempt
    if skill_level >= attempt:
        print "Success! you hit"
        skill_exp = skill_exp +1
        #skill_level = skill_level +1
        return skill_exp, skill_level
    else:
        print "Failure! you miss"
        return skill_exp, skill_level

skill_exp = 1
skill_level = 1
iteration = 1

while True:
    skill_exp, skill_level = skill_test(skill_exp, skill_level)
    skill_level = get_level(skill_exp)
    #if skill_exp >= 10:
    #    skill_exp = 1
    #    skill_level = skill_level + 1
    time.sleep(.1)
    print 'Iteration Number ---------------: ', iteration
    iteration = iteration + 1
