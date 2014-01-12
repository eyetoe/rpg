#!/usr/bin/env python

from clint.textui import colored
from player import *
from monster import *
from lib.roll import Roll
from lib.getch import getch
r = Roll()
g = getch()

# Generate a 'Consider Adjective'
if float(monster_level) > float(player_level):
    con_adj = colored.red('gruesome')
elif float(monster_level) < float(player_level):
    con_adj = colored.green('diminutive')
else:
    con_adj = colored.blue('comparable')

# Initiative, if succeed Fight or Flee, of fail, monster get's first attack

def check_initiative():

    friend = float(player_perception)
    friend_roll = r.d20()
    foe = float(player_perception)
    foe_roll= r.d20()

    print 'player:', friend, '+', friend_roll,'vs', 'monster:', foe, '+', foe_roll

    if friend + friend_roll >= foe + foe_roll:
        print 'You notice a', con_adj, monster_name, 'lurking.'
    else:
        print 'You have been surprised by a', con_adj, monster_name, '!'

# Fight or Flight?
def fight_or_flight():

    print 'Would you like to '+colored.cyan('(a)')+'ttack the', con_adj, monster_name, 'or '+colored.cyan('(e)')+'vade?'
    k = g()
    if k == 'e':
        print 'You attempt to retreat...'
    elif k == 'a':
        print 'You begin your attack...'
        which_attack()
    else:
        fight_or_flight()


# Evade

# Which attack?
def which_attack():
    print 'Attack with: '+colored.cyan('(m)')+'elee, '+colored.cyan('(r)')+'anged, or '+colored.cyan('(s)')+'pell?'
    k = g()
    if k == 's':
        print 'You channel arcane engergy to cast...', player_spell
    elif k == 'r':
        print 'You ready your...', player_ranged
    elif k == 'm':
        print 'You raise your...', player_melee
    else:
        which_attack()
    

    # Does it hit?

    # How much damage?

    # Did it die?


# Monster attack

    # Does it hit?

    # How much damage?

    # Did we die?


# Flow

check_initiative()
fight_or_flight()
