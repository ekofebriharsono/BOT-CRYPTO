import time
import random
try:
	import requests
except:
	exit("\nModule not installed\n")

dataMiner = []

def appDoge (cookie,name):
    browser = [
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36"
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
	]

    header = {
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

    url = "https://btcs2u.tk/auto-trx/claim.php?coin=DOGE"
    x = requests.get(url,headers=header)
	
    while True:
        verify = requests.get(f"https://btcs2u.tk/auto-trx/claim.php?coin=DOGE",headers=header)
        if verify.status_code != 200:
            print(". Failed => " + name)
        else:
            print(". Success => " +name)
        break
	
def addDataMiner(name, user_id, cookie):
    data = [name,user_id,cookie]
    dataMiner.append(data)