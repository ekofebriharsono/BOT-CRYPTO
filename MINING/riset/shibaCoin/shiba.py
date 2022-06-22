import time
import initFunctionShiba as fs

print("Add Miner")
fs.addDataMiner("eko","EC-UserId-619418","PHPSESSID=a4425903e141cd6d278eb613e91ada20; __dtsu=1040163980245877388B2A478B569AF7; SHIBToken=llKJA9OJe4SSwM2vRT7fQseHXa0gB1Xc")
fs.addDataMiner("adhiq","EC-UserId-620435","PHPSESSID=ed8a819367aef09774a920f918e66dd3; __dtsu=4C30163983531037130698E423DDC2C0; SHIBToken=IkEE1gRUDHiWqdlJO0VlXy8JXeE0IuWP")
fs.addDataMiner("ulum","EC-UserId-620774","PHPSESSID=b71d0386ef562df837e6acf7b704f992; __dtsu=6D001639548790820464C42E7731E768; SHIBToken=wFxRMgmcYXRfUo6TpvhtLhOV7z7EBNvh")
fs.addDataMiner("nawawi","EC-UserId-622302","PHPSESSID=5c5a5e5d0ebdee07b5181df142f7905f; __dtsu=10401639837084414030CA6A57F96C1D; SHIBToken=fqdjmQ36d1yNoPsCmjyjjaPKit10l1FN")
fs.addDataMiner("hasbi","EC-UserId-570852","PHPSESSID=8c9f4839b3ab107e2885f47448be5404; __dtsu=4C301639638038B14D664CC3A761B210; SHIBToken=iT5UrqC8QguanroKPlZYv56KUS9wjEVe")

while True:
	print("Starting SHIBA")
	for data in fs.dataMiner:
		try:
			wallet = data[1]
			name = data[0]
			cookie = data[2]
			
			if "EC" not in wallet: 
				exit("Your Wallet Invalid!")
			else: 
				print("Shiba 1")
				fs.appShiba1(wallet , name)
				print("Shiba 2")
				fs.appShiba2(cookie , name)
				# print("Shiba 3")
				# fs.appShiba3(cookie , name)

		except KeyboardInterrupt:
			exit()
	time.sleep(90)
		
