#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

#Enter yoursubnet with CIDR notation (e.g. 10.0.0.0.24)
scan("10.0.0.0/24")