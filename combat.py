#!/usr/bin/env python

import sys
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
    elif k == 'x':
        print 'Exiting...'
        sys.exit(0)
    else:
        fight_or_flight()


# Evade

# Which attack?
def which_attack():
    print 'Attack with: '+colored.cyan('(m)')+'elee, '+colored.cyan('(r)')+'anged, or '+colored.cyan('(s)')+'pell?'
    k = g()
    if k == 's':
        print 'You channel arcane engergy to cast', player_ready_spell
        current_attack = ( player_ready_spell, player_arcana )
        does_it_hit(current_attack, monster_defence)
    elif k == 'r':
        print 'You ready your', player_ready_ranged
        current_attack = ( player_ready_ranged, player_ranged )
        does_it_hit(current_attack, monster_defence)
    elif k == 'm':
        print 'You raise your', player_ready_melee
        current_attack = ( player_ready_melee, player_melee )
        does_it_hit(current_attack, monster_defence)
    else:
        which_attack()

# Does it hit?
def does_it_hit(current_attack, current_defence):
    weapon = current_attack[0]
    attacker_base = float(current_attack[1])
    attacker_roll = r.d20()
    defender_base = float(current_defence)
    defender_roll= r.d20()
    
    print 'attacker:', attacker_base, '+', attacker_roll,'vs', 'defender:', defender_base, '+', defender_roll

    if attacker_base + attacker_roll >= defender_base + defender_roll:
        print colored.green('The'), colored.green(weapon), colored.green('hits!')
    else:
        print colored.red('The'), colored.red(weapon), colored.red('misses!')
    fight_or_flight()
    


    # How much damage?

    # Did it die?


# Monster attack

    # Does it hit?

    # How much damage?

    # Did we die?


# Flow

check_initiative()
fight_or_flight()
