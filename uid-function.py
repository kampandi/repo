#!/usr/bin/python

import commands
dic={}

def uid(x):
 for i in commands.getoutput('cat /tmp/passwd').split('\n'):
  if int(i.split(':')[2]) == x:
   dic[i.split(':')[0]] = i.split(':')[-1]

uid(8)
print dic
