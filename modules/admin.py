#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
admin.py - Phenny Admin Module
Copyright 2008-9, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

def join(phenny, input): 
   u"""Entra al cana especificat. Només els administradors."""
   # Can only be done in privmsg by an admin
   if input.sender.startswith('#'): return
   if input.admin: 
      channel, key = input.group(1), input.group(2)
      if not key: 
         phenny.write(['JOIN'], channel)
      else: phenny.write(['JOIN', channel, key])
join.commands = ['join','entra']
join.priority = 'low'
join.example = '.entra #exemple or .entra #exemple contrassenya'

def part(phenny, input): 
   u"""Daixa el canal especificat. Només els administradors."""
   # Can only be done in privmsg by an admin
   if input.sender.startswith('#'): return
   if input.admin: 
      phenny.write(['PART'], input.group(2))
part.commands = ['part','surt']
part.priority = 'low'
part.example = '.deixa #exemple'

def quit(phenny, input): 
   """Surt del servidor. Només l'owner."""
   # Can only be done in privmsg by the owner
   if input.sender.startswith('#'): return
   if input.owner: 
      phenny.write(['QUIT'])
      __import__('os')._exit(0)
quit.commands = ['quit']
quit.priority = 'low'

def msg(phenny, input): 
   # Can only be done in privmsg by an admin
   if input.sender.startswith('#'): return
   a, b = input.group(2), input.group(3)
   if (not a) or (not b): return
   if input.admin: 
      phenny.msg(a, b)
msg.rule = (['msg'], r'(#?\S+) (.+)')
msg.priority = 'low'

def me(phenny, input): 
   # Can only be done in privmsg by an admin
   if input.sender.startswith('#'): return
   if input.admin: 
      msg = '\x01ACTION %s\x01' % input.group(3)
      phenny.msg(input.group(2) or input.sender, msg)
me.rule = (['me'], r'(#?\S+) (.+)')
me.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
