import os
import time
import platform

if platform.python_version() != "3.7.11":
	exit("Please setup your python")

dataMiner = []
dataCoin = []

def addDataMiner(name, user_id):
    data = [name,user_id]
    dataMiner.append(data)

def addDataCoin(name):
    data = [name]
    dataCoin.append(data)

def generateCommand(coin,name):
    resultCommand = "nohup python -u public_html/"+coin+"/"+name+"/"+coin+"-"+name+".py &"
    return resultCommand

def startMining(data):
    for miner in data:
        for coin in dataCoin:
            command = generateCommand(coin[0],miner[0])
            resultCommand = os.system(command)
            if resultCommand == 0 :
                print("Running " + coin[0] + " by " + miner[0])
            else :
                print("Failed " + coin[0] + " by " + miner[0])
            time.sleep(1)
        print("============================")
        
def seeMonitor():
    os.system("ps aux")
        
print("Add Miner")
addDataMiner("eko","EC-UserId-619418")
addDataMiner("adhiq","EC-UserId-620435")
addDataMiner("ulum","EC-UserId-620774")
addDataMiner("nawawi","EC-UserId-622302")
addDataMiner("hasbi","EC-UserId-570852")

print("Add coin")
addDataCoin("shiba")
# addDataCoin("tron")

print("Starting . . .")
startMining(dataMiner)
seeMonitor()


