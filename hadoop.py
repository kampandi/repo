#!/usr/bin/python

import time
import commands
import os
import sys
import pexpect

#class style:
BOLD = '\033[1m'
END = '\033[0m'
RED="\033[0;31m"


virsh=commands.getoutput('virsh list --all').split('\n')
virsh.pop(0)
virsh.pop(0)
virsh.pop(-1)

for i in virsh:
        if i.split()[-1] == 'off':
                print ("%s is provisioned and shutdown status" %i.split()[1])
        else:
                print ("%s is provisioned and running status" %i.split()[1])


class Create_vm():
        def __init__(self,CPU,memory):
                ping=os.system("ping -c 2 192.168.0.10")
                if ping == 0:
                        print "your instance will provision in 60 seconds with SElinux disabled mo
de"
                        time.sleep(60)
                        os.system("virt-install --name=%s --disk path=/toshiba-docker/%s.qcow2,siz
e=10 --graphics none --vcpus=%s --memory=%s --location ftp://pxe-server/pub --network bridge=br0 -
-os-type=linux --os-variant=rhel7 --extra-args console=ttyS0" %(self,self,CPU,memory))
                else:
                        print "pxe-server is not reachable"
        def sshkey(master,*agents):
                master=master
                agents=agents
                pkg_chk=os.system('rpm -qa | grep -i pexpect')
                if pkg_chk == 0:
                        user = 'root'
                        password = 'root123'
                        master_host = '%s' %master
                        agents_host= '%s' %agents
                        master_command='mkdir /root/.ssh;ssh-keygen -t rsa -f /root/.ssh/id_rsa -q
 -P "";chmod 700 /root/.ssh /root/.ssh/id_rsa.pub;cat /root/.ssh/id_rsa.pub > /root/.ssh/authorize
d_keys'
                        def dossh(user,password,host,command):
                                try:
                                        child =  pexpect.spawn("ssh  -o ServerAliveInterval=100 -n
 %s@%s '%s'" % (user,host,command),logfile=sys.stdout,timeout=None)
                                        i = child.expect(['password:', r'\(yes\/no\)',r'.*[$#] ',p
expect.EOF])
                                        if i == 0:
                                                child.sendline(password)
                                        elif i == 1:
                                                child.sendline("yes")
                                                ret1 = child.expect(["password:",pexpect.EOF])
                                                if ret1 == 0:
                                                        child.sendline(password)
                                                else:
                                                        pass
                                        else:
                                                pass
                                        data = child.read()
                                        print data
                                        child.close()
                                        return True
                                except Exception as error:
                                        print error
                                        return False
                else:
                        print "pexpect is not installed"

dossh(user, password, master_host, master_command)
