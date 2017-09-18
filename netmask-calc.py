#!/usr/bin/python

import sys,commands,os
args=(sys.argv, len(sys.argv))

if args[1] == 1:
	print "Usage: is ./subnet.py <ip/subnet>"
	sys.exit()

ip=sys.argv[1].split('/')[0]
print "Network is", ip
oct1=ip[0]
oct2=ip[1]
oct3=ip[2]
oct4=int(ip[-1])+1
ip_list=ip.split('.')
ip_list[-1]=oct4

print ip
def mask(bits):
	if bits == 24:
		print "Addresses in network is 256"
	if bits == 25:
		print "Addresses in network is 128"
	if bits == 26:
		print "Addresses in network is 64"
	if bits == 27:
		print "Addresses in network is 32"
	if bits == 28:
		print "Addresses in network is 16"
	if bits == 29:
		print "Addresses in network is 8"
	if bits == 30:
		print "Addresses in network is 4"
	if bits == 31:
		print "Addresses in network is 2"
	if bits == 32:
		print "Addresses in network is 1"
	return


bits=sys.argv[1].split('/')[1]
mask(int(bits))
