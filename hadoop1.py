#!/usr/bin/python

import time
import sys
import os
import argparse

parser = argparse.ArgumentParser(description="Hadoop setup")
parser.add_argument("-m",help="Master Node")
parser.add_argument("-a",help="Agent Nodes")
args = parser.parse_args()

########### Pre Requesties for ssh #######################################
rpmcheck=os.system('rpm -qa | grep -i pexpect')
if rpmcheck != 0:
 yumcheck=os.system('yum list all pexpect > /dev/null')
 if yumcheck != 0:
  print "configure the pexpect repository and install it"
 else:
  print "pexpect module will install in 30 secs"
  time.sleep(30)
  os.system('yum install -y pexpect')

############## User Interactive login ########################################
class Login:
 def __init__(self,user,password,command):
  self.user=user
  self.password=password
  self.command=command
 def ssh(self):
  child = pexpect.spawn('ssh %s@%s %s' % (self.user,self.host,self.command),logfile=sys.stdout,timeout=None)
  prompt = child.expect(['password:', r"yes/no",pexpect.EOF])
  if prompt == 0:
   child.sendline(self.password)
   data = child.read()
   print data
   child.close()
  elif prompt == 1:
   child.sendline("yes")
   child.expect("password:")
   child.sendline(self.password)
   data = child.read()
   print data
   child.close()

############## Host Entries for DNS########################################
class Hostentry(Login):
 os.system('cp -p /etc/hosts /etc/hosts.$(date +%d%m%y)')
 def __init__(self,user,password,hostname):
  Login.__init__(self,user,password)
  self.hostname=hostname
 def ipinput(self,hostname):
  IP=raw_input("please enter the IP for %s : " %hostname)
  cmd='echo "%s       %s" >> /etc/hosts'%(hostname,IP)
  os.system(cmd)

ipinput (args.m)
for hostname in hosts:
 ipinput(hostname)

###########################################################################
