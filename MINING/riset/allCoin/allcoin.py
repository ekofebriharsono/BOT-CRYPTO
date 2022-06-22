import time
import initFunctionAllCoin as fs

print("Add Miner")
fs.addDataMiner("eko","EC-UserId-619418","PHPSESSID=77a23204d3f462b1c726aaab59418908; uniqueID=EC-UserId-619418; __dtsu=104016398545306626FC74765104DD2A; token_QpUJAAAAAAAAGu98Hdz1l_lcSZ2rY60Ajjk9U1c=BAYAYb4xvwFhvjHPgAGBAsAAIPyN4O2AwNLXW2UFTMFY7bGRBqve6A9O0akbrmMgrNkDwQBHMEUCIQCkGYM2aD4z8pCew7o8xbko3k1T8vRyoCDyHN7uq5hCfAIgcra1dEPGVsIvl8bQ4wH8U5ITNIU7XUwl0M_e5N6S8gU")
fs.addDataMiner("adhiq","EC-UserId-620435","PHPSESSID=d33d41fd4a46dfef4a8a9fd9b8babbb9; __dtsu=6D001639548790820464C42E7731E768; token_QpUJAAAAAAAAGu98Hdz1l_lcSZ2rY60Ajjk9U1c=BAYAYb3vFgFhve8WgAGBAsAAICxl4rMPcHv3ud2mDzEfv8eMBJK5ogChwWvk5BeRAiY9wQBGMEQCIF5lvyje8vOpUnoVIhUCQoi91m-94kbpviogKfzlXZY5AiAb2l8nWelUR8kR7ykBUpTNQWTHYRSvHxM8ige64L6Ayg")
# fs.addDataMiner("ulum","EC-UserId-620774")
# fs.addDataMiner("nawawi","EC-UserId-622302")
fs.addDataMiner("hasbi","EC-UserId-570852","PHPSESSID=8f91d159d456c4cbd57ebe6f668807fc; __dtsu=51A016398370516ECDE6DACBE12C84FD; token_QpUJAAAAAAAAGu98Hdz1l_lcSZ2rY60Ajjk9U1c=BAYAYb3r5gFhve2XgAGBAsAAIL9r418gMbrMjjbqfv9x_V9QN1eyIz2kLBVXFHPzhk7iwQBHMEUCIGWYe0tZuRhLaEP914TwwmOK8zI2AgC-0z4COT7RkQ58AiEA1ATyfXdsdvD2Cl0GMSbrB1CActEQaVXziFYUXIkf6vk;")

while True:
	print("Starting CrytoClaim")
	for data in fs.dataMiner:
		try:
			wallet = data[1]
			name = data[0]
			cookie = data[2]
			
			if "EC" not in wallet: 
				exit("Your Wallet Invalid!")
			else: 
				# print("Shiba 1")
				# fs.appShiba1(wallet , name)
				# print("Shiba 2")
				# fs.appShiba2(cookie , name)
				print("All Coin")
				fs.appAllCoin(cookie , name)

		except KeyboardInterrupt:
			exit()
	time.sleep(90)