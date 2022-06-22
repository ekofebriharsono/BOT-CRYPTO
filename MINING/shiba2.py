#!/usr/bin/python
# Author : Kingtebe
# Date : 07-10-2021, 01.32 WIB
# Silahkan rikod, para recoder terhormat !!

import os
import sys
import time
import random
import platform
import urllib
import json

try:
	import requests
except:
	exit("\nModule not installed\n")

if platform.python_version().split(".")[0] != "3":
	exit("\n ~> Tidak support untuk python2\n    ketik: python %s "%sys.argv[0]+"\n")

url = "https://api.myip.com" ### JSON IP

BBlack='\033[1;30m'       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White

def countdown(second):
	while second:
		mins, secs = divmod(second,90)
		timer = '  \033[37m~\033[30m> \033[37mWaiting \033[30m⟨\033[33m{:02d}:{:02d}\033[30m⟩ \033[37mseconds'.format(mins,secs)
		print(timer,end="\r")
		time.sleep(1)
		second -= 1

def App(cookie):
	browser = [
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
	]	
	headers = {
		"Host":"shiba100s.ga",
		"upgrade-insecure-requests": "1",
		"user-agent":random.choice(browser),
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"content-type": "text/html; charset=UTF-8",
		"accept-language":"en-US,en;q=0.9",
		"X-Requested-With":"XML_HttpRequest",
		"cookie":cookie,
	}
	
	#url = 'https://shiba100s.ga/claim.php?coin=SHIB'
	#x = requests.get(url,headers=headers)
	#print(x.text)
	count = 1
	while True:
		#numeric = random.randint(1000,9999)
		verify = requests.get(f"https://shiba100s.ga/claim.php?coin=SHIB",headers=headers)		
		#print(verify.status_code)
		if count == 1:
			countdown(90)
		else:
			if verify.status_code != 200:
				print(f"  {BWhite}[{BRed}!{BWhite}] {BWhite}Failed {BWhite}({BRed}{count}{BWhite}) get reward ~~{BRed}> {BGreen}.00300000 SHIB")
				count += 1
			else:
				print(f"  {BWhite}[{BGreen}•{BWhite}] Succes {BWhite}({BGreen}{count}{BWhite}) get reward ~~{BRed}> {BGreen}0.00300000 SHIB")
				count += 1
			countdown(90)
try:
	os.system("cls" if os.name == "nt" else "clear")
	print(f"\n {BWhite}[{BGreen}$$${BWhite}] YA-HA!!!")
	print(f"{BWhite}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	cookie = input(f"  {BWhite}[{BGreen}•{BWhite}] Cookie {BRed}: {BWhite}")
	if "P" not in cookie:
		cookie = input(f"  {BWhite}[{BGreen}•{BWhite}] Cookie {BRed}: {BWhite}")
	else:
		App(cookie)

except KeyboardInterrupt:
	exit()
