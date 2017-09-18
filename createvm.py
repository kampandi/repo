#!/usr/bin/python

import os
import sys

if len(sys.argv) < 4:
 print "script should use as <scriptname> <hostname> <no of CPU> <memory size>"
 sys.exit()
else:
 hostname=sys.argv[1]
 CPU=sys.argv[2]
 memory=sys.argv[3]

def createvm(hostname,CPU,memory):
 ping=os.system("ping -c 2 192.168.0.10 > /dev/null")
 virtual=os.system("grep -E 'svm|vmx' /proc/cpuinfo > /dev/null")
 kvm=os.system("rpm -qa | grep -i kvm > /dev/null")
 if ping != 0:
  print "Check the pxe server (192.168.0.10) status"
  sys.exit()
 elif virtual != 0:
   print "Enable the virtualization in bios"
   sys.exit()
 elif kvm != 0:
   print "Install the kvm"
   sys.exit()
 else:
  os.system("virt-install --name=%s --disk path=/toshiba-docker/%s.qcow2,size=10 --graphics none --vcpus=%s --memory=%s --location ftp://pxe-server/pub --network bridge=br0 --os-type=linux --os-variant=rhel7 --extra-args console=ttyS0" %(hostname,hostname,CPU,memory))

createvm(hostname,CPU,memory)
