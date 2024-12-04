#!/bin/bash
clear
echo $(date)
echo "Computer Name: " $HOSTNAME
echo "System Info:"
uname -a
echo "Operating System:"
cat /etc/os-release | grep PRETTY_NAME
cat /etc/of-release | grep VERSION_ID
echo "Total RAM:"
cat /proc/meminfo | grep "MemTotal"
echo "Storage devices:"
df -h
echo "IP Addresses:"
hostname -I
echo "Created by"
whoami