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
		mins, secs = divmod(second,70)
		timer = '  \033[37m~\033[30m> \033[37mWaiting \033[30m⟨\033[33m{:02d}:{:02d}\033[30m⟩ \033[37mseconds'.format(mins,secs)
		print(timer,end="\r")
		time.sleep(1)
		second -= 1

def App(userid):
	browser = [
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36"
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
	]
	headers = {
		"Host":"btcs2u.tk",
		"upgrade-insecure-requests": "1",
		"user-agent":random.choice(browser),
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"content-type": "text/html; charset=UTF-8",
		"accept-language":"en-US,en;q=0.9",
		"X-Requested-With":"XML_HttpRequest",
		"cookie":cookie,
		"referer": "https://btcs2u.tk/auto-trx/claim.php?coin=DOGE"
	}
	
	url = 'https://btcs2u.tk/auto-trx/claim.php?coin=DOGE'
	x = requests.get(url,headers=headers)
	
	wallet1 = x.text.split('<title>Claim DOGE -')[1]
	wallet = wallet1.split('</title>')[0]
	
	balance1 = x.text.split('<div class="col ThirdLayer card">Balance: <br>')[1]
	balance = balance1.split('<!-- <span class="Smalltext">0</span> --></div>')[0]
	
	kepala()
	print(f" {BWhite}{BGreen}Wallet {BWhite}{BRed} : {BWhite} {wallet}")
	print(f" {BWhite}{BGreen}Balance {BWhite}{BRed} : {BWhite} {balance}")
	print(f"{BWhite}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

	count = 1	
	while True:
		verify = requests.get(f"https://btcs2u.tk/auto-trx/claim.php?coin=DOGE",headers=headers)
		balance2 = verify.text.split('<div class="col ThirdLayer card">Balance: <br>')[1]
		balance3 = balance2.split('<!-- <span class="Smalltext">0</span> --></div>')[0]
		cekoncek = balance2.split('DOGE Satoshi <!-- <span class="Smalltext">0</span> --></div>')[0]
		jumlahke = int(cekoncek)
		angka = 0
		if count == 1:
			if verify.status_code == 200:
				countdown(60)
				count += 1
			else:
				print(f"  Error Bre")
		else:
			if verify.status_code != 200:				
				print(f"  {BWhite}[{BRed}!{BWhite}] Cek Your Connection Bre")
				print(f"{BWhite}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				count += 1
			else:
				if angka == jumlahke:
					ket2 = verify.text.split('<div class="alert alert-success"><i style="font-size:25px;" class="material-icons">checked</i> <span>')[1]
					sukses = ket2.split('</span> </div><br>')[0]
					print(f"{BWhite}[{BGreen}•{BWhite}] {BGreen} {sukses}")
					print(f"{BWhite}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
					count = 1
				else:
					print(f" {BWhite}{BGreen}Add Balance {BWhite}{BRed} \033[37m~\033[30m> {BWhite} {balance3}")
				
				count += 1
			countdown(60)
	
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
