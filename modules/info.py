#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
info.py - Phenny Information Module
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

def doc(phenny, input): 
   """Mostra la documentació d'una ordre, i a vegades un exemple."""
   name = input.group(1)
   name = name.lower()

   if phenny.doc.has_key(name): 
      phenny.reply(phenny.doc[name][0])
      if phenny.doc[name][1]: 
         phenny.say('e.g. ' + phenny.doc[name][1])
doc.rule = ('$nick', '(?i)(?:help|doc|ajuda) +([A-Za-z]+)(?:\?+)?$')
doc.commands = ['help','doc','ajuda']
doc.example = '$nickname: ajuda uno? - .ajuda uno'
doc.priority = 'low'

def commands(phenny, input): 
   # This function only works in private message
   names = ', '.join(sorted(phenny.doc.iterkeys()))
   phenny.say('Ordres que reconeixo: ' + names + '.')
   phenny.say((u"Per ajuda d'una ordre en concret, escriu '.ajuda exemple', on exemple és " + 
               "l'ordre per la qual necessites ajuda.") % phenny.nick)
commands.commands = ['commands', 'ordres', 'o']
commands.priority = 'low'

def help(phenny, input): 
   response = (
      'Hola, sóc un bot del model \'phenny\'! La meva funció és jugar a l\'uno (escriu .uno). El meu owner és %s.'
   ) % phenny.config.owner
   phenny.reply(response)
help.rule = ('$nick', r'(?i)help(?:[?!]+)?$')
help.commands = ['info','ajuda']
help.priority = 'low'

def stats(phenny, input): 
   u"""Informació sobre els patrons d'ús de les ordres."""
   commands = {}
   users = {}
   channels = {}

   ignore = set(['f_note', 'startup', 'message', 'noteuri'])
   for (name, user), count in phenny.stats.items(): 
      if name in ignore: continue
      if not user: continue

      if not user.startswith('#'): 
         try: users[user] += count
         except KeyError: users[user] = count
      else: 
         try: commands[name] += count
         except KeyError: commands[name] = count

         try: channels[user] += count
         except KeyError: channels[user] = count

   comrank = sorted([(b, a) for (a, b) in commands.iteritems()], reverse=True)
   userank = sorted([(b, a) for (a, b) in users.iteritems()], reverse=True)
   charank = sorted([(b, a) for (a, b) in channels.iteritems()], reverse=True)

   # most heavily used commands
   creply = 'Ordres més utlitzades: '
   for count, command in comrank[:10]: 
      creply += '%s (%s), ' % (command, count)
   phenny.say(creply.rstrip(', '))

   # most heavy users
   reply = 'power users: '
   for count, user in userank[:10]: 
      reply += '%s (%s), ' % (user, count)
   phenny.say(reply.rstrip(', '))

   # most heavy channels
   chreply = 'power channels: '
   for count, channel in charank[:3]: 
      chreply += '%s (%s), ' % (channel, count)
   phenny.say(chreply.rstrip(', '))
stats.commands = ['stats']
stats.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
