import time
import initFunctionsTron as fs

print("Add Miner")
fs.addDataMiner("eko","EC-UserId-619418")
# fs.addDataMiner("adhiq","EC-UserId-620435")
# fs.addDataMiner("ulum","EC-UserId-620774")
# fs.addDataMiner("nawawi","EC-UserId-622302")
# fs.addDataMiner("hasbi","EC-UserId-570852")

while True:
	print("Starting TRON")
	for data in fs.dataMiner:
		try:
			wallet = data[1]
			name = data[0]
			
			if "EC" not in wallet: 
				exit("Your Wallet Invalid!")
			else: 
				fs.App(wallet , name)

		except KeyboardInterrupt:
			exit()
	time.sleep(90)