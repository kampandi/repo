#!/usr/bin/python

import argparse, os, time

parser = argparse.ArgumentParser(description="Hadoop setup")
parser.add_argument("-m",help="Master Node")
parser.add_argument("-a",help="Agent Nodes",nargs='+')
parser.add_argument("-p",help="package name")
parser.add_argument("-s",help="servername for package installation")
args = parser.parse_args()
masternode=args.m

class Login:
 def __init__(user,password,host,command):
  user='root'
  password='root123'
  host=args.h
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
 def install(host,package):
  yumcheck=os.system('yum list all %s > /dev/null' %package)
  if yumcheck != 0:
   print ("configure the %s repository and install it" %package)
  else:
   print  ("%s will install in 30 secs" %package)
   time.sleep(30)
   os.system('yum install -y %s' %package)

if args.h == masternode:
 install(args.h,args.p)
else:
 os.system('ssh %s "yum install -y %s' %(host,package))
