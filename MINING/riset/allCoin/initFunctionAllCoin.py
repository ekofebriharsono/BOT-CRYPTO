import time
import random
try:
	import requests
except:
	exit("\nModule not installed\n")

dataMiner = []

def appAllCoin (cookie,name):
    browser = [
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
	    ]	
    headers = {
        "Host":"cryptoclaim.space",
        "upgrade-insecure-requests": "1",
		"user-agent":random.choice(browser),
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"content-type": "text/html; charset=UTF-8",
		"accept-language":"en-US,en;q=0.9",
		"X-Requested-With":"XML_HttpRequest",
		"cookie":cookie,
    }

    while True:
        
        verify = requests.get(f"https://cryptoclaim.space/home?BTC=1&BCH=1&BCN=1&DASH=1&DGB=1&DOGE=1&ETH=1&LSK=1&LTC=1&XMR=1&NEO=1&PPC=1&POT=1&XRP=1&STRAT=1&TRX=1&WAVES=1&ZEC=1&XTZ=1&PIVX=1&ETC=1&ADA=1&KMD=1&VTC=1&ZEN=1",headers=headers)
        if verify.status_code != 200:
            print(". Failed => " + name)
        else:
            print(". Success => " + name)
        break
	
def addDataMiner(name, user_id, cookie):
    data = [name,user_id,cookie]
    dataMiner.append(data)