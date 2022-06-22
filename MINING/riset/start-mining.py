import platform
import initFunction as fs

if platform.python_version() != "3.7.11":
	exit("Please setup your python || run : python setup.py")
        
print("Add coin")
fs.addDataCoin("shiba")
fs.addDataCoin("allcoin")
fs.addDataCoin("doge")
# fs.addDataCoin("tron")

print("Starting . . .")
fs.startMining(fs.dataCoin)
fs.seeMonitor()


