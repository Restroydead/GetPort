import os
import sys
import time
import socket
from colorama import Fore, init, Back, Style
from base_dan import BASE_DAN

init()
FPS = 0
os.system("chcp 1251")
os.system("cls")
isWork = True

def scan():

	hostName = input(Fore.LIGHTWHITE_EX + "[HostName] --> ")
	print()
	#port = [20, 21, 22, 23, 42, 43, 53, 67, 69, 80, 110, 139, 8000, 8080, 3128, 3389, 6588, 1080, 5900, 8888]
	port = BASE_DAN
	print(Fore.LIGHTCYAN_EX + "STATUS:     PORT:    SATUTS:")
	for i in port:
		try:
			soc = socket.socket()
			soc.settimeout(FPS)
			soc.connect((hostName, i))

		except socket.error:
			print(Fore.LIGHTRED_EX + "[-] ", Fore.LIGHTWHITE_EX + f"Port --> {i} --> " + Fore.LIGHTRED_EX + "[CLOSED]")

		else:
			print(Fore.LIGHTGREEN_EX + "[+] ", Fore.LIGHTWHITE_EX + f"Port --> {i} --> " + Fore.LIGHTGREEN_EX + "[OPEN]")

while (isWork != False):

	print(Fore.LIGHTWHITE_EX +"-" * 50)
	print(Fore.LIGHTWHITE_EX + "\t[1] ==> scanning")
	print(Fore.LIGHTWHITE_EX + "\t[2] ==> IP host")
	print(Fore.LIGHTWHITE_EX + "\t[3] ==> clear shell")
	print(Fore.LIGHTWHITE_EX + "\t[4] ==> exit")
	print("-" * 50, "\n")

	command = input(Fore.LIGHTWHITE_EX + "[command] --> ")
	print()

	if command == "1":
	   FPS = float(input(Fore.LIGHTWHITE_EX + "[choose a delay] --> "))
	   print()
	   scan()
	else:
		pass

	if command == "2":
		ip_host = input(Fore.LIGHTWHITE_EX + "[HostName] --> ")
		print()
		print(Fore.LIGHTGREEN_EX + "IP Host ==> ", socket.gethostbyname(ip_host))

	if command == "3":
		os.system("cls")
	else:
		pass

	if command == "4":
		sys.exit()

	time.sleep(1)