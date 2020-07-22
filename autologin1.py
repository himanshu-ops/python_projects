#!/bin/python
import sys
import os

#os.system("sshpass -p password ssh himanshu@192.168.43.34" + " " .join(sys.argv[1:]))
os.system("sshpass -p password ssh himanshu@192.168.43.192 touch /home/himanshu/Desktop/test.txt")
