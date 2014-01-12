#!/usr/bin/env python
import os
import sys    
import termios
import fcntl

class _Getch:
    def __init__(self):
        try:
            self.impl = _myGetch()
        except ImportError:
            print 'exiting, cant call _myGetch()'

    def __call_(self): return self.impl()

class _myGetch:
    def __init__(self):
        import tty, sys

    def __call__(self):
#def _myGetch():
        import os
        import sys    
        import termios
        import fcntl
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
    
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    
        try:        
            while 1:            
                try:
                    c = sys.stdin.read(1)
                    break
                except IOError: pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        return c

if __name__ == '__main__': # a little test
   print 'Press a key'
   inkey = _myGetch()
   import sys
   for i in xrange(sys.maxint):
      k=inkey()
      if inkey <>'':break
   print 'you pressed', k
   #print 'you pressed', inkey

