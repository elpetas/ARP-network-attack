# Scapy Packet Spoofing
This code is designed to spoof packets using the Scapy library in Python. Scapy is a powerful tool for packet manipulation, and it allows us to modify packets at various layers of the OSI model. This specific script is designed to modify TCP packets between two virtual machines (VMs) and print out the transformation applied to the payload of the packet.

## Prerequisites
Before using this script, you must have Scapy installed. If you do not already have Scapy installed, you can install it using pip:

python
Copy code
pip install scapy
## Usage
Run the script using python3 <script_name>.py command in the terminal.
Enter the IP address and MAC address of VM A when prompted.
Enter the IP address and MAC address of VM B when prompted.
Once the script is running, it will begin sniffing packets on filter 'tcp' between VM A and VM B.
If a packet is found with a payload, it will apply a transformation to the payload and send the new packet to VM B. If the packet does not have a payload, it will be sent back to VM A without modification.
## Understanding the Code
The script begins by importing necessary modules and libraries such as re and Scapy.

Then, the user is prompted to enter the IP and MAC addresses of the two virtual machines (VMs) involved in the communication.

Next, the script defines the spoof_pkt function which takes a packet as input and applies a transformation to the payload of the packet. The transformation involves replacing all alphabetic characters with the letter 'Z'. The script then creates a new packet with the modified payload and sends it to the destination VM. If the packet does not have a payload, it is simply sent back to the source VM without modification.

Finally, the script sniffs packets on filter 'tcp' using the sniff function and passes each packet to the spoof_pkt function for processing.

## Disclaimer
This script is for educational purposes only. Use it at your own risk and only on networks that you are authorized to access.
