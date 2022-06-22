import random
try:
	import requests
except:
	exit("\nModule not installed\n")

dataMiner = []

def App (userid,name):
    browser = [
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36"
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
	]

    headers = {
		"Host":"thora.world",
		"user-agent":random.choice(browser),
	}

    while True:
        numeric = random.randint(1000,9999)
        verify = requests.get(f"https://thora.world/faucet.php?microwallet=ExpressCrypto&id1={userid}&currency=TRX&startclaim=Start%20claiming&key=0642f{numeric}f59aab752fe2e8f78470d62",headers=headers)
        if verify.status_code != 200:
            print(". Failed => " + name)
        else:
            print(". Success => " + name)
        break

def addDataMiner(name, user_id):
    data = [name,user_id]
    dataMiner.append(data)