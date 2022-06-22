import time
import random
try:
	import requests
except:
	exit("\nModule not installed\n")

dataMiner = []

def appShiba1 (userid,name):
    browser = [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
	]

    headers = {
		"Host":"shiba.thora.world",
		"user-agent":random.choice(browser),
	}

    while True:
        numeric = random.randint(1000,9999)
        verify = requests.get(f"https://shiba.thora.world/faucet.php?microwallet=ExpressCrypto&id1={userid}&currency=SHIB&startclaim=Start%20claiming&key=0642f{numeric}f59aab752fe2e8f78470d62",headers=headers)
        if verify.status_code != 200:
            print(". Failed => " + name)
        else:
            print(". Success => " + name)
        break

def appShiba2 (cookie,name):
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
    while True:
        
        verify = requests.get(f"https://shiba100s.ga/claim.php?coin=SHIB",headers=headers)
        if verify.status_code != 200:
            print(". Failed => " + name)
        else:
            print(". Success => " + name)
        break

def appShiba3 (cookie,name):
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
		"cookie":"PHPSESSID=c2ecbe9c31396cec82d05ca6d5020807; __dtsu=51A01639827160E2BF71F507E2443C4C; token_QpUJAAAAAAAAGu98Hdz1l_lcSZ2rY60Ajjk9U1c=BAYAYb3GaQFhvcc6gAGBAsAAILDdJquqNr-fCrVgMkp-Y_1AY--GMXqko2eIqb3aH-dUwQBHMEUCIQCtVI4KkZxNtLN7IKm8SRkktQgSWGSZXU-W-JwLQEI8GQIgH7J7gpoC_YqrEV63WotpOOr9TF0yGtARHb6xRDVolFA",
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