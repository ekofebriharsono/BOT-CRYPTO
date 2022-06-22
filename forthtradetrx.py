#!/usr/bin/python
# Author : YA-HA!!!

import os
import sys
import time
import random
import platform
try:
	import requests
except:
	exit("\nModule not installed\n")

if platform.python_version().split(".")[0] != "3":
	exit("\n ~> Tidak support untuk python2\n    ketik: python %s "%sys.argv[0]+"\n")

#url = "https://api.myip.com"

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
		mins, secs = divmod(second,60)
		timer = '  \033[37m~\033[30m> \033[37mWaiting \033[30m⟨\033[33m{:02d}:{:02d}\033[30m⟩ \033[37mseconds'.format(mins,secs)
		print(timer,end="\r")
		time.sleep(1)
		second -= 1

def App(cookie):
	browser = [
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
	]
	headers = {
		"Host":"forthtrade.com",
		"upgrade-insecure-requests": "1",
		"user-agent":random.choice(browser),
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"content-type": "text/html; charset=UTF-8",
		"accept-language":"en-US,en;q=0.9",
		"X-Requested-With":"XML_HttpRequest",
		"cookie":cookie,
	}
	
	kepala()
	
	url = 'https://forthtrade.com/tronminer'
	x = requests.get(url,headers=headers)
	hambat1 = x.text.split('<input type="text" id="tronwallet" name="tronwallet" size="40" placeholder="FaucetPay linked Tron wallet" style="width: 100%; max-width: 400px; z-index: 99999; position: relative;" onchange="updateWallet(this.value);" autocomplete="on" value="')[1]
	hambat2 = hambat1.split('"></div>')[0]
	#print(hambat2)
	#exit()
	print(f" {BWhite}{BGreen}Wallet {BWhite}{BRed} : {BWhite} {hambat2}")
	print(f"{BWhite}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	
	count = 1
	ts = time.time()
	while True:
		verify = requests.get(f"https://forthtrade.com/tronpm.php?q={ts}",headers=headers)
		if count == 1:
			if verify.status_code == 200:
				countdown(600)
				count += 1
			else:
				print(f"  Error Bre")
		else:
			if verify.status_code != 200:
				print(f"  {BWhite}[{BRed}!{BWhite}] {BWhite}Failed {BWhite}({BRed}{count}{BWhite}) get reward ~~{BRed}> {BGreen}TRX")
				count += 1
			else:
				print(f"  {BWhite}[{BGreen}•{BWhite}] Succes {BWhite}({BGreen}{count}{BWhite}) get reward ~~{BRed}> {BGreen}TRX")
				count += 1
			countdown(600)
			
def kepala():
	os.system("cls" if os.name == "nt" else "clear")
	print(f"\n {BWhite}[{BGreen}$$${BWhite}] YA-HA!!!")
	print(f"{BWhite}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	
try:
	kepala()
	cookie = input(f"  {BWhite}[{BGreen}•{BWhite}] Cookie {BRed}: {BWhite}")
	if "P" not in cookie:
		cookie = input(f"  {BWhite}[{BGreen}•{BWhite}] Cookie {BRed}: {BWhite}")
	else:
		App(cookie)

except KeyboardInterrupt:
	exit()
