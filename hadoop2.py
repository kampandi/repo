#!/usr/bin/python

import time
import sys
import os
import argparse

parser = argparse.ArgumentParser(description="Hadoop setup")
parser.add_argument("-m",help="Master Node")
parser.add_argument("-a",help="Agent Nodes",nargs='+')
args = parser.parse_args()
masternode=args.m

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

def ssh(user,password,hostname,command):
 user='root'
 password='root123'
 child = pexpect.spawn('ssh %s@%s %s' % (user,hostname,command),logfile=sys.stdout,timeout=None)
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

def createkey(hostname,command):
 hostname=arg.m
 command=os.system('mkdir /root/.ssh;cd /root/.ssh;ssh-keygen -t rsa')

############## Host Entries for DNS########################################
os.system('cp -p /etc/hosts /etc/hosts.$(date +%d%m%y)')
def ipinput(hostname):
 IP=raw_input("please enter the IP for %s : " %hostname)
 cmd='echo "%s       %s" >> /etc/hosts'%(hostname,IP)
 os.system(cmd)

ipinput (args.m)
for hostname in args.a:
 ipinput(hostname)
############## ############## ############## ############## ###############

################Install the packages########################################
def install(package):
 yumcheck=os.system('yum list all %s > /dev/null' %package)
 if yumcheck != 0:
  print ("configure the %s repository and install it" %package)
 else:
  print  ("%s will install in 30 secs" %package)
  time.sleep(30)
  os.system('yum install -y %s' %package)

install(args.p)
