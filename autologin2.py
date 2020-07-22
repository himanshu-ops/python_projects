#!/bin/python

import paramiko

ip='192.168.1.102'
port=22
username='himanshu'
password='password'

cmd='rm -rvf /home/himanshu/Desktop/him.txt && touch /home/himanshu/Desktop/himanshu.txt' 

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)
