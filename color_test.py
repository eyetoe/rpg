#!/usr/bin/env python

from clint.textui import colored
from player import *
from monster import *
from lib.roll import Roll
from lib.getch import getch
r = Roll()
g = getch()


print '################################################################################'
print 'Color Test, this is normal text'
print '################################################################################'
print colored.blue('This is bold', bold=True), colored.blue('This is not')
print colored.red('This is bold', bold=True), colored.red('This is not')
print colored.green('This is bold', bold=True), colored.green('This is not')
print colored.yellow('This is bold', bold=True), colored.yellow('This is not')
print colored.magenta('This is bold', bold=True), colored.magenta('This is not')
print colored.cyan('This is bold', bold=True), colored.cyan('This is not')
print colored.black('This is bold', bold=True), colored.black('This is not')
print colored.white('This is bold', bold=True), colored.white('This is not')
print colored.disable()
print 'normal print... the end'
print '################################################################################'
