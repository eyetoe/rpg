#!/usr/local/bin/python

################################################################################
def levels():
    #a,b = 1000,2000
    a,b = 1,2
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

################################################################################

def level_progression():

    progression = levels()
    lp = {}

    for level in range(1, 51):
        experience = progression.next()
        lp[level] = experience
    
    #print lp
    return lp

################################################################################

def get_level(exp):
    levels = level_progression()
    for key, value in levels.iteritems():
        if exp >= value:
            level = key
    return level

################################################################################

if __name__ == "__main__":
    level_progression()
    #flappy = level_progression()
    #print flappy

