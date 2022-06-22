import time
import random
try:
	import requests
except:
	print("Module not installed")

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


	ts = time.time()
	while True:
		verify = requests.get(f"https://forthtrade.com/tronpm.php?q={ts}",headers=headers)
		if verify.status_code != 200:
				print("Failed")
		else:
			print("Success")
		time.sleep(600)
		
try:
	cookie = "PHPSESSID=3u9gv71n65scn2v511ueeqluos; session_cookie=3u9gv71n65scn2v511ueeqluos_2477599; session_random=2477599; session_ip=118.97.70.226; session_cntr=ID; ads1533859=1; __cf_bm=RIoswUnAgUUcQgcjThOrjVRGtacYg9U7X.auluJxY98-1649132990-0-AUe4lsLAJ9n5GVJLfOUtiM23kpaELx3jduUslqKOMYn7bNWOmygJwNFkhs6S34lS4gdj00BzHLZLvFI/oZt5GXDMEe828y5t6XuLcwTJMiJBKONhRF8KY5BstHB5a0f54Q==; cookie_consent_user_accepted=true; _ga=GA1.2.506986285.1649133000; _gid=GA1.2.1204675475.1649133000; lang=en; aHR0cHM6Ly9mb3J0aHRyYWRlLmNvbS90cm9ubWluZXI==1649133011791; cookie_consent_level=%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D; tronwallet=TXSSWUwrjy1kcxSbVYrRojJaDWN7Q48DRM"
	App(cookie)

except KeyboardInterrupt:
	exit()
